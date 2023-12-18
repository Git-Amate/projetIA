from random import *

def init_agent():
    return {"q_values": {"attack": 0, "defend": 0}, "total_reward": 0}


def choose_action(q_values):
    if uniform(0, 1) < 0.1:
        #print(uniform(0, 1))
        return choice(["attack", "defend"])
    else:
        return max(q_values, key=q_values.get)

def update_q_values(q_values, action, reward):
    q_values[action] = q_values[action] + 0.1 * (reward - q_values[action])
    return q_values

def find_nash_equilibrium_for_player(matrix):

    strategies = ["defend", "attack"]

    # Recherche de l'équilibre de Nash
    for strat_joueur1 in strategies:
        for strat_joueur2 in strategies:
            # Obtention des gains associés à cette combinaison de stratégies
            gain_joueur1 = matrix[strategies.index(strat_joueur1)][1]
            gain_joueur2 = matrix[strategies.index(strat_joueur2)][0]

            # Vérification si c'est un équilibre de Nash
            if gain_joueur1 >= matrix[strategies.index(strat_joueur1)][0] and \
                gain_joueur2 >= matrix[strategies.index(strat_joueur2)][1]:
                #print(f"Équilibre de Nash trouvé : Joueur 1 {strat_joueur1}, Joueur 2 {strat_joueur2}")
                return strat_joueur1
