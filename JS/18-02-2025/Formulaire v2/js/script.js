function formSubmit(event){
    let allValid = true;

    document.getElementById("signUpForm").querySelectorAll(".error").forEach(function(divError){
        divError.classList.remove("error");
        divError.removeChild(divError.querySelector("div"));
    });

    document.getElementById("signUpForm").querySelectorAll("input[required], textarea[required], select[required]").forEach(function(input){
        
        if(input.value.trim() == ""){
            input.closest("div").classList.add("error");
            let div = document.createElement("div");
            let texte = document.createTextNode("Attention, champ obligatoire");
            div.appendChild(texte);
            input.closest("div").appendChild(div);

            allValid = false;
        }
    });

    let inputMail = document.getElementById("email");

    if(inputMail.value != ""){
        const emailRegex = new RegExp("^[A-Za-z0-9.\-_\+]+@[A-Za-z0-9.\-]+[.]{1}[A-Za-z0-9]{2,}$", "i");

        if(!emailRegex.test(inputMail.value)){
            inputMail.closest("div").classList.add("error");
            let div = document.createElement("div");
            let texte = document.createTextNode("Adresse e-mail invalide. Veuillez saisir une adresse au format nom@domaine.fr, par exemple : pierre.dupont@gmail.com.");
            div.appendChild(texte);
            inputMail.closest("div").appendChild(div)
            allValid = false;
        }
    }

    if (!allValid){
        event.preventDefault(); //bloque le submit
    }

}

document.getElementById("signUpForm").addEventListener("submit", formSubmit);
document.getElementById("btn").addEventListener("click", formSubmit);