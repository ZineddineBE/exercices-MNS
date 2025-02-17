# Écrivez l’algorithme qui affiche à l’écran les lignes suivantes :
# 10 11 12 13 14 15
# 20 21 22 23 24 25
# 30 31 32 33 34 35
# 40 41 42 43 44 45
# 50 51 52 53 54 55

# chaine = ""
# chaine2 = ""
# chaine3 = ""
# chaine4 = ""
# chaine5 = ""

# for i in range(10, 16):
#     chaine += str(i) + " "
# for i in range(20, 26):
#     chaine2 += str(i) + " "
# for i in range(30, 36):
#     chaine3 += str(i) + " "
# for i in range(40, 46):
#     chaine4 += str(i) + " "
# for i in range(50, 56):
#     chaine5 += str(i) + " "

# print(f"{chaine}\n{chaine2}\n{chaine3}\n{chaine4}\n{chaine5}")


value = 10
for i in range(5):
    for j in range(6):
        print(value, end = " ")
        value += 1
    value += 4
    print()


# CORRECTION

# for row in range(1, 6):
#     for col in range(0, 6):
#         print(f"{row}{col}", end=" ")
#     print()

# for row in range(10, 60, 10):
#     for col in range(0, 6):
#         print(f"{row + col}", end=" ")
#     print()

# table = ""
# for row in range(10, 60, 10):
#     for col in range(0, 6):
#         table += f"{row + col} "
#     table += "\n"
    
# print(table)