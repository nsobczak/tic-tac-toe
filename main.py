# -*- coding: utf-8 -*-
"""
###############
# tic-tac-toe #
###############
Created on Tue Apr 14 17:08:22 2015

@author: Nicolas Sobczak
"""

# %%____________________________________________________________________________________________________
#  Config

# Import
import random as rdm
import numpy as np
from copy import deepcopy

# Initialisation
grilleVide = np.array([[0, 0, 0],
                       [0, 0, 0],
                       [0, 0, 0]])

# Création dico possibilités de victoire
dico = {}
dico['L1'] = ([1, 1], [1, 2], [1, 3])
dico['L2'] = ([2, 1], [2, 2], [2, 3])
dico['L3'] = ([3, 1], [3, 2], [3, 3])
dico['C1'] = ([1, 1], [2, 1], [3, 1])
dico['C2'] = ([1, 2], [2, 2], [3, 2])
dico['C3'] = ([1, 3], [2, 3], [3, 3])
dico['D1'] = ([1, 1], [2, 2], [3, 3])
dico['D2'] = ([3, 1], [2, 2], [1, 3])
lCles = ['L1', 'L2', 'L3', 'C1', 'C2', 'C3', 'D1', 'D2']


# ______________________________________________________________________________
# %%                             Niveau 0+


# %% Fonction qui choisi la liste des cases composant le coup gagnant
def coup_gagnant(grille):
    cle_choisie = 0
    for cle in lCles:
        row = dico[cle]
        compteur = 0
        for n in range(3):
            case = row[n]
            i = case[0]
            j = case[1]
            if grille[i - 1][j - 1] == -1:
                compteur += 1
            elif grille[i - 1][j - 1] == 1:
                compteur -= 1
        if compteur == 2 and cle_choisie == 0:
            cle_choisie = cle

    if cle_choisie == 0:
        res = 'aleatoire'
    else:
        res = cle_choisie

    return res


# %% Fonction qui choisi une case aléatoirement
def coup_ordi_aleatoire(grille):
    i = rdm.choice([0, 1, 2])
    j = rdm.choice([0, 1, 2])
    # print("i j :", i+1, j+1)
    if grille[i][j] != 0:
        grille = coup_ordi_aleatoire(grille)
    else:
        grille[i][j] = -1
    return grille


# %% Fonction qui effectue un coup gagnant
def coup_ordi_gagnant(grille, cle):
    choix = dico[cle]
    c = 0
    case = choix[c]
    i = case[0]
    j = case[1]
    while grille[i - 1][j - 1] != 0:
        c += 1
        case = choix[c]
        i = case[0]
        j = case[1]
    grille[i - 1][j - 1] = -1
    return grille


# ______________________________________________________________________________
# %%                             Niveau 1

def valNum_posOrdi(grille, i, j):
    res = 0
    grille[i][j] = -1

    # colonne
    compteur_O = 0
    compteur_J = 0

    for n in range(3):
        if grille[n][j] == -1:
            compteur_O += 1
        elif grille[n][j] == 1:
            compteur_J += 1

    if compteur_O == 3:
        res += 10000
    elif compteur_O == 2 and compteur_J == 0:
        res += 200
    elif compteur_O == 1 and compteur_J == 0:
        res += 30

    if compteur_J == 2:
        res -= 200
    elif compteur_J == 1:
        res -= 30

    # ligne
    compteur_O = 0
    compteur_J = 0

    for m in range(3):
        if grille[i][m] == -1:
            compteur_O += 1
        elif grille[i][m] == 1:
            compteur_J += 1

    if compteur_O == 3:
        res += 10000
    elif compteur_O == 2 and compteur_J == 0:
        res += 200
    elif compteur_O == 1 and compteur_J == 0:
        res += 30

    if compteur_J == 2:
        res -= 200
    elif compteur_J == 1:
        res -= 30

    # diagonale 1
    if [i + 1, j + 1] in dico['D1']:
        compteur_O = 0
        compteur_J = 0

        for n in range(3):
            if grille[n][n] == -1:
                compteur_O += 1
            elif grille[n][n] == 1:
                compteur_J += 1

        if compteur_O == 3:
            res += 10000
        elif compteur_O == 2 and compteur_J == 0:
            res += 200
        elif compteur_O == 1 and compteur_J == 0:
            res += 30

        if compteur_J == 2:
            res -= 200
        elif compteur_J == 1:
            res -= 30

    # diagonale 2
    if [i + 1, j + 1] in dico['D2']:
        compteur_O = 0
        compteur_J = 0

        for n in range(3):
            if grille[2 - n][n] == -1:
                compteur_O += 1
            elif grille[2 - n][n] == 1:
                compteur_J += 1

        if compteur_O == 3:
            res += 10000
        elif compteur_O == 2 and compteur_J == 0:
            res += 200
        elif compteur_O == 1 and compteur_J == 0:
            res += 30

        if compteur_J == 2:
            res -= 200
        elif compteur_J == 1:
            res -= 30

    return res

# %% fonction qui choisit le meilleur coup possible
def coup_ordi_optimal(grille):
    lisCoord = []
    lisVal = []

    # recherche des cases libres
    for i in range(3):
        for j in range(3):
            if grille[i][j] == 0:
                lisCoord += [[i, j]]

    # recherche de la meilleure position possible
    for coord in lisCoord:
        i = coord[0]
        j = coord[1]
        grilleTest = deepcopy(grille)
        grilleTest[i][j] = -1
        valPos = valNum_posOrdi(grilleTest, i, j)
        lisVal += [valPos]
    valMax = max(lisVal)
    indice = lisVal.index(valMax)
    coord = lisCoord[indice]
    i = coord[0]
    j = coord[1]

    grille[i][j] = -1

    return grille


# %%____________________________________________________________________________


# """""""""""""""""""""" L'ordinateur met des -1 """"""""""""""""""""
### Niveau 0 ###
def tour_ordi_n0(grille):
    cle = coup_gagnant(grille)
    if cle == 'aleatoire':
        grille = coup_ordi_aleatoire(grille)

    else:
        grille = coup_ordi_gagnant(grille, cle)
    return grille


### Niveau 1 ###
def tour_ordi_n1(grille):
    grille = coup_ordi_optimal(grille)
    return grille


# %%""""""""""""""""""""" Le joueur met des 1"""""""""""""""""""""""""""
def tour_joueur(grille):
    i = input("\nentrer la ligne (de 1 à 3)\n")
    while i not in ['1', '2', '3']:
        i = input("\nentrer la ligne (de 1 à 3)\n")
    j = input("\nentrer la colonne (de 1 à 3)\n")
    while j not in ['1', '2', '3']:
        j = input("\nentrer la colonne (de 1 à 3)\n")
    i = int(i) - 1
    j = int(j) - 1
    # print("i j :", i,j)
    if grille[i][j] != 0:
        grille = tour_joueur(grille)
    else:
        grille[i][j] = 1
    return grille


# %%""""""""""""""""" Condition de fin de partie""""""""""""""""""""""""
def partie_finie(grille):
    res = False

    # vérification lignes
    for i in range(3):
        n = 0
        for j in range(3):
            if grille[i][j] == 1:
                n += 1
            elif grille[i][j] == -1:
                n -= 1
        if n == 3 or n == -3:
            res = True

    # vérification colonnes
    if not res:
        for j in range(3):
            n = 0
            for i in range(3):
                if grille[i][j] == 1:
                    n += 1
                elif grille[i][j] == -1:
                    n -= 1
            if n == 3 or n == -3:
                res = True

    # vérification 1ere diagonale
    if not res:
        n = 0
        for i in range(3):
            if grille[i][i] == 1:
                n += 1
            elif grille[i][i] == -1:
                n -= 1
        if n == 3 or n == -3:
            res = True

    # vérification 2eme diagonale
    if not res:
        n = 0
        for i in range(3):
            if grille[2 - i][i] == 1:
                n += 1
            elif grille[2 - i][i] == -1:
                n -= 1
        if n == 3 or n == -3:
            res = True

    return res


# %% Grille pleine
def grille_pleine(grille):
    res = True
    for i in range(3):
        for j in range(3):
            if grille[i][j] == 0:
                res = False
    return res


# ______________________________________________________________________________
# %%                          Fonction principale

def nouvelle_partie():
    # initialisation
    grille = deepcopy(grilleVide)
    print(grille)

    niveau = input("\nchoix du niveau (de 0 à 1)\n")
    niveau = int(niveau)
    if niveau not in [0, 1]:
        niveau = 0
    print('niveau :', niveau)

    # maj
    while not partie_finie(grille):
        grille = tour_joueur(grille)

        if partie_finie(grille):
            print('\ngagné\n')

        else:
            if not grille_pleine(grille):
                if niveau == 0:
                    grille = tour_ordi_n0(grille)
                elif niveau == 1:
                    grille = tour_ordi_n1(grille)

                if partie_finie(grille):
                    print('\nperdu\n')
            else:
                print("\négalité\n")
                break
        print(grille)

    return grille



# %%____________________________________________________________________________________________________
#  ____________________________________________________________________________________________________
def monMain():
    nouvelle_partie()


if __name__ == "__main__":
    monMain()
