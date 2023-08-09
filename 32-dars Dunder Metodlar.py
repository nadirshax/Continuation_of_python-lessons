class Avto:
    __num__avto = 0
    """Avtomobilning xususiyatlari"""
    def __init__(self,make,model,rang,yil,narh):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        Avto.__num__avto += 1
        
avto1 = Avto("GM","malibu","qora",2019,25000)
print(avto1)
