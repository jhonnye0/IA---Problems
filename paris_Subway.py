import pandas as pd
import numpy as np
import math

tableDistance = pd.read_excel("tableDistances.xls")
times = np.true_divide(tableDistance, 30.0)

class State:
    def __init__(self, node, n_str, neighboors, lines, cost, depth, dad):
        self.node = node
        self.lines = lines
        self.n_str = n_str
        self.neighboors = neighboors
        if(dad != None):
            self.cost = dad.cost + cost
        else:
            self.cost = cost;
        self.depth = depth
        self.dad = dad

#Definindo os estados

E1 = State(1, 'E1', [2], ['B'], 1000, 0, None)
E2 = State(2, 'E2', [1,3,9,10], ['Y', 'B'], 1000, 0, None)
E3 = State(3, 'E3', [2,4,9,13], ['B', 'R'], 1000, 0, None)
E4 = State(4, 'E4', [3,5,8,13], ['B', 'G'], 1000, 0, None)
E5 = State(5, 'E5', [4,6,7,8], ['Y', 'B'], 1000, 0, None)
E6 = State(6, 'E6', [5], ['B'], 1000, 0, None)
E7 = State(7, 'E7', [5], ['Y'], 1000, 0, None)
E8 = State(8, 'E8', [4,5,9,12], ['Y','G'], 1000, 0, None)
E9 = State(9, 'E9', [2,3,8,11], ['Y','R'], 1000, 0, None)
E10 = State(10, 'E10', [2], ['Y'], 1000, 0, None)
E11 = State(11, 'E11', [9], ['R'], 1000, 0, None)
E12 = State(12, 'E12', [8], ['G'], 1000, 0, None)
E13 = State(13, 'E13', [3,4,14], ['R', 'G'], 1000, 0, None)
E14 = State(14, 'E14', [13], ['G'], 1000, 0, None)

#Coletar a referencia do objeto a partir do numero
reference = {1: E1, 2: E2, 3: E3, 4: E4, 5: E5,
             6: E6, 7: E7, 8: E8, 9:E9, 10: E10, 11: E11, 12:E12,
             13: E13, 14: E14}

#DEFININDO A ORIGEM E DESTINO

source = E9
source.cost = 0
source.depth = 0

destiny = E7

total_time = 0

#Definindo função custo em relação ao tempo

def g(state_i, state_j):
    if(state_i.dad == None):
        return times[state_i.n_str][state_j.node-1]
    if(state_i.dad.dad == None):
        return times[state_i.n_str][state_j.node-1]
    if(np.intersect1d(state_i.lines, state_j.lines)): # Atribuindo 4 min
        return 4/60 + times[state_i.n_str][state_j.node-1]

#Definindo função heuristica

def h(state_i):
    return tableDistance[state_i.n_str][destiny.node-1]

def f(state_i, state_j):
    global total_time
    total_time += g(state_i, state_j)
    
    return h(state_i) + g(state_i, state_j)

def is_Solution(i):
    if (i.node == destiny.node):
        return True
    return False    

#Transição de estado
    
costs = []

def MoveNextStation(state):
    
    costs.clear()
    
    for i in state.neighboors:
        costs.append((f(reference[i], state),i))
        
        # Atualizando o pai
        reference[i].dad = state
        reference[i].depth = state.depth+1
        
        # Atualizando o custo
        if(reference[i].cost > state.cost + g(state, reference[i])):
            reference[i].cost = state.cost + g(state, reference[i]) 
    
    # Ordenando para saber o melhor
    costs.sort()    
    
    return reference[costs[0][1]]  # Next Node


node = source

while(True):
    
    print(node.node)
    path.append(node)
    
    if(is_Solution(node)):
        break;
    
    node = MoveNextStation(node)
    
print("Custo total: {}".format(total_time))
