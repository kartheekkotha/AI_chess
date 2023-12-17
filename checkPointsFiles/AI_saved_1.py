# %%
import random
import math
from queue import PriorityQueue

# %% [markdown]
# The Puzzle class contains 
# - generateStates to generate the next states given the piece to move 
# - play function to generate all possible states and select the best state 

# %%
class Puzzle:
    def __init__(self) -> None:
        pass
    def play(self , presentState):
        # generate the possible states
        return 0
    def move(self, pieceToMove , presentState):
        # make the move respectively given the instruction 
        return 0

# %% [markdown]
# The class State is the class 
# - initialize the state 
# - check for the win / loss 
# - check for a draw 

# %%
class State:
    def __init__(self , finalState = [1,2,3,4,5,6,7,8,0]):
        puzz = Puzzle()
        self.finalState = finalState.copy()
        initialState  = puzz.play(finalState)
        # initialState = [1,0,6,4,3,2,7,5,8]
        self.initialState = initialState
    def get_intialState(self):
        return self.initialState
    def set_initialState(self , stateEx):
        self.initialState = stateEx.copy()
    def isDraw(self,presentState):
        return True
    def isWin(self,presentState):
        return True
    def islost(self,presentState):
        return True

# %% [markdown]
# The Heuristic class 
# - to calculate the specific Heuristic given the state

# %%
class Heuristic:
    stateNew = State()
#     FinalState = stateNew.get_finalState()
    def __init__(self , heuristicChoice):
          self.heuristic = heuristicChoice
    def getHeuristic(self, presentState):
          if(self.heuristic ==0):
                return self.nWrongTiles(presentState)
    #First Heuristic Function 
    def nWrongTiles(self, presentState):
            return 0    

# %% [markdown]
# The Graph class is to 
# - create the different graph algorithms to do the state search 
# - Add any helper functions if needed

# %%
class Graph():
    #This function to is to check the array in the 2-D array
    def checkArray(self, arrayArray, elementArray):
        for i in arrayArray:
            flag = True
            for j in range(len(elementArray)):
                if(i[j]!=elementArray[j]):
                    flag = False
            if(flag == True):
                return True
        return False
    #Helper function for array to string
    def arrToStr(self , arr):
        string = ""
        for i in arr:
            string+= str(i)
        return string
    #Helper function for string to array
    def strToArr(self , str):
        arr = []
        for i in str:
            arr.append(int(i))
        return arr
    #Function to return the path of steps chosen to get to goal node
    def construct_path(self, state ,parent, found_goal):
        moves_path = []
        while found_goal != state.get_intialState():
            foundstr = self.arrToStr(found_goal)
            parent_state, move = parent[foundstr]
            moves_path.append(move)
            found_goal = self.strToArr(parent_state)
        moves_path.reverse()
        moves_char = []
        for i in moves_path:
            if(i == 0):
                moves_char.append("L")
            elif(i == 1):
                moves_char.append("R")
            elif(i==2):
                moves_char.append("U")
            elif(i==3):
                moves_char.append("D")
        return moves_char
  
    def greedySearch(self, stateObj , initialState, heuristicChoice):
        player = Puzzle()
        closed = []#visited List
        parents = {}
        heuristicObj = Heuristic(heuristicChoice)
        open = PriorityQueue() #openToGoList 
        open.put((heuristicObj.getHeuristic(initialState),initialState))
        while(open.empty() == False):
            heuristicVal , currentState = open.get()
            # currentState = open.get()[1]
            print(f"The heuristic value of the state {currentState} is : {heuristicVal}")
            if(stateObj.comparator(currentState)):
               return self.construct_path(stateObj , parents  , currentState) 
            if(self.checkArray(closed , currentState)== False):
                closed.append(currentState)
                for move in [0,1,2,3]:
                    nextState = player.move(move, currentState)
                    if(nextState is not None):
                        if(self.checkArray(closed , nextState) == False):
                            open.put((heuristicObj.getHeuristic(nextState),nextState))
                            nextStr = self.arrToStr(nextState)
                            curStr = self.arrToStr(currentState)
                            parents[nextStr] = (curStr , move)
                    else:
                        pass 
        return None
    

    def AstarSearch(self, stateObj , initialState, heuristicChoice):
        player = Puzzle()
        closed = []#visited List
        parents = {}
        heuristicObj = Heuristic(heuristicChoice)
        open = PriorityQueue() #openToGoList 
        open.put((heuristicObj.getHeuristic(initialState),initialState))
        while(open.empty() == False):
            heuristicVal , currentState = open.get()
            # currentState = open.get()[1]
            print(f"The heuristic(h(n) + depth) value of the state {currentState} is : {heuristicVal}")
            if(stateObj.comparator(currentState)):
               return self.construct_path(stateObj , parents  , currentState) 
            if(self.checkArray(closed , currentState)== False):
                closed.append(currentState)
                for move in [0,1,2,3]:
                    nextState = player.move(move, currentState)
                    if(nextState is not None):
                        if(self.checkArray(closed , nextState) == False):
                            depth = len(self.construct_path(stateObj , parents  , currentState)) + 1 
                            open.put(((heuristicObj.getHeuristic(nextState)+depth),nextState))
                            nextStr = self.arrToStr(nextState)
                            curStr = self.arrToStr(currentState)
                            parents[nextStr] = (curStr , move)
                    else:
                        pass 
        return None


# %% [markdown]
# TO RUN CODE AND IF ANY FUNTIONS ARE NEEDED WE WILL ADD BELOW 

# %%
graphObj = Graph()

# %%



