# 1. Créez une liste de 5 nombres entiers.
# 2. Écrivez une fonction qui prend cette liste en entrée et renvoie la liste inversée (sans
# utiliser les méthodes reverse() ou [::-1] ).
# 3. Affichez la liste originale et la liste inversée.

liste = [5, 4, 8, 2, -65]

liste_inversee = []

for i in range(len(liste)):
    liste_inversee.insert(0, liste[i])

print(f"La liste originale : {liste}")
print(f"La liste inversée : {liste_inversee}")