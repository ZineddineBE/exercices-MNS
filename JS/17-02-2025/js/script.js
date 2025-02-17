let buttonFR = document.getElementById("btn-fr");
let buttonEN = document.getElementById("btn-en");
let buttonList = document.getElementById("btn-list");
let h1 = document.querySelector("h1");

buttonEN.style.display = "none";

buttonFR.addEventListener("click", function(){

    h1.innerText = "Bonjour le monde !";
    h1.classList.toggle("french");
    buttonFR.style.display = "none";
    buttonEN.style.display = "block";
    buttonList.innerText = "Ajouter un élément dans la liste";
    document.querySelectorAll("li").forEach(function(li) {
        li.innerText = "Élément crée avec JS";
    });
});

buttonEN.addEventListener("click", function(){

    h1.innerText = "Hello World !";
    h1.classList.remove("french");
    buttonFR.style.display = "block";
    buttonEN.style.display = "none";
    buttonList.innerText = "Add an element in the list";
    document.querySelectorAll("li").forEach(function(li) {
        li.innerText = "Element created with JS";
    });
});

buttonList.addEventListener("click", function(){

    let li = document.createElement("li");
    let text;
    if (h1.innerText.match(/^Bonjour/)){
        text = document.createTextNode("Élément crée avec JS");
    } else{
        text = document.createTextNode("Element created with JS");
    }
    li.appendChild(text);
    document.getElementById("list").appendChild(li);

});