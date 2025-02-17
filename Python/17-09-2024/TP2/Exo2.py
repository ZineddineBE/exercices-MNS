#Saisir trois nombres et afficher un message indiquant s’ils sont triés en ordre croissant ou non.

print("=== Affiche un message si les 3 nombres sont dans l'ordre croissant ou non ===")

nb1 = int(input("Premier nombre : "))
nb2 = int(input("Second nombre : "))
nb3 = int(input("Troisième nombre : "))

if (nb1 < nb2 and nb2 < nb3):
    print("Les nombres sont dans l'ordre croissant")
elif (nb1 == nb2 and nb2 == nb3):
    print("Les nombres sont égaux")
else:
    print("Les nombres NE sont PAS dans l'ordre croissant")

print("=== FIN DU PROGRAMME ===")

