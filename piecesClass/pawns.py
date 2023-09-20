from design import Design



class Pawn(Design):
    def __init__(self, pos, id ) -> None:
        self.id = id 
        self.name = "P"
        self.strId = str(id)
        self.pos = pos
        self.SetColor()
        self.UP = []
        self.DOWN = []
        

    def move(self,board:list):
        if self.id == 2:
            return self.moveDown(board)
        if self.id == 1:
            return self.moveUp(board)
    
    

    def moveDown(self, board): # for id 2
        self.DOWN = []
        try:
            if self.pos[0]+1 < 8:   
                if board[self.pos[0]+1][self.pos[1]].id == 3:
                    self.DOWN.append((self.pos[0]+1,self.pos[1]))
        except:
            pass
        try:
            if self.pos[0]+1 <8 and self.pos[1]+1 < 8:  
                if board[self.pos[0]+1][self.pos[1]+1].id == 1:
                    self.DOWN.append((self.pos[0]+1,self.pos[1]+1))
        except:
            pass

        try:
            if self.pos[0]+1 <8 and self.pos[1]-1 >= 0:  
                if board[self.pos[0]+1][self.pos[1]-1].id == 1:
                    self.DOWN.append((self.pos[0]+1,self.pos[1]-1))
        except:
            pass

        try:
            if self.pos[0] == 1:   # move for starting point where pawn can move 2 squares
                if board[self.pos[0]+2][self.pos[1]].id == 3:
                    self.DOWN.append((self.pos[0]+2,self.pos[1]))
        except:
            pass

        


        return self.DOWN


    def moveUp(self,board): # for id 1
        self.DOWN = []
        try:
            if self.pos[0]-1 >= 0:
                if board[self.pos[0]-1][self.pos[1]].id == 3:
                    self.DOWN.append((self.pos[0]-1,self.pos[1]))
        except:
            pass

        try:
            if self.pos[0]-1 >= 0 and self.pos[1]+1 < 8:   
                if board[self.pos[0]-1][self.pos[1]+1].id == 2:
                    self.DOWN.append((self.pos[0]-1,self.pos[1]+1))
        except:
            pass

        try:
            if self.pos[0]-1 >= 0 and self.pos[1]-1 >= 0:  
                if board[self.pos[0]-1][self.pos[1]-1].id == 2:
                    self.DOWN.append((self.pos[0]-1,self.pos[1]-1))
        except:
            pass

        try:
            if self.pos[0] == 6 and board[self.pos[0]-1][self.pos[1]].id == 3:  
                if board[self.pos[0]-2][self.pos[1]].id == 3:
                    self.DOWN.append((self.pos[0]-2,self.pos[1]))
        except:
            pass

        self.SetColor()
        return self.DOWN



    
    
# def func(self,board,num3,num1=0,num2=0):
    #     """
    #     num3 = id (only if this id appears return y,x)
    #     +num1 on rows from self
    #     +num2 on cols from self
    #     """
    #     try:
    #         if self.pos[0]+num1 < 8:   
    #             if board[self.pos[0]+num1][self.pos[1]+num2].id == num3:
    #                 self.DOWN.append((self.pos[0]+num1,self.pos[1]+num2))
    #     except:
    #         pass

    