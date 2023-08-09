yosh = int(input('yoshingiz nechchida? '))

if yosh <=4:
    print('sizga kirish bepul')
    narh="1000"


   # //// mana shu yo'l bilan qilsa bo'ladi //////

elif yosh <=12:
    print("sizga kirish 5000 so'm")
    narh = '3000'
else:
    print("sizga kirish 10000 so'm")
    narh = "20000"


    #tagida alohida print yoziladi

    narh = "2000"
    print(f"sizga kirish {narh} so'm")
    
    
    kun = input("Bugun nima kun?>>>")
if kun.lower()=='shanba' or kun.lower()=='yakshanba':
    print('Bugun dam olish kuni.')
else:
    print('Bugun ish kuni.')
    
    
    
    
    kun = input("Bugun nima kun?")
harorat = float(input("Havo harorati qanday?"))
if kun.lower()=='yakshanba' and harorat>=30:
    print("Cho'milgani ketdik!")
elif kun.lower()=='yakshanba' and harorat<30:
    print("Uyda dam olamiz!")
    
    
    
    
narh = 15000 # mijoz 15 so'mga ovqat oldi
choy = True
salat = False
non = True
kompot = True
assorti = False
#Quyidagi har bir shart alohida tekshiriladi va bir-biriga bog'liq emas
if choy:   # agar choy olsa
    print("Mijoz choy oldi.")
    narh = narh + 3000
if salat:  # agar salat olsa
    print("Mijoz salat oldi.")
    narh = narh + 5000
if non:    # agar non olsa
    print("Mijoz non oldi.")
    narh = narh + 2000
if kompot: # agar kompot olsa
    print("Mijoz kompot oldi.")
    narh = narh + 5000
if assorti: # agar assorti olsa
    print("Mijoz assorti oldi.")
    narh = narh + 15000
    
print(f"Jami {narh} so'm")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    