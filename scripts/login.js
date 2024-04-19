let password = '';
const handleUsernameChange = async node => {
    fetch('/checkUsernameExists', {
        method: "POST",
        body: "username=" + node.value,
    }).then(async response => {
        const responseValue = await response.json();
        /* values should '' or a valid password string */
        if(responseValue.usernameExists !== '') {
            password = responseValue.usernameExists;
            let submitButton = document.getElementById('submitButton');
            submitButton.innerHTML = 'Login';
            document.getElementById('signUpBits').style.display = 'none';

            let faveAnimal = document.getElementById('faveAnimal');
            faveAnimal.required = false;
            let hiddenInput = document.getElementById('signupOrLogin');
            hiddenInput.value = 'login';
        } else {
            password = '';
            let submitButton = document.getElementById('submitButton');
            submitButton.innerHTML = 'Sign Up';
            document.getElementById('signUpBits').style.display = 'block';

            let faveAnimal = document.getElementById('faveAnimal');
            faveAnimal.required = true;
            let hiddenInput = document.getElementById('signupOrLogin');
            hiddenInput.value = 'signup';
        }
    });
};

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
        let containsIllegalChars = false;
        for(let i=0; i<inputs.length; ++i) {
            let input = inputs.item(i);
            if(input.value.includes('=') || input.value.includes('&')) {
                document.getElementById('forbiddenChars').style.display = '';
                containsIllegalChars = true;
                break;
            }
        }
        shouldSubmit = !containsIllegalChars;
        if( shouldSubmit ) {
            document.getElementById('forbiddenChars').style.display = 'none';
        }
        const userEnteredPassword = document.getElementById('password').value;
        if( userEnteredPassword !== password ) {
            shouldSubmit = false;
            document.getElementById('wrongPassword').style.display = '';
        }
        else {
            document.getElementById('wrongPassword').style.display = 'none';
        }
        if(shouldSubmit) {
            e.target.submit();
        }
    };
};