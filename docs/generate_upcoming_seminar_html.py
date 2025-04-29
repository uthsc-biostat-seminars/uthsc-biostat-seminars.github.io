"""
<!DOCTYPE html>
<html>
<head>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
.accordion {
  background-color: #a0dab3;
  color: #58595b;
  cursor: pointer;
  padding: 18px;
  width: 100%;
  border: none;
  text-align: left;
  outline: none;
  font-size: 15px;
  font-family: "Montserrat", sans-serif;
  border: 1px solid #bcbec0;
  transition: 0.4s;
}

.active, .accordion:hover {
  background-color: #00965e;
  color: white;
}

h2 {
  font-family: "Montserrat", sans-serif; 
}

p {
  font-family: "Montserrat", sans-serif;
}

.panel {
  padding: 0 18px;
  display: none;
  background-color: white;
  overflow: hidden;
}
</style>
</head>
<body>

<button class="accordion">2023</button> # Put the year here
<div class="panel">
  <p></p>
    <button class="accordion">2023-11-13, Dr. Xichen Mou, University of Memphis, Generalized kernel machine regression</button> # Put the date, speaker, and title here
  <div class="panel"> # Put the abstract here
    <p>Kernel Machine Regression (KMR) serves as a nonparametric regression approach fundamental in numerous scientific domains. By utilizing a map determined by the kernel function, KMR transforms original predictors into a higher-dimensional feature space, simplifying the recognition of patterns between outcomes and independent variables. KMR is invaluable in studies within the biomedical and environmental health sectors, where it aids in identifying crucial exposure points and gauging their impact on results. In our study, we introduce the Generalized Bayesian Kernel Machine Regression (GBKMR) which integrates the KMR model within the Bayesian context. GBKMR not only complements the conventional KMR but also suits a range of outcome data, from continuous to binary and count data. Simulation studies confirm GBKMR's superior precision and robustness. We further employ this method on a real data set to pinpoint specific cytosine phosphate guanine (CpG) locations correlated with health-related outcomes or exposures.</p>
  </div>

    <button class="accordion">Section 1.b</button> # Put the date, speaker, and title here
  <div class="panel"> # put the abstract here
    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
  </div>
</div>

<button class="accordion">Section 2</button> # The next year
<div class="panel"> 
  <p></p>
    <button class="accordion">(date, speaker, title)</button>
    <div class="panel">
        <p>Abstract</p>
    </div>
</div>

"""




# First acquire data from https://github.com/uthsc-biostat-seminars/Seminars/blob/main/upcoming_seminars.tsv
# Then generate html file for the website

import pandas as pd
import os

os.makedirs('../upcoming', exist_ok=True)

# Read data

df = pd.read_csv('https://raw.githubusercontent.com/uthsc-biostat-seminars/Seminars/refs/heads/main/upcoming_seminars.tsv', sep='\t')
# there are 5 columns: Date, Speaker, Affiliation, Title, Abstract
# everything is in string format

html = """
<!DOCTYPE html>
<html>
<head>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
.accordion {
  background-color: #a0dab3;
  color: #58595b;
  cursor: pointer;
  padding: 18px;
  width: 100%;
  border: none;
  text-align: left;
  outline: none;
  font-size: 15px;
  font-family: "Montserrat", sans-serif;
  font-weight: bold;
  border: 1px solid #bcbec0;
  transition: 0.4s;
}


.active, .accordion:hover {
  background-color: #00965e;
  color: white;
}

h2 {
  font-family: "Montserrat", sans-serif; 
}

p {
  font-family: "Montserrat", sans-serif;
}

.panel {
  padding: 0 18px;
  display: none;
  background-color: white;
  overflow: hidden;
}
</style>
</head>
<body>


"""
# remove '"' from the years
df['Date'] = df['Date'].str.replace('"', '')
# reversely sort all rows by Date
df = df.sort_values(by='Date', ascending=True)
#print(df)
years = df['Date'].str.split('-').str[0].unique()

for year in years:
    if year == years[0]:
      html += f'<button class="accordion active">{year}</button>\n<div class="panel"  style="display: block;">\n<p></p>\n'
    else:
      html += f'<button class="accordion">{year}</button>\n<div class="panel">\n<p></p>\n'
    # for i in range(len(df)-1, -1, -1):
    for i in range(len(df)):
        if df['Date'][i].startswith(year):
            # remove '"' from the strings
            df.loc[i, 'Speaker'] = df['Speaker'][i].replace('"', '')
            df.loc[i, 'Affiliation'] = df['Affiliation'][i].replace('"', '')
            df.loc[i, 'Title'] = df['Title'][i].replace('"', '')
            df.loc[i, 'Abstract'] = df['Abstract'][i].replace('"', '')
            # df['Speaker'][i] = df['Speaker'][i].replace('"', '')
            # df['Affiliation'][i] = df['Affiliation'][i].replace('"', '')
            # df['Title'][i] = df['Title'][i].replace('"', '')
            # df['Abstract'][i] = df['Abstract'][i].replace('"', '')
            # if i == len(df)-1 and year == years[0]:
            if i == 0 and year == years[0]:
              html += f'<button class="accordion active">{df["Date"][i]} <br> {df["Speaker"][i]}, {df["Affiliation"][i]} <br> {df["Title"][i]}</button>\n<div class="panel" style="display: block;">\n<p>{df["Abstract"][i]}</p>\n</div>\n'
            else:
              html += f'<button class="accordion">{df["Date"][i]} <br> {df["Speaker"][i]}, {df["Affiliation"][i]} <br> {df["Title"][i]}</button>\n<div class="panel">\n<p>{df["Abstract"][i]}</p>\n</div>\n'
    html += '</div>\n'

# add </body> </html>
html += """
<script>
var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var panel = this.nextElementSibling;
    if (panel.style.display === "block") {
      panel.style.display = "none";
    } else {
      panel.style.display = "block";
    }
  });
}
</script>

</body>
</html>

"""


with open('../uthsc-biostat-seminars.github.io/upcoming/index.html', 'w') as f:
    f.write(html)

print('upcoming/index.html has been generated')
