# Groupe8-simulationintermediaire

Avant d'exécuter le code, n'oublier d'ajouter les modules et bibilothèques importés en debut de code :
import matplotlib.pyplot as plt
import math
import csv

# Experience et exploitation :
L'expérience realisé est un lancé (sans vitesse initiale) d'une balle de tennis (diametre : 6,7 cm et masse : 55 g) a 2,20 m du sol.
Les resultats experimentaux ont été obtenus a l'aide d'avimeca, et correspondent à 18 pointages avec un pointage toutes les 0,040 s. 
Le fichier csv contient 5 séries pour la même expérience realisée.
Le but est d'essayer de se rapprocher au maximum des résultats théoriques (qui ont été obtenus en amont).

Pour travailler sur le fichier csv, nous vous conseillons d'ouvrir le fichier à l'aide d'un tableur tel que excel pour avoir une meilleure visibilite

Il est ainsi possible de faire une étude de vos propres résultats, en ajoutant directement au fichier csv 18 valeurs de hauteur de pointages sur une expérience strictement identique (voir parametres plus haut) et vous pouvez également supprimer les résultats que nous avons obtenus pour ajouter uniquement les vôtres.

Si vous voulez ajouter votre propre expérience, il suffit d'ajouter les valeurs de hauteur que vous avez relevées sur chaque pointage comme precedemment (en supprimant les valeurs de notre experience), mais il ne faut pas oublier de modifier les résultats théoriques !
ceux ci sont definis dans la partie commentee par # Definition des resultats theoriques à la ligne 50 :
il s' agira alors de modifier l'équation comprise dans x.append() : celle ci est definie en fonction du temps t[i] qui depend de chaque itération.

Pour que la modification des résultats experimentaux ne provoque aucune erreur, il faut bien faire attention à ce que chaque colonne contienne uniquement les résultats d'une même experience (une valeur de hauteur a chaque ligne), et que toutes les colonnes fassent le même nombre de lignes.
