# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 21:31:59 2023

@author: asus
"""


import datetime as dt

# datetime()
# hozir = dt.datetime.now()
# print(hozir)

# """Sanani ajratib olish"""
# print(hozir.date())

# """VAqtni ajratib olish"""
# print(hozir.time())

# """Soatni ajratib olish"""
# print(hozir.hour)

# """Minutni ajratib olish"""
# print(hozir.minute)

# """Sekundni ajratib olish"""
# print(hozir.second)



##DATE()
# bugun = dt.date.today()
# print(f"Bugungi sana: {bugun}")

# ertaga = dt.date(2023, 4, 13)
# print(f"Ertangi sana {ertaga}")



##TIME

# hozir = dt.datetime.now()
# vaqtHozir = hozir.time()
# print(f"Hozir soat: {vaqtHozir}")
# vaqtKeyin = dt.time(23,45,00)
# print(vaqtKeyin)



"""SANALAR ORASIDAGI FARQ"""

# bugun = dt.date.today()
# ramazon_tugashi = dt.date(2023, 4, 22)
# farq = ramazon_tugashi-bugun
# print(farq)
# print(f"Ramazon tugashiga {farq.days} kun qoldi")




"""Soatlar orasidagi farq"""
hozir = dt.datetime.now()
futbol = dt.datetime(2023,4,12, 23, 55, 00)
farq = futbol - hozir
sekundlar = farq.seconds
minutlar = int(sekundlar/60)
soatlar = int(minutlar/60)
print(f"Futbolga boshlanishiga {farq.days} kun {soatlar}soat qoldi")

















      







