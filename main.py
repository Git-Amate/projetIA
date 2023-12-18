from random import *
from agents import *
from agents2 import *

'''
Theorie des jeux: Domaine concurencielle multi agent

matrice de gain
        |------------------------------------------------------x---|
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


agent = init_agent()


def determine_reward(agent_action, opponent_action):
    if agent_action == opponent_action == "attack":
        return (2,2)
    if agent_action == opponent_action == "defend":
        return (5,5)
    if agent_action == "attack" and opponent_action == "defend":
        return (0,10)
    if agent_action == "defend" and opponent_action == "attack":
        return (10,0)

# Entraînement de l'agent sur plusieurs itérations
tab = []
cpt = 0
reward_apponent_total = 0


def agentIntelligent(randomOrAlwaysdefendingOrAlwaysAttakingAgent,nbrAffrontement):
    reward_apponent_total = 0
    for i in range(nbrAffrontement):
        action = choose_action(agent["q_values"])
        action_opponent = randomOrAlwaysdefendingOrAlwaysAttakingAgent()
        reward_agentIntelligent,reward_opponent = determine_reward(action, action_opponent)
        #print(reward_opponent)
        agent["q_values"] = update_q_values(agent["q_values"], action, reward_agentIntelligent)
        agent["total_reward"] += reward_agentIntelligent
        reward_apponent_total += reward_opponent
        print("Action choisie:", action)
        print(action_opponent)
        print(reward_agentIntelligent)

    # Affichage des résultats
    #print("agent entrainé")
    #print("Total Reward:", agent["total_reward"])
    #print("Total Reward opponent:", reward_apponent_total)
    #print("Q-values:", agent["q_values"])


def agentEquilibredeNash(randomOrAlwaysdefendingOrAlwaysAttakingAgent,agentEquilibre,nbrAffrontement):
    reward_apponent_total = 0
    total_reward_agent = 0
    for i in range(nbrAffrontement):
        action = agentEquilibre
        action_opponent = randomOrAlwaysdefendingOrAlwaysAttakingAgent()
        reward_agent,reward_opponent = determine_reward(action, action_opponent)
        if nbrAffrontement > 1:
            total_reward_agent += reward_agent
        else:
            total_reward_agent = reward_agent
        #reward_apponent_total += reward_opponent
        #print("Action choisie:", action)
        #print(agent["total_reward"])
    return total_reward_agent


def agentIntelligentV1(copyorRestfulAgent,nbrAffrontement):
    tab = []
    cpt = 0
    reward_apponent_total = 0
    boool = False
    for i in range(nbrAffrontement):
        action = choose_action(agent["q_values"])
        #print(copyorRestfulAgent.__name__)
        if copyorRestfulAgent.__name__ == "resentful_agent":
            action_opponent,boool = copyorRestfulAgent(i, tab,boool)
        else:
            action_opponent = copyorRestfulAgent(i,tab)
        reward_agentIntelligent, reward_opponent = determine_reward(action, action_opponent)
        #print(reward_agent, reward_opponent)
        agent["q_values"] = update_q_values(agent["q_values"], action, reward_agentIntelligent)
        agent["total_reward"] += reward_agentIntelligent
        reward_apponent_total += reward_opponent
        print("Action choisie:", action)
        print("action Adversaire", action_opponent)
        print(reward_agentIntelligent)
        #print(agent["q_values"])
        cpt += 1
        tab.append((action_opponent, action))
    #print("agent enté")
    #print("Total Reward:", agent["total_reward"])
    #print("Total Reward opponent:", reward_apponent_total)
    #print("Q-values:", agent["q_values"])

def agentEquilibreDeNashV1(copyorRestfulAgent,agentEquilibre,nbrAffrontement):
    tab = []
    cpt = 0
    total_reward_agent = 0
    boool = False
    for i in range(nbrAffrontement):
        action = agentEquilibre
        if copyorRestfulAgent.__name__ == "resentful_agent":
            action_opponent,boool = copyorRestfulAgent(i, tab,boool)
        else:
            action_opponent = copyorRestfulAgent(i,tab)
        reward_agent, reward_opponent = determine_reward(action, action_opponent)
        #print(reward_agent, reward_opponent)
        if nbrAffrontement > 1:
            total_reward_agent += reward_agent
        else:
            total_reward_agent = reward_agent
        #reward_apponent_total += reward_opponent
        #print("Action choisie:", action)
        #print("action Adversaire",action_opponent)
        #print(agent["q_values"])
        cpt += 1
        tab.append((action_opponent, action))
    return total_reward_agent
    #print("agent enté")
    #print("Total Reward:", agent["total_reward"])
    #print("Total Reward opponent:", reward_apponent_total)
    #print("Q-values:", agent["q_values"])

def game(nbrderepetion,nbraffrontement,tab):
    for i in range (nbrderepetion):
        # agent intelligent against other agent
        agentIntelligent(always_defending_agent,nbraffrontement)
        agentIntelligent(always_attack_agent,nbraffrontement)
        agentIntelligent(random_agent,nbraffrontement)
        agentIntelligentV1(resentful_agent,nbraffrontement)
        agentIntelligentV1(copy_agent,nbraffrontement)
        #print(agent)
        #print(agent["total_reward"])

        # agent equilibre de nash against other agent
        # r1 = agentIntelligentV2(find_nash_equilibrium_for_player(matrice_de_gain))
        r2 = agentEquilibredeNash(always_defending_agent, find_nash_equilibrium_for_player(matrice_de_gain),nbraffrontement)
        r3 = agentEquilibredeNash(always_attack_agent, find_nash_equilibrium_for_player(matrice_de_gain),nbraffrontement)
        r4 = agentEquilibredeNash(random_agent, find_nash_equilibrium_for_player(matrice_de_gain),nbraffrontement)
        r5 = agentEquilibreDeNashV1(resentful_agent, find_nash_equilibrium_for_player(matrice_de_gain),nbraffrontement)
        r6 = agentEquilibreDeNashV1(copy_agent, find_nash_equilibrium_for_player(matrice_de_gain),nbraffrontement)
        total = r2 + r3 + r4 + r5 + r6
        #print(total)
        tab.append((agent["total_reward"],total))
        agent["total_reward"] = 0






