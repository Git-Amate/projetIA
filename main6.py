from random import *

'''
Theorie des jeux: Domaine concurencielle multi agent

matrice de gain
        |---------------------------------------------------------|
        |                        User B                           |
        -----------------------------------------------------------
        | Actions         | se défendre       | Attaquer          |
--------|-----------------|-------------------|-------------------|
User    | Se défendre     | 5,5               | 10,0               |
A       | Attaquer        | 0,10               | 2,2                 |
-------------------------------------------------------------------

Si les deux magasins (A et B) choisissent de se défendre, chacun d'entre eux gagne 5 clients
Si A attaque pendant que B se défend, le magasin A qui attaque gagne 0 client
Si les deux magasins attaquent, chacun gagne 2 clients.
Si A defend pendant que B attaque, A gagne 10 clients
'''

matrice_de_gain = [[5,5],[0,10],
                   [10,0],[2,2]]

def init_agent():
    return {"q_values": {"attack": 0, "defend": 0}, "total_reward": 0}

def choose_action(q_values):
    if uniform(0, 1) < 0.1:
        print(uniform(0, 1))
        return choice(["attack", "defend"])
    else:
        return max(q_values, key=q_values.get)

def update_q_values(q_values, action, reward):
    q_values[action] = q_values[action] + 0.1 * (reward - q_values[action])
    return q_values

# Exemple d'utilisation
agent = init_agent()

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
                print(f"Équilibre de Nash trouvé : Joueur 1 {strat_joueur1}, Joueur 2 {strat_joueur2}")
                return strat_joueur1

    print("Aucun équilibre de Nash trouvé.")


def determine_reward(agent_action, opponent_action):
    if agent_action == opponent_action == "attack":
        return (2,2)
    if agent_action == opponent_action == "defend":
        return (5,5)
    if agent_action == "attack" and opponent_action == "defend":
        return (0,10)
    if agent_action == "defend" and opponent_action == "attack":
        return (10,0)


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

# Entraînement de l'agent sur plusieurs itérations
tab = []
cpt = 0
reward_apponent_total = 0

def agentIntelligent(randomOrAlwaysdefendingOrAlwaysAttakingAgent):
    reward_apponent_total = 0
    for i in range(100):
        action = choose_action(agent["q_values"])
        action_opponent = randomOrAlwaysdefendingOrAlwaysAttakingAgent()
        reward_agent,reward_opponent = determine_reward(action, action_opponent)
        #print(reward_opponent)
        agent["q_values"] = update_q_values(agent["q_values"], action, reward_agent)
        agent["total_reward"] += reward_agent
        reward_apponent_total += reward_opponent
        print("Action choisie:", action)
        print(agent["q_values"])
    # Affichage des résultats
    print("agent entrainé")
    #print("Total Reward:", agent["total_reward"])
    #print("Total Reward opponent:", reward_apponent_total)
    #print("Q-values:", agent["q_values"])


def agentIntelligentV1(copyorRestfulAgent):
    tab = []
    cpt = 0
    reward_apponent_total = 0
    boool = False
    for i in range(100):
        action = choose_action(agent["q_values"])
        if copyorRestfulAgent.__name__ == "resentful_agent":
            action_opponent,boool = copyorRestfulAgent(i, tab,boool)
        else:
            action_opponent = copyorRestfulAgent(i,tab)
        reward_agent, reward_opponent = determine_reward(action, action_opponent)
        print(reward_agent, reward_opponent)
        agent["q_values"] = update_q_values(agent["q_values"], action, reward_agent)
        agent["total_reward"] += reward_agent
        reward_apponent_total += reward_opponent
        print("Action choisie:", action)
        print("action Adversaire",action_opponent)
        print(agent["q_values"])
        cpt += 1
        tab.append((action_opponent, action))
    print("agent enté")
    #print("Total Reward:", agent["total_reward"])
    #print("Total Reward opponent:", reward_apponent_total)
    #print("Q-values:", agent["q_values"])

def agentIntelligentV2(agentEquilibre):
    reward_apponent_total = 0
    agent["total_reward"] = 0
    for i in range(100):
        action = choose_action(agent["q_values"])
        action_opponent = agentEquilibre
        reward_agent, reward_opponent = determine_reward(action, action_opponent)
        print(action_opponent)
        agent["q_values"] = update_q_values(agent["q_values"], action, reward_agent)
        agent["total_reward"] += reward_agent
        reward_apponent_total += reward_opponent
        print("Action choisie:", action)
        print(agent["q_values"])
    # Affichage des résultats
    print("agent entrainé")
    print("Total Reward:", agent["total_reward"])
    print("Total Reward opponent:", reward_apponent_total)
    print("Q-values:", agent["q_values"])


#print(find_nash_equilibrium_for_player(matrice_de_gain))

#agentIntelligent(always_defending_agent)
#print("---------------------")
#agentIntelligentV1(resentful_agent)
#print("---------------------")
agentIntelligentV2(find_nash_equilibrium_for_player(matrice_de_gain))

