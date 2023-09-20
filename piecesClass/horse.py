from design import Design




class Knight(Design):
    def __init__(self, pos, id ) -> None:
        self.id = id 
        self.strId = str(id)
        self.name = "H"
        self.pos = pos  
        self.SetColor()


    def move(self,board:list): #checks where is posible to move to
        moves = []
        possible_moves = []
        if self.pos[0]+2 < 8 and self.pos[1]+1 < 8:
            moves.append(board[self.pos[0]+2][self.pos[1]+1])

        if self.pos[0]+2 < 8 and self.pos[1]-1  >= 0:  
            moves.append(board[self.pos[0]+2][self.pos[1]-1])

        if self.pos[0]-2 >= 0 and self.pos[1]+1 < 8:
            moves.append(board[self.pos[0]-2][self.pos[1]+1])

        if self.pos[0]-2 >= 0 and self.pos[1]-1 >=0:
            moves.append(board[self.pos[0]-2][self.pos[1]-1])

        if self.pos[0]+1 < 8 and self.pos[1]+2 <8:
            moves.append(board[self.pos[0]+1][self.pos[1]+2])

        if self.pos[0]+1 < 8 and self.pos[1]-2 >=0:
            moves.append(board[self.pos[0]+1][self.pos[1]-2])

        if self.pos[0]-1 >= 0 and self.pos[1]+2 <8:
            moves.append(board[self.pos[0]-1][self.pos[1]+2])

        if self.pos[0]-1 >= 0 and self.pos[1]-2 >=0:
            moves.append(board[self.pos[0]-1][self.pos[1]-2])

        for move in moves:
            try:
                if move.id != self.id:
                    possible_moves.append(move.pos)

            except:
                pass

        self.SetColor()
        return possible_moves
    


        
