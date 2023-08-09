# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 14:56:47 2023

@author: asus
"""


# print("yaqin do'slaringiz ro'yxati tuzamiz.")
# ismlar = []
# n = 1
# while True:
#     savol = f"{n}-do'slaringiz ismini kiriting:"
#     ism = input (savol)
#     ismlar.append(ism)
#     takrorlash = input("yana ism qo'shamizmi (ha/yo;q)")
#     n+=1
#     if takrorlash !='ha':
#         break
# print("do'slaringiz ro'yxati:")
# for ism in ismlar:
#     print(ism.title())
    


# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Do'slaringiz ismini kiriting:")
#     yosh = input(f"{ism.title()}ning yoshini kiriting:")
#     dostlar[ism] = int(yosh)
    
    
#     javob = input("Yana ma'lumot qo'shasizmi!(ha/yo'q)")
#     if javob == "yo'q":
#         ishora = False

# for ism,yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")





# cars = ['malibu','lada','nexia','audi','bmw','damas','lacetti','lada']
# car = 'lada'
# while car in cars:
#     cars.remove(car)
    
# print(cars)


 
talabalar = ['ali','vali','husan','hasan',]
baholangan_talabalar = {}
while talabalar:
    talaba = talabalar.pop()
    baho = input(f"{talaba.title()}ning bahosini kiriting:")
    print(f"{talaba.title()} baholandi")
    baholangan_talabalar[talaba] = int(baho)
    print(baholangan_talabalar)



