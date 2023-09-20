from space import Space
from Rooks import *
from pawns import Pawn
from horse import Knight
from runners import Runner
from queen import Queen
from king import King
### player 1 is down player 2 up



class Board():
    def __init__(self) -> None:
        self.board = [
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            []
        ]

        count = 0
        for i in self.board:
            for x in range(8):
                i.append(Space((count,x)))
            count+=1
        
    def change(self,y,x,obj): # change index in matrix to new obj
        obj.pos = (y,x)
        self.board[y][x] = obj

        
    def move(self, frm:tuple, mve:tuple): #replace 2 objects on board
        y,x=frm
        y1,x1=mve
        piece = self.board[y][x]
        posible_moves = piece.move(self.board) 
        if mve not in posible_moves:
            return "error"
        self.change(y1,x1,piece)
        self.change(y,x,Space((y,x)))

    def add_piece(self,piece):
        y,x = piece.pos
        self.board[y][x] = piece

    def index_help(self):
        print(" ", ["0","1","2","3","4","5","6","7"])
        index = 0
        for x in self.board:
            print(index , [i.name for i in x])
            index +=1

    def set_game(self):

        # set pieces player 2 
        self.board[0][0] = Rook((0,0),2)
        self.board[0][1] = Knight((0,1),2)
        self.board[0][2] = Runner((0,2),2)
        self.board[0][3] = Queen((0,3),2)
        self.board[0][4] = King((0,4),2)
        self.board[0][5] = Runner((0,5),2)
        self.board[0][6] = Knight((0,6),2)
        self.board[0][7] = Rook((0,7),2)
        for i in self.board[1]:
            y,x = i.pos
            self.board[y][x] = Pawn((y,x),2)
        # set pieces player1
        self.board[7][0] = Rook((7,0),1)
        self.board[7][1] = Knight((7,1),1)
        self.board[7][2] = Runner((7,2),1)
        self.board[7][3] = Queen((7,3),1)
        self.board[7][4] = King((7,4),1)
        self.board[7][5] = Runner((7,5),1)
        self.board[7][6] = Knight((7,6),1)
        self.board[7][7] = Rook((7,7),1)
        for i in self.board[6]:
            y,x = i.pos
            self.board[y][x] = Pawn((y,x),1)
        
    def get_piece_moves(self, tpl: tuple):
        piece = self.board[tpl[0]][tpl[1]]
        return piece.move(self.board)
    
    def check():
        pass

    def check_win(self):
        whiteMoves = [] # white.id = 1
        blackMoves = [] # black.id = 2
        board = self.board
        checkonwhite = False 
        checkonblack = False

        for r in board:
            for c in r:
                if c.id == 1:
                    if c.name == "K":
                        whiteKing = c
                    for mv in c.move(board):
                        whiteMoves.append(mv)
                elif c.id == 2:
                    if c.name == "K":
                        blackKing = c
                    for mv in c.move(board):
                        blackMoves.append(mv)
                       

        if whiteKing in blackMoves:
            
            for mv in whiteKing.move(board):

                if mv not in blackMoves:
                    checkonwhite = True


        if blackKing in whiteMoves:
            
            for mv in blackKing.move(board):

                if mv not in blackMoves:

                    checkonblack = True
        
        if checkonwhite:
            return "blackwins"
        if checkonblack:
            return "whitewins"
        
        return False
                    
                    









    

                
                

        



# board = Board()
# rok1 = Rook((1,6),1)
# rok2 = Rook((2,6),2)
# pawn1 = Pawn((0,0),2)
# pawn2 = Pawn((0,1),1)
# p1 = Pawn((0,0),2)
# p2 = Pawn((1,1),1)
# p3 = Queen((3,3),2)
# board.add_piece(p1)
# board.add_piece(p2)
# board.add_piece(p3)
# print(p3.move(board.board))
# for y,x in p3.move(board.board):
#     board.board[y][x].name = "@"












# board.index_help()
