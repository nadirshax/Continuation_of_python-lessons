# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 21:21:43 2023

@author: asus
"""

class Avto:
    __num__avto = 0
    """Avtomobilning xususiyatlari"""
    def __init__(self,make,model,rang,yil,narh):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        Avto.__num__avto += 1
        
    # def __str__(self):
    #     return f"Avto:{self.make} {self.model}" 
    
    def __repr__(self):
        return f"Avto: {self.make}, {self.model}, {self.rang}, {self.yil}-yil ,{self.narh}-narhi"
    
    def __eq__(self,y):
        return self.narh == y.narh
    
    def __lt__(self,y):
        return self.narh<y.narh
    
    def __le__ (self,y):
        return self.narh <=y.narh
    
    
    def __getitem__(self,index):
        return self.avtolar[index]
    
    
class Avtosalon:
    def __init__(self,name):
        self.name =  name
        self.avtolar = []
        
    def __repr__(self):
        return f"{self.name} avtosaloni"
    
avto1 = Avtosalon("Nadirshax")
    
    
    
avto1 = Avto("GM","malibu","qora",2019,25000)
print(avto1)

avto2 = Avto("GM","lacetti","qizil",2013,12000)
print(avto2)