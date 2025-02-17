from classes.Cup import Cup
from classes.Material import Material
import jsonpickle

f = open("data/cups.json", "r")
my_cup = jsonpickle.decode(f.read())

if not my_cup:

    porcelaine = Material("Porcelaine", 15)
    my_cup = Cup(porcelaine, 330, "Bleu")
    my_cup.fill("Coffee")


f = open("data/cups.json", "w")
f.write(jsonpickle.encode(my_cup))
f.close()

