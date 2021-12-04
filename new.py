import datetime
from openpyxl import workbook, load_workbook

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
        wb=load_workbook('Book1.xlsx')
        ws=wb.active
        ws.title="Invoice"
        ws.append([date.strftime("%x"),date.strftime("%X"),self.name,self.price,self.qty,self.qty*self.price,self.todaySale,f"#{self.dta}"])
        wb.save('Book1.xlsx')
    def updteTotal(self):
        with open('totalSale.txt') as f:
            self.dta=int(f.read())
            self.dta+=1
        with open('totalSale.txt','w') as f:
            f.write(str(self.dta))

choice = 'y'
while choice =='y' or choice =='Y':
    name=input("Enter the name of product: ")
    qty=int(input("Enter the qty: "))
    price=float(input("Enter the price: "))
    id=int(input("Enter the id: "))
    ob1=Sales(name,qty,price,id)
    ob1.updteTotal()
    ob1.writeinExcel()
    choice=input("Want to enter more?(y/n) ")
