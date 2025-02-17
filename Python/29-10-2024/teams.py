from random import randint

ran1 = ["Lilian", "LaitA", "Zineddine", "Luc", "Aurélia", "Nine", "Carmello", "Mehdi", "Jordane", "Franck", "Jim", "José", "vide"]
ran2 = ["Yannick", "Flavio", "Julian", "Alexandra", "Anthony", "Arnaud", "Alexandre", "Océane", "Ruzyanna", "Sarah", "Abdel", "Lucas", "Nabil"]

team1 = []
team2 = []
team3 = []
team4 = []
team5 = []
team6 = []
team7 = []
team8 = []
team9 = []
team10 = []
team11 = []
team12 = []

teams = [team1, team2, team3, team4, team5, team6, team7, team8, team9, team10, team11, team12]

for team in teams:
    i = 12
    n = 12
    eleve1 = randint(0,i)
    eleve2 = randint(0,n)
    print(eleve1)
    print(eleve2)
    team.append(ran1[eleve1])
    team.append(ran2[eleve2])

    ran1.remove(ran1[eleve1])
    ran2.remove(ran2[eleve2])

    i = i-1
    n = n-1

    print(team)


