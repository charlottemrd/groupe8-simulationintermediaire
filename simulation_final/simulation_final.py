import matplotlib.pyplot as plt
import math
import csv

# Definition des moyennes sur les resultats experimentaux

#Initialisation des variables
yPoints = []
lineCount = 0
numberOfExperiences = 0
yMean = 0
yVar = []
listEcartType = []
variance = 0

# Exploitation du fichier csv
with open('donnees_simulation.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for row in csv_reader:
        if numberOfExperiences == 0:
            numberOfExperiences = len(row)
            print("\nMoyenne et ecart-type des mesures pour chaque point pour", numberOfExperiences, "experiences similaires : \n")
        for i in range(numberOfExperiences):
            yVar.append(float(row[i]))
            yMean += yVar[i]
        yMean /= numberOfExperiences
        for i in yVar:
            variance += (i - yMean) ** 2
        ecartType = math.sqrt(variance/numberOfExperiences)
        print("Au point", lineCount + 1, " : ", yMean, "m / ", ecartType, " m")

        #Reinitialisation des variables et ajout dans les tableaux
        listEcartType.append(ecartType)
        yPoints.append(yMean)
        yMean = 0
        yVar = []
        lineCount += 1
        variance = 0

# Definition de l'axe temporel
t = [0.000]
nextTimeValue = t[0]
for i in range(lineCount-1):
    nextTimeValue += 0.0400
    t.append(nextTimeValue)

# Definition des resultats theoriques
x = []
for i in range(len(t)):
    x.append(2.25 - 57.88 * math.log(math.cosh(t[i] / 2.42)))

# Definition de la marge d'erreur
margin = 0
delta = [abs(x[i] - yPoints[i]) for i in range(len(x))]
for i in delta:
    margin += i
margin = margin / len(delta)

#Affichage
print("\nLa marge d'erreur moyenne est de", margin / 2.25 * 100, "%")
print("Ce qui equivaut a une erreur moyenne de", margin * 100, "cm")
plt.plot(t, yPoints, "g+-", label="Resultats experimentaux")
plt.plot(t, x, "r+-", label="Resultats theoriques")
plt.plot(t, delta, "b+", label="Marge d'erreur pour chaque point")
plt.errorbar(t, yPoints, listEcartType, color='green', ecolor='skyblue', capsize=3, label="Barre d'erreur pour chaque point")
plt.ylabel("Hauteur (m)")
plt.xlabel("Temps (s)")
plt.legend()
plt.title("Etude du mouvement de la chute d'une balle de Tennis")
plt.show()