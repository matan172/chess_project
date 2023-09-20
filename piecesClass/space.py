from design import Design



class Space(Design): # for empty spaces
    def __init__(self,pos:tuple) -> None:
        self.id = 3
        self.pos = pos
        self.strId = str(id)
        self.y,self.x = pos
        self.name = "Space"
        self.SetColor()
        
    def move(self,board):
        self.SetColor()
        return []
    



    
