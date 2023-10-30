# %% [markdown]
# Representation of each stateQ
# - First trying with 6 x 6 matrix ! 

# %%
import random
import math
import copy
from queue import PriorityQueue

# %%
def colorx(color):
    if(color == "B"):
        return "W"
    else:
        return "B"

# %% [markdown]
# The class State is the class 
# - initialize the state 
# - check for the win / loss 
# - check for a draw 

# %%
STATE = [['WR','WP','0','0','BP','BR'],['WK','WP','0','0','BP','BK'],['WQ','WP','0','0','BP','BQ'],['WKi','WP','0','0','BP','BKi'],['WK','WP','0','0','BP','BK'],['WR','WP','0','0','BP','BR']]
print(STATE[0][5])

# %%
class State:
    def __init__(self , initialState = [['WR','WP','0','0','BP','BR'],['WK','WP','0','0','BP','BK'],['WQ','WP','0','0','BP','BQ'],['WKi','WP','0','0','BP','BKi'],['WK','WP','0','0','BP','BK'],['WR','WP','0','0','BP','BR']]):
        self.initialState = copy.deepcopy(initialState)
        self.currentState = copy.deepcopy(initialState)
        # puzz = Puzzle()
        # initialState  = puzz.play(finalState)
        # initialState = [1,0,6,4,3,2,7,5,8]
        # self.initialState = initialState
    def isOccupied(self , x , y , color = "NULL"):
        #isOccupied Function takes the three argumentions two coordinates and color and returns bool accordingly
        if self.currentState[x][y] == '0':
            return False
        else:
            if(color == "B"):
                if self.currentState[x][y][0] == 'B':
                    return True
                else:
                    return False
            elif(color == "W"):
                if self.currentState[x][y][0] == 'W':
                    return True
                else:
                    return False
            else:
                return True
    def isAttackedby(self,stateObj,x,y,color):
        #Get all the squares that are attacked by the particular side:
        board = stateObj.get_currentState()
        listofAttackedSquares = []
        puzzObj = Puzzle()
        for x in range(6):
            for y in range(6):
                if board[x][y]!='0' and board[x][y][0]==color:
                    listofAttackedSquares.extend(puzzObj.availableMoves(stateObj,x,y,1)) 
        return (x,y) in listofAttackedSquares
    def isCheck(self,stateObj, color):
        board = stateObj.get_currentState()
        oppColor = colorx(color)
        piece = color +'Ki'
        #Get the coordinates of the king:
        x,y = self.getCoordinates(board,piece)[0]
        return self.isAttackedby(stateObj,x,y,oppColor)
    def isCheckmate(self,presentState, color):
        return False
    def isDraw(self,presentState):
        return False
    def isWin(self,presentState):
        return False
    def islost(self,presentState):
        return False
    def getCoordinates(self ,presentState, piece):
        listOfCoordinates =  []
        for i in range(0,6):
            for j in range(0,6):
                if presentState[i][j] == piece:
                    listOfCoordinates.append([i,j])
        return listOfCoordinates
    def set_initialState(self , stateEx):
        self.initialState = stateEx.copy()
    def get_intialState(self):
        return self.initialState
    def set_currentState(self , stateEx):
        self.currentState = stateEx.copy()
    def get_currentState(self):
        return self.currentState
    def print_state(self):
        print("0   1   2   3   4   5 - Y/X")
        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in self.currentState]))
    def reset(self):
        #This function to avoid the saving in the memory in jupyter notebooks 
        self.currentState = self.initialState.copy()

# %%
testCode = State()
testCode.print_state()
presentState = testCode.get_currentState()
presentState[1][1] = '0'
testCode.print_state()
print(testCode.get_intialState())
testCode.reset()
testCode.print_state()

# %%
#Testing box of the state 
testState = State()
testState.print_state()
print(testState.isOccupied(0,0))
print(testState.isOccupied(0,1,"B"))
print(testState.isOccupied(0,1,"W"))
print(testState.isOccupied(5,5))
print(testState.isOccupied(5,5,"B"))
print(testState.isOccupied(5,5,"W"))
print(testState.isOccupied(3,3))
print(testState.isOccupied(3,3,"B"))
print(testState.isOccupied(3,3,"W"))

# %% [markdown]
# The Puzzle class contains 
# - generateStates to generate the next states given the piece to move 
# - play function to generate all possible states and select the best state 

# %%
string = "BKi"
print(string[0])
print(string[1:])

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
    def movePiece(self , x , y , presentStateobj , xnew , ynew):
        presentState = presentStateobj.get_currentState()
        presentState[xnew][ynew] = presentState[x][y]
        presentState[x][y] = '0'
    def availableMoves(self , stateObj , x , y , choice = 0):
        possiblePositions = []
        currentState = stateObj.get_currentState()
        pieceTomove = currentState[x][y]
        if(pieceTomove== '0'):
            return []
        color = pieceTomove[0]
        oppColor = colorx(color)
        pieceTomove = pieceTomove[1:]
        #possible next squares for the pawn(Soldier:) ) piece to move
        if(pieceTomove == 'P'):
            # It can't make move front when there is a black in front of it so when we search for the attacks we should ignore it
            # 
            if(color == "W"):
                if(y<5 and not stateObj.isOccupied(x,y+1) and choice == 0):
                    possiblePositions.append((x,y+1))
                if(x!= 0 and stateObj.isOccupied(x-1,y+1,"B")):
                    possiblePositions.append((x-1,y+1))
                if(x!= 5 and stateObj.isOccupied(x+1,y+1,"B")):
                    possiblePositions.append((x+1,y+1))
            else:
                if(y>2 and not stateObj.isOccupied(x,y-1) and choice == 0):
                    possiblePositions.append((x,y-1))
                if(x!= 0 and stateObj.isOccupied(x-1,y-1,"W")):
                    possiblePositions.append((x-1,y-1))
                if(x!= 5 and stateObj.isOccupied(x+1,y-1,"W")):
                    possiblePositions.append((x+1,y-1))
        #possible next squares for the rook(Elepant:) ) piece to move     
        elif(pieceTomove == 'R'):
            for i in [-1,1]:
                #checking the horizontal squares
                kx = x
                while True:
                    kx = kx + i
                    if kx<=5 and kx>=0:
                        if stateObj.isOccupied(kx,y,color):
                            break
                        elif not stateObj.isOccupied(kx,y):
                            possiblePositions.append((kx,y))
                        else:
                            if stateObj.isOccupied(kx,y,oppColor):
                                possiblePositions.append((kx,y))
                            break        
                    else:
                        break
            for i in [-1,1]:
                #Now using the same method, get the vertical squares:
                ky = y
                while True:
                    ky = ky + i 
                    if ky<=5 and ky>=0: 
                        if stateObj.isOccupied(x,ky,color):
                            break
                        elif not stateObj.isOccupied(x,ky):
                            possiblePositions.append((x,ky))
                        else:
                            if stateObj.isOccupied(x,ky,oppColor):
                                possiblePositions.append((x,ky))
                            break
                    else:
                        break
        #possible next squares for the Knight(Horse:) ) piece to move     
        elif(pieceTomove == 'K'):
            #The movements are (x+-=2 and y+-=1) or (x+-=1 and y+-=2)
            for i in [-2,2]:
                for j in [-1,1]:
                    kx = x + i
                    ky = y + j
                    if kx<=5 and kx>=0 and ky<=5 and ky>=0:
                        if not stateObj.isOccupied(kx,ky,color):
                            possiblePositions.append((kx,ky))
                        else:
                            if stateObj.isOccupied(kx,ky,oppColor):
                                possiblePositions.append((kx,ky))
            for i in [-1,1]:
                for j in [-2,2]:
                    kx = x + i
                    ky = y + j
                    if kx<=5 and kx>=0 and ky<=5 and ky>=0:
                        if not stateObj.isOccupied(kx,ky,color):
                            possiblePositions.append((kx,ky))
                        else:
                            if stateObj.isOccupied(kx,ky,oppColor):
                                possiblePositions.append((kx,ky))
        #possible next squares for the Queen piece to move
        elif(pieceTomove == 'Q'):
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    if(i==0 and j==0):
                        continue
                    kx = x + i
                    ky = y + j
                    while True:
                        if kx<=5 and kx>=0 and ky<=5 and ky>=0:
                            if stateObj.isOccupied(kx,ky,color):
                                break
                            elif not stateObj.isOccupied(kx,ky):
                                possiblePositions.append((kx,ky))
                            else:
                                if stateObj.isOccupied(kx,ky,oppColor):
                                    possiblePositions.append((kx,ky))
                                break
                        else:
                            break
                        kx = kx + i
                        ky = ky + j
        #possible next squares for the King piece to move
        elif(pieceTomove == 'Ki'):
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    if(i==0 and j==0):
                        continue
                    kx = x + i
                    ky = y + j
                    if kx<=5 and kx>=0 and ky<=5 and ky>=0:
                        if not stateObj.isOccupied(kx,ky,color):
                            possiblePositions.append((kx,ky))
                        else:
                            if stateObj.isOccupied(kx,ky,oppColor):
                                possiblePositions.append((kx,ky))
        #Make sure the possible states will not make moving king check 
        if(choice == 0):
            new_list = []
            for coordinates in possiblePositions:
                x2 = coordinates[0]
                y2 = coordinates[1]
                temp_obj= State(copy.deepcopy(stateObj.get_currentState()))
                self.movePiece(x,y,temp_obj,x2,y2)
                if not stateObj.isCheck(temp_obj,color):
                    new_list.append(coordinates)
            possiblePositions = new_list 
        return possiblePositions

# %%
testState = State()
# testState.print_state()
puzz = Puzzle()
while(True):
    print("To Exit enter 0 else 1: ")
    temp = int(input())
    if(temp == 0):
        testState.reset()
        break
    print("Current State is")
    testState.print_state()
    [x,y] = list(input("Enter the coordinates of the piece to move: ").split())
    x = int(x)
    y = int(y)
    print(f"The piece at {x} , {y} is {testState.currentState[x][y]}")
    print("The Possible states are: ")
    nextPossible = puzz.availableMoves(testState , x , y , 0)
    if(nextPossible == []):
        print("No Possible Moves")
    else:
        print("The Possible states are, select a number: ")
        for i in range(0,len(nextPossible)):
            print(i , nextPossible[i])
        nextSelectedState = int(input())
        [xnew,ynew] = nextPossible[nextSelectedState]
        puzz.movePiece(x,y,testState,xnew,ynew)
        print("The new state is: ")
        testState.print_state()

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



