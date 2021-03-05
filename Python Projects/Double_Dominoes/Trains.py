import numpy as np

class Train:
    def __init__(self, name, x, status):
        self.name = name
        self.x = np.array([12])
        self.status = False
    
    #getters
    def get_array(self):
        return self.x

    def get_status(self):
        return self.status

    #setters
    def set_status(self, y):
        self.status = y
    
    def set_array(self,y):
        self.x = y

    

    