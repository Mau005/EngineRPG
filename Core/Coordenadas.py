#coding: utf-8
#author: mau

class Coordenadas():
    
    def __init__(self):
        #representa la posicion en el tilemap
        self.__pos = {"x": 0, "y": 0, "z":0}
        
        
        
    def update(self,pos):
        pass
    
    def draw(self, *dt):
        pass
        
    def get_pos(self):
        return self.__pos
    
    def set_pos_x(self,x):
        self.__pos["x"] = x
    def set_pos_y(self,y):
        self.__pos["y"] = y
    def set_pos_x(self,z):
        self.__pos["z"] = z
        
    def get_pos_x(self):
        return self.__pos["x"]
    
    def get_pos_y(self):
        return self.__pos["y"]
    
    def get_pos_z(self):
        return self.__pos["z"]
    
    def info(self):
        return f"Pos: x:{self.__pos['x']}, y:{self.__pos['y']}, z:{self.__pos['z']}, \n"