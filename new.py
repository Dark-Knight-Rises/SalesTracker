import datetime

class Sales:
    todaySale =0
    def __init__(self,name,qty,price,id):
        self.name=name
        self.qty=qty
        self.price=price
        self.id=id
        Sales.todaySale+=1
    def writeinExcel(self):
        date=datetime.datetime.now()
        print(date.strftime("%x")) #date
        print(date.strftime("%X")) #time
    def updteTotal(self):
        with open('totalSale.txt') as f:
            dta=int(f.read())
            dta+=1
        with open('totalSale.txt','w') as f:
            f.write(str(dta))

choice = 'y'
i=1
while choice =='y' or choice =='Y':
    name=input("Enter the name of product: ")
    qty=int(input("Enter the qty: "))
    price=float(input("Enter the price: "))
    id=int(input("Enter the id: "))
    s=f"ob{i}"
    s=Sales(name,qty,price,id)
    print(s)
    # s.updteTotal()
    # s.writeinExcel()
    choice=input("Want to enter more?(y/n) ")
    i+=1
