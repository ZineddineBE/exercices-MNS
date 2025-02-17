# Le contrôle d’une centrale nucléaire se fait par l’examen de températures.
# Si la différence entre la température ambiante et la température des bassins de refroidissement est
# inférieure à 20 °C ou si elle dépasse 40 °C, affichez une alarme.

print("=== CALCUL DE LA DIFFERENCE DE TEMPERATURE ENTRE LA TEMPERATURE AMBIANTE ET LA TEMPERATURE DES BASSINS DE REFROIDISSEMENT ===")

temp_ambiante = float(input("Saisissez la valeur de la température ambiante : "))
temp_bassins_refroidissement = float(input("Saisissez la valeur de la température des bassins de refroidissement : "))

delta_temp = abs(temp_ambiante - temp_bassins_refroidissement)

if (delta_temp < 20 or delta_temp > 40):
    print("ALERTE !!! PROBLEME DE TEMPERATURE !!!")
else:
    print("Tout va bien.")

print("=== FIN DU PROGRAMME ===")

