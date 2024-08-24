# Bike Rental System : (Using OOPs)

class BikeShop :
    def __init__(self,stock):
        self.stock=stock
    def displaybike(self):
        print("Total bikes : ",self.stock)
    def rentforbike(self,q) :
            if q<=0 :
                print("Enter proper value")
            elif q>self.stock :
                print("Enter the value less than stock")
            else :
                self.stock=self.stock-q
                print("Total price : " , q*100)
                print("Remaining stock : " , self.stock)
while True :
    obj=BikeShop(100)
    uc=int(input('''
1. Display stocks 
2. Rent a bike 
3. Exit    
    '''))
    if uc==1 :
        obj.displaybike()
    elif uc==2 :
        n=int(input("Enter the quantity : "))
        obj.rentforbike(n)
    else :
        break
