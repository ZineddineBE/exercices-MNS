const express = require("express");
const cors = require("cors");
const mysql = require("mysql2");
const bcrypt = require("bcrypt");
const jwtUtil = require("jsonwebtoken");
const app = express();

// Configuration de la base de données
const connection = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "",
  database: "project-angular",
});

// Connexion à la base de données
connection.connect((err) => {
  if (err) {
    console.error("Erreur de connexion à la base de données :", err);
    return;
  }
  console.log("Connecté à la base de données MySQL");
});

app.use(cors());
app.use(express.json());

app.get("/", (req, res) => {
  res.send("hello");
});

app.post("/inscription", (req, res) => {
  const utilisateur = req.body;

  bcrypt.hash(utilisateur.password, 10, (err, hash) => {
    connection.query(
      "INSERT INTO utilisateur (utilisateur_email, utilisateur_password) VALUES (?,?)",
      [utilisateur.email, hash],
      (err, hash) => {
        if (err) {
          console.debug(err);
          return res.sendStatus(500);
        }
        res.json({
          message: "utilisateur : '" + utilisateur.email + "' enregistré",
        });
      }
    );
  });
});

app.post("/connexion", (req, res) => {
  const utilisateur = req.body;

  connection.query(
    "SELECT * FROM utilisateur WHERE utilisateur_email = ?",
    [utilisateur.email],
    (err, resultat) => {
      if (err) {
        console.debug(err);
        return res.sendStatus(500);
      }

      if (resultat.length != 1) {
        return res.sendStatus(401);
      }

      bcrypt.compare(utilisateur.password, resultat[0].utilisateur_password,
        (err, compatible) => {
        console.log(compatible);

          if (err) {
            console.debug(err);
            return res.sendStatus(500);
          }

          if (compatible) {
            return res.send(
                jwtUtil.sign({email : utilisateur.email}, "azerty123")
            );
          }
          return res.sendStatus(401);
        })
    }
  );
});

app.get("/retards", (req, res) => {
  const jwt = req.headers["authorization"];

  if(!jwt) {
    res.sendStatus(401);
  }

  try{
    const data = jwtUtil.verify(jwt, "azerty123");

    connection.query("SELECT * FROM retard", (err, retards) => {
      res.json(retards);
    });
  } catch{
    res.sendStatus(403);
  }
  
});

app.listen(5000, () => {
  console.log("Server is running on port 5000");
});
