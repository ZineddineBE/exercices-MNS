const express = require("express");
const cors = require("cors");
const mysql = require("mysql2")
const app = express();

// Configuration de la base de données
const connection = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "",
  database: "tier-list",
});

connection.connect((err) => {
    if (err) {
        console.error("Erreur de connexion à la base de données :", err);
        return;
    }
    console.log("Connecté à la base de données MySQL");
});

app.use(cors());
app.use(express.json());

app.get("/", (req, res) =>{
    res.send('Hello la tcheam c\'est Michou !');
});




app.get("/categories", (req, res) =>{

    connection.query("SELECT c.categorie_id, c.categorie_titre, i.image_url, i.image_id as image_id FROM categorie C LEFT JOIN image i ON c.categorie_id = i.categorie_id ORDER BY c.categorie_id", (err, resultat)=>{
            const categories = [];

            for (let ligne of resultat){

                const categoriesExistantes = categories.find(c => c.id === ligne.categorie_id);
                //si on a déjà ajouté cette catégorie à la liste des résulats
                if(categoriesExistantes){
                    categoriesExistantes.images.push({id: ligne.image_id, url: ligne.image_url});
                } else{
                    categories.push({id: ligne.categorie_id, titre: ligne.categorie_titre, images: (ligne.image_url ? [{id: ligne.image_id, url: ligne.image_url}] : [])});
                }
            }
            res.json(categories);
    });
});

app.post("/image", (req, res) =>{

    connection.query(
        "INSERT INTO image (image_url, categorie_id) VALUES (?, ?)",
        [req.body.url, req.body.categorie_id],
        (err, resultat) => {
            res.json({ message: "Image ajoutée avec succès"})
        });
});

app.delete("/image/:id", (req, res) =>{
    const imageId = req.params["id"];

    connection.query(
        "DELETE FROM image WHERE image_id = ?",
        [imageId],
        (err, resultat) => {
        res.json({ message: "Image supprimée avec succès", deletedId: imageId })
    });
});

app.post("/categorie", (req, res) =>{

    connection.query(
        "INSERT INTO categorie (categorie_titre) VALUES (?)",
        [req.body.newCategorie],
        (err, resultat) => {
            res.json({ message: "Catégorie ajoutée avec succès"})
        });
});

app.delete("/categorie/:id", (req, res) =>{
    const indexCategorie = req.params["id"];

    connection.query(
        "DELETE FROM categorie WHERE categorie_id = ?",
        [indexCategorie],
        (err, resultat) => {
        res.json({ message: "Catégorie supprimée avec succès", deletedId: indexCategorie })
    });
});

app.put("/image", (req, res) =>{

    console.log(req.body);

    connection.query(
        "UPDATE image SET categorie_id = ? WHERE image_id = ?",
        [req.body.indexCategorie, req.body.id],
        (err, resultat) => {
        res.json({ message: "Catégorie déplacée avec succès", imageId: req.body.id })
    });
});


    // const categories = [
    //     {
    //     "titre": "S",
    //     "images": [
    //         "https://media.ouest-france.fr/v1/pictures/MjAyMDExYmUzNzA4N2QyM2Y3NzQxZDk2YTBkMDRjNjIzM2M1ZTI?width=1260&height=708&focuspoint=50%2C25&cropresize=1&client_id=bpeditorial&sign=0542e4177706f55f226b8d0f6f904ed554e6d7401541e76980b0ae0a5ff16dce",
    //         "https://www.dexerto.fr/cdn-image/wp-content/uploads/sites/2/2024/07/09/ichigo-bleach-tybw.jpg?width=1200&quality=60&format=auto",
    //         "https://www.mangabox.fr/wp-content/uploads/2024/08/arc-narratif-mha-1024x576.png",
    //         "https://thegame0.com/wp-content/uploads/2024/03/HXH.webp",
    //         "https://fr.web.img6.acsta.net/pictures/18/09/24/11/16/5831346.jpg",
    //         "https://i0.wp.com/www.cinechos.com/wp-content/uploads/2024/06/banniere-demon-slayer-edited-1.webp"
    //     ]
    //     },
    //     {
    //         "titre": "A",
    //         "images": [
    //             "https://www.fulguropop.com/wp-content/uploads/2020/11/Titan-2.jpg",
    //             "https://preview.redd.it/0qyc2js23m1c1.jpg?auto=webp&s=cddb4afbfcb792365318f6fba2cfc5057b9def02",
    //             "https://i0.wp.com/www.gohanblog.fr/www/wp-content/uploads/2016/03/avis-assassination-classroom.jpg",
    //             "https://sm.ign.com/t/ign_fr/screenshot/default/blob_f41u.1280.jpg",
    //             "https://www.radiofrance.fr/s3/cruiser-production-eu3/2019/06/bb7290f8-b0d1-4ef4-9c50-1d04cf4b69b7/640x340_opm.jpg",
    //             "https://play-lh.googleusercontent.com/otQBqtf2YVXBMjKPNI5C_HRcoe3Wg2dn_yT0tGJCfAqIlNeuhcsbsKZ6d8YbalckK3E9bTE4YG8QRcvvY3c",
    //             "https://cdn-uploads.gameblog.fr/img/news/635307_674055d2e7f49.jpg"
    //         ]
    //     },
    //     {
    //         "titre": "B",
    //         "images": [
    //             "https://occ-0-8407-90.1.nflxso.net/dnm/api/v6/E8vDc_W8CLv7-yMQu8KMEC7Rrr8/AAAABXC_I-eMsDb5BcESLtgdySV0JMklEtYUFtsz4mkx9zaNDuPtK-hdZYAlQoBDwEcVSPsI_JGPUtu9GYmL8SsLVO0cWUwjiBTYtz46.jpg?r=ead",
    //             "https://www.shoshosein.com/sites/default/files/fiches/animes/fire-force/fire-force.jpg",
    //             "https://www.ecranlarge.com/content/uploads/2021/09/fairy-tail-photo-1395482.jpg",
    //             "https://mangaculte.fr/wp-content/uploads/2023/07/Baki-wallpaper.png.webp",
    //             "https://fr.web.img2.acsta.net/pictures/21/06/30/12/00/4012840.jpg",
    //             "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQyZ4cnIli5NxYGVwXY32rUtcc7u128tDFUGQ&s"
    //         ]
    //     },
    //     {
    //         "titre": "C",
    //         "images": [
    //             "https://static.bandainamcoent.eu/high/seven-deadly-sins/seven-deadly-sins/00-page-setup/sds_game-thumbnail.jpg",
    //             "https://fr.web.img4.acsta.net/c_310_420/pictures/21/11/22/10/54/0321052.jpg",
    //             "https://m.media-amazon.com/images/M/MV5BZDAwMzA3MzktNGRhYy00ZDRmLWFjODQtMDI5MDRhZGQxNWVjXkEyXkFqcGdeQWRpZWdtb25n._V1_.jpg"
    //         ]
    //     },
    //     {
    //         "titre": "D",
    //         "images": [
    //             "https://www.radiocampuslorraine.com/wp-content/uploads/2018/01/dgnmydguiaa9cn8.jpg"
    //         ]
    //     },
    //     {
    //         "titre": "E",
    //         "images": [
    //             "https://fr.web.img5.acsta.net/pictures/20/03/10/12/07/4001550.jpg"
    //         ]
    //     },
    //     {
    //         "titre": "Pas vue",
    //         "images": []
    //     }

    // ]
    // res.json(categories);

app.listen(5000, () =>{
    console.log("Server is running on port 5000 !");
});

