# ------------------------------------ TO DO LIST MONGODB Zineddine BEOUCHE ------------------------------------

import function
import os

cont = True

while cont:
    function.menu()
    choice = input(f"\n{function.BOLD}Voulez-vous continuer ? (o/n) :{function.RESET} ").strip().lower()
    while choice != 'o' and choice !='n':
        print(f"\n{function.WARNING}Choix invalide, saisissez o ou n (o : oui / n : non){function.RESET}\n")
        choice = input(f"\n{function.BOLD}Voulez-vous continuer ? (o/n) :{function.RESET} ").strip().lower()

    if choice != 'o':
        cont = False

print(f"\n\033[1;36mMerci d'avoir utilisé mon programme {os.getenv("USERNAME")} !{function.RESET}")
function.redirection()




    