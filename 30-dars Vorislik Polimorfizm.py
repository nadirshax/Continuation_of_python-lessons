# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 20:04:41 2023

@author: asus
"""

class Shaxs:
    """Shaxs haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self. tyil = tyil
        
        
    def get_info(self):
            """Shaxs haqida ma'lumot"""
            info = f"{self.ism} {self.familiya}."
            info += f"Passport:{self.passport}, {self.tyil}-yilda tug'ilgan."
            return info
        
    def get_age(self,yil):
            """Shaxsning yoshini qaytaruvchi ma'lumot"""
            return yil - self.tyil
        
        
# inson = Shaxs("Nodir","Shadiyev","AB0785787",1993)
# print(f"{inson.get_info()}. {inson.get_age(2023)} yoshda.")
        
        
        
class Talaba(Shaxs):
    """Talaba classi"""
    def __init__(self, ism, familiya, passport, tyil, idraqam, Manzil):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self. bosqich = 1
        self.Manzil = Manzil
        
    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam
    
    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich


class Manzil:
    """Manzil saqlash uchun class"""
    def __init__(self,uy, kocha, tuman, viloyat):
        """Manzil xususiyatlari"""
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat
        
    def Get_Manzil(self):
        """Manzilni ko'rish"""
        Manzil = f"{self.viloyat} viloyat, {self.tuman} tumani,"
        Manzil += f"{self.kocha} ko'chasi {self.uy}-uy,"
        return Manzil
    
Talaba1_Manzil = Manzil(49," Bog'ichinor", "Yuqori chirchiq", "Toshkent viloyati")
Talaba1 = Talaba("Nodir", "Shadiyev", "AB0785787", 1993,"07271993",Talaba1_Manzil )
    
inson = Shaxs("Nodir", "Shadiyev", "AB0785787", 1993)
# inson = Manzil(49,"Bog'ichinor","Yuqori chirchiq","Toshkent viloyati".capitalize())
