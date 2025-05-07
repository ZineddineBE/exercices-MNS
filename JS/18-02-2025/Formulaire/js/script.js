document.getElementById("signUpForm").addEventListener("submit", function(event){
    let allValid = true;
    
    // "lastname", "firstname", "email", "password", "confirmPassword"
    let inputArray = [];

    let inputs = document.getElementsByClassName("input");
    for (let i = 0; i < inputs.length-2; i++) {
      inputArray.push(inputs[i].id);
    }

    console.log(inputArray);

    for(let inputId of inputArray){
        let input = this.querySelector("#" + inputId);

        if(input.value.trim() == ""){
            input.closest("div").classList.add("error");
            let div = document.createElement("div");
            let texte = document.createTextNode("Attention, champ oblogatoire");
            div.appendChild(texte);
            input.closest("div").appendChild(div);

            allValid = false;
        }

    }

    input = this.querySelector("#email");
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

    if(input.value.trim() == "" || !emailRegex.test(input.value.trim())){
        input.closest("div").classList.add("error");
        let div = document.createElement("div");
        let texte = document.createTextNode("Attention, champ oblogatoire");
        div.appendChild(texte);
        input.closest("div").appendChild(div);

        allValid = false;
    }

    if (!allValid){
        event.preventDefault(); //bloque le submit
    }

});