import numpy as np

class Player:
    #constructor
    def __init__(self, x, name):
        self.name = name
        self.x = np.array([[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]])

    #getter
    def get_array(self):
        return self.x
    
    #setter
    def set_array(self, y):
        self.x = y
    
    #append
    def append_array(self, y):
        np.append(self.x, y)

    #delete value
    def delete_value(self, y):
        np.delete(self.x, y)
    
     



