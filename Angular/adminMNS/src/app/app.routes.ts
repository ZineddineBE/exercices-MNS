import { Routes } from '@angular/router';
import { AccueilComponent } from './pages/accueil/accueil.component';
import { ConnexionComponent } from './pages/connexion/connexion.component';
import { Page404Component } from './pages/page404/page404.component';
import { InscriptionComponent } from './pages/inscription/inscription.component';

export const routes: Routes = [
    {
        path: 'inscription',
        component: InscriptionComponent
    },
    {
        path: 'connexion',
        component: ConnexionComponent
    },
    {
        path: 'accueil',
        component: AccueilComponent
    },
    {
        path: '',
        redirectTo: 'accueil',
        pathMatch: 'full'
    },
    {
        path: '**',
        component: Page404Component
    }
];
