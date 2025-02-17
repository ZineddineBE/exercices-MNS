# Cherchons à résoudre l’équation « ax + b = 0 ».
# Pour cela, saisissons les deux nombres a et b et affichons le résultat correspondant.
# Si a = 0 et b = 0 alors l’ensemble des solutions est l’ensemble R.
# Si a = 0 et b!= 0 alors l’ensemble des solutions est l’ensemble vide.
# Si a!= 0 alors la solution est (-b / a).

print("=== ON RESOUD L'EQUATION ax + b = 0 ===")

a = int(input("Saisissez la valeur de a : "))
b = int(input("Saisissez la valeur de b : "))

if (a == 0 and b == 0):
    print(f"La solutions de l'équation {a}x + {b} est l’ensemble R.")
elif (a == 0 and b != 0):
    print(f"La solutions de l'équation {a}x + {b} est l’ensemble vide.")
elif (a != 0):
    print(f"La solutions de l'équation {a}x + {b}, {-b/a}")

print("=== FIN DU PROGRAMME ===")
