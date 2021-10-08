#coding: utf-8
#author: mau

class SizeTools():
    
    @staticmethod
    def set_aspecto(windows,cantX,cantY):
        cantX = windows[0]/cantX
        cantY = windows[1]/cantY
        return {"cuadroX":cantX,"cuadroY":cantY}