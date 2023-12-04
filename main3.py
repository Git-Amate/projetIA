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

choix_possible = ["attaquer","defendre"]

'''
Nous allons definir differente fonction représentant different cas de scenario,

Les deux agents jouents des stratégies au hasard
l'agent B va reproduire les mêmes actions que l'agent A
L'agent B va toujours se defendre mais si A attaque il va toujours attaquer A
les deux agents vont jouer de maniere à maximiser leur gains

'''

def attribution_de_gain(action_joueurA,action_joueurB):
    gain_joueurA = 0
    gain_joueurB = 0
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
    return (gain_joueurA,gain_joueurB)

def random_agent():
    action_joueur = randint(0, 1)
    return action_joueur

def always_attack_agent():
    action_joueur = 0
    return action_joueur

def always_defending_agent():
    action_joueur = 1
    return action_joueur

def resentful_agent(i,tabl):
    trahison = False
    if i > 0:
        a,b = tabl[i-1]
        if b == 0:
            trahison = True
            action_joueur = 0
        elif trahison ==True:
            action_joueur = 0
        else:
            action_joueur = 1
    else:
        action_joueur = 1
    return action_joueur

def copy_agent(i,tabl):
    if i>0:
        a,b = tabl[i-1]
        action_joueur = b
    else:
        action_joueur = randint(0,1)
    return action_joueur

def game():
    tab = []
    tab_action = []
    cpt = 0
    agents = [(random_agent, []),
                  (always_attack_agent,[]),
                  (always_defending_agent,[]),
                  (resentful_agent,[cpt,tab_action]),
                  (copy_agent, [cpt,tab_action])]
    dictionnaire = {"copy_agent": 0, "resentful_agent": 0, "random_agent": 0, "always_attack_agent": 0,
                   "always_defending_agent": 0}
    #agent_choisi1, params1 = choice(agents)
    #agent_choisi2, params2 = choice(agents)
    for k in agents:
        for j in agents:
            agent_choisi1, params1 = k
            agent_choisi2, params2 = j
            print((agent_choisi1.__name__) + " VS " + agent_choisi2.__name__)
            if agent_choisi1.__name__ == agent_choisi2.__name__:
                pass
            else:
                for i in range (0,5):
                    if params2:
                        params2[0] = cpt
                        params2[1] = tab_action
                    if params1:
                        params1[0] = cpt
                        params1[1] = tab_action
                    action_joueur1 = agent_choisi1(*params1)
                    print("l'agent " + str(agent_choisi1.__name__) + " a choisi " + choix_possible[action_joueur1])
                    action_joueur2 = agent_choisi2(*params2)
                    print("l'agent " + str(agent_choisi2.__name__) + " a choisi " +choix_possible[action_joueur2])
                    if agent_choisi2.__name__ == "copy_agent" or agent_choisi2.__name__ == "resentful_agent":
                        gains = attribution_de_gain(action_joueur2, action_joueur1)
                        tab_action.append((action_joueur2, action_joueur1))
                        x,y = gains
                        if x>y:
                            dictionnaire[agent_choisi2.__name__] = dictionnaire[agent_choisi2.__name__]+1
                        else:
                            dictionnaire[agent_choisi1.__name__] = dictionnaire[agent_choisi1.__name__] + 1
                        tab.append(gains)
                        cpt = cpt + 1
                    else:
                        gains = attribution_de_gain(action_joueur1, action_joueur2)
                        tab_action.append((action_joueur1, action_joueur2))
                        x, y = gains
                        if x > y:
                            dictionnaire[agent_choisi1.__name__] = dictionnaire[agent_choisi1.__name__] + 1
                        else:
                            dictionnaire[agent_choisi2.__name__] = dictionnaire[agent_choisi2.__name__] + 1
                        tab.append(gains)
                        cpt = cpt + 1
    return dictionnaire


print(game())

