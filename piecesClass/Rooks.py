
from design import Design


class Rook(Design):
    def __init__(self, pos, id ) -> None:
        self.id = id 
        self.name = "Z"
        self.pos = pos
        self.strId = str(id)
        


    def get_moves(self,board:list): #checks all spaces on board in diagnal
        count = 1
        moves1 = []
        moves2 = []
        moves3 = []
        moves4 = [] 
        while True:
            failcounter = 0
            try:
                move = board[self.pos[0]+count][self.pos[1]]
                if (self.pos[0]+count) < 0 or (self.pos[1]) < 0:
                    failcounter +=1
                else:
                    moves1.append(move)
           
            except:
                failcounter +=1
                
            try:
                move = board[self.pos[0]-count][self.pos[1]]
                if (self.pos[0]-count) < 0 or (self.pos[1]) < 0:
                    failcounter +=1
                else:
                    moves2.append(move)
            except:
                failcounter +=1
                
            try:
                move = board[self.pos[0]][self.pos[1]-count]
                if (self.pos[0]) < 0 or (self.pos[1]-count) < 0:
                    failcounter +=1
                else:
                    moves3.append(move)
            except:
                failcounter +=1
                
            try:
                move = board[self.pos[0]][self.pos[1]+count]
                if (self.pos[0]) < 0 or (self.pos[1]+count) < 0:
                    failcounter +=1
                else:
                    moves4.append(move)
            except:
                failcounter +=1
                
            if failcounter == 4:
                break
            count +=1

        return [moves1,moves2,moves3,moves4]
        
    def move(self,board:list):
        moves = [] 
        for mlist in self.get_moves(board):
            for move in mlist:
                if move.id == 3:
                    moves.append(move.pos)
                elif move.id != self.id:
                    moves.append(move.pos)
                    break
                else: break
        self.SetColor()
        return list(set(moves))
    










        




