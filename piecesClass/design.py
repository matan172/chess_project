


class Design():
    def SetColor(self):  
        y,x = abs(self.pos[0]),abs(self.pos[1])  
        if (y+x) % 2 == 0:
            self.color = "white"
        else:
            self.color = "black"
        #print((y+x)%2,self.color)



