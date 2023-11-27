# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 09:25:25 2023

@author: Kartikay
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 11:34:16 2023

@author: Kartikay
"""
"""
['q', '0', '0', 'k', 'n', 'r']
['0', '0', 'N', 'p', 'p', 'p']
['0', 'p', '0', '0', '0', '0']
['0', 'P', '0', '0', '0', '0']
['0', '0', 'P', 'Q', 'P', 'P']
['r', '0', '0', 'K', 'N', 'R']

[['0', '0', '0', '0', '0', '0'],['p', '0', '0', 'k', '0', '0'],['P', '0', '0', '0', '0', '0'],['0', '0', '0', 'r', '0', '0'],['0', '0', '0', '0', 'R', '0'],['K', '0', '0', '0', '0', '0']]

[['0', '0', '0', '0', '0', '0'],['p', '0', '0', '0', 'Q', '0'],['q', 'p', 'k', '0', '0', 'N'],['n', '0', '0', '0', '0', '0'],['P', '0', 'P', '0', '0', '0'],['R', '0', 'K', 'R', '0', '0']]

[['r', 'n', 'q', '0', '0', '0'],['0', '0', 'k', 'p', '0', '0'],['0', 'N', 'p', 'p', '0', 'Q'],['P', '0', 'N', '0', '0', '0'],['0', '0', '0', '0', '0', '0'],['R', '0', '0', 'K', 'R', '0']]

[['0', '0', 'N', '0', '0', '0'],['0', '0', 'P', '0', '0', 'k'],['0', '0', '0', '0', '0', '0'],['P', '0', '0', '0', '0', 'p'],['K', '0', '0', '0', '0', 'P'],['0', '0', '0', '0', 'R', '0']]

[['r', 'n', '0', '0', 'n', 'N'],['p', 'q', '0', 'k', 'N', '0'],['0', 'p', '0', 'p', '0', '0'],['0', 'P', '0', 'P', '0', 'p'],['0', 'Q', 'P', '0', '0', 'P'],['R', '0', '0', 'K', 'R', '0']]

[['k','0','0','0','0','0'],['0','0','0','0','0','0'],['0','0','0','0','0','0'],['0','0','0','0','0','0'],['0','0','0','0','0','0'],['K','Q','0','0','0','0']]

[['k','0','0','0','0','0'],['Q','0','0','0','0','0'],['0','P','0','0','0','0'],['0','0','0','0','0','0'],['0','0','0','0','0','0'],['K','0','0','0','0','0']]

[['r','n','q','k','n','r'],['p','p','p','p','p','p'],['0','0','0','0','0','0'],['0','0','0','0','0','0'],['P','P','P','P','P','P'],['R','N','Q','K','N','R']]                                                      

r 0 0 q n r ,0 0 0 n k p ,p P P p p 0 ,N 0 0 0 0 0 ,P 0 N Q 0 P ,R 0 0 K R 0 

q 0 0 k n r,0 0 N p p p,0 p 0 0 0 0,0 P 0 0 0 0,0 0 P Q P P,r 0 0 K N R

p r 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,R 0 0 0 0 P

r 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,0 0 0 0 0 0,R 0 0 0 0 0

r n q k n r,p p p p p p,0 0 0 0 0 0,0 0 0 0 0 0,P P P P P P,R N Q K N R

r n q k n r
p p p p p p
0 0 0 0 0 0
0 0 0 0 0 0
R N Q K N R

['r','kn','q','k','kn','r']
['p','p','p','p','p','p']
['0','0','0','0','0','0']
['0','0','0','0','0','0']
['P','P','P','P','P','P']
['R','Kn','Q','K','Kn','R']

"""
import random
import pygame
import copy

def colorx(color):
    if(color == "B"):
        return "W"
    else:
        return "B"
searched = {} 

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
        if(x>5 or x<0 or y > 5 or y <0):
            return False
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
    def isAttackedby(self,stateObj,xi,yi,color):
        #Get all the squares that are attacked by the particular side:
        board = stateObj.get_currentState()
        listofAttackedSquares = []
        puzzObj = Puzzle()
        # print("In attack by")
        for x in range(6):
            for y in range(6):
                if board[x][y]!='0' and board[x][y][0]==color:
                    listofAttackedSquares.extend(puzzObj.availablePieceMoves(stateObj,x,y,1)) 
        # print("List of Attaclks", listofAttackedSquares)
        output = False
        for i in listofAttackedSquares:
            if i[1][0]==xi and i[1][1]==yi:
                output = True
                break
        return output
    def piecesInBoard(self , stateObj ,color= "NULL"):
        #This function returns the number of pieces in the board of the particular color
        piecesLeft = []
        board = stateObj.get_currentState()
        for i in range(0,6):
            for j in range(0,6):
                if board[i][j] != '0':
                    if(color == "NULL"):
                        piecesLeft.append(board[i][j])
                    elif board[i][j][0] == color:
                        piecesLeft.append(board[i][j])
        return piecesLeft
    def positionsOccupied(self , stateObj , color = "NULL"):
        #This function returns the list of positions occupied by the pieces of the particular color
        positions = []
        board = stateObj.get_currentState()
        for i in range(0,6):
            for j in range(0,6):
                if board[i][j] != '0':
                    if(color == "NULL"):
                        positions.append([i,j])
                    elif board[i][j][0] == color:
                        positions.append([i,j])
        return positions
    def isCheck(self,stateObj, color):
        board = stateObj.get_currentState()
        # print("board",board)
        oppColor = colorx(color)
        piece = color +'Ki'
        #Get the coordinates of the king:
        x,y = self.getCoordinates(board,piece)[0]
        # print("In check , king position ", x ,y)
        return self.isAttackedby(stateObj,x,y,oppColor)
    def isStalemate(self , stateObj, color= "NULL"):
        if color=="NULL":
            return self.isStalemate(stateObj,'W') or self.isStalemate(stateObj,'B')
        puzzObj = Puzzle()
        if not self.isCheck(stateObj,color) and puzzObj.availableMoves(stateObj,color)==[]:
                return True
        return False
    def isCheckmate(self , stateObj, color= "NULL"):
        if color=="NULL":
            return self.isCheckmate(stateObj,'W') or self.isCheckmate(stateObj,'B')
        puzzObj = Puzzle()
        if self.isCheck(stateObj,color) and puzzObj.availableMoves(stateObj,color)==[]:
                return True
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


class Puzzle:
    def __init__(self) -> None:
        pass

    def movePiece(self , x , y , presentStateobj , xnew , ynew):
        presentState = presentStateobj.get_currentState()
        presentState[xnew][ynew] = presentState[x][y]
        presentState[x][y] = '0'
    def availablePieceMoves(self , stateObj , x , y , choice = 0):
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
                    # print("not check" , x, y , x2 , y2)
                    new_list.append([[x,y],[x2,y2]])
            possiblePositions = new_list 
        if(choice == 1):
            new_list = []
            for coordinates in possiblePositions:
                x2 = coordinates[0]
                y2 = coordinates[1]
                new_list.append([[x,y],[x2,y2]])
            possiblePositions = new_list
        return possiblePositions
    def availableMoves(self , stateObj , color):
        #This function returns all the possible moves for the particular color
        #First get the positions of the pieces of the color
        positions = stateObj.positionsOccupied(stateObj,color)
        #Now get the available moves for each piece:
        availableMoves = []
        for position in positions:
            x = position[0]
            y = position[1]
            availableMoves.extend(self.availablePieceMoves(stateObj,x,y))
        return availableMoves
    


class Heuristic:
    stateNew = State()
#     FinalState = stateNew.get_finalState()

    def __init__(self):
            self.pawn_table = [  0, 50, 10,  5,  0,  5,
                                          0, 50, 10,  5,  0, -5,
                                          0, 50, 20, 10,  0, -10,
                                          0, 50, 30, 25, 20,  0,
                                          0, 50, 30, 25, 20,  0,
                                          0, 50, 20, 10,  0, -10]
            self.knight_table = [-50, -40, -30, -30, -40, -50,
                                                -40, -20,   0,   5, -20, -90,
                                                -30,   0,  10,  15,   0, -30,
                                                -30,   0,  15,  20,   5, -30,
                                                -40, -20,   0,   5, -20, -90,
                                                -50, -40, -30, -30, -40, -50]
            self.rook_table = [ 0,  5, -5, -5, -5,  0,
                                          0, 10,  0,  0,  0,  0,
                                          0, 10,  0,  0,  0,  0,
                                          0, 10,  0,  0,  0,  5,
                                          0, 10,  0,  0,  0,  5,
                                          0,  5, -5, -5,  0,  0]
            self.queen_table = [-20, -10, -10,  -5, -10, -20,
                                          -10,   0,   0,   0,   0, -10,
                                          -10,   0,   5,   5,   5, -10,
                                                -5,   0,   5,   5,   5,  -5,
                                          -10,   0,   5,   5,   5, -10,
                                          -20, -10, -10,   0, -10, -20]
            self.king_table = [-30, -40, -40, -50, -50, -30,
                                          -40, -40, -20, -20, -20, -10,
                                          -40, -40,   0,   0,   0,   0,
                                          -50, -50,   0,   0,   0,   0,
                                          -50, -50,   0,   0,   0,   0,
                                          -40, -40,   0,   0,   0,   0]
            self.king_endgame_table = [-50, -30, -30, -30, -30, -30,
                                                      -40, -20, -10, -10, -10, -10,
                                                      -40,   0,  20,  30,  30,  20,
                                                      -50,   0,  30,  40,  40,  30,
                                                      -50,   0,  30,  40,  40,  30,
                                                      -40, -20, -10, -10, -10, -10]

    def getHeuristic(self, presentState):
          if(self.heuristic ==0):
                return self.nWrongTiles(presentState)
    #First Heuristic Function 
    def nWrongTiles(self, presentState):
            return 0
    def count(self, board , piece):
            count = 0
            for i in range(0,6):
                  for j in range(0,6):
                        if board[i][j] == piece:
                              count = count + 1
            return count
    
    def pieceSquareTable(self,flatboard,gamephase):
      #Initialize score:
      score = 0
      #Go through each square:
      for i in range(36):
            if flatboard[i]==0:
                  #Empty square
                  continue
            #Get data:
            piece = flatboard[i][1:]
            color = flatboard[i][0]
            sign = +1
            #Adjust index if black piece, since piece sqaure tables
            #were designed for white:
            if color=='B':
                  #  i = (7-i/8)*8 + i%8
                  # Adjust index if black piece, since piece square tables were designed for white:
                  i = (5 - i//6)*6 + i%6
            #Adjust score:
            if piece=='P':
                  score += sign*self.pawn_table[i]
            elif piece=='K':
                  score+= sign*self.knight_table[i]
            elif piece=='R':
                  score+=sign*self.rook_table[i]

            elif piece=='Q':
                  score+=sign*self.queen_table[i]
            elif piece=='Ki':
                  #King has different table values based on phase
                  #of the game:
                  if gamephase=='opening':
                        score+=sign*self.king_table[i]
                  else:
                        score+=sign*self.king_endgame_table[i]
      return score  
    def doubledPawns(self ,stateObj,color):
      #Get indices of pawns:
      currentState = stateObj.get_currentState()
      listofpawns = stateObj.getCoordinates(currentState ,color+"P")
      #Count the number of doubled pawns by counting occurences of
      #repeats in their x-coordinates:
      repeats = 0
      temp = []
      for pawnpos in listofpawns:
            if pawnpos[1] in temp:
                  repeats = repeats + 1
            else:
                  temp.append(pawnpos[1])
      return repeats
# isOccupied(self , x , y , color = "NULL"):
    def blockedPawns(self ,stateObj,color):
      currentState = stateObj.get_currentState()
      listofpawns = stateObj.getCoordinates(currentState ,color+"P")
      blocked = 0
      #Self explanatory:
      for pawnpos in listofpawns:
            if ((color=='w' and stateObj.isOccupied(pawnpos[0],pawnpos[1]+1,'B')) or (color=='b' and stateObj.isOccupied(pawnpos[0],pawnpos[1]-1,'W'))):
                  blocked = blocked + 1
      return blocked
    def isolatedPawns(self ,stateObj,color):
      currentState = stateObj.get_currentState()
      listofpawns = stateObj.getCoordinates(currentState ,color+"P")
      #Get x coordinates of all the pawns:
      xlist = [y for (x,y) in listofpawns]
      isolated = 0
      for x in xlist:
            if x!=0 and x!=5:
                  #For non-edge cases:
                  if x-1 not in xlist and x+1 not in xlist:
                        isolated+=1
            elif x==0 and 1 not in xlist:
                  #Left edge:
                  isolated+=1
            elif x==5 and 4 not in xlist:
                  #Right edge:
                  isolated+=1
      return isolated

    def evaluate(self , presentState):
      if presentState.isCheckmate(presentState,'W'):
        #Major advantage to black
        return -20000
      if presentState.isCheckmate(presentState,'B'):
        
        #Major advantage to white
        return 20000
      if presentState.isStalemate(presentState,'W'):
        #Stalemate
        return -10000
      if presentState.isStalemate(presentState,'B'):
         #Stalemate
         return 10000
      board = presentState.get_currentState()
      flatboard = [x for row in board for x in row]
      C_BP = self.count(board,'BP')
      C_BR = self.count(board,'BR')
      C_BK = self.count(board,'BK')
      C_BQ = self.count(board,'BQ')
      C_WP = self.count(board,'WP')
      C_WR = self.count(board,'WR')
      C_WK = self.count(board,'WK')
      C_WQ = self.count(board,'WQ')
      # whiteMaterial = 9*Qw + 5*Rw + 3*Nw + 3*Bw + 1*Pw
      # blackMaterial = 9*Qb + 5*Rb + 3*Nb + 3*Bb + 1*Pb
      whiteMaterial = 9*C_WQ + 5*C_WR + 3*C_WK + 1*C_WP
      blackMaterial = 9*C_BQ + 5*C_BR + 3*C_BK + 1*C_BP
      # numofmoves = len(position.gethistory())
      gamephase = 'opening'
      # if numofmoves>40 or (whiteMaterial<14 and blackMaterial<14):
      #       gamephase = 'ending'
      #A note again: Determining game phase is again one the attempts
      #to make the AI smarter when analysing boards and has not been 
      #implemented to its full potential.
      #Calculate number of doubled, blocked, and isolated pawns for 
      #both sides:
      Dw = self.doubledPawns(presentState,'white')
      Db = self.doubledPawns(presentState,'black')
      Sw = self.blockedPawns(presentState,'white')
      Sb = self.blockedPawns(presentState,'black')
      Iw = self.isolatedPawns(presentState,'white')
      Ib = self.isolatedPawns(presentState,'black')
      #Evaluate position based on above data:
      evaluation1 = 900*(C_WQ - C_BQ) + 500*(C_WR - C_BR) +320*(C_WK - C_BK) +100*(C_WP- C_BP ) +-30*(Dw-Db + Sw-Sb + Iw- Ib)
      #Evaluate position based on piece square tables:
      evaluation2 = self.pieceSquareTable(flatboard,gamephase)
      #Sum the evaluations:
      evaluation = evaluation1 + evaluation2
      #Return it:
      return evaluation


class Graph:
    def __init__(self):
        pass
    def pos2key(self , stateObj , player):
    #Get board:
        board = stateObj.get_currentState()
        #Convert the board into a tuple so it is hashable:
        boardTuple = []
        for row in board:
            boardTuple.append(tuple(row))
        boardTuple = tuple(boardTuple)
        #Get castling rights:
        key = (boardTuple, player)        #Return the key:
        return key
    def negMax(self , stateObj , depth , alpha , beta , color , bestMoveReturn , root = True):
        heuristicObj = Heuristic()
        puzzObj = Puzzle()
        colorsign = 1 if color == "W" else -1
        currentPosition = stateObj.get_currentState()
        if(root):
            key = self.pos2key(stateObj , color)
            # if key in openings:
            #     bestMoveReturn[:] = random.choice(openings[key])
            #     return
        global searched
        if(depth == 0):
            return colorsign * heuristicObj.evaluate(stateObj)
        moves = puzzObj.availableMoves(stateObj , color)
        # print("moves: ",moves)
        if(moves == []):
            return colorsign * heuristicObj.evaluate(stateObj)
        if(root):
            bestMove = moves[0]
        bestValue = -100000
        for move in moves:
            newState = copy.deepcopy(stateObj)
            puzzObj.movePiece(move[0][0],move[0][1],newState,move[1][0],move[1][1])
            key = self.pos2key(newState , color)
            if(key in searched):
                value = searched[key]
            else:
                value = -self.negMax(newState,depth-1,-beta,-alpha,colorx(color),[],False)
                searched[key] = value
            if(value > bestValue):
                bestValue = value
                if(root):
                    bestMove = move
            alpha = max(alpha,value)
            if(alpha >= beta):
                break
        if(root):
            searched = {}
            bestMoveReturn[:] =  bestMove
            return
        return bestValue


class Generator:
    def kingcheck(self,T,c):
        black=['r','n','b','q','k','p']
        white=['R','N','B','Q','K','P']
        flg=0
        for i in range(0,6):
            for j in range(0,6):
                if T[i][j]=='k' and c==0:
                    flg=1
                    break
                if T[i][j]=='K'and c==1:
                    flg=1
                    break
            if flg==1:
                break
        if c==0:
            if i<5:
                if j<5:
                    if T[i+1][j+1]=='P':
                        return True
                    for k in range(j+1,6):
                        if T[i][k] in black or T[i][k] in ['K','N','P','B']:
                            break
                        if T[i][k]=='Q' or T[i][k]=='R':
                            return True
                    k=min(5-i,5-j)
                    for l in range(1,k+1):
                        if T[i+l][j+l] in black or T[i+l][j+l] in ['K','N','P','R']:
                            break
                        if T[i+l][j+l] in ['Q','B']:
                            return True
                if j>0:
                    if T[i+1][j-1]=='P':
                        return True
                    for k in reversed(range(0,j)):
                        if T[i][k] in black or T[i][k] in ['K','N','P','B']:
                            break
                        if T[i][k]=='Q' or T[i][k]=='R':
                            return True
                    k=min(5-i,j)
                    for l in range(1,k+1):
                        if T[i+l][j-l] in black or T[i+l][j-l] in ['K','N','P','R']:
                            break
                        if T[i+l][j-l] in ['Q','B']:
                            return True               
                for k in range(i+1,6):
                    if T[k][j] in black or T[k][j] in ['K','N','P','B']:
                        break
                    if T[k][j]=='Q' or T[k][j]=='R':
                        return True
            if i>0:
                if j<5:
                    for k in range(j+1,6):
                        if T[i][k] in black or T[i][k] in ['K','N','P','B']:
                            break
                        if T[i][k]=='Q' or T[i][k]=='R':
                            return True
                    k=min(i,5-j)
                    for l in range(1,k+1):
                        if T[i-l][j+l] in black or T[i-l][j+l] in ['K','N','P','R']:
                            break
                        if T[i-l][j+l] in ['Q','B']:
                            return True
                if j>0:
                    for k in reversed(range(0,j)):
                        if T[i][k] in black or T[i][k] in ['K','N','P','B']:
                            break
                        if T[i][k]=='Q' or T[i][k]=='R':
                            return True
                    k=min(i,j)
                    for l in range(1,k+1):
                        if T[i-l][j-l] in black or T[i-l][j-l] in ['K','N','P','R']:
                            break
                        if T[i-l][j-l] in ['Q','B']:
                            return True
                    
                for k in reversed(range(0,i)):
                    if T[k][j] in black or T[k][j] in ['K','N','P','B']:
                        break
                    if T[k][j]=='Q' or T[k][j]=='R':
                        return True
            J1=[[i+2,j+1],[i+2,j-1],[i-2,j+1],[i-2,j-1],[i+1,j+2],[i-1,j+2],[i+1,j-2],[i-1,j-2]]
            J2=[[i+1,j+1],[i+1,j-1],[i-1,j+1],[i-1,j-1],[i,j+1],[i,j-1],[i+1,j],[i-1,j]]
            for k in J1:
                if 0<=k[0]<=5 and 0<=k[1]<=5:
                    if T[k[0]][k[1]]=='N':
                        print("Nighto")
                        return True
            for k in J2:
                if 0<=k[0]<=5 and 0<=k[1]<=5:
                    if T[k[0]][k[1]]=='K':
                        return True
        if c==1:
            if i<5:
                if j<5:
                    for k in range(j+1,6):
                        if T[i][k] in white or T[i][k] in ['k','n','p','b']:
                            break
                        if T[i][k]=='q' or T[i][k]=='r':
                            print("Here1")
                            return True
                    k=min(5-i,5-j)
                    for l in range(1,k+1):
                        if T[i+l][j+l] in white or T[i+l][j+l] in ['k','n','p','r']:
                            break
                        if T[i+l][j+l] in ['q','b']:
                            return True
                if j>0:
                    for k in reversed(range(0,j)):
                        if T[i][k] in white or T[i][k] in ['k','n','p','b']:
                            break
                        if T[i][k]=='q' or T[i][k]=='r':
                            print("Here3")
                            return True
                    k=min(5-i,j)
                    for l in range(1,k+1):
                        if T[i+l][j-l] in white or T[i+l][j-l] in ['k','n','p','r']:
                            break
                        if T[i+l][j-l] in ['q','b']:
                            return True                
                for k in range(i+1,6):
                    if T[k][j] in white or T[k][j] in ['k','n','p','b']:
                        break
                    if T[k][j]=='q' or T[k][j]=='r':
                        print("Here5")
                        return True
            if i>0:
                if j<5:
                    if T[i-1][j+1]=='p':
                        print("Here6")
                        return True
                    for k in range(j+1,6):
                        if T[i][k] in white or T[i][k] in ['k','n','p','b']:
                            break
                        if T[i][k]=='q' or T[i][k]=='r':
                            print("Here7")
                            return True
                    k=min(i,5-j)
                    for l in range(1,k+1):
                        if T[i-l][j+l] in white or T[i-l][j+l] in ['k','n','p','r']:
                            break
                        if T[i-l][j+l] in ['q','b']:
                            return True
                if j>0:
                    if T[i-1][j-1]=='p':
                        print("Here9")
                        return True
                    for k in reversed(range(0,j)):
                        if T[i][k] in white or T[i][k] in ['k','n','p','b']:
                            break
                        if T[i][k]=='q' or T[i][k]=='r':
                            print("Here10")
                            return True
                    k=min(i,j)
                    for l in range(1,k+1):
                        if T[i-l][j-l] in white or T[i-l][j-l] in ['k','n','p','r']:
                            break
                        if T[i-l][j-l] in ['q','b']:
                            return True
                    
                for k in reversed(range(0,i)):
                    if T[k][j] in white or T[k][j] in ['k','n','p','b']:
                        break
                    if T[k][j]=='q' or T[k][j]=='r':
                        return True
            J1=[[i+2,j+1],[i+2,j-1],[i-2,j+1],[i-2,j-1],[i+1,j+2],[i-1,j+2],[i+1,j-2],[i-1,j-2]]
            J2=[[i+1,j+1],[i+1,j-1],[i-1,j+1],[i-1,j-1],[i,j+1],[i,j-1],[i+1,j],[i-1,j]]
            for k in J1:
                if 0<=k[0]<=5 and 0<=k[1]<=5:
                    if T[k[0]][k[1]]=='n':
                        print("Here12")
                        return True
            for k in J2:
                if 0<=k[0]<=5 and 0<=k[1]<=5:
                    if T[k[0]][k[1]]=='k':
                        print("Here13")
                        return True          
        return False
            
                
                
        
    def movleg(self,T,i,j,c):
        black=['r','n','b','q','k','p']
        white=['R','N','B','Q','K','P']
        s=[]
        if T[i][j]=='0':
            return s
        count=0
        for a in T:
            for b in a:
                if b=='k' or b=='K':
                    count=count+1
        if count==1:
            s.append(T)
            return s

        if c==0:
            if T[i][j]=='r' or T[i][j]=='q':
                for k in range(i+1,6):
                    if T[k][j] in white:
                        M=copy.deepcopy(T)
                        M[i][j]='0'
                        M[k][j]=T[i][j]
                        s.append(M)
                        break
                    if T[k][j] in black:
                        break
                    M=copy.deepcopy(T)
                    M[i][j]='0'
                    M[k][j]=T[i][j]
                    s.append(M)
                for k in range(j+1,6):
                    if T[i][k] in white:
                        M=copy.deepcopy(T)
                        M[i][j]='0'
                        M[i][k]=T[i][j]
                        s.append(M)
                        break
                    if T[i][k] in black:
                        break
                    M=copy.deepcopy(T)
                    M[i][j]='0'
                    M[i][k]=T[i][j]
                    s.append(M)
                for k in reversed(range(0,i)):
                    if T[k][j] in white:
                        M=copy.deepcopy(T)
                        M[i][j]='0'
                        M[k][j]=T[i][j]
                        s.append(M)
                        break
                    if T[k][j] in black:
                        break
                    M=copy.deepcopy(T)
                    M[i][j]='0'
                    M[k][j]=T[i][j]
                    s.append(M)
                for k in reversed(range(0,j)):
                    if T[i][k] in white:
                        M=copy.deepcopy(T)
                        M[i][j]='0'
                        M[i][k]=T[i][j]
                        s.append(M)
                        break
                    if T[i][k] in black:
                        break
                    M=copy.deepcopy(T)
                    M[i][j]='0'
                    M[i][k]=T[i][j]
                    s.append(M)
            
            if T[i][j]=='n':
                J=[[i+2,j+1],[i+2,j-1],[i-2,j+1],[i-2,j-1],[i+1,j+2],[i-1,j+2],[i+1,j-2],[i-1,j-2]]
                for k in range(0,8):
                    if(0<=J[k][0]<=5 and 0<=J[k][1]<=5):
                        if T[J[k][0]][J[k][1]] not in black:
                            M=copy.deepcopy(T)
                            M[i][j]='0'
                            M[J[k][0]][J[k][1]]=T[i][j]
                            s.append(M)
            
            
            if T[i][j]=='b' or T[i][j]=='q':
                J1=[[0],[0],[0],[0],[0]]
                J2=[[0],[0],[0],[0],[0]]
                J3=[[0],[0],[0],[0],[0]]
                J4=[[0],[0],[0],[0],[0]]
                for k in range(1,6):
                    J1[k-1]=[i+k,j+k]
                    J2[k-1]=[i+k,j-k]
                    J3[k-1]=[i-k,j+k]
                    J4[k-1]=[i-k,j-k]
                #print(J1)
                for k in range(0,5):
                    if(0<=J1[k][0]<=5 and 0<=J1[k][1]<=5):
                        if T[J1[k][0]][J1[k][1]] in black:
                            break
                        if T[J1[k][0]][J1[k][1]] in white:
                            M=copy.deepcopy(T)
                            M[i][j]='0'
                            M[J1[k][0]][J1[k][1]]=T[i][j]
                            s.append(M)
                            break
                        M=copy.deepcopy(T)
                        M[i][j]='0'
                        M[J1[k][0]][J1[k][1]]=T[i][j]
                        s.append(M)
                for k in range(0,5):
                    if(0<=J2[k][0]<=5 and 0<=J2[k][1]<=5):
                        if T[J2[k][0]][J2[k][1]] in black:
                            break
                        if T[J2[k][0]][J2[k][1]] in white:
                            M=copy.deepcopy(T)
                            M[i][j]='0'
                            M[J2[k][0]][J2[k][1]]=T[i][j]
                            s.append(M)
                            break
                        M=copy.deepcopy(T)
                        M[i][j]='0'
                        M[J2[k][0]][J2[k][1]]=T[i][j]
                        s.append(M)
                for k in range(0,5):
                    if(0<=J3[k][0]<=5 and 0<=J3[k][1]<=5):
                        if T[J3[k][0]][J3[k][1]] in black:
                            break
                        if T[J3[k][0]][J3[k][1]] in white:
                            M=copy.deepcopy(T)
                            M[i][j]='0'
                            M[J3[k][0]][J3[k][1]]=T[i][j]
                            s.append(M)
                            break
                        M=copy.deepcopy(T)
                        M[i][j]='0'
                        M[J3[k][0]][J3[k][1]]=T[i][j]
                        s.append(M)
                for k in range(0,5):
                    if(0<=J4[k][0]<=5 and 0<=J4[k][1]<=5):
                        if T[J4[k][0]][J4[k][1]] in black:
                            break
                        if T[J4[k][0]][J4[k][1]] in white:
                            M=copy.deepcopy(T)
                            M[i][j]='0'
                            M[J4[k][0]][J4[k][1]]=T[i][j]
                            s.append(M)
                            break
                        M=copy.deepcopy(T)
                        M[i][j]='0'
                        M[J4[k][0]][J4[k][1]]=T[i][j]
                        s.append(M)
            
            if(T[i][j]=='p'):
                if(i<5 and T[i+1][j] not in white and T[i+1][j] not in black):
                    if(i+1==5):
                        M=copy.deepcopy(T)
                        M[i][j]='0'
                        M[i+1][j]='q'
                        s.append(M)
                        M=copy.deepcopy(T)
                        M[i][j]='0'
                        M[i+1][j]='r'
                        s.append(M)
                        M=copy.deepcopy(T)
                        M[i][j]='0'
                        M[i+1][j]='n'
                        s.append(M)
                    else:
                        M=copy.deepcopy(T)
                        M[i][j]='0'
                        M[i+1][j]='p'
                        s.append(M)
                if(i<5):
                    if(j<5):
                        if(T[i+1][j+1] in white):
                            if(i+1==5):
                                M=copy.deepcopy(T)
                                M[i][j]='0'
                                M[i+1][j+1]='q'
                                s.append(M)
                                M=copy.deepcopy(T)
                                M[i][j]='0'
                                M[i+1][j+1]='r'
                                s.append(M)
                                M=copy.deepcopy(T)
                                M[i][j]='0'
                                M[i+1][j+1]='n'
                                s.append(M)
                            else:
                                M=copy.deepcopy(T)
                                M[i][j]='0'
                                M[i+1][j+1]='p'
                                s.append(M)
                                
                    if(j>0):
                        if(T[i+1][j-1] in white):
                            if(i+1==5):
                                M=copy.deepcopy(T)
                                M[i][j]='0'
                                M[i+1][j-1]='q'
                                s.append(M)
                                M=copy.deepcopy(T)
                                M[i][j]='0'
                                M[i+1][j-1]='r'
                                s.append(M)
                                M=copy.deepcopy(T)
                                M[i][j]='0'
                                M[i+1][j-1]='n'
                                s.append(M)
                            else:
                                M=copy.deepcopy(T)
                                M[i][j]='0'
                                M[i+1][j-1]='p'
                                s.append(M)
                    
                    
            
            if(T[i][j]=='k'):
                for k in [-1,0,1]:
                    for l in [-1,0,1]:
                        if 0<=i+k<=5 and 0<=j+l<=5:
                            if(T[i+k][j+l] not in black):
                                M=copy.deepcopy(T)
                                M[i][j]='0'
                                M[i+k][j+l]=T[i][j]
                                s.append(M)
                                
            return(s)

        if c==1:
            if T[i][j]=='R' or T[i][j]=='Q':
                for k in range(i+1,6):
                    if T[k][j] in black:
                        M=copy.deepcopy(T)
                        M[i][j]='0'
                        M[k][j]=T[i][j]
                        s.append(M)
                        break
                    if T[k][j] in white:
                        break
                    M=copy.deepcopy(T)
                    M[i][j]='0'
                    M[k][j]=T[i][j]
                    s.append(M)
                for k in range(j+1,6):
                    if T[i][k] in black:
                        M=copy.deepcopy(T)
                        M[i][j]='0'
                        M[i][k]=T[i][j]
                        s.append(M)
                        break
                    if T[i][k] in white:
                        break
                    M=copy.deepcopy(T)
                    M[i][j]='0'
                    M[i][k]=T[i][j]
                    s.append(M)
                for k in reversed(range(0,i)):
                    if T[k][j] in black:
                        M=copy.deepcopy(T)
                        M[i][j]='0'
                        M[k][j]=T[i][j]
                        s.append(M)
                        break
                    if T[k][j] in white:
                        break
                    M=copy.deepcopy(T)
                    M[i][j]='0'
                    M[k][j]=T[i][j]
                    s.append(M)
                for k in reversed(range(0,j)):
                    if T[i][k] in black:
                        M=copy.deepcopy(T)
                        M[i][j]='0'
                        M[i][k]=T[i][j]
                        s.append(M)
                        break
                    if T[i][k] in white:
                        break
                    M=copy.deepcopy(T)
                    M[i][j]='0'
                    M[i][k]=T[i][j]
                    s.append(M)
            
            if T[i][j]=='N':
                J=[[i+2,j+1],[i+2,j-1],[i-2,j+1],[i-2,j-1],[i+1,j+2],[i-1,j+2],[i+1,j-2],[i-1,j-2]]
                for k in range(0,8):
                    if(0<=J[k][0]<=5 and 0<=J[k][1]<=5):
                        if T[J[k][0]][J[k][1]] not in white:
                            M=copy.deepcopy(T)
                            M[i][j]='0'
                            M[J[k][0]][J[k][1]]=T[i][j]
                            s.append(M)
            
            
            if T[i][j]=='B' or T[i][j]=='Q':
                J1=[[0],[0],[0],[0],[0]]
                J2=[[0],[0],[0],[0],[0]]
                J3=[[0],[0],[0],[0],[0]]
                J4=[[0],[0],[0],[0],[0]]
                for k in range(1,6):
                    J1[k-1]=[i+k,j+k]
                    J2[k-1]=[i+k,j-k]
                    J3[k-1]=[i-k,j+k]
                    J4[k-1]=[i-k,j-k]
                #print(J1)
                for k in range(0,5):
                    if(0<=J1[k][0]<=5 and 0<=J1[k][1]<=5):
                        if T[J1[k][0]][J1[k][1]] in white:
                            break
                        if T[J1[k][0]][J1[k][1]] in black:
                            M=copy.deepcopy(T)
                            M[i][j]='0'
                            M[J1[k][0]][J1[k][1]]=T[i][j]
                            s.append(M)
                            break
                        M=copy.deepcopy(T)
                        M[i][j]='0'
                        M[J1[k][0]][J1[k][1]]=T[i][j]
                        s.append(M)
                for k in range(0,5):
                    if(0<=J2[k][0]<=5 and 0<=J2[k][1]<=5):
                        if T[J2[k][0]][J2[k][1]] in white:
                            break
                        if T[J2[k][0]][J2[k][1]] in black:
                            M=copy.deepcopy(T)
                            M[i][j]='0'
                            M[J2[k][0]][J2[k][1]]=T[i][j]
                            s.append(M)
                            break
                        M=copy.deepcopy(T)
                        M[i][j]='0'
                        M[J2[k][0]][J2[k][1]]=T[i][j]
                        s.append(M)
                for k in range(0,5):
                    if(0<=J3[k][0]<=5 and 0<=J3[k][1]<=5):
                        if T[J3[k][0]][J3[k][1]] in white:
                            break
                        if T[J3[k][0]][J3[k][1]] in black:
                            M=copy.deepcopy(T)
                            M[i][j]='0'
                            M[J3[k][0]][J3[k][1]]=T[i][j]
                            s.append(M)
                            break
                        M=copy.deepcopy(T)
                        M[i][j]='0'
                        M[J3[k][0]][J3[k][1]]=T[i][j]
                        s.append(M)
                for k in range(0,5):
                    if(0<=J4[k][0]<=5 and 0<=J4[k][1]<=5):
                        if T[J4[k][0]][J4[k][1]] in white:
                            break
                        if T[J4[k][0]][J4[k][1]] in black:
                            M=copy.deepcopy(T)
                            M[i][j]='0'
                            M[J4[k][0]][J4[k][1]]=T[i][j]
                            s.append(M)
                            break
                        M=copy.deepcopy(T)
                        M[i][j]='0'
                        M[J4[k][0]][J4[k][1]]=T[i][j]
                        s.append(M)
            
            if(T[i][j]=='P'):
                if(i>0 and T[i-1][j] not in white and T[i-1][j] not in black):
                    if(i-1==0):
                        M=copy.deepcopy(T)
                        M[i][j]='0'
                        M[i-1][j]='Q'
                        s.append(M)
                        M=copy.deepcopy(T)
                        M[i][j]='0'
                        M[i-1][j]='R'
                        s.append(M)
                        M=copy.deepcopy(T)
                        M[i][j]='0'
                        M[i-1][j]='N'
                        s.append(M)
                    else:
                        M=copy.deepcopy(T)
                        M[i][j]='0'
                        M[i-1][j]='P'
                        s.append(M)
                if(i>0):
                    if(j<5):
                        if(T[i-1][j+1] in black):
                            if(i-1==0):
                                M=copy.deepcopy(T)
                                M[i][j]='0'
                                M[i-1][j+1]='Q'
                                s.append(M)
                                M=copy.deepcopy(T)
                                M[i][j]='0'
                                M[i-1][j+1]='R'
                                s.append(M)
                                M=copy.deepcopy(T)
                                M[i][j]='0'
                                M[i-1][j+1]='N'
                                s.append(M)
                            else:
                                M=copy.deepcopy(T)
                                M[i][j]='0'
                                M[i-1][j+1]='P'
                                s.append(M)
                    if(j>0):
                        if(T[i-1][j-1] in black):
                            if(i-1==0):
                                M=copy.deepcopy(T)
                                M[i][j]='0'
                                M[i-1][j-1]='Q'
                                s.append(M)
                                M=copy.deepcopy(T)
                                M[i][j]='0'
                                M[i-1][j-1]='R'
                                s.append(M)
                                M=copy.deepcopy(T)
                                M[i][j]='0'
                                M[i-1][j-1]='N'
                                s.append(M)
                            else:
                                M=copy.deepcopy(T)
                                M[i][j]='0'
                                M[i-1][j-1]='P'
                                s.append(M)
            
            if(T[i][j]=='K'):
                for k in [-1,0,1]:
                    for l in [-1,0,1]:
                        if 0<=i+k<=5 and 0<=j+l<=5:
                            if(T[i+k][j+l] not in white):
                                M=copy.deepcopy(T)
                                M[i][j]='0'
                                M[i+k][j+l]=T[i][j]
                                s.append(M)
            
            
            for z in s:
                count=0
                for a in z:
                    for b in a:
                        if b=='k' or b=='K':
                            count=count+1
                if count==1:
                    #print("Here")
                    s=[]
                    s.append(z)
                    return s
                
                
                
            return(s)
                        

    def minmax(self,T,c,d,n):
        Y=Generator()
        if n==d:
            legal=[]
            rand=[]
            if(c==1):
                for i in range(0,6):
                    for j in range(0,6):
                        s=Y.movleg(T,i,j,c)
                        for k in range(0,len(s)):
                            legal.append(s[k])
                k=0
                M=-9000
                for i in range(0,len(legal)):
                    V=Y.gvalu(legal[i],c)
                    if V>M:
                        rand=[]
                        M=V
                        k=i
                        rand.append(legal[k])
                    elif V==M:
                        rand.append(legal[i])
            if(c==0):
                for i in range(0,6):
                    for j in range(0,6):
                        s=Y.movleg(T,i,j,c)
                        for k in range(0,len(s)):
                            legal.append(s[k])
                k=0
                M=9000
                for i in range(0,len(legal)):
                    V=Y.gvalu(legal[i],c)
                    if V<M:
                        rand=[]
                        M=V
                        k=i
                        rand.append(legal[k])
                    elif V==M:
                        rand.append(legal[i])
            if(n==1):
                G=random.choice(rand)
                while Y.kingcheck(G, c) and G!=[]:
                    rand.remove(G)
                    legal.remove(G)
                    if rand==[]:
                        G=[]
                        break
                    G=random.choice(rand)
                if G==[]:
                    while legal!=[]:
                        if(Y.kingcheck(legal[0], c)):
                            legal.remove(legal[0])
                        else:
                            if legal[0]!=T:
                                return legal[0]
                            else: legal.remove(T)
                    return T
                return G
                    
                #return random.choice(rand)
            else:
                return M
        else:
            legal=[]
            rand=[]
            for i in range(0,6):
                for j in range(0,6):
                    s=Y.movleg(T,i,j,c)
                    for k in range(0,len(s)):
                        legal.append(s[k])
            if(c==1):
                k=0
                M=-9000
                for i in range(0,len(legal)):
                    V=Y.minmax(legal[i],(c+1)%2,d,n+1)
                    if V>M:
                        rand=[]
                        M=V
                        k=i
                        rand.append(legal[k])
                    elif V==M:
                        rand.append(legal[i])
            if(c==0):
                k=0
                M=9000
                for i in range(0,len(legal)):
                    V=Y.minmax(legal[i],(c+1)%2,d,n+1)
                    if V<M:
                        rand=[]
                        M=V
                        k=i
                        rand.append(legal[k])
                    elif V==M:
                        rand.append(legal[i])
            if n==1:
                G=random.choice(rand)
                while Y.kingcheck(G, c) and G!=[]:
                    rand.remove(G)
                    legal.remove(G)
                    if rand==[]:
                        G=[]
                        break
                    G=random.choice(rand)
                if G==[]:
                    
                    while legal!=[]:
                        print(legal[0])
                        print(Y.kingcheck(legal[0], c))
                        print("")
                        if(Y.kingcheck(legal[0], c)):
                            legal.remove(legal[0])
                        else:
                            if legal[0]!=T:
                                return legal[0]
                            else: legal.remove(T)
                    return T
                return G
                #return random.choice(rand)
            else:
                return M



    def minmax3(self,T,c,d,n,a,b):
        Y=Generator()
        if n==1:
            legal=[]
            rand=[]
            for i in range(0,6):
                for j in range(0,6):
                    s=Y.movleg(T,i,j,c)
                    for k in range(0,len(s)):
                        legal.append(s[k])
            if(c==1):
                k=0
                M=-9000
                for i in range(0,len(legal)):
                    V=Y.minmax3(legal[i],(c+1)%2,d,n+1,a,b)
                    if V>M:
                        rand=[]
                        M=V
                        k=i
                        rand.append(legal[k])
                    elif V==M:
                        rand.append(legal[i])
            if(c==0):
                k=0
                M=9000
                for i in range(0,len(legal)):
                    V=Y.minmax3(legal[i],(c+1)%2,d,n+1,a,b)
                    if V<M:
                        rand=[]
                        M=V
                        k=i
                        rand.append(legal[k])
                    elif V==M:
                        rand.append(legal[i])
            if n==1:
                G=random.choice(rand)
                while Y.kingcheck(G, c) and G!=[]:
                    rand.remove(G)
                    legal.remove(G)
                    if rand==[]:
                        G=[]
                        break
                    G=random.choice(rand)
                if G==[]:
                    
                    while legal!=[]:
                        print(legal[0])
                        print(Y.kingcheck(legal[0], c))
                        print("")
                        if(Y.kingcheck(legal[0], c)):
                            legal.remove(legal[0])
                        else:
                            if legal[0]!=T:
                                return legal[0]
                            else: legal.remove(T)
                    return T
                return G
                #return random.choice(rand)
            else:
                return M
            
        elif n==d:
            legal=[]
            rand=[]
            if(c==1):
                for i in range(0,6):
                    for j in range(0,6):
                        s=Y.movleg(T,i,j,c)
                        for k in range(0,len(s)):
                            legal.append(s[k])
                k=0
                M=-9000
                for i in range(0,len(legal)):
                    V=Y.gvalu(legal[i],c)
                    m=M
                    if V>M:
                        M=V
                    if M>a:
                        a=M
                    #M=max(V,M)
                    #a=max(a,M)
                    if n==1:
                        if V>m:
                            rand=[]
                            m=V
                            k=i
                            rand.append(legal[k])
                        elif V==m:
                            rand.append(legal[i])
                    if(b<=a):
                        break

            if(c==0):
                for i in range(0,6):
                    for j in range(0,6):
                        s=Y.movleg(T,i,j,c)
                        for k in range(0,len(s)):
                            legal.append(s[k])
                k=0
                M=9000
                for i in range(0,len(legal)):
                    V=Y.gvalu(legal[i],c)
                    m=M
                    if V<M:
                        M=V
                    if M<b:
                        b=M
                    #M=min(V,M)
                    #b=min(b,M)
                    if n==1:
                        if V<m:
                            rand=[]
                            m=V
                            k=i
                            rand.append(legal[k])
                        elif V==m:
                            rand.append(legal[i])
                    if(b<=a):
                        break
            if(n==1):
                G=random.choice(rand)
                while Y.kingcheck(G, c) and G!=[]:
                    rand.remove(G)
                    legal.remove(G)
                    if rand==[]:
                        G=[]
                        break
                    G=random.choice(rand)
                if G==[]:
                    while legal!=[]:
                        if(Y.kingcheck(legal[0], c)):
                            legal.remove(legal[0])
                        else:
                            if legal[0]!=T:
                                return legal[0]
                            else: legal.remove(T)
                    return T
                return G
                    
                #return random.choice(rand)
            else:
                return M
        else:
            legal=[]
            rand=[]
            for i in range(0,6):
                for j in range(0,6):
                    s=Y.movleg(T,i,j,c)
                    for k in range(0,len(s)):
                        legal.append(s[k])
            if(c==1):
                k=0
                M=-9000
                for i in range(0,len(legal)):
                    V=Y.minmax3(legal[i],(c+1)%2,d,n+1,a,b)
                    m=M
                    if V>M:
                        M=V
                    if M>a:
                        a=M
                    #M=max(V,M)
                    #a=max(a,M)
                    if n==1:
                        if V>m:
                            rand=[]
                            m=V
                            k=i
                            rand.append(legal[k])
                        elif V==m:
                            rand.append(legal[i])
                    if (b<=a):
                        break
            if(c==0):
                k=0
                M=9000
                for i in range(0,len(legal)):
                    V=Y.minmax3(legal[i],(c+1)%2,d,n+1,a,b)
                    m=M
                    if V<M:
                        M=V
                    if M<b:
                        b=M
                    #M=min(V,M)
                    #b=min(b,M)
                    if n==1:
                        if V<m:
                            rand=[]
                            m=V
                            k=i
                            rand.append(legal[k])
                        elif V==m:
                            rand.append(legal[i])
                    if(b<=a):
                        break
            if n==1:
                G=random.choice(rand)
                while Y.kingcheck(G, c) and G!=[]:
                    rand.remove(G)
                    legal.remove(G)
                    if rand==[]:
                        G=[]
                        break
                    G=random.choice(rand)
                if G==[]:
                    
                    while legal!=[]:
                        print(legal[0])
                        print(Y.kingcheck(legal[0], c))
                        print("")
                        if(Y.kingcheck(legal[0], c)):
                            legal.remove(legal[0])
                        else:
                            if legal[0]!=T:
                                return legal[0]
                            else: legal.remove(T)
                    return T
                return G
                #return random.choice(rand)
            else:
                return M
    
    def minmax4(self,T,c,d,n,a,b):
        Y=Generator()
        if n==1:
            legal=[]
            rand=[]
            for i in range(0,6):
                for j in range(0,6):
                    s=Y.movleg(T,i,j,c)
                    for k in range(0,len(s)):
                        legal.append(s[k])
            if(c==1):
                k=0
                M=-9000
                for i in range(0,len(legal)):
                    V=Y.minmax4(legal[i],(c+1)%2,d,n+1,a,b)
                    if V>M:
                        rand=[]
                        M=V
                        k=i
                        rand.append(legal[k])
                    elif V==M:
                        rand.append(legal[i])
            if(c==0):
                k=0
                M=9000
                for i in range(0,len(legal)):
                    V=Y.minmax4(legal[i],(c+1)%2,d,n+1,a,b)
                    if V<M:
                        rand=[]
                        M=V
                        k=i
                        rand.append(legal[k])
                    elif V==M:
                        rand.append(legal[i])
            if n==1:
                G=random.choice(rand)
                while Y.kingcheck(G, c) and G!=[]:
                    rand.remove(G)
                    legal.remove(G)
                    if rand==[]:
                        G=[]
                        break
                    G=random.choice(rand)
                if G==[]:
                    
                    while legal!=[]:
                        print(legal[0])
                        print(Y.kingcheck(legal[0], c))
                        print("")
                        if(Y.kingcheck(legal[0], c)):
                            legal.remove(legal[0])
                        else:
                            if legal[0]!=T:
                                return legal[0]
                            else: legal.remove(T)
                    return T
                return G
                #return random.choice(rand)
            else:
                return M
            
        elif n==d:
            legal=[]
            rand=[]
            if(c==1):
                for i in range(0,6):
                    for j in range(0,6):
                        s=Y.movleg(T,i,j,c)
                        for k in range(0,len(s)):
                            legal.append(s[k])
                k=0
                M=-9000
                for i in range(0,len(legal)):
                    V=Y.evalu(legal[i],c)
                    m=M
                    if V>M:
                        M=V
                    if M>a:
                        a=M
                    #M=max(V,M)
                    #a=max(a,M)
                    if n==1:
                        if V>m:
                            rand=[]
                            m=V
                            k=i
                            rand.append(legal[k])
                        elif V==m:
                            rand.append(legal[i])
                    if(b<=a):
                        break
    
            if(c==0):
                for i in range(0,6):
                    for j in range(0,6):
                        s=Y.movleg(T,i,j,c)
                        for k in range(0,len(s)):
                            legal.append(s[k])
                k=0
                M=9000
                for i in range(0,len(legal)):
                    V=Y.evalu(legal[i],c)
                    m=M
                    if V<M:
                        M=V
                    if M<b:
                        b=M
                    #M=min(V,M)
                    #b=min(b,M)
                    if n==1:
                        if V<m:
                            rand=[]
                            m=V
                            k=i
                            rand.append(legal[k])
                        elif V==m:
                            rand.append(legal[i])
                    if(b<=a):
                        break
            if(n==1):
                G=random.choice(rand)
                while Y.kingcheck(G, c) and G!=[]:
                    rand.remove(G)
                    legal.remove(G)
                    if rand==[]:
                        G=[]
                        break
                    G=random.choice(rand)
                if G==[]:
                    while legal!=[]:
                        if(Y.kingcheck(legal[0], c)):
                            legal.remove(legal[0])
                        else:
                            if legal[0]!=T:
                                return legal[0]
                            else: legal.remove(T)
                    return T
                return G
                    
                #return random.choice(rand)
            else:
                return M
        else:
            legal=[]
            rand=[]
            for i in range(0,6):
                for j in range(0,6):
                    s=Y.movleg(T,i,j,c)
                    for k in range(0,len(s)):
                        legal.append(s[k])
            if(c==1):
                k=0
                M=-9000
                for i in range(0,len(legal)):
                    V=Y.minmax4(legal[i],(c+1)%2,d,n+1,a,b)
                    m=M
                    if V>M:
                        M=V
                    if M>a:
                        a=M
                    #M=max(V,M)
                    #a=max(a,M)
                    if n==1:
                        if V>m:
                            rand=[]
                            m=V
                            k=i
                            rand.append(legal[k])
                        elif V==m:
                            rand.append(legal[i])
                    if (b<=a):
                        break
            if(c==0):
                k=0
                M=9000
                for i in range(0,len(legal)):
                    V=Y.minmax4(legal[i],(c+1)%2,d,n+1,a,b)
                    m=M
                    if V<M:
                        M=V
                    if M<b:
                        b=M
                    #M=min(V,M)
                    #b=min(b,M)
                    if n==1:
                        if V<m:
                            rand=[]
                            m=V
                            k=i
                            rand.append(legal[k])
                        elif V==m:
                            rand.append(legal[i])
                    if(b<=a):
                        break
            if n==1:
                G=random.choice(rand)
                while Y.kingcheck(G, c) and G!=[]:
                    rand.remove(G)
                    legal.remove(G)
                    if rand==[]:
                        G=[]
                        break
                    G=random.choice(rand)
                if G==[]:
                    
                    while legal!=[]:
                        print(legal[0])
                        print(Y.kingcheck(legal[0], c))
                        print("")
                        if(Y.kingcheck(legal[0], c)):
                            legal.remove(legal[0])
                        else:
                            if legal[0]!=T:
                                return legal[0]
                            else: legal.remove(T)
                    return T
                return G
                #return random.choice(rand)
            else:
                return M            

        
                                    

    def game(self,T,c):
        Y=Generator()
        black=['r','n','b','q','k','p']
        white=['R','N','B','Q','K','P']
        legal=[]
        str=""
        if(c==0):
            G=Y.minmax4(T, c, 4, 1,-90000,90000)
            
        else:
            gameState = State()
            puzzObj = Puzzle()
            gameGraphObj = Graph()
            searched = {}
            #print(T)
            gameState.set_currentState(group1ToGroup5(T))
            #gameState.print_state()
            bestMove = [None] 
            gameGraphObj.negMax(gameState ,depth=3, alpha= -1000000, beta=1000000, color="W", bestMoveReturn=bestMove, root=True)
            if(bestMove != [None]):
                puzzObj.movePiece(bestMove[0][0] , bestMove[0][1] , gameState , bestMove[1][0] , bestMove[1][1])
            #gameState.print_state()
            G = group5ToGroup1(gameState.get_currentState())
            #print(G)
            #G=Y.minmax3(T, c, 4, 1,-90000,90000)
        if c==1:
            print("White Move")
        if c==0:
            print("Black Move")
        for i in range(0,6):
            print(G[i])
            for j in range(0,6):
                str=str+G[i][j]
                str=str+" "
            if i!=5:
                str=str+","
        return str

    def gvalu(self,T,c): 
        e=0
        v=[5,3,3,9,90,1]
        V=[5,3,3,9,90,1]
        if c==0:
            V[4]=900
        if c==1:
            v[4]=900
        black=['r','n','b','q','k','p']
        white=['R','N','B','Q','K','P']
        b=[[1,1,1,1,1,1],[1,1.1,1.1,1.1,1.1,1],[1,1.2,1.2,1.2,1.2,1],[1.1,1.3,1.3,1.3,1.3,1.1],[1.5,1.5,1.5,1.5,1.5,1.5],[1,1,1,1,1,1]]
        br=[[1,1,1,1,1,1],[0.9,0.9,0.9,0.9,0.9,0.9],[0.8,0.8,0.8,0.8,0.8,0.8],[0.8,0.8,0.8,0.8,0.8,0.8],[1.1,1.1,1.1,1.1,1.1,1.1],[1,1,1,1,1,1]]
        bn=[[1,1,1,1,1,1],[1,1.01,1.01,1.01,1.01,1],[1,1.01,1.01,1.01,1.01,1],[1.2,1.3,1.3,1.3,1.3,1.2],[1,1.1,1.1,1.1,1.1,1],[1,1,1,1,1,1,1]]
        B=[[1,1,1,1,1,1],[1.5,1.5,1.5,1.5,1.5,1.5],[1.1,1.3,1.3,1.3,1.3,1.1],[1,1.2,1.2,1.2,1.2,1],[1,1.1,1.1,1.1,1.1,1],[1,1,1,1,1,1]]
        BR=[[1,1,1,1,1,1],[1.1,1.1,1.1,1.1,1.1,1.1],[0.8,0.8,0.8,0.8,0.8,0.8],[0.8,0.8,0.8,0.8,0.8,0.8],[0.9,0.9,0.9,0.9,0.9,0.9],[1,1,1,1,1,1]]
        BN=[[1, 1, 1, 1, 1, 1, 1],[1, 1.1, 1.1, 1.1, 1.1, 1],[1.2, 1.3, 1.3, 1.3, 1.3, 1.2],[1, 1.01, 1.01, 1.01, 1.01, 1],[1, 1.01, 1.01, 1.01, 1.01, 1],[1, 1, 1, 1, 1, 1]]
        for i in range(0,6):
            for j in range(0,6):
                for k in range(0,6):
                    if T[i][j]==black[k]:
                        if T[i][j]=='p':
                            e=e-v[k]*b[i][j]
                        
                        #elif T[i][j]=='r':
                            #e=e-v[k]*br[i][j]
                            
                        elif T[i][j]=='n':
                            e=e-v[k]*bn[i][j]
                        else:
                            e=e-v[k]
                    if T[i][j]==white[k]:
                        if T[i][j]=='P':
                            e=e+V[k]*B[i][j]
                        #elif T[i][j]=='R':
                            #e=e+V[k]*BR[i][j]
                        elif T[i][j]=='N':
                            e=e+V[k]*BN[i][j]
                        else:
                            e=e+V[k]
        return(e)
    def evalu(self,T,c):
        e=0
        v=[5,3,3,9,90,1]
        V=[5,3,3,9,90,1]
        if c==0:
            V[4]=900
        if c==1:
            v[4]=900
        black=['r','n','b','q','k','p']
        white=['R','N','B','Q','K','P']
        b=[[1,1,1,1,1,1],[1,1.1,1.1,1.1,1.1,1],[1,1.2,1.2,1.2,1.2,1],[1.1,1.3,1.3,1.3,1.3,1.1],[1.5,1.5,1.5,1.5,1.5,1.5],[1,1,1,1,1,1]]
        br=[[1,1,1,1,1,1],[0.9,0.9,0.9,0.9,0.9,0.9],[0.8,0.8,0.8,0.8,0.8,0.8],[0.8,0.8,0.8,0.8,0.8,0.8],[1.1,1.1,1.1,1.1,1.1,1.1],[1,1,1,1,1,1]]
        bn=[[1,1,1,1,1,1],[1,1.01,1.01,1.01,1.01,1],[1,1.01,1.01,1.01,1.01,1],[1.2,1.3,1.3,1.3,1.3,1.2],[1,1.1,1.1,1.1,1.1,1],[1,1,1,1,1,1,1]]
        B=[[1,1,1,1,1,1],[1.5,1.5,1.5,1.5,1.5,1.5],[1.1,1.3,1.3,1.3,1.3,1.1],[1,1.2,1.2,1.2,1.2,1],[1,1.1,1.1,1.1,1.1,1],[1,1,1,1,1,1]]
        BR=[[1,1,1,1,1,1],[1.1,1.1,1.1,1.1,1.1,1.1],[0.8,0.8,0.8,0.8,0.8,0.8],[0.8,0.8,0.8,0.8,0.8,0.8],[0.9,0.9,0.9,0.9,0.9,0.9],[1,1,1,1,1,1]]
        BN=[[1, 1, 1, 1, 1, 1, 1],[1, 1.1, 1.1, 1.1, 1.1, 1],[1.2, 1.3, 1.3, 1.3, 1.3, 1.2],[1, 1.01, 1.01, 1.01, 1.01, 1],[1, 1.01, 1.01, 1.01, 1.01, 1],[1, 1, 1, 1, 1, 1]]
        for i in range(0,6):
            for j in range(0,6):
                for k in range(0,6):
                    if T[i][j]==black[k]:
                        if T[i][j]=='p':
                            e=e-v[k]*b[i][j]
                        
                        #elif T[i][j]=='r':
                            #e=e-v[k]*br[i][j]
                            
                        elif T[i][j]=='n':
                            e=e-v[k]*bn[i][j]
                        else:
                            e=e-v[k]
                    if T[i][j]==white[k]:
                        if T[i][j]=='P':
                            e=e+V[k]*B[i][j]
                        #elif T[i][j]=='R':
                            #e=e+V[k]*BR[i][j]
                        elif T[i][j]=='N':
                            e=e+V[k]*BN[i][j]
                        else:
                            e=e+V[k]
        return(e)

import numpy as np
"""
def group1ToGroup5(state):
    converted_state = [['WR','WP','0','0','BP','BR'],
                      ['WK','WP','0','0','BP','BK'],
                      ['WQ','WP','0','0','BP','BQ'],
                      ['WKi','WP','0','0','BP','BKi'],
                      ['WK','WP','0','0','BP','BK'],
                      ['WR','WP','0','0','BP','BR']]
    
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 'r':
                converted_state[i][j] = 'BR'
            elif state[i][j] == 'kn':
                converted_state[i][j] = 'BK'
            elif state[i][j] == 'q':
                converted_state[i][j] = 'BQ'
            elif state[i][j] == 'k':
                converted_state[i][j] = 'BKi'
            elif state[i][j] == 'p':
                converted_state[i][j] = 'BP'
            elif state[i][j] == 'R':
                converted_state[i][j] = 'WR'
            elif state[i][j] == 'Kn':
                converted_state[i][j] = 'WK'
            elif state[i][j] == 'Q':
                converted_state[i][j] = 'WQ'
            elif state[i][j] == 'K':
                converted_state[i][j] = 'WKi'
            elif state[i][j] == 'P':
                converted_state[i][j] = 'WP'
            elif state[i][j] == '0':
                converted_state[i][j] = '0'
    arr = np.array(converted_state)
    arr = np.transpose(arr)
    arr = np.flip(arr, axis = 1)
    arr = arr.tolist()
    return arr

def group5ToGroup1(state):
    converted_state = [['0' for _ in range(6)] for _ in range(6)]
    
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 'BR':
                converted_state[i][j] = 'r'
            elif state[i][j] == 'BK':
                converted_state[i][j] = 'kn'
            elif state[i][j] == 'BQ':
                converted_state[i][j] = 'q'
            elif state[i][j] == 'BKi':
                converted_state[i][j] = 'k'
            elif state[i][j] == 'BP':
                converted_state[i][j] = 'p'
            elif state[i][j] == 'WR':
                converted_state[i][j] = 'R'
            elif state[i][j] == 'WK':
                converted_state[i][j] = 'Kn'
            elif state[i][j] == 'WQ':
                converted_state[i][j] = 'Q'
            elif state[i][j] == 'WKi':
                converted_state[i][j] = 'K'
            elif state[i][j] == 'WP':
                converted_state[i][j] = 'P'
            elif state[i][j] == '0':
                converted_state[i][j] = '0'

    arr = np.array(converted_state)
    arr = np.flip(arr, axis = 1)
    arr = np.transpose(arr)
    arr = arr.tolist()
    return arr
"""
def group1ToGroup5(state):
    converted_state = [['0' for _ in range(6)] for _ in range(6)]
    
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[j][i] == 'r':
                converted_state[i][j] = 'BR'
            elif state[j][i] == 'n':
                converted_state[i][j] = 'BK'
            elif state[j][i] == 'q':
                converted_state[i][j] = 'BQ'
            elif state[j][i] == 'k':
                converted_state[i][j] = 'BKi'
            elif state[j][i] == 'p':
                converted_state[i][j] = 'BP'
            elif state[j][i] == 'R':
                converted_state[i][j] = 'WR'
            elif state[j][i] == 'N':
                converted_state[i][j] = 'WK'
            elif state[j][i] == 'Q':
                converted_state[i][j] = 'WQ'
            elif state[j][i] == 'K':
                converted_state[i][j] = 'WKi'
            elif state[j][i] == 'P':
                converted_state[i][j] = 'WP'
            elif state[j][i] == '0':
                converted_state[i][j] = '0'
    c1 = converted_state
    for i in range(len(state)):
        c1[i] = c1[i][::-1]
    return c1

def group5ToGroup1(state):
    converted_state = [['0' for _ in range(6)] for _ in range(6)]
    
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 'BR':
                converted_state[j][i] = 'r'
            elif state[i][j] == 'BK':
                converted_state[j][i] = 'n'
            elif state[i][j] == 'BQ':
                converted_state[j][i] = 'q'
            elif state[i][j] == 'BKi':
                converted_state[j][i] = 'k'
            elif state[i][j] == 'BP':
                converted_state[j][i] = 'p'
            elif state[i][j] == 'WR':
                converted_state[j][i] = 'R'
            elif state[i][j] == 'WK':
                converted_state[j][i] = 'N'
            elif state[i][j] == 'WQ':
                converted_state[j][i] = 'Q'
            elif state[i][j] == 'WKi':
                converted_state[j][i] = 'K'
            elif state[i][j] == 'WP':
                converted_state[j][i] = 'P'
            elif state[i][j] == '0':
                converted_state[j][i] = '0'

    c1 = converted_state
    c1 = c1[::-1]

    return c1
T=[['r','n','q','k','n','r'],['p','p','p','p','p','p'],['0','0','0','0','0','0'],['0','0','0','0','0','0'],['P','P','P','P','P','P'],['R','N','Q','K','N','R']]

gameState = State()
puzzObj = Puzzle()
gameGraphObj = Graph()

pygame.init()
board=pygame.display.set_mode((804, 804))
color1=(255,255,255)
color2=(150,150,150)
for i in range(0,6):
    for j in range(0,6):
        if((i+j)%2==0):        
            pygame.draw.rect(board,color1,pygame.Rect(134*i, 134*j, 134*(i+1), 134*(j+1)))
        else:
            pygame.draw.rect(board,color2,pygame.Rect(134*i, 134*j, 134*(i+1), 134*(j+1)))
font=pygame.font.Font('seguisym.ttf', 134)
for i in range(0,6):
    for j in range(0,6):
        if T[i][j]=='P':
            board.blit(font.render("\u2659", True, (0,0,0)),(134*j, 134*i-15))
        if T[i][j]=='K':
            board.blit(font.render("\u2654", True, (0,0,0)),(134*j, 134*i-15))
        if T[i][j]=='R':
            board.blit(font.render("\u2656", True, (0,0,0)),(134*j, 134*i-15))
        if T[i][j]=='N':
            board.blit(font.render("\u2658", True, (0,0,0)),(134*j, 134*i-15))
        if T[i][j]=='Q':
            board.blit(font.render("\u2655", True, (0,0,0)),(134*j, 134*i-15))
        if T[i][j]=='p':
            board.blit(font.render("\u265F", True, (0,0,0)),(134*j, 134*i-15))
        if T[i][j]=='k':
            board.blit(font.render("\u265A", True, (0,0,0)),(134*j, 134*i-15))
        if T[i][j]=='r':
            board.blit(font.render("\u265C", True, (0,0,0)),(134*j, 134*i-15))
        if T[i][j]=='n':
            board.blit(font.render("\u265E", True, (0,0,0)),(134*j, 134*i-15))
        if T[i][j]=='q':
            board.blit(font.render("\u265B", True, (0,0,0)),(134*j, 134*i-15))
Y=Generator()
run=True
k=-1
while run:
    k=k+1
    pygame.display.flip()
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run=False
    print("")
    str=Y.game(T,(k+1)%2)
    K=[[0],[0],[0],[0],[0],[0]]
    lst1=str.split(",")
    for j in range(0,6):
        K[j]=lst1[j].split()
    if T==K:
        if Y.kingcheck(T,1)==True:
            print("Black Wins")
        elif Y.kingcheck(T, 0)==True:
            print("White Wins")
        else:
            print("Draw")
        break
    T=copy.deepcopy(K)
    for i in range(0,6):
        for j in range(0,6):
            if((i+j)%2==0):        
                pygame.draw.rect(board,color1,pygame.Rect(134*i, 134*j, 134*(i+1), 134*(j+1)))
            else:
                pygame.draw.rect(board,color2,pygame.Rect(134*i, 134*j, 134*(i+1), 134*(j+1)))
    font=pygame.font.Font('seguisym.ttf', 134)
    for i in range(0,6):
        for j in range(0,6):
            if T[i][j]=='P':
                board.blit(font.render("\u2659", True, (0,0,0)),(134*j, 134*i-15))
            if T[i][j]=='K':
                board.blit(font.render("\u2654", True, (0,0,0)),(134*j, 134*i-15))
            if T[i][j]=='R':
                board.blit(font.render("\u2656", True, (0,0,0)),(134*j, 134*i-15))
            if T[i][j]=='N':
                board.blit(font.render("\u2658", True, (0,0,0)),(134*j, 134*i-15))
            if T[i][j]=='Q':
                board.blit(font.render("\u2655", True, (0,0,0)),(134*j, 134*i-15))
            if T[i][j]=='p':
                board.blit(font.render("\u265F", True, (0,0,0)),(134*j, 134*i-15))
            if T[i][j]=='k':
                board.blit(font.render("\u265A", True, (0,0,0)),(134*j, 134*i-15))
            if T[i][j]=='r':
                board.blit(font.render("\u265C", True, (0,0,0)),(134*j, 134*i-15))
            if T[i][j]=='n':
                board.blit(font.render("\u265E", True, (0,0,0)),(134*j, 134*i-15))
            if T[i][j]=='q':
                board.blit(font.render("\u265B", True, (0,0,0)),(134*j, 134*i-15))
pygame.quit()















"""
while True:
    T=[[0],[0],[0],[0],[0],[0]]
    str=input("Enter the Board ")
    lst1=str.split(",")
    for i in range(0,6):
        T[i]=lst1[i].split()
        print(T[i])
    Y=Generator();
    """ """
    print("")
    str=Y.game(T, 0)
    print(str)
    """  """
    for i in range(0,20):
        print("")
        str=Y.game(T,(i+1)%2)
        T=[[0],[0],[0],[0],[0],[0]]
        lst1=str.split(",")
        for j in range(0,6):
            T[j]=lst1[j].split()

"""         
    

