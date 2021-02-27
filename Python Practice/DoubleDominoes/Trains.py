import numpy as np

class Train:
    def __init__(self, name, x, status):
        self.name = name
        self.x = np.array([[12,12]])
        self.status = status
    
    #getter
    def get_array(self):
        return self.x

    def get_status(self):
        return self.status

    def set_status(self, y):
        self.status = y
    
    def set_array(self,y):
        self.x = y

    

    