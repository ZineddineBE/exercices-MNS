document.querySelectorAll(".moins").forEach(function(moinsButton) {
    moinsButton.addEventListener("click", function() {
        let quantiteElement = this.closest("article").querySelector(".quantiteArticle");
        let qte = parseInt(quantiteElement.innerText);
        if (qte > 0) { 
            qte -= 1;
        }
        quantiteElement.innerText = qte;
    });
});

document.querySelectorAll(".plus").forEach(function(plusButton) {
    plusButton.addEventListener("click", function() {
        let quantiteElement = this.closest("article").querySelector(".quantiteArticle");
        let qte = parseInt(quantiteElement.innerText);
        qte += 1;
        quantiteElement.innerText = qte;
    });
});

document.querySelectorAll(".addCart").forEach(function(button) {
    button.addEventListener("click", function() {
        let nomArticle = this.closest("article").querySelector("h3").innerText;
        let prix = parseFloat(this.closest("article").querySelector("span").innerText.replace("€", ""));

        let quantiteElement = this.closest("article").querySelector(".quantiteArticle");
        let qte = parseInt(quantiteElement.innerText);

        if (qte === 0) {
            return;
        }

        let nomTable = document.querySelectorAll(".nomArticle");
        let quantiteTable = document.querySelectorAll(".quantite");
        let prixTable = document.querySelectorAll(".prix");
        let quantiteTotale = document.getElementById("quantiteTotale");
        let prixTotal = document.getElementById("prixTotal");

        let total = parseFloat(prixTotal.innerText.replace("€", ""));
        let totalQuantite = parseInt(quantiteTotale.innerText);

        if (isNaN(total)) {
            total = 0;
        }

        if (isNaN(totalQuantite)) {
            totalQuantite = 0;
        }

        for (let i = 0; i < nomTable.length; i++) {
            if (nomTable[i].innerText === "") { 
                nomTable[i].innerText = nomArticle;
                quantiteTable[i].innerText = qte;
                prixTable[i].innerText = (prix * qte).toFixed(2) + "€";
                total += prix * qte;
                totalQuantite += qte;
                break;
            } else if (nomTable[i].innerText === nomArticle) {
                let quantite = parseInt(quantiteTable[i].innerText) + qte;
                quantiteTable[i].innerText = quantite;

                let prixArticles = prix * quantite;
                prixTable[i].innerText = prixArticles.toFixed(2) + "€";

                total += prix * qte;
                totalQuantite += qte;
                break;
            }
        }

        prixTotal.innerText = total.toFixed(2) + "€";
        quantiteTotale.innerText = totalQuantite;
        quantiteElement.innerText = "0";
    });
});