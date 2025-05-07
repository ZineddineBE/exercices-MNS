import { HttpClient } from '@angular/common/http';
import { Component, inject } from '@angular/core';
import { FormBuilder, FormsModule, ReactiveFormsModule, Validators } from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';
import {MatInputModule} from '@angular/material/input';

@Component({
  selector: 'app-inscription',
  imports: [MatButtonModule, MatInputModule, FormsModule, ReactiveFormsModule],
  templateUrl: './inscription.component.html',
  styleUrl: './inscription.component.scss'
})
export class InscriptionComponent {

  formBuilder = inject(FormBuilder);

  http = inject(HttpClient);

  formulaire = this.formBuilder.group(
    {
      email : ['', [Validators.email, Validators.required]],
      password : ['', [Validators.required]],
      confirmPassword : ['', [Validators.required]],
    })
  
  onInscription() {
    if(this.formulaire.valid){
      this.http
      .post("http://localhost:5000/inscription", this.formulaire.value)
      .subscribe(reponse => console.log(reponse))
    }
    
  }

}
