import math
#Q1 a)
def determinant(a, b, c):
    det = b**2 - 4*a*c
    return det

def zero_quadratique(a,b,c):
    if determinant(a,b,c) < 0:
        return None
    if determinant(a,b,c) == 0:
        zero = (-b / (2*a))
        return zero
    if determinant(a,b,c) > 0:
        zero_1 = (-b + math.sqrt(determinant(a,b,c)))/ (2*a)
        zero_2 = (-b - math.sqrt(determinant(a,b,c)))/ (2*a)
        return zero_1,zero_2

#Exemple avec déterminant positif
print(zero_quadratique(1,5,1))
#Exemple avec déterminant nul
print(zero_quadratique(1,2,1))
#Exemple avec déterminant négatif
print(zero_quadratique(10,2,7))

#Q1 b)
# fonction imposition salaire de la série 2
club_social = 2
pourcentage_rqap = 0.494/100

def imposition(salaire):
    impot_a_payer = 0
    if (salaire >= 0 and salaire <= 51780):
        impot_a_payer = 14/100 * salaire
    #Dans le elif, on peut ajouter and salaire >51780, c'est syntaxiquement correct, mais inutile
    elif (salaire < 103545):
        impot_a_payer = 19/100 * salaire
    #idem au elif précédent
    elif (salaire < 126000):
        impot_a_payer = 24/100*salaire
    elif (salaire >=126000):
        impot_a_payer = 25.75/100*salaire
    else:
        print("Le salaire entré n'est pas valide")
    
    return impot_a_payer

def rqap(montant):
    retenue = 0
    if montant > 94000:
        retenue = pourcentage_rqap * 94000
    else:
        retenue = pourcentage_rqap * montant
    return retenue


def assurance_maladie(niveau_protection):
    if (niveau_protection == 'A'):
        return 75.45
    elif (niveau_protection == 'B'):
        return 59.34
    elif(niveau_protection == 'C'):
        return 37.23
    
def deduction(montant_brut, niveau_assurance):
    somme = 0
    somme += imposition(montant_brut)
    somme += rqap(montant_brut)
    somme += assurance_maladie(niveau_assurance)
    somme += club_social
    
    return somme

print(imposition(101000))
print(rqap(101000))
print(assurance_maladie('A'))
print(deduction(101000,'A'))

# c)
def salaire(montant_annuel, niveau_protection):
    salaire_annuel = montant_annuel - deduction(montant_annuel, niveau_protection)
    salaire_hebdo = round(salaire_annuel /52,2)
    return salaire_hebdo
print(salaire(101000, 'A'))

#d)
compteur = 0
def ticket():
    global compteur
    compteur +=2  #c'est un raccourcis pour faire compteur = compteur + 2
#Aucun return

#e)
plus_haut = 1.5

def mise_a_jour_hauteur(hauteur):
    global plus_haut
    if (hauteur > plus_haut):
        plus_haut = hauteur
#Aucun else 

#f)
lapins_totaux = 2
prix_nourriture = 4.6

def lapin_repro():
    global lapins_totaux
    lapins_totaux = lapins_totaux * 2

def lapin_vente(nombre_lapins):
    global lapins_totaux
    lapins_totaux = lapins_totaux-nombre_lapins

def lapin_nourriture():
    prix_total = lapins_totaux * prix_nourriture
    print("La nourriture des lapins présentement coûte", prix_total, "dollars")

print(lapins_totaux)
lapin_repro()
lapin_repro()
lapin_vente(1)
lapin_nourriture()
print(lapins_totaux)
lapin_nourriture()
lapin_repro()
lapin_vente(6)
print(lapins_totaux)
        
#g)        
limite = 10
def est_croissant(heure):
    h1 = hauteur(heure)
    h2 = hauteur(heure +1)
    if (h2-h1 > 0):
        return True
    else:
        return False


def alarme(heure):
    if(hauteur(heure) > limite):
        print("DANGER, vous êtes déjà dans le pétrin présentement!")
    elif (hauteur(heure + 2) > limite):
        if (heure + 2 < limite):
            temps = temps_sinus(limite) - heure
        else:
            temps = temps_sinus(limite) - heure + 12
            
        print("ALARME!!, il faut quitter les lieux dans maximum", round(temps,2), "heure!")   
    else:
        print("Vous êtes en sécurité pour au moins les 2 prochaines heures")
        
def temps_sinus(hauteur):
    t = (math.asin((hauteur-6.9)/5.9) +1.97)*6 / math.pi
    return t
    
def hauteur(heure):
    h = 5.9*math.sin(math.pi * heure /6 -1.97) +6.9
    return h

alarme(6)
alarme(11)
alarme(16)