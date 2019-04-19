# Route Finding AI Example
# Based on long link

# objectives
# demonstrate Markov Decision Process AKA MDP
# Demonstrate the bellman equation AKA Qfunction

# import the numpy library so we can use this in the program
# to use the id library we just type the alias ql
import numpy as ql

# R is the reward matrix for each possible state
# the one values Represent the nodes(Verticies) of the graph
# All the values are the same across as they are down
R = ql.matrix([[0, 0, 0, 0, 1, 0],
              [0, 0, 0, 1, 0, 1],
              [0, 0, 100, 1, 0, 0],
              [0, 1, 1, 0, 1, 0],
              [1, 0, 0, 1, 0, 0],
              [0, 1, 0, 0, 0, 0]])
# print("The Variable R is a type", type(R), "variable and holds the value", R, "End of the Line...")

# Q is the learning matrix which rewards are learned
# here we are creating a 6 by 6 matrix
Q = ql.matrix(ql.zeros([6, 6]))
# print ("The Variable Q is a type", type(Q), "variable and holds the value", Q, "End of the Line...")

# Gamma: it's form of penalty or uncertainty for learning
# if the value is 1, the rewards would be too high
# this way the system knows it is learning.
# float variable gamma
gamma = 0.8
# print ("The Variable gamma is a type", type(gamma), "variable and holds the value", gamma, "End of the Line...")

# agent_s_state the agent the name of the system calculating
# s is the state the agent is going from and the s' the state it's going to
# this state can be random or it can be chosen as long as the rest of the choices
# are not determined. Randomness is part of the stochastic process
agent_s_state = 1
# print ("The Variable agent_s_state is a type", type(agent_s_state),
# "variable and holds the value", agent_s_state, "End of the Line...")

# the possible "a" actions when the agent is in a given state
# This gives our agent sll the possible actions in the environment
# that is all this function does. do not over think this!


def possible_actions(state):
    current_state_row = R[state]
    # print ("The Variable state is a type", type(state), "variable and holds the value", state, "End of the Line...")
    # print ("The Variable current_state_row is a type", type(current_state_row),
    # "variable and holds the value", current_state_row, "End of the Line...")
    possible_act = ql.where(current_state_row > 0)[1]
    # print ("The Variable possible_act is a type", type(possible_act),
    #  "variable and holds the value", possible_act, "End of the Line...")
    return possible_act


# get available actions in the current state
PossibleAction = possible_actions(agent_s_state)
# print ("The Variable PossibleAction is a type", type(PossibleAction),
# "variable and holds the value", PossibleAction, "End of the Line...")

# this function chooses at random which action to be performed within range
# of all the available actions
# heere your AI is making a random choice
# nothing more intellignet that that in this function


def action_choice(available_actions_range):
    if sum(PossibleAction) > 0:
        next_action = int(Q).random.choice(PossibleAction, 1)
    if sum(PossibleAction) <= 0:
        next_action = int(Q.random.choice(5, 1))
    return next_action


# grabbing a random action and putting it into the action
# Sample  next action to be performed
action = action_choice(PossibleAction)

# A version of bellmans equation for reinforcement learning using the Q function
# this reinforcment algoritm is a memoryless process
# the transition function T from one state to another
# is not in the equation below. T is done by the random choice above


def reward(current_state, action, gamma):
    Max_State = ql.where(Q[action, ] == ql.max(Q[action, ]))[1]

    if Max_State.shape[0] > 1:
        Max_State = int(ql.random.choice(Max_State, size = 1))
    else:
        Max_State = int(Max_State)







