# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 21:04:11 2023

@author: asus
"""


def upper():
    pass


class car:
    def __init__(self,make,model,year,km=0,price=None):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.__km = km
        
    def set_price(self,price):
        self.price = price
        
    def add_km(self,km):
        if km >=0:
            self.__km += km
        else:
            raise ValueError("km manfiy bo'lishi mumkin emas")
            
    def get_info(self):
        
        info = f"{self.make,upper()} {self.model.title()},"
        info += f"self.year-yil {self.__km}-km yurgan."
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
        