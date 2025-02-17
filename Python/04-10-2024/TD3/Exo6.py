# Écrivez un algorithme qui convertisse un nombre de la base 10 vers la base 2 (en binaire).
# Le principe utilisé est celui de la division entière.
# Prenons le chiffre 19 pour le convertir en base 2.
# La division entière de 19 par 2 donne un quotient de 9 et un reste de 1.
# La division entière de 9 par 2 donne un quotient de 4 et un reste de 1.
# Plaçons les restes dans l’ordre inverse de leur apparition, nous obtenons « 11 ».
# La division de 4 par 2 donne un quotient de 2 et un reste de 0.
# L’accumulation des restes donne « 011 ».
# La division de 2 par 2 donne un quotient de 1 et un reste de 0.
# L’accumulation des restes donne « 0011 ».
# La division de 1 par 2 donne un quotient de 0 et un reste de 1.
# L’accumulation des restes donne « 10011 ».
# La conversion s’arrête là et le chiffre 19 converti en base 2 est « 10011 »

chiffre = int(input("Convertissons le chiffre que vous saisissez en binaire :\n"))
quotient = chiffre

binaire = []

chaine = ""

while (chiffre > 0 ):
    quotient = chiffre % 2
    binaire.append(quotient)
    chiffre = chiffre // 2
binaire.reverse()
for value in binaire:
    chaine += str(value)

print(chaine)


# CORRECTION 

# n = int(input("Saisir un nombre à convertir en base 2 : "))
# res = ""

# while n != 0:
#     q = n // 2
#     r = n % 2
#     res = str(r) + res
#     print(res)
#     n = q
    


