document.querySelectorAll('.accordion, .nested-accordion').forEach(accordionElement => {
    accordionElement.addEventListener('click', function(event) {
        const targetElement = event.target.closest('.container');
        if (targetElement) {
            targetElement.classList.toggle('active');
        }
        event.stopPropagation();
    });
});
