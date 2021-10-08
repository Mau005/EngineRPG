#coding: utf-8
#author: mau

class PreObjeto():
    def __init__(self,id_objeto,ruta_objeto):
        self.__id_objeto = id_objeto
        self.__ruta_objeto = ruta_objeto
        
        
    def get_id_objeto(self):
        return self.__id_objeto
    
    def get_ruta_objeto(self):
        return self.__ruta_objeto