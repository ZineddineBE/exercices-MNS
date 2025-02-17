# a = int(input("Saisissez un nombre : \n"))
# binary = str(a)
# if (binary[len(binary)-1] == "1"):
#    decimal = 1 
# else:
#     decimal = 0
# for i in range(1, len(binary)):
#     decimal = decimal + int(binary[len(binary)-i-1])*(2**(i*2-i))
# print(decimal)


a = int(input("Saisissez un chiffre en binaire : \n"))
binary = str(a)
coeff = 1
decimal = 0
for i in range(len(binary)):
    decimal = decimal + int(binary[-i-1])*(coeff)
    coeff = coeff * 2
print(f"est égal à {decimal} décimal")


#for i in reversed(binary) ---> parcourir la chaine de caractère à l'envers
