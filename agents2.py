from random import *

def random_agent():
    action_joueur = choice(["attack", "defend"])
    return action_joueur

def always_attack_agent():
    action_joueur = "attack"
    return action_joueur

def always_defending_agent():
    action_joueur = "defend"
    return action_joueur


def resentful_agent(i,tabl,trahison):
    if i > 0:
        a,b = tabl[i-1]
        if b == "attack":
            trahison = True
            action_joueur = "attack"
        elif trahison ==True:
            action_joueur = "attack"
        else:
            action_joueur = "defend"
    else:
        action_joueur = "defend"
    return action_joueur,trahison

def copy_agent(i,tabl):
    if i>0:
        a,b = tabl[i-1]
        action_joueur = b
    else:
        action_joueur = "defend"
    return action_joueur
