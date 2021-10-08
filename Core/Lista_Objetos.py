#coding: utf-8
#author: mau

from Render.Objeto import Objeto
from Render.PreObjeto import PreObjeto
import copy, sys
from Core.control_errores import logger as loger


class Lista_Objetos():
    
    def __init__(self):
        local_sprite = "Assets/imagenes"
        self.__lista_sprites = {1:f"{local_sprite}/Building_Fieldstone_1/Column_1.png"}
        
        self._listado_objeto = {1:PreObjeto(1,self.__lista_sprites[1])}
        
        
        
    def get_objeto(self,id_objeto):
        try:
            loger.debug(f"the image is loaded successfully id: {id_objeto}")
            return Objeto(self._listado_objeto[1].get_ruta_objeto())
        except KeyError:
            loger.error(f"Error loading image id:{id_objeto}")
            return None