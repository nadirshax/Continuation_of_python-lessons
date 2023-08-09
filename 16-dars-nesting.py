# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 13:42:17 2023

@author: asus
"""


# car0 = {
#         'model':'malibu',
#         'rang':'qora',
#         'yil':'2014',
#         'narh':'10000$',
#         'km':'5000',
#         'karobka':'avtomat'
#         }
# car1 = {
#         'model':'lada',
#         'rang':'qizil',
#         'yil':'2019',
#         'narh':'15000$',
#         'km':'100',
#         'karobka':'mexanik'
#         }
# car2 = {
#         'model':'nexia',
#         'rang':'oq',
#         'yil':'2009',
#         'narh':'6000$',
#         'km':'500',
#         'karobka':'mexanik'
#         }
# # car = car2
# # print(f"{car['model'].title()}, "
# #       f"{car ['rang']} rang, "
# #       f"{car ['yil']}-yil, {car['narh']}$"
# #       )


# cars = [car0, car1, car2]
# for car in cars:
#     print(f"{car['model'].title()}, "
#       f"{car ['rang']} rang, "
#       f"{car ['yil']}-yil, {car['narh']}"
   
#       )
    
hamkasiblar = {
    'ali':{'familiya':'ahmadov',
           't.yili':1995,
           'malumoti':'oliy',
           'tillar':['python','c++']
        },
    'abbos':{'familiya':'jalilov',
             't.yili':1994,
             'malumoti':'oliy',
             'tillar':['html','css','js']
        },
    'sardor':{'familiya':'tursunov',
              't.yili':2001,
              'malumoti':"o'rta maxsus",
              'tillar':['php','jango']},
    }
    
for ism, info in hamkasiblar.items():
    print(f"\n{ism.title()} {info ['familiya'].title()},"
         f"{info['t.yili']}-yilda tug'ilgan."
         f"malumoti: {info['malumoti']}. \n"
         "Quyidagi dasturlash tillarini biladi")
    for til in info['tillar']:
        print(til.upper())
    
























