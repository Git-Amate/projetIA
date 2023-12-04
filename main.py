from random import *

#Matrice de decison
'''
Theorie des jeux: Domaine concurencielle multi agent

matrice de gain
        |---------------------------------------------------------|
        |                        User B                           |
        -----------------------------------------------------------
        | Actions         | se défendre       | Attaquer          |
--------|-----------------|-------------------|-------------------|
User    | Se défendre     | 5,5               | 10,0               |
A       | Attaquer        | 0,10              | 2,2                 |
-------------------------------------------------------------------

Si les deux magasins (A et B) choisissent de se défendre, chacun d'entre eux gagne 5 clients
Si A attaque pendant que B se défend, le magasin A qui attaque gagne 0 client
Si les deux magasins attaquent, chacun gagne 2 clients.
Si A defend pendant que B attaque, A gagne 10 clients
'''

# Ici la matrice de gain
matrice_de_gain = [[5,5],[10,0],
                   [0,10],[2,2]]

'''
Nous allons definir differente fonction représentant different cas de scenario,

Les deux agents jouents des stratégies au hasard
l'agent B va reproduire les mêmes actions que l'agent A
L'agent B va toujours se defendre mais si A attaque il va toujours attaquer A
les deux agents vont jouer de maniere à maximiser leur gains

'''

def fonction1():
    choix_possible = ["attaquer","defendre"]
    cpt = 0
    gain_joueurA = 0
    gain_joueurB = 0

    #Nous allons jour sur 5 tours
    while cpt < 5:
        action_joueurA = randint(0,1)
        print("le joueur A choisi l'action : "+choix_possible[action_joueurA])
        action_joueurB = randint(0,1)
        print("le joueur B choisi l'action : " + choix_possible[action_joueurB])
        print("-----------------------------------------------")
        if choix_possible[action_joueurA] == choix_possible[action_joueurB] == "attaquer":
            gain_joueurA = gain_joueurA + 2
            gain_joueurB = gain_joueurB + 2
        if choix_possible[action_joueurA] == choix_possible[action_joueurB] == "defendre":
            gain_joueurA = gain_joueurA + 5
            gain_joueurB = gain_joueurB + 5
        if choix_possible[action_joueurA] == "attaquer" and choix_possible[action_joueurB] == "defendre":
            gain_joueurA = gain_joueurA + 0
            gain_joueurB = gain_joueurB + 10
        if choix_possible[action_joueurA] == "defendre" and choix_possible[action_joueurB] == "attaquer":
            gain_joueurA = gain_joueurA + 10
            gain_joueurB = gain_joueurB + 0
        cpt+=1

    return (gain_joueurA,gain_joueurB)

def fonction2():
    choix_possible = ["attaquer","defendre"]
    cpt = 0
    gain_joueurA = 0
    gain_joueurB = 0

    #Nous allons jour sur 5 tours
    while cpt < 5:
        action_joueurA = randint(0,1)
        print("le joueur A choisi l'action : "+choix_possible[action_joueurA])
        action_joueurB = action_joueurA
        print("le joueur B choisi l'action : " + choix_possible[action_joueurB])
        print("-----------------------------------------------")
        if choix_possible[action_joueurA] == choix_possible[action_joueurB] == "attaquer":
            gain_joueurA = gain_joueurA + 2
            gain_joueurB = gain_joueurB + 2
        if choix_possible[action_joueurA] == choix_possible[action_joueurB] == "defendre":
            gain_joueurA = gain_joueurA + 5
            gain_joueurB = gain_joueurB + 5
        if choix_possible[action_joueurA] == "attaquer" and choix_possible[action_joueurB] == "defendre":
            gain_joueurA = gain_joueurA + 0
            gain_joueurB = gain_joueurB + 10
        if choix_possible[action_joueurA] == "defendre" and choix_possible[action_joueurB] == "attaquer":
            gain_joueurA = gain_joueurA + 10
            gain_joueurB = gain_joueurB + 0
        cpt+=1

    return (gain_joueurA,gain_joueurB)

def fonction3():
    choix_possible = ["attaquer","defendre"]
    cpt = 0
    gain_joueurA = 0
    gain_joueurB = 0
    tour_suivant = False
    #Nous allons jour sur 5 tours
    while cpt < 5:
        action_joueurA = randint(0,1)
        print("le joueur A choisi l'action : "+choix_possible[action_joueurA])
        if action_joueurA == 0 and tour_suivant == False :
            action_joueurB = randint(0,1)
            print("le joueur B choisi l'action : " + choix_possible[action_joueurB])
            print("-----------------------------------------------")
            tour_suivant = True
        else:
            action_joueurB = 0
            print("le joueur B choisi l'action : " + choix_possible[action_joueurB])
            print("-----------------------------------------------")
        if choix_possible[action_joueurA] == choix_possible[action_joueurB] == "attaquer":
            gain_joueurA = gain_joueurA + 2
            gain_joueurB = gain_joueurB + 2
        if choix_possible[action_joueurA] == choix_possible[action_joueurB] == "defendre":
            gain_joueurA = gain_joueurA + 5
            gain_joueurB = gain_joueurB + 5
        if choix_possible[action_joueurA] == "attaquer" and choix_possible[action_joueurB] == "defendre":
            gain_joueurA = gain_joueurA + 0
            gain_joueurB = gain_joueurB + 10
        if choix_possible[action_joueurA] == "defendre" and choix_possible[action_joueurB] == "attaquer":
            gain_joueurA = gain_joueurA + 10
            gain_joueurB = gain_joueurB + 0
        cpt+=1
    return (gain_joueurA, gain_joueurB)


print(fonction3())
