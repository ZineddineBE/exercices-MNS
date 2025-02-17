# 1. Créez une liste contenant les prénoms suivants : "Alice", "Bob", "Charlie", "David",
# "Eve".
# 2. Affichez le premier et le dernier élément de la liste.
# 3. Ajoutez le prénom "Frank" à la liste.
# 4. Remplacez le prénom "David" par "Daniel".
# 5. Supprimez le prénom "Charlie" de la liste.
# 6. Affichez la longueur de la liste à chaque étape.


prenoms = ["Alice", "Bob", "Charlie", "David", "Eve"]
print(f"Taille de la liste à l'étape 1 : {len(prenoms)}\n")

print(prenoms[0])
print(prenoms[len(prenoms)-1])
print(f"Taille de la liste à l'étape 2 : {len(prenoms)}\n")


prenoms.append("Frank")
print(f"Taille de la liste à l'étape 3 : {len(prenoms)}\n")

prenoms = list(map(lambda x: x.replace('David', 'Daniel'), prenoms))
print(f"Taille de la liste à l'étape 4 : {len(prenoms)}\n")

prenoms.remove("Charlie")
print(f"Taille de la liste à l'étape 5 : {len(prenoms)}\n")


