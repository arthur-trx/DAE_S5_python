import random

# Liste des mots du pendu. On peut en ajouter bien sûr.
listeMots = [
    "armoire",
    "boucle",
    "buisson",
    "bureau",
    "chaise",
    "carton",
    "couteau",
    "fichier",
    "garage",
    "glace",
    "journal",
    "kiwi",
    "lampe",
    "liste",
    "montagne",
    "remise",
    "sandale",
    "taxi",
    "vampire",
    "volant",
]

dessins = [
"""
---------
 |     |
 |
 |
 |
 |
 |""",
 """
 ---------
 |     |
 |     o
 |
 |
 |
 |""",
 """
 ---------
 |     |
 |     O
 |    -+-
 |
 |
 |""",
 """
 ---------
 |     |
 |     O
 |   /-+-
 |
 |
 |""",
 """
 ---------
 |     |
 |     O
 |   /-+-/
 |
 |
 |""",
 """
 ---------
 |     |
 |     O
 |   /-+-/
 |    |
 |
 |""",
 """
 ---------
 |     |
 |     O
 |   /-+-/
 |    | |
 |
 |"""]


#Fonctions du jeu de pendu

## A compléter
def choisirMot(L):
    """
    Cette fonction choisit un mot au hasard dans la liste de mots L
    donnée en paramètre.
    """
    """random.choice(L)"""
    return L[random.randint(0, len(L)-1)]


def genMotMasque(mot_complet, lettres_trouvees):
    """Cette fonction renvoie un mot masqué tout ou en partie, en fonction :
    - du mot d'origine (type str)
    - des lettres déjà trouvées (type list)

    On renvoie le mot d'origine avec des * remplaçant les lettres que l'on
    n'a pas encore trouvées."""


    mot = []
    for i in range(0, len(mot_complet) ) :
        if mot_complet[i] in lettres_trouvees :
            mot.append(mot_complet[i])
        else :
            mot.append('*')
    return mot

## A compléter
def lireLettre(propositions):
    """
     Demande une lettre à l'utilisateur en s'assurant qu'elle n'a pas déjà
     été proposée, puis ajoute cette lettre à la liste des lettres déjà
     proposées.

    Exemple ci-dessous :


     Entrez une proposition de lettre : A
     Une seule lettre en minuscule, s'il vous plaît.
     Entrez une proposition de lettre : a
     Cette lettre a déjà été proposée.
     Entrez une proposition de lettre : qsdf
     Une seule lettre en minuscule, s'il vous plaît.
     Entrez une proposition de lettre : e
     'e'

     ['a', 'b', 'c', 'e']
    """
    pasOK=True
    while pasOK:
        lettre = input ("enter une proposition de lettre : ")
        if len(lettre)  !=  1:
            pasOK=True
        else :
            if lettre.isupper() :
                pasOK = True
            else :
                if lettre in propositions :
                    pasOK=True
                else :
                    pasOK=False


    propositions.append(lettre) # on ajoute la nouvelle lettre
    return lettre

## A compléter
def dessinerPendu(erreur):
    print(dessins[erreur])


## A compléter
def jouerPartie():
    """
     Joue une partie de pendu
     retourne True si gagné, False si perdu
    """

    #
    # Initialisations des variables utiles au jeu
    #
    erreurs = 0
    max_erreurs = 7
    mot = choisirMot(listeMots)
    lettres_proposees = [] #pour l'instant vide
    Trouve = False #variable permettant d'arreter la boucle de jeu

    #
    # Boucle d'interrogation de l'utilisateur
    #
    while not Trouve:
        #Algorithme du jeu
        # A COMPLETER
        dessinerPendu(erreurs)
        temp = genMotMasque(mot, lettres_proposees)
        print("le mot est :", temp)
        print("letres proposées : ", lettres_proposees)
        lireLettre(lettres_proposees)
        if lettres_proposees[-1] in mot :
            temp = genMotMasque(mot,lettres_proposees)
            print(temp)
            if '*' not in temp :
                Trouve = True

        else :
            erreurs += 1
            print("nb erreur :", erreurs)
            if erreurs >= max_erreurs :
                print("********************************* tu as perdu ********************************************")
                break
            else :
                dessinerPendu(erreurs)




jouerPartie()