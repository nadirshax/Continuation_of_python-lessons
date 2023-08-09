# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 23:57:29 2023

@author: asus
"""

class talaba:
    def __init__(self,ism,familiya,tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        
    def get_name(self):
        return self.ism
    
    def get_lastname(self):
        return self.familiya
    
    def get_age(self,yil):
        return yil - self.tyil
    def tanishtir(self):
        return (f"Ismim {self.ism} {self.familiya},tug'ilgan yilim.{self.tyil}")
    
    
talaba1 = talaba('Olim',' Xasanov', 1998)
talaba2 = talaba('Ali', 'Olimov', 1995)
talaba3 = talaba('Anvar', 'Komilov', 1993)
    
        