# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 20:06:19 2023

@author: asus
"""

def bahola (ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input (f"talaba {ism.title()}ning bahosini kiriting: ")
        baholar [ism]= int(baho)
        
    return baholar
            
talabalar = ['ali','vali','rasul','olim','komil']
baholar = bahola(talabalar)
# print(baholar)
print(f"umumiy baholar{baholar}")


