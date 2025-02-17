
// Pins Moteurs
#define MOTOR_LEFT_1 9
#define MOTOR_LEFT_2 8
#define MOTOR_LEFT_PWM 10
#define MOTOR_RIGHT_1 7
#define MOTOR_RIGHT_2 6
#define MOTOR_RIGHT_PWM 5

// Pins Capteur Ultrason
#define TRIG_PIN 4
#define ECHO_PIN 3

// Variables globales
long duree;
int distance;

void setup() {
  // Configuration Moteurs
  pinMode(MOTOR_LEFT_1, OUTPUT);
  pinMode(MOTOR_LEFT_2, OUTPUT);
  pinMode(MOTOR_RIGHT_1, OUTPUT);
  pinMode(MOTOR_RIGHT_2, OUTPUT);
  pinMode(MOTOR_LEFT_PWM, OUTPUT);
  pinMode(MOTOR_RIGHT_PWM, OUTPUT);

  // Configuration Capteur Ultrason
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);

  // Communication Série pour débogage
  Serial.begin(9600);
}

// Fonction pour calculer la distance
int calculerDistance() {
  // Envoi impulsion ultrason
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  // Mesure du temps de réponse
  duree = pulseIn(ECHO_PIN, HIGH);

  // Calcul distance en cm
  distance = duree * 0.034 / 2;
  return distance;
}
// Mouvements de base
void arreter() {
  digitalWrite(MOTOR_LEFT_1, LOW);
  digitalWrite(MOTOR_LEFT_2, LOW);
  digitalWrite(MOTOR_RIGHT_1, LOW);
  digitalWrite(MOTOR_RIGHT_2, LOW);
}

void avancer(int vitesse) {
  digitalWrite(MOTOR_LEFT_1, HIGH);
  digitalWrite(MOTOR_LEFT_2, LOW);
  digitalWrite(MOTOR_RIGHT_1, HIGH);
  digitalWrite(MOTOR_RIGHT_2, LOW);

  analogWrite(MOTOR_LEFT_PWM, vitesse);
  analogWrite(MOTOR_RIGHT_PWM, vitesse);
}

void reculer(int vitesse) {
  digitalWrite(MOTOR_LEFT_1, LOW);
  digitalWrite(MOTOR_LEFT_2, HIGH);
  digitalWrite(MOTOR_RIGHT_1, LOW);
  digitalWrite(MOTOR_RIGHT_2, HIGH);

  analogWrite(MOTOR_LEFT_PWM, vitesse);
  analogWrite(MOTOR_RIGHT_PWM, vitesse);
}

void tournerDroite(int vitesse) {
  digitalWrite(MOTOR_LEFT_1, HIGH);
  digitalWrite(MOTOR_LEFT_2, LOW);
  digitalWrite(MOTOR_RIGHT_1, LOW);
  digitalWrite(MOTOR_RIGHT_2, HIGH);

  analogWrite(MOTOR_LEFT_PWM, vitesse);
  analogWrite(MOTOR_RIGHT_PWM, vitesse);
}

void tournerGauche(int vitesse) {
  digitalWrite(MOTOR_LEFT_1, LOW);
  digitalWrite(MOTOR_LEFT_2, HIGH);
  digitalWrite(MOTOR_RIGHT_1, HIGH);
  digitalWrite(MOTOR_RIGHT_2, LOW);

  analogWrite(MOTOR_LEFT_PWM, vitesse);
  analogWrite(MOTOR_RIGHT_PWM, vitesse);
}

void loop() {
  // Mesure de la distance
  int distanceActuelle = calculerDistance();

  // Affichage pour débogage
  Serial.print("Distance : ");
  Serial.print(distanceActuelle);
  Serial.println(" cm");

  // Logique de navigation
  if (distanceActuelle > 30) {
    // Pas d'obstacle, avance normalement
    avancer(200);  // Vitesse moyenne
  } else if (distanceActuelle > 15) {
    // Obstacle proche, ralentit
    avancer(100);
  } else {
    // Obstacle très proche, évitement
    arreter();
    delay(200);

    // Recule un peu
    reculer(150);
    delay(500);

    // Tourne à droite pour éviter
    tournerDroite(200);
    delay(500);
  }

  // Petit délai entre chaque cycle
  delay(100);
}