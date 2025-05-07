import { HttpClient } from '@angular/common/http';
import { Component, inject } from '@angular/core';
import { FormsModule } from '@angular/forms';

type Categorie = {
    id: number,
    titre: string,
    images: Image[];
}

type Image = {
    id: number,
    url: string;
}

@Component({
  selector: 'app-accueil',
  imports: [FormsModule],
  templateUrl: './accueil.component.html',
  styleUrl: './accueil.component.scss'
})
export class AccueilComponent {
    urlImageSaisie: string = '';
    nomNouvelleCategorie = "";
    categories: Categorie[] = [];
    categorieSelectionnee: number = 0;

    http = inject(HttpClient);
    
    ngOnInit(){

        this.refresh();

        // const enregistrement = localStorage.getItem('categories');

        // const categoriesParDefaut: Categorie[] = [
        //     {
        //         titre: "S",
        //         images: [],
        //     },
        //     {
        //         titre: "A",
        //         images: [],
        //     },
        //     {
        //         titre: "B",
        //         images: [],

        //     }, 
        //     {
        //         titre: "C",
        //         images: [],
        //     },
        //     {
        //         titre: "D",
        //         images: [],
        //     },
        //     {
        //         titre: "E",
        //         images: [],
        //     }
        // ];

        // if(enregistrement == null){
        //     localStorage.setItem('categories', JSON.stringify(categoriesParDefaut));
            
        // }
        // this.categories = JSON.parse(localStorage.getItem('categories')!);
    }

    refresh(){
        this.http
            .get<Categorie[]>("http://localhost:5000/categories")
            .subscribe(categories => this.categories = categories)
    }

    sauvegarde(){
        localStorage.setItem('categories', JSON.stringify(this.categories));
    }

    onClicAjouterImage(){
        // this.categories[this.categorieSelectionnee].images.push(this.urlImageSaisie);
        // this.sauvegarde();

        this.http
            .post("http://localhost:5000/image", {url: this.urlImageSaisie, categorie_id: this.categorieSelectionnee})
            .subscribe(resultat => this.refresh());

        this.urlImageSaisie = "";
        
    }

    onClicAjouterCategorie(){
        // this.categories.push({
        //     titre : this.nomNouvelleCategorie,
        //     images : [],
        // })
        // this.nomNouvelleCategorie = "";

        // this.sauvegarde();

        this.http
            .post("http://localhost:5000/categorie", {newCategorie: this.nomNouvelleCategorie})
            .subscribe(resultat => 
                this.refresh());

        this.nomNouvelleCategorie = "";
        
    }
    

    deplacerImage(idNouvelleCategorie: number, indexImage: number){ //, descendre : boolean = true
        // let url = this.categories[indexCategorie].images[indexImage];
        // this.categories[indexCategorie + (descendre ? 1 : -1)].images.push(url);

        // this.categories[indexCategorie].images.splice(indexImage, 1);

        // this.sauvegarde();



        this.http.put("http://localhost:5000/image", {indexCategorie: idNouvelleCategorie, id: indexImage})
        .subscribe(() => this.refresh());

    }

    supprimerImage(imageId : number){
        // this.categories[indexCategorie].images.splice(indexImage, 1);
        // this.sauvegarde();

        this.http.delete("http://localhost:5000/image/" + imageId)
        .subscribe(resultat => this.refresh());

    }

    

    supprimerCategorie(indexCategorie : number){
        // this.categories.splice(indexCategorie, 1);

        this.http.delete("http://localhost:5000/categorie/" + indexCategorie)
        .subscribe(resultat => this.refresh());
    }
}
