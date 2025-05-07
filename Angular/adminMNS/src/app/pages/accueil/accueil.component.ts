import { HttpClient } from '@angular/common/http';
import { Component, inject } from '@angular/core';

@Component({
  selector: 'app-accueil',
  imports: [],
  templateUrl: './accueil.component.html',
  styleUrl: './accueil.component.scss'
})

export class AccueilComponent {

  http = inject(HttpClient)

  retards: Retard[] = [];

  ngOnInit() {

    const jwt = localStorage.getItem("jwt")

    if(jwt){

      this.http.get<Retard[]>("http://localhost:5000/retards", 
        {
          headers : {Authorization : jwt! },
        })
      .subscribe(retards => this.retards = retards)

    }
  }

  
}
