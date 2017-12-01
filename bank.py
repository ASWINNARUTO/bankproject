import pymysql
import pymysql.cursors
import random
import datetime
import time
def creation():
    try:
        password=input("Enter the password for database")
        db=pymysql.connect("localhost","root",password)
        cur=db.cursor()
        cur.execute("create database bankac")
        cur.execute("use bankac")
        db=pymysql.connect("localhost","root",password,"bankac")
        cur=db.cursor()
        cur.execute("""create table Cusdetails(cusid varchar(15) primary key,accountno int(10),username varchar(20),country varchar(12),state varchar(12),city varchar(12),
addline1 varchar(100),addline2 varchar(100),pincode varchar(12))""")
        cur.execute("""create table AccountDetails(cusid varchar(15),accountno int(10) primary key,money int(15),accounttype varchar(100),password varchar(100))""")
        cur.execute("""create table AccountTransaction(cusid varchar(15),accountno int(10) primary key,date date,trastype varchar(12),Amount int(23),Balance int(13))""")
        cur.execute("""create table Admindetails(Adminid varchar(14),adminpassword varchar(14))""")
        cur.execute("""insert into admindetails values(%s,%s)""",('aswinkumar','superman'))
        cur.execute("""create table closedaccount(accountno int(5),deleteddate date)""")
        db.commit()
    except:
        a=menu()
def create():
    try:
        password=input("Enter the password for database") 
        db=pymysql.connect("localhost","root",password,"bankac")
        cur=db.cursor()
        return(cur,db)
    except:
        print("wrong database password")
        a=menu()
        
     
    
    
def generator():
    h=random.randint(100,10001)
    return(h)
class menu:
    def __init__(self):
        print("              Main Menu")
        print("1. Sign up(New Customers)")
        print("2. Sign in(Existing Customers)")
        print("3. Admin Sign In")
        print("4. Quit")
        n=int(input("Enter your choice....")) 
        if(n==1):
            s=Signup()
        if(n==2):
            s=Signin()
        if(n==3):
            s=Admin()
        if(n==4):
            exit()
    
class Signup:
    def __init__(self):
        try:
            self.username=input("\nEnter the user name...")
            self.country=input("\nEnter the country...")
            self.state=input("\nEnter the state...")
            self.Addrline1=input("\nEnter the address line 1...")
            self.Addrline2=input("\nEnter the address line 2...")
            self.city=input("\nEnter the city name...")
            while(True):
                self.pincode=input("\nEnter the pincode......")
                if(len(self.pincode)>6):
                    break
                else:
                    print("Wrong pincode")
            self.choose=int(input("\nEnter the type of account\n1.Savings Account\n2.Current Account"))
            if(self.choose==1):
                self.Accounttype=100
                self.money=0
            if(self.choose==2):
                self.Accounttype=0
                while(True):
                    self.money=int(input("Enter the amount of money(minimum 5k)"))
                    if(self.account>5000):
                        break
                    else:
                        print("amount should be greater than 5000")
            self.customerid=self.username+str(generator())
            self.accountno=generator()
        except:
            print("error we will redirect")
            a=menu()
            
        while(True):
            self.password=input("\nEnter the password...")
            self.cpass=input("\nconfirm password...")
            if(self.password!=self.cpass and len(self.password)<6):
                print("\nEnter the password again")
            else:
                break
        
        (cur,db)=create()
        
        try:
            cur.execute("insert into Cusdetails values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.customerid,self.accountno,self.username,self.country,self.state,self.city,self.Addrline1,self.Addrline2,self.pincode))
            cur.execute("insert into AccountDetails values(%s,%s,%s,%s,%s)",(self.customerid,self.accountno,self.money,self.Accounttype,self.password))
        except:
            cur.rollback()
        db.commit()
        print("the data entered successfully happy banking\n")
        print("your Automatically generated customerid is ",self.customerid)
        print("your Automatically generated accountno is",self.accountno)
        while(True):
            i=input("\ndo u want to continue to your account press(y\n)..")
            try:
                if(i=='y'):
                    s=Signin()
                else:
                    exit()
            except:
                print("\nyou have pressed wrong symbol we are going to menu")
                a=menu()

class Signin(menu):
    def __init__(self):
        self.customerid=input("\nEnter the customerid...")
        (cur,db)=create()
        cur.execute("select password from accountdetails where cusid=%s",self.customerid)
        data=cur.fetchone()
        datas=data[0]
        self.tries=3
        while(self.tries>0):
            self.password=input("\nEnter the password...")
            if(datas==self.password):
                print("\nWelcome to our bank please choose the operation below")
                self.options()
            else:
                self.tries-=1
                print("\nEnter the correct password you have",self.tries,"left")
        print("your chance is over now try again later")
        exit()
    def options(self):
        while(True):
            print("\n1.Address Change\n2.Money deposit\n3.Money Withdrawl\n4.Print Statement\n5.Transfer Money\n6.Account Closure\n7.Customers Logut")
            select=int(input("\nEnter you choice...."))
            if(select==1):
                self.Addresschange()
            if(select==2):
                self.Moneydeposit()
            if(select==3):
                self.Moneywithdraw()
            if(select==4):
                self.PrintStatement()
            if(select==5):
                self.TransferMoney()
            if(select==6):
                self.Accountclosure()
            if(select==7):
                print("you are successfully logout")
                a=menu()

    def Addresschange(self):
        self.newcon=input("\nEnter the new country name..")
        self.newstate=input("\nEnter the new state name..")
        self.newcity=input("\nEnter the new city name...")
        self.newAddrline1=input("\nEnter the new Address line 1...")
        self.newAddrline2=input("\nEnter the new Address line 2...")
        while(True):
            self.newPincode=int(input("\nEnter the new Pincode..."))
            if(len(str(self.newPincode))<6):
                print("The pincode is wrong enter the correct one...")
            else:
                break
        (cur,db)=create()
        try:
            cur.execute("""update cusdetails set country=%s,state=%s,city=%s,addline1=%s,addline2=%s,pincode=%s where cusid=%s""",(self.newcon,self.newstate,self.newcity,self.newAddrline1,self.newAddrline2,self.newPincode,self.customerid))
        except:
            print("Table update error redirecting wait")
            db.rollback()
            self.Addresschange()
        print("\nThank You vey much your address has been changed successfully")
        db.commit()
        

    
    
    def Moneydeposit(self):
        self.date=str(datetime.date.today())
        self.transtype='credit'
        while(True):
                self.amount=int(input("\nEnter the Amount to be deposited"))
                self.accountno=input("\nEnter the account no where the money to deposited")
                
                (cur,db)=create()
                try:
                    cur.execute("""select * from accountdetails where accountno=%s""",(self.accountno))
                except:
                    print("\nwrong account no")
                if(self.amount>0):
                        break
                else:
                        print("you amount is negative value")
        
        (cur,db)=create()
        try:
            cur.execute("update Accountdetails set money=money+%s where accountno=%s",(self.amount,self.accountno))
            cur.execute("select money from accountdetails where accountno=%s",(self.accountno))
            a=cur.fetchone()
            self.balance=int(a[0])
            cur.execute("insert into accounttransaction values(%s,%s,%s,%s,%s,%s)""",(self.customerid,self.accountno,self.date,self.transtype,self.amount,self.balance))
        except:
            print("Deposit failed")
            db.rollback()
            a=menu()
        db.commit()
        print("\nThe amount",self.amount, "has been successfully deposited to account no",self.accountno)
        while(True):
                a=input("\nif you want to continue press(y/n)")
                if(a=='y'):
                        self.Moneydeposit()
                else:
                        self.options()
                

    def Moneywithdraw(self):
        self.transtype='debit'
        while(True):
                self.date=str(datetime.date.today())
                self.amount=int(input("\nEnter the Amount to be withdrawed"))
                self.accountno=int(input("\nEnter the account no where the money to withdrawed"))
                
                (cur,db)=create()
                cur.execute("select accountno,money from accountdetails where cusid=%s",(self.customerid))
                a=cur.fetchone()
                i=int(a[0])
                j=int(a[1])
                if(i==self.accountno and self.amount<j):
                        break
                else:
                        print("\nyou have entered wrong accountno/you dont have suffient money in you account")
                        self.options()
        try:
            (cur,db)=create()
            cur.execute("update accountdetails set money=money-%s where cusid=%s",(self.amount,self.customerid))
            cur.execute("select money from accountdetails where accountno=%s",(self.accountno))
            c=cur.fetchone()
            self.balance=int(c[0])
            cur.execute("insert into accounttransaction values(%s,%s,%s,%s,%s,%s)""",(self.customerid,self.accountno,self.date,self.transtype,self.amount,self.balance))
        except:
            print("Withdraw failed")
            db.rollback()
        db.commit()
        db.close()
        print("\nThe amount",self.amount, "has been successfully withdrawed from your account no",self.accountno)
        print("\nyour new balance is",self.balance)
        while(True):
                a=input("\nif you want to continue press(y/n)")
                if(a=='y'):
                        self.Moneywithdraw()
                else:
                        self.options()

    
    def PrintStatement(self):
        while(True):
                self.accountno=int(input("\nEnter the account no...."))
                self.datefrom=input("\nDate from(year-month-date)...")
                self.dateto=input("\ndate to(year-month-date)...")
                l=self.datefrom.split('-')
                r=self.dateto.split('-')
                d0=datetime.date(int(l[0]),int(l[1]),int(l[2]))
                d1=datetime.date(int(r[0]),int(r[1]),int(r[2]))
                delta=d1-d0
                (cur,db)=create()
                cur.execute("select accountno from accountdetails where cusid=%s",(self.customerid))
                a=cur.fetchone()
                i=a[0]
                if(delta.days>0 and i==self.accountno):
                        print("\n Welcome you trasaction are below")
                        break
                else:
                        print("\nWrong date input/invalid account no")
        try:
            cur.execute("select * from accounttransaction where accountno=%s and date>=%s and date<=%s",(self.accountno,self.datefrom,self.dateto))
            a=cur.fetchall()
        except:
            print("sorry the error will be cleared soon")
            a=menu()
        print("|Customerid   |    Accountno   |  date  |   Amount  |transaction type|   balance  |\n")
        for i in a:
                self.customerid=i[0]
                self.accountno=i[1]
                self.date=i[2]
                self.tras=i[3]
                self.amount=i[4]
                self.balance=i[5]
                print("|",self.customerid,"|",self.accountno,"|",self.date,"|",self.trans,"|",self.amount,"|",self.balance,"|")
        
        while(True):
                a=input("\nif you want to continue press(y/n)")
                if(a=='y'):
                        self.PrintSatement()
                else:
                        self.options()

    def TransferMoney(self):
        self.transtype='debit'
        self.transtype1='credit'
        while(True):
                self.amount=int(input("\nEnter the Amount to be withdrawed"))
                self.date=str(datetime.date.today())
                self.accountTo=int(input("\nEnter the account no where the money to transfered"))
                self.accountno=int(input("\nEnter you account no "))
                self.customerid=input("\nEnter you customer id")
                (cur,db)=create()
                cur.execute("select accountno from accountdetails where cusid=%s",(self.customerid))
                a=cur.fetchone()
                i=a[0]
                cur.execute("select money from accountdetails where cusid=%s",(self.customerid))
                b=cur.fetchone()
                j=int(b[0])
                if(self.amount<j and a==self.accountno):
                    break
                else:
                    print("amount is not suffient to tansfer")
        (cur,db)=create()
        cur.execute("update Accountdetails set money=money-%s where cusid=%s",(self.amount,self.customerid))
        cur.execute("update Accountdetails set money=money+%s where accountno=%s",(self.amount,self.accountTo))
        db.commit()
        cur.execute("select money from accountdetails where accountno=%s",(self.accountno))
        c=cur.fetchone()
        self.balance1=int(c[0])
        cur.execute("select money from accountdetails where accountno=%s",(self.accountTo))
        d=cur.fetchone()
        self.balance2=d[0]
        cur.execute("insert into accounttransaction values(%s,%s,%s,%s,%s,%s)",(self.customerid,self.accountno,self.date,self.transtype,self.amount,self.balance1))
        cur.execute("select cusid from accountdetails where accountno=%s",(self.accountTo))
        a=cur.fetchone()
        cus=a[0]
        cur.execute("insert into accounttransaction values(%s,%s,%s,%s,%s,%s)",(cus,self.accountTo,self.date,self.transtype1,self.amount,self.balance2))

        print("\nThe amount",self.amount, "has been successfully transfered to your account no",self.accountTo)
        print("\nyour new balance is",self.balance1)
        print("\nThat account balance is",self.balance2)
        db.commit()
        
        while(True):
                a=input("\nif you want to continue press(y/n)")
                if(a=='y'):
                        self.TransferMoney()
                else:
                        self.options()

    def Accountclosure(self):
        
        try:          
            (cur,db)=create()
            self.date=str(datetime.date.today())
            cur.execute("select * from cusdetails where cusid=%s",(self.customerid))
            a=cur.fetchone()
            self.accountno=int(a[1])
            cur.execute("insert into closedaccount values(%s,%s)",(self.accountno,self.date))
            cur.execute("select addline1,addline2,pincode from cusdetails where cusid=%s",(self.customerid))
            p=cur.fetchone()
            self.addrline1=p[0]
            self.addrline2=p[1]
            self.pincode=p[2]
            cur.execute("select money from accountdetails where cusid=%s",(self.customerid))
            sup=cur.fetchone()
            self.money=sup[0]
            cur.execute("delete from cusdetails where cusid=%s",(self.customerid))
            cur.execute("delete from accountdetails where cusid=%s",(self.customerid))
            cur.execute("delete from accounttransaction where cusid=%s",(self.customerid))
            print("\nyour account is successfully closed you money ",self.money,"is trasfered to address",self.addrline1,self.addrline1,self.pincode)
            db.commit()
        except:
            print("\error in closing account")
            self.options()
            
        
            
class Admin(menu):
   def __init__(self):
                try:
                    self.adminid=input("\nEnter the admin id...")
                    self.password=input("\nEnter the password..")
                    (cur,db)=create()
                    cur.execute("select adminpassword from admindetails where adminid=%s",self.adminid)
                    passs=cur.fetchone()
                    self.pas=passs[0]
                    self.tries=3
                    while(self.tries>0):
                          
                            if(self.pas==self.password):
                                    print("\nWelcome Admin please choose the operation below")
                                    self.options1()
                            else:
                                    self.tries-=1
                                    print("\nEnter the correct password you have",self.tries,"left")
                    print("your chance is over now try again later")
                    exit()
                except:
                    print("error")
                    print("redirecting")
   def options1(self):                              
                while(True):
                
                    print("\nEnter your choice \n1.colsure account\n2.logout\n")
                    self.choose=int(input("Enter you choice"))
                    if(self.choose==1):
                            (cur,db)=create()
                            print("the closed accounts are ")
                            print("|accountno|deletedate|")
                            
                            try:
                                cur.execute("select * from closedaccount")
                                r=cur.fetchall()
                                for row in r:
                                    self.accountno=row[0]
                                    self.deletedate=row[1]
                                    print("|",self.accountno,"|",self.deletedate,"|\n")
                                self.choose=input("type y if you want to continue or not")
                            except:
                                print("error we redirect")
                                db.rollback()
                                a=menu()
                    if(self.choose==2):
                            a=menu()
                            
creation()
a=menu()
