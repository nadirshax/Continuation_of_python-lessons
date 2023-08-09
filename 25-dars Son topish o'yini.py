# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 20:23:55 2023

@author: asus
"""



# import random
# def sontop(x=10):
#     tasodifiy_son = random.randint(1,x)
#     print(f"men 1 dan {x} gacha son o'yladim.Topa olasizmi:\n Tayyor bo'lsangiz boshladik")
    
#     while True:
#         taxmin = int(input(">>>"))
#         if taxmin<tasodifiy_son:
#             print("Xato. Men o'ylagan son bundan kattaroq.Yana xarakat qiling:")
#         elif taxmin>tasodifiy_son:
#             print("Xato. Men o'ylagan son bundan kichikroq.Yana xarakat qiling:")
#         else:
#             break
#     print("Tabriklaymiz topdingiz")    
            


import random
def sontop(x=10):
    tasodifiy_son = random.randint(1,x)
    print(f"men 1 dan {x} gacha son o'yladim.Topa olasizmi:\n Tayyor bo'lsangiz boshladik")
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin=int(input(">>>"))
        if taxmin<tasodifiy_son:
            print("Xato.men o'ylagan son bundan kattaroq.Yana urunib ko'ring:")
        elif taxmin>tasodifiy_son:
            print("Xato.men o'ylagan son bundan kichikroq.Yana urunib lo'ring:")
        else:
            break
    return taxminlar
    print(f"Tabriklaymiz.{taxminlar} ta taxmin bilan topdingiz")
        
    
    
    
    
def sontop_pc(x=10):
    input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing.Men topaman.")
    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = random.randbytes(quyi,yuqori)
        else:
            taxmin = quyi
        javob= input(f"Siz.{taxmin} sonini o'yladingiz:to'g'ri(t),"
                     
                     f"Men o'ylagan son bundan kattaroq(+),yoki kichikroq (-)".lower())
        if javob =="-":
            yuqori = taxmin -1
        elif javob == "+":
            quyi = taxmin + 1
        else:
            break
        print(f"Men {taxminlar} ya taxmin bilan topdim!")
        return taxminlar
    
    
    
    
def play(x=10):
    yana = True
    while yana:
        taxminlar_user = sontop(x)
        taxminlar_pc = sontop_pc(x)
        
        if taxminlar_user>taxminlar_pc:
            print("Men yutdim")
        elif taxminlar_user()<taxminlar_pc:
            print("Siz yutdingiz")
        else:
            print("Durrang")
        yana = int(input("Yana o'ynaysizmi! ha(1) yo'q(0):"))
        
        


































# ism = input('ismingiz nima?\n>>>') # foydalanuvchi ismini so'raymiz
# if ism.lower() != 'ali': # agar ism aliga teng bo'lmasa ...
#     print(f"uzr, {ism.title()} biz alini kutayapmiz.") # quyidagi xabar chiqadi
# else:
#     print("salom, ali")
    







# ism = input('ismingiz kim?\n>>>') # foydalanuvchi ismini so'raymiz
# if ism.lower() != 'ali': # agar ism aliga teng bo'lmasa ...
#     print(f"uzr, {ism.title()} biz alini kutayapmiz.") # quyidagi xabar chiqadi
# else:
#     print("salom, ali")
    