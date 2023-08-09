# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 16:47:46 2023

@author: asus
"""

def salom_ber(ism):
    """Salom beradigan dasturiy funksiya"""
    print(f"Assalomu aleykum, hurmatli {ism.title()}")
    
salom_ber('ali')


# def toliq_ism(ism,familiya):
#     """Toliq ism sharifini beradi"""
# print(f"Foydalanuvchi ismi: {ism.title()} \n"
#       f"foydalanuvchi familiyasi: {familiya.title()}")



def toliq_ism(ism, familiya):
    """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
    print(f"Foydalanuvchi ismi: {ism.title()}\n"
          f"Foydalanuvchi familiyasi: {familiya.title()}")

toliq_ism('ali','olimov')



def yosh_xislobla(ism,tugilgan_yil):
    """Yoshini xisoblab beradigan funksiya"""
    print(f"{ism.title()} {2023-tugilgan_yil} yoshdas")

yosh_xislobla('ali',1993)

































