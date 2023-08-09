# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 13:37:26 2023

@author: asus
"""

from uuid import uuid4
class Avto:
    __num_avto = 0
    def __init__(self,maket,model,rang,yil,narh,km=0):
        self.maket = maket
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        self.__id = uuid4()
        Avto.__num_avto += 1
     
    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto
    
    def get_km(self):
        return self.__km
    
    def get__id(self):
        return self.__id 
    
    def add_km(self,km):
        if km>=0:
            self.__km += km
        else:
            print("Mashinani km kamaytirib bo'lmaydi")
            
  
          
avto1 = Avto("gm","nexia","qora",2021,8000,30000)
avto2 = Avto("gm","damas","oq",2023,10000,000)
avto3 = Avto("gm","malibu","qizil",2019,25000,40000)
print(Avto.get_num_avto())


            
            
        
        
        
        
        