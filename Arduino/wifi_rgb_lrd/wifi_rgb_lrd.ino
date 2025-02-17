/*
 * Ce code Arduino a été développé par newbiely.fr
 * Ce code Arduino est mis à disposition du public sans aucune restriction.
 * Pour des instructions complètes et des schémas de câblage, veuillez visiter:
 * https://newbiely.fr/tutorials/arduino/arduino-uno-r4-wifi-controls-led-via-web
*/

#include <WiFiS3.h>

#define borneENA 10       // On associe la borne "ENA" du L298N à la pin D10 de l'arduino
#define borneIN1 9        // On associe la borne "IN1" du L298N à la pin D9 de l'arduino
#define borneIN2 8        // On associe la borne "IN2" du L298N à la pin D8 de l'arduino
#define borneIN3 7        // On associe la borne "IN3" du L298N à la pin D7 de l'arduino
#define borneIN4 6        // On associe la borne "IN4" du L298N à la pin D6 de l'arduino
#define borneENB 5        // On associe la borne "ENB" du L298N à la pin D5 de l'arduino
#define Broche_Echo 3     // Broche Echo du HC-SR04 sur D7 //
#define Broche_Trigger 4  // Broche Trigger du HC-SR04 sur D8 //

// const int redPin = 7; // R petal on RGB LED module connected to digital pin 11
// const int greenPin = 6; // G petal on RGB LED module connected to digital pin 9
// const int bluePin = 5; // B petal on RGB LED module connected to digital pin 10
// const int alim = 8; // B petal on RGB LED module connected to digital pin 10

const char ssid[] = "Xiaomi 13";  // change your network SSID (name)
const char pass[] = "zizou5798";  // change your network password (use for WPA, or use as key for WEP)

int status = WL_IDLE_STATUS;

WiFiServer server(80);

void setup() {
  //Initialize serial and wait for port to open:
  Serial.begin(9600);

  // Configuration de toutes les pins de l'Arduino en "sortie" (car elles attaquent les entrées du module L298N)
  pinMode(borneENA, OUTPUT);
  pinMode(borneIN1, OUTPUT);
  pinMode(borneIN2, OUTPUT);
  pinMode(borneIN3, OUTPUT);
  pinMode(borneIN4, OUTPUT);
  pinMode(borneENB, OUTPUT);

  // Configuration de toutes les pins pour le capteur de distance
  pinMode(Broche_Trigger, OUTPUT);  // Broche Trigger en sortie //
  pinMode(Broche_Echo, INPUT);      // Broche Echo en entree //
  // pinMode(redPin, OUTPUT); // sets the redPin to be an output
  // pinMode(greenPin, OUTPUT); // sets the greenPin to be an output
  // pinMode(bluePin, OUTPUT); // sets the bluePin to be an output
  // pinMode(alim, OUTPUT); // sets the alim to be an output

  String fv = WiFi.firmwareVersion();
  if (fv < WIFI_FIRMWARE_LATEST_VERSION) {
    Serial.println("Please upgrade the firmware");
  }

  // attempt to connect to WiFi network:
  while (status != WL_CONNECTED) {
    Serial.print("Attempting to connect to SSID: ");
    Serial.println(ssid);
    // Connect to WPA/WPA2 network. Change this line if using open or WEP network:
    status = WiFi.begin(ssid, pass);

    // wait 10 seconds for connection:
    delay(10000);
  }
  server.begin();
  // you're connected now, so print out the status:
  printWifiStatus();
}

void loop() {
  // listen for incoming clients
  WiFiClient client = server.available();
  if (client) {
    // read the first line of HTTP request header
    String HTTP_req = "";
    while (client.connected()) {
      if (client.available()) {
        Serial.println("New HTTP Request");
        HTTP_req = client.readStringUntil('\n');  // read the first line of HTTP request
        Serial.print("<< ");
        Serial.println(HTTP_req);  // print HTTP request to Serial Monitor
        break;
      }
    }

    // read the remaining lines of HTTP request header
    while (client.connected()) {
      if (client.available()) {
        String HTTP_header = client.readStringUntil('\n');  // read the header line of HTTP request

        if (HTTP_header.equals("\r"))  // the end of HTTP request
          break;

        Serial.print("<< ");
        Serial.println(HTTP_header);  // print HTTP request to Serial Monitor
      }
    }

    if (HTTP_req.indexOf("GET") == 0) {           // check if request method is GET
                                                  // expected header is one of the following:
                                                  // - GET led1/on
                                                  // - GET led1/off
      if (HTTP_req.indexOf("led1/rouge") > -1) {  // check the path
                                                  // digitalWrite(alim, HIGH);
        // color(255, 0, 0); // turn the RGB LED red                  // turn off LED
        Serial.println("Turned LED red");
        delay(1000);
        // digitalWrite(alim, LOW);

      } else if (HTTP_req.indexOf("avancer") > -1) {  // check the path
        avancer();
       
      } else if (HTTP_req.indexOf("reculer") > -1) {  // check the path
        reculer();
      }else if (HTTP_req.indexOf("stop") > -1) {  // check the path
        stop(2000);
      } else if (HTTP_req.indexOf("led1/vert") > -1) {  // check the path
                                                        // digitalWrite(alim, HIGH);
        // color(0,255, 0); // turn the RGB LED green
        Serial.println("Turned LED green");
      } else if (HTTP_req.indexOf("led1/bleu") > -1) {  // check the path
                                                        // digitalWrite(alim, HIGH);
        // color(0, 0, 255); // turn the RGB LED blue
        Serial.println("Turned LED blue");
      } else {
        Serial.println("No command");
      }
    }

    // send the HTTP response
    // send the HTTP response header
    client.println("HTTP/1.1 200 OK");
    client.println("Content-Type: text/html");
    client.println("Connection: close");  // the connection will be closed after completion of the response
    client.println();                     // the separator between HTTP header and body
    // send the HTTP response body
    client.println("<!DOCTYPE HTML>");
    client.println("<html>");
    client.println("<head>");
    client.println("<link rel=\"icon\" href=\"data:,\">");
    client.println("</head>");
    client.println("<a href=\"/led1/rouge\">LED ROUGE</a>");
    client.println("<br><br>");
    client.println("<a href=\"/led1/vert\">LED VERT</a>");
    client.println("<br><br>");
    client.println("<a href=\"/led1/bleu\">LED BLEU</a>");
    client.println("<br><br>");
    client.println("<a href=\"/avancer\">AVANCER</a>");
    client.println("<br><br>");
    client.println("<a href=\"/reculer\">RECULER</a>");
    client.println("<br><br>");
    client.println("<a href=\"/stop\">STOP</a>");
    client.println("</html>");
    client.flush();

    // give the web browser time to receive the data
    delay(10);

    // close the connection:
    client.stop();
  }
}

void printWifiStatus() {
  // print your board's IP address:
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());

  // print the received signal strength:
  Serial.print("signal strength (RSSI):");
  Serial.print(WiFi.RSSI());
  Serial.println(" dBm");
}

// void color (unsigned char red, unsigned char green, unsigned char blue) // the color generating function
// {
//   analogWrite(redPin, red);
//   analogWrite(bluePin, blue);
//   analogWrite(greenPin, green);
// }

void lancerRotationMoteurPontA() {
  digitalWrite(borneENA, HIGH);  // Active l'alimentation du moteur 1S
  // delay(2000);                        // et attend 2 secondes

  // digitalWrite(borneENA, LOW);        // Désactive l'alimentation du moteur 1
  // delay(1000);                        // et attend 1 seconde
}

void lancerRotationMoteurPontB() {
  digitalWrite(borneENB, HIGH);  // Active l'alimentation du moteur 1
  // delay(2000);                        // et attend 2 secondes

  // digitalWrite(borneENB, LOW);        // Désactive l'alimentation du moteur 1
  // delay(1000);                        // et attend 1 seconde
}

void reculer() {
  digitalWrite(borneIN1, HIGH);
  digitalWrite(borneIN2, LOW);

  digitalWrite(borneIN3, LOW);
  digitalWrite(borneIN4, HIGH);
  lancerRotationMoteurPontA();
  lancerRotationMoteurPontB();
}

void avancer() {
  digitalWrite(borneIN1, LOW);
  digitalWrite(borneIN2, HIGH);

  digitalWrite(borneIN3, HIGH);
  digitalWrite(borneIN4, LOW);
  lancerRotationMoteurPontA();
  lancerRotationMoteurPontB();
}

// Fonction qui arrête la voiture pendant x temps
void stop(int Timer) {
  digitalWrite(borneENA, LOW);
  digitalWrite(borneENB, LOW);

  delay(Timer);
}
