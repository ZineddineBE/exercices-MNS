//*******************************************************************************//
// Association des entrées du L298N, aux sorties utilisées sur notre Arduino Uno //
//*******************************************************************************//
#define borneENA        10      // On associe la borne "ENA" du L298N à la pin D10 de l'arduino
#define borneIN1        9       // On associe la borne "IN1" du L298N à la pin D9 de l'arduino
#define borneIN2        8       // On associe la borne "IN2" du L298N à la pin D8 de l'arduino
#define borneIN3        7       // On associe la borne "IN3" du L298N à la pin D7 de l'arduino
#define borneIN4        6       // On associe la borne "IN4" du L298N à la pin D6 de l'arduino
#define borneENB        5       // On associe la borne "ENB" du L298N à la pin D5 de l'arduino
#define Broche_Echo 3 // Broche Echo du HC-SR04 sur D7 //
#define Broche_Trigger 4 // Broche Trigger du HC-SR04 sur D8 //

// Definition des variables pour le capteur de distance
int MesureMaxi = 300; // Distance maxi a mesurer //
int MesureMini = 3; // Distance mini a mesurer //
long Duree;
long Distance;

int Timer;

//*******//
// SETUP //
//*******//
void setup() {
  
  // Configuration de toutes les pins de l'Arduino en "sortie" (car elles attaquent les entrées du module L298N)
  pinMode(borneENA, OUTPUT);
  pinMode(borneIN1, OUTPUT);
  pinMode(borneIN2, OUTPUT);
  pinMode(borneIN3, OUTPUT);
  pinMode(borneIN4, OUTPUT);
  pinMode(borneENB, OUTPUT);

  // Configuration de toutes les pins pour le capteur de distance
  pinMode(Broche_Trigger, OUTPUT); // Broche Trigger en sortie //
  pinMode(Broche_Echo, INPUT); // Broche Echo en entree //
  Serial.begin (9600);
}

//**************************//
// Boucle principale : LOOP //
//**************************//
void loop() {

 

  // Debut de la mesure avec un signal de 10 µS applique sur TRIG //
  digitalWrite(Broche_Trigger, LOW); // On efface l'etat logique de TRIG //
  delayMicroseconds(2);
  digitalWrite(Broche_Trigger, HIGH); // On met la broche TRIG a "1" pendant 10µS //
  delayMicroseconds(10);
  digitalWrite(Broche_Trigger, LOW); // On remet la broche TRIG a "0" //
  // On mesure combien de temps le niveau logique haut est actif sur ECHO //
  Duree = pulseIn(Broche_Echo, HIGH);
  // Calcul de la distance grace au temps mesure //
  Distance = Duree*0.034/2; // *** voir explications apres l'exemple de code *** //
  // Verification si valeur mesuree dans la plage //
  if (Distance >= MesureMaxi || Distance <= MesureMini) {
  // Si la distance est hors plage, on affiche un message d'erreur //
    Serial.println("Distance de mesure en dehors de la plage (3 cm à 3 m)");
  }
  else {
    // Affichage dans le moniteur serie de la distance mesuree //
    Serial.print("Distance mesuree :");
    Serial.print(Distance);
    Serial.println("cm");
  }
  // Puis... on boucle à l'infini !

  if (Distance < 50) {
    stop(1000);
    reculer(1000);
  }
  avancer();

}



//************************************************************************************//
// Fonction : lancerRotationMoteurPontA()                                             //
// But :      Active l'alimentation du moteur branché sur le pont A                   //
//            pendant 2 secondes, puis le met à l'arrêt (au moins 1 seconde)          //
//************************************************************************************//
void lancerRotationMoteurPontA() {
  digitalWrite(borneENA, HIGH);       // Active l'alimentation du moteur 1S
  // delay(2000);                        // et attend 2 secondes
  
  // digitalWrite(borneENA, LOW);        // Désactive l'alimentation du moteur 1
  // delay(1000);                        // et attend 1 seconde
}

void lancerRotationMoteurPontB() {
  digitalWrite(borneENB, HIGH);       // Active l'alimentation du moteur 1
  // delay(2000);                        // et attend 2 secondes
  
  // digitalWrite(borneENB, LOW);        // Désactive l'alimentation du moteur 1
  // delay(1000);                        // et attend 1 seconde
}

// Fonction qui fait avancer la voiture
void avancer() {
    digitalWrite(borneIN1, HIGH);                  
  digitalWrite(borneIN2, LOW);

  digitalWrite(borneIN3, LOW);                  
  digitalWrite(borneIN4, HIGH);
  lancerRotationMoteurPontA();
  lancerRotationMoteurPontB();
}

// Fonction qui arrête la voiture pendant x temps
void stop(int Timer) {
  digitalWrite(borneENA, LOW); 
  digitalWrite(borneENB, LOW);

  delay(Timer);
}

// Fonction qui fait reculer la voiture pendant x temps
void reculer(int Timer) {

  digitalWrite(borneIN1, LOW);                  
  digitalWrite(borneIN2, HIGH);

  digitalWrite(borneIN3, HIGH);                  
  digitalWrite(borneIN4, LOW);
    lancerRotationMoteurPontA();
  lancerRotationMoteurPontB();

  delay(Timer);
  
}