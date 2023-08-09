class Talaba:
    def __init__(self,ism,familiya,tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        
    def get_name(self):
        return self.ism
    
    def get_lastnam(self):
        return self.familiya
    
    def get_age(self,yil):
        return yil - self.tyil
    
        
    def tanishtir(self):
        print(f"Ismim{self.ism} {self.familiya}, Tug'ilgan yilim {self.tyil}")
        
Talaba1 = Talaba("Nodir","Shadiyev",1993)
Talaba2 = Talaba("Gauhar","Amanbayeva",1995)
Talaba3 = Talaba("Olim","Alimov",1987)

