import numpy as np

#Question 1
#a)
animaux = ["chiens", "chats", "furets", "ratons laveurs", "mulots", "grenouilles"]
#b)
print(animaux)
#c)
print(animaux[2])
#d)
print(animaux[1:4])
#e) Au besoin, afficher avec un print
animaux.remove("mulots")
#f) Au besoin, afficher avec un print
animaux.pop(1)
#g)
print(animaux[1])
#h) Au besoin, afficher avec un print
animaux.append("renards")
#i)
animaux.insert(2, "orignaux")
print(animaux)
#j)
print("La liste animaux contient ", len(animaux), "animaux")

#Question 2
masses = [23, 56, 45.4, 32, 78, 56.9, 23.6, 100.2, 54.3]
elements = ["valise","sac de ciment", "nourriture chien", "enfant", "adulte", "roche", "télévision", "piano", "haltères"]
#a)
print("il y a " , len(masses), " masses dans la liste masses et il y a ", len(elements), "éléments dans la liste elements")
#b)
print("À la position 8, on retrouve l'élément",elements[7], "qui a une masse de", masses[7], "kg" )
#c)
print("La moyenne est",round(np.mean(masses),2), "kg et l'écart-type", round(np.std(masses),2), "kg")
#d)
mon_index = elements.index("adulte") #vous pouvez print(), mais le but est de réutiliser le contenu de la variable, on ne veux pas y aller à l'oeil.
elements.pop(mon_index)
masses.pop(mon_index)

mon_index = elements.index("enfant") #On écrase la valeur de mon_index
elements.pop(mon_index)
masses.pop(mon_index)

#e)

if "valise" in elements:
    mon_index = elements.index("valise")  #j'ai choisi la variabel mon_index, donc j'écraserai la valeur précédente
    masses[mon_index] = masses[mon_index] * 9.8
else:
    elements.append("valise")
    masses.append(34)

print(elements)
print(masses)

if "voiture" in elements:
    mon_index = elements.index("voiture")  #j'ai choisi la variabel mon_index, donc j'écraserai la valeur précédente
    poids = masses[mon_index] * 9.8
    print(poids)
else:
    elements.append("voiture")
    masses.append(2000)

print(elements)
print(masses)


#Réponse note: remplacer les mots par une variable déclarée avant la structure if.
#Réponse note2: valise et Valise sont traités comme des mots différents...


#f)
valeur_min = min(masses)
mon_index_min = masses.index(valeur_min)
masses.pop(mon_index_min)
elements.pop(mon_index_min)

valeur_max = max(masses)
mon_index_max = masses.index(valeur_max)
masses.pop(mon_index_max)
elements.pop(mon_index_max)

print(elements)
print(masses)


#Question 3
#a)
ma_variable = "mot mystère"
liste_mixte = ["neige", 28, "soleil", 55.6, 26, -9, ma_variable, 0.22, (9,8), "pluie", [4,5,6]]
n = len(liste_mixte)

import random #à mettre au début du fichier

nombre_aleatoire = random.randint(1, n)
print(liste_mixte[nombre_aleatoire-1])
if isinstance(liste_mixte[nombre_aleatoire-1], (int, float)):
    print("C'est un nombre")
else:
    print("Ce n'est pas un nombre")
    
#Autres alternative:
if isinstance(liste_mixte[nombre_aleatoire-1], int) or isinstance(liste_mixte[nombre_aleatoire-1], float):
    print("C'est un nombre")
else:
    print("Ce n'est pas un nombre")

#Étape 6 et 7
if isinstance(liste_mixte[nombre_aleatoire-1], (int, float)):
    if liste_mixte[nombre_aleatoire-1] < 1:
        liste_mixte.pop(nombre_aleatoire-1)
        print("C'est un nombre")
elif isinstance(liste_mixte[nombre_aleatoire-1], str):
    liste_mixte[nombre_aleatoire-1] = liste_mixte[nombre_aleatoire-1] + "-vérifié"
    print("C'est une chaîne de caractères")
else:
    print("Ce n'est pas un nombre")

print(liste_mixte)