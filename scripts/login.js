window.onload = e => {
    const colours = ['Aqua', 'Black', 'Blue', 'Fuchsia', 'Gray', 'Green', 'Lime', 
        'Maroon', 'Navy', 'Olive', 'Purple', 'Red', 'Silver', 'Teal', 'Yellow'];

    let coloursDropdown = document.getElementById('faveColour');
    colours.forEach(colour => {
        coloursDropdown.innerHTML +=
            "<option value=\"" + colour.toLowerCase() + "\">" + 
                colour + 
            "</option>";
    });

    const animalSizes = ['tiny', 'small', 'medium', 'large', 'gigantic'];
    let animalsDropdown = document.getElementById('animalSize');
    animalSizes.forEach(size => {
        animalsDropdown.innerHTML +=
            "<option value=\"" + size.toLowerCase() + "\">" + 
                size + 
            "</option>";
    });

    document.getElementById('form').onsubmit = e => {
        e.preventDefault();
        let shouldSubmit = true;
        let inputs = document.getElementsByTagName('input');
        for(let i=0; i<inputs.length; ++i) {
            let input = inputs.item(i);
            if(input.value.includes('=') || input.value.includes('&')) {
                document.getElementById('forbiddenChars').style.display = '';
                shouldSubmit = false;
            }
        }
        if(shouldSubmit) {
            e.target.submit();
        }
    };
};