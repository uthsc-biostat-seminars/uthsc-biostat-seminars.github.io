import pandas as pd 

# get data from github
url = "https://raw.githubusercontent.com/uthsc-biostat-seminars/Seminars/main/seminars.tsv"
df = pd.read_csv(url, sep='\t')
# for all columns, remove "" and leading/trailing spaces
df = df.applymap(lambda x: x.strip().replace('"', '') if isinstance(x, str) else x)

# get years column from Date column
df['Year'] = df['Date'].apply(lambda x: x.split('-')[0])

# reverse the rows order so that the most recent seminar is at the top
df = df.iloc[::-1]

# generate html file, with nested accordion

"""
Example of HTML being created:

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link rel="stylesheet" href="nested_styles.css">
</head>

<body>
    <div class="accordion-body">
        <div class="accordion">
            <div class="container">
                <div class="label">2023</div>
                    <div class="container">
                        <div class="accordion">
                            <div class="container">
                                <div class="label">(Date, Speaker, Title)</div>
                                    <div class="content">
                                    (Abstract)
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

      <script src="nested_test.js" type="text/javascript"></script>
</body>

"""


# header

html = "" 
html += "<!DOCTYPE html>\n"
html += "<html lang=\"en\">\n"
html += "<head>\n"
html += "    <meta charset=\"UTF-8\">\n"
html += "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
html += "    <meta http-equiv=\"X-UA-Compatible\" content=\"ie=edge\">\n"
html += "    <title>Document</title>\n"
html += "    <link rel=\"stylesheet\" href=\"nested_styles.css\">\n"
html += "</head>\n"

# body
html += "<body>\n"
html += '    <div class=\"accordion-body">\n'

# loop through the data
# for date at 2023, categorize the seminars at 2023 and so on
for year in df['Year'].unique():
    html += '        <div class=\"accordion\">\n'
    html += '            <div class=\"container\">\n'
    html += '                <div class=\"label\">' + year + '</div>\n'
    html += '                <div class=\"container\">\n'
    html += '                    <div class=\"accordion\">\n'
    html += '                        <div class=\"container\">\n'
    for index, row in df[df['Year'] == year].iterrows():
        html += '                            <div class=\"label\">(' + row['Date'] + ', ' + row['Speaker'] + ', ' + row['Title'] + ')</div>\n'
        html += '                            <div class=\"content\">\n'
        html += '                                ' + row['Abstract'] + '\n'
        html += '                            </div>\n'
    html += '                        </div>\n'
    html += '                    </div>\n'
    html += '                </div>\n'
    html += '            </div>\n'

# close the body

# footer
html += "    <script src=\"nested_test.js\" type=\"text/javascript\"></script>\n"
html += "</body>\n"
html += "</html>\n"

# write to file to the same directory as this script
with open("seminars.html", "w") as file:
    file.write(html)
