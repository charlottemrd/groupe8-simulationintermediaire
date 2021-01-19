# Groupe8-simulationintermediaire

Avant d'exécuter le code, n'oublier d'ajouter les modules et bibilothèques importés en debut de code :
import matplotlib.pyplot as plt
import math
import csv

# Experience et exploitation :
L'expérience realisée est un lancé (sans vitesse initiale) d'une balle de tennis (diamètre : 6,7 cm et masse : 55 g) à 2,20 m du sol.
Les résultats experimentaux ont été obtenus a l'aide d'avimeca, et correspondent à 18 pointages avec un pointage toutes les 0,040 s. 
Le fichier csv contient 5 séries pour la même expérience realisée.
Le but est d'essayer de se rapprocher au maximum des résultats théoriques (qui ont été obtenus en amont).

Pour travailler sur le fichier csv, nous vous conseillons d'ouvrir le fichier à l'aide d'un tableur tel que excel pour avoir une meilleure visibilité

Il est ainsi possible de faire une étude de vos propres résultats, en ajoutant directement au fichier csv 18 valeurs de hauteur de pointages sur une expérience strictement identique (voir paramètres plus haut) et vous pouvez également supprimer les résultats que nous avons obtenus pour ajouter uniquement les vôtres.

Si vous voulez ajouter votre propre expérience, il suffit d'ajouter les valeurs de hauteur que vous avez relevées sur chaque pointage comme précédemment (en supprimant les valeurs de notre expérience), mais il ne faut pas oublier de modifier les résultats théoriques !
Ceux-ci sont definis dans la partie commentée par # Definition des résultats theoriques à la ligne 50 :
Il s' agira alors de modifier l'équation comprise dans x.append() : celle ci est definie en fonction du temps t[i] qui dépend de chaque itération.

Pour que la modification des résultats experimentaux ne provoque aucune erreur, il faut bien faire attention à ce que chaque colonne contienne uniquement les résultats d'une même expérience (une valeur de hauteur a chaque ligne), et que toutes les colonnes fassent le même nombre de lignes.
