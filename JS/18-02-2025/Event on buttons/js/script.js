let modal = document.getElementById("modal");
let buttonDisplayModal = document.getElementById("displayModal");
let buttonCloseModal = document.getElementById("closeModal");
let backModal = document.getElementById("backModal");

buttonDisplayModal.addEventListener("click", function(){
    modal.style.display = "flex";
    document.querySelector("#modal>div").focus();
});

buttonCloseModal.addEventListener("click", function(){
    modal.style.display = "none";
});

buttonDisplayModal.addEventListener("focus", function(){
    document.querySelector("#modal>div").focus();
});
