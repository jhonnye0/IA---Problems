import random
import copy

class State:
    def __init__(self, mis, can, boatSide, dad, cost, depth, operator):
        self.mis = mis
        self.can = can
        self.boatSide = boatSide
        self.dad = dad
        self.cost = cost
        self.depth = depth
        self.operator = operator
    def __eq__(self, another):
        if(another == None): 
            return False
        return (self.mis == another.mis and 
              self.can == another.can and
              self.boatSide == another.boatSide)

# =======================================OPERAÇOES ======================================================
def operation_MoveTwoMis(state):
    new_state = copy.copy(state)       # copia os atributos
    new_state.dad = state              # atribui o pai
                                       # O new_state possui o mesmo custo do pai
    new_state.depth += 1               # incrementa a profundidade
    new_state.operator = 2             # sinal de mover "dois" para o outro lado
    
    new_state.mis += (-2 + 4*state.boatSide)
    
    new_state.boatSide = 1 if 0 else 1   # move o barco para o outro lado
    return new_state

def operation_MoveOneMisOneCan(state):
    new_state = copy.copy(state)       # copia os atributos
    new_state.dad = state              # atribui o pai
                                       # O new_state possui o mesmo custo do pai
    new_state.depth += 1               # incrementa a profundidade
    new_state.operator = 11            # sinal de mover "dois" para o outro lado
    
    new_state.can += (-1 + 2*state.boatSide)
    new_state.mis += (-1 + 2*state.boatSide)
    
    if(new_state.boatSide == 1):    # move o barco para o outro lado
        new_state.boatSide = 0
    else:
        new_state.boatSide = 1
    return new_state

def operation_MoveTwoCan(state):
    new_state = copy.copy(state)       # copia os atributos
    new_state.dad = state              # atribui o pai
                                       # O new_state possui o mesmo custo do pai
    new_state.depth += 1               # incrementa a profundidade
    new_state.operator = 2             # sinal de mover "dois" para o outro lado
    
    new_state.can += (-2 + 4*state.boatSide)
    
    if(new_state.boatSide == 1):    # move o barco para o outro lado
        new_state.boatSide = 0
    else:
        new_state.boatSide = 1
    return new_state

def operation_MoveOneMis(state):
    new_state = copy.copy(state)       # copia os atributos
    new_state.dad = state              # atribui o pai
                                       # O new_state possui o mesmo custo do pai
    new_state.depth += 1               # incrementa a profundidade
    new_state.operator = 1             # sinal de mover "dois" para o outro lado
    
    new_state.mis += (-1 + 2*state.boatSide)
    
    if(new_state.boatSide == 1):    # move o barco para o outro lado
        new_state.boatSide = 0
    else:
        new_state.boatSide = 1
    return new_state

def operation_MoveOneCan(state):
    new_state = copy.copy(state)       # copia os atributos
    new_state.dad = state              # atribui o pai
                                       # O new_state possui o mesmo custo do pai
    new_state.depth += 1               # incrementa a profundidade
    new_state.operator = 1             # sinal de mover "dois" para o outro lado
    
    new_state.can += (-1 + 2*state.boatSide)
    
    if(new_state.boatSide == 1):    # move o barco para o outro lado
        new_state.boatSide = 0
    else:
        new_state.boatSide = 1
    return new_state
# --------------------------------------------------------------------------------------------------------------
# =======================================Checagens de Validade e Solução ======================================================

def isValid(state):
    if(state == None): 
        return False
    if(state.mis == state.dad.mis and
       state.can == state.dad.can and
       state.boatSide == state.dad.boatSide):
        return False
    if(state.dad.dad != None and state.mis == state.dad.dad.mis and
       state.can == state.dad.dad.can and
       state.boatSide == state.dad.dad.boatSide):
        return False
    if((state.mis < 0 or state.mis > 3) or (state.can < 0 or state.can > 3)): 
        return False
    if((state.mis != 0 and state.mis < state.can) or 
        (3-state.mis != 0 and 3-state.mis < 3-state.can)): return False
    return True


def isSolution(state):
    if(state.mis == 0 and state.can == 0 and state.boatSide == 1): return True
    return False
#-------------------------------------------------------------------------------------------------------------------------
def print_list(this_list):
    for state in this_list:
        print("({},{},{})".format(state.mis, state.can, state.boatSide))

bound = []

inicial = State(3, 3, 0, None, 1, 0, None)

bound.append(inicial)

Solution = None

count = 0;
#=======================================EFETUAÇÃO DAS TRANSIÇOES DE ESTADO=====================================================
while(True):
    if(len(bound) == 0):
        print("No Solution")
        break
    
    print(count)
    print_list(bound)
    
    state = bound[0]
    
    bound.pop(0)
    
    if(isSolution(state)):
        Solution = state
        print("({},{},{})".format(state.mis, state.can, state.boatSide))
        break
    else:
        new_state = operation_MoveTwoMis(state)
        if(isValid(new_state)):
            bound.append(new_state)
        new_state = operation_MoveOneMisOneCan(state)
        if(isValid(new_state)):
            bound.append(new_state)
        new_state = operation_MoveTwoCan(state)
        if(isValid(new_state)):
            bound.append(new_state)
        new_state = operation_MoveOneMis(state)
        if(isValid(new_state)):
            bound.append(new_state)
        new_state = operation_MoveOneCan(state)
        if(isValid(new_state)):
            bound.append(new_state)
    count += 1
    
list = []

def getPath(state):
    while(state != None):
        list.append(state)
        state = state.dad
        
getPath(Solution)
list.reverse()

print_list(list)
