document.querySelectorAll(".addCart").forEach(function(button){
    button.addEventListener("click", function(){
        console.log(this.closest("article").querySelector("h3").innerText);
        console.log("Id: " + this.getAttribute("data-id")+ "\n\n");
    });
});