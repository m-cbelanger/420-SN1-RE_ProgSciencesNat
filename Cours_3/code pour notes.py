

def jeux_olympiques(annee):
    bissextile = annee_bissextile(annee)
    if bissextile == True:
        return "été"
    elif annee % 2 == 0:
        return "hiver"
    
def annee_bissextile(annee):
    if annee % 4 == 0:
        return True;
    return False;
    
print(jeux_olympiques(2026))



def fonction_a():
    print('fonction_a() début')
    fonction_b()
    fonction_d()
    print('fonction_a() fin')

def fonction_b():
    print('fonction_b() début')
    fonction_c()
    print('fonction_b() fin')

def fonction_c():
    print('fonction_c() début')
    print('fonction_c() fin')

def fonction_d():
    print('fonction_d() début')
    print('fonction_d() fin')

fonction_a()





compteur_global = 0
echantillon_test = 5

def prise_temperature(temperature, num_echantillon):
    global compteur_global
    if (num_echantillon == echantillon_test):
        compteur_global += 1
    if (temperature > 37):
        return "chaud"
    else:
        return "froid"


def prise_pH(pH, num_echantillon):
    global compteur_global
    if (num_echantillon == echantillon_test):
        compteur_global += 1
    if (pH < 7):
        return "acide"
    elif (pH == 7):
        return "neutre"
    else:
        return "basique"

print(compteur_global)
prise_pH(8, 6)
prise_pH(8.2, 5)
prise_temperature(28, 5)
prise_temperature(39, 9)
prise_pH(7.8, 5)
print(compteur_global)




constante_acceleration_gravite = 9.8

def calculer_energie_potentielle(masse, hauteur):
    energie_potentielle = masse * constante_acceleration_gravite * hauteur
    return energie_potentielle

# Utilisation de la variable globale "constante_acceleration_gravite" dans la fonction
resultat_energie = calculer_energie_potentielle(2, 5)
print("L'énergie potentielle est :", resultat_energie)