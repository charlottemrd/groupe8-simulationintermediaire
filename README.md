# groupe8-simulationintermediaire

/!\ ne pas oublier d'ajouter les modules et bibilothèques importes en debut de code :
import matplotlib.pyplot as plt
import math
import csv

experience et exploitation :
l'experience realise est un lance (sans vitesse initiale) d'une balle de tennis (diametre : 6,7 cm et masse : 55 g) a 2,20 m du sol.
les resultats experimentaux ont ete obtenus a l'aide d'avimeca, et correspondent a 18 pointages avec un pointage toutes les 0,040 s. 
le fichier csv contient 5 series pour la meme experience realisee.
le but est d'essayer de se rapprocher au maximum des resultats theoriques (qui ont ete obtenus en amont).

pour travailler sur le fichier csv, nous vous conseillons d'ouvrir le fichier a l'aide d'un tableur tel que excel pour avoir une meilleure visibilite

il est ainsi possible de faire une etude de vos propres resultats, en ajoutant directement au fichier csv 18 valeurs de hauteur de pointages sur une experience strictement identique (voir parametres plus haut) et vous pouvez egalement supprimer les resultats que nous avons obtenus pour ajouter uniquement les votres.

si vous voulez ajouter votre propre experience, il suffit d'ajouter les valeurs de hauteur que vous avez relevees sur chaque pointage comme precedemment (en supprimant les valeurs de notre experience), mais il ne faut pas oublier de modifier les resultats theoriques !
ceux ci sont definis dans la partie commentee par # Definition des resultats theoriques à la ligne 50 :
il sagira alors de modifier l'equation comprise dans x.append() : celle ci est definie en fonction du temps t[i] qui depend de chaque iteration.

Pour que la modification des resultats experimentaux ne provoque aucune erreur, il faut bien faire attention à ce que chaque colonne contienne uniquement les resultats d'une meme experience (une valeur de hauteur a chaque ligne), et que toutes les colonnes fassent le meme nombre de lignes.
