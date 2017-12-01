
#import pyodbc(for odbc connectivity)
import pymysql
import pymysql.cursors
import random
import datetime
import time



#basic creation function....
def basiccreate():
    try:
        print("Hi u must have configured the database!!!")
        password=input("Enter the password for database")
        db=pymysql.connect("localhost","root",password)
        cur=db.cursor()
        cur.execute("create database bankaccount")
        cur.execute("use bankaccount")
        db=pymysql.connect("localhost","root",password,"bankaccount")
        cur=db.cursor()
        cur.execute("""create table Custdetails(custid varchar(15) primary key,acctno int(10) unique,username varchar(20),country varchar(12),state varchar(12),city varchar(12),
addr varchar(20),pincode varchar(12))""")
        cur.execute("""create table AcctDetails(custid varchar(15),acctno int(10) primary key,money int(15),accttype varchar(100),password varchar(100))""")
        cur.execute("""create table AcctTrans(custid varchar(15),acctno int(10) primary key,date date,trastype varchar(12),Amount int(23),Balance int(13))""")
        cur.execute("""create table Admindetails(Adminid varchar(14),adminpassword varchar(14))""")
        cur.execute("""insert into Admindetails values(%s,%s)""",('balaji','balag'))
        cur.execute("""create table closedacct(acctno int(5),deleteddate date)""")
        db.commit()
    except:
        a=mainmenu()










#this is used to create a custonmer db....
def create():
    try:
        password=input("Enter the password for database")
        db=pymysql.connect("localhost","root",password,"bankaccount")
        cur=db.cursor()
        return(cur,db)
    except:
        print("worng password for dataabse")
        a=mainmenu()



#random number generation...
    
def randomizer():
    h=random.randint(1000,10001)
    return(h)





#basic main menu....

class mainmenu:
    def __init__(self):
        print("!!Main Menu!!")
        print("1. Sign up")
        print("2. Sign in")
        print("3. Admin Sign In")
        print("4. Exit")
        choose=int(input("Enter your choice....")) 
        if(choose==1):
            s=Signingup()
        elif(n==2):
            s=Signin()
        elif(n==3):
            s=admin()
        elif(n==4):
            exit()




#for newly joining customers!!!!
class Signingup:
    def __init__(self):
        try:
            self.username=input("\nEnter the user name\t")
            self.country=input("\nEnter the country\t")
            self.state=input("\nEnter the state\t")
            self.Addr1=input("\nEnter the addr line 1\t")
            self.Addr2=input("\nEnter the addr line2\t")
            self.city=input("\nEnter the city name\t")
            while(True):
                self.pincode=input("\nEnter the pincode\t")
                print("please enter pincode exactly 6numbers or else it will be rejected!!!")
                if(len(self.pincode)==6):
                    break
                else:
                    print("Wrong pincode")
            self.choose=int(input("\nEnter the type of account\n1.Savings Account\n2.Current Account\t"))
            if(self.choose==1):
                self.Accounttype=100
                self.money=0
            if(self.choose==2):
                self.Accounttype=0
                while(True):
                    self.money=int(input("please enter the amount(min 5000)"))
                    if(self.account>5000):
                        break
                    else:
                        print("amount should be greater than 10000(business purposes)!!!!")
            self.custid=self.username+str(randomizer())
            self.acctno=randomizer()
        except:
            print("error again mainmenu enter")
            a=mainmenu()
            
        while(True):
            self.password=input("\nEnter the password\t")
            self.cpass=input("\nconfirm password\t")
            #passsword should be 6characters
            if(self.password!=self.cpass and len(self.password)<6):
                print("\nEnter the password again")
            else:
                break
        
        (cur,db)=create()
        
        try:
            cur.execute("insert into Custdetails values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.custid,self.acctno,self.username,self.country,self.state,self.city,self.Addr1,self.Addr2,self.pincode))
            cur.execute("insert into AcctDetails values(%s,%s,%s,%s,%s)",(self.custid,self.acctno,self.money,self.Accttype,self.password))
        except:
            cur.rollback()
        db.commit()
        print("the data updated happy banking\n")
        print("your customerid is ",self.custid)
        print("your accountno is",self.acctno)
        #please note these details
        while(True):
            i=input("\ndo u want to continue to your account press(y\n)\t")
            try:
                if(i=='y'):
                    s=Signin()
                else:
                    exit()
            except:
                print("\nyou have pressed wrong symbol we are going to mainmenu")
                a=mainmenu()


                






#old customer signin
                
class Signin(mainmenu):
    def __init__(self):
        self.custid=input("\nEnter the customerid...")
        (cur,db)=create()
        cur.execute("select password from acctdetails where cusid=%s",self.custid)
        data=cur.fetchone()
        datas=data[0]
        self.tries=5
        while(self.tries>0):
            self.password=input("\nEnter the password...")
            if(datas==self.password):
                print("\nWelcome!!!please choose the operation below")
                self.option()
            else:
                self.tries-=1
                print("\nEnter the correct password you have",self.tries,"left")
        print("your chance is over now try again later")
        exit()
    def option(self):
        while(True):
            print("\n1.Address Change\n2.Money deposit\n3.Money Withdrawl\n4.Print Statement\n5.Transfer Money\n6.Account Closure\n7.Customers Logut")
            select=int(input("\nEnter you choice...."))
            if(select==1):
                self.Addresschange()
            elif(select==2):
                self.Moneydeposit()
            elif(select==3):
                self.Moneywithdraw()
            elif(select==4):
                self.PrintStatement()
            elif(select==5):
                self.TransferMoney()
            elif(select==6):
                self.Accountclosure()
            elif(select==7):
                print("you are successfully logout")
                a=mainmenu()






#address CHANGING!!!!

    def Addresschange(self):
        self.newcon=input("\nEnter the new country name!!")
        self.newstate=input("\nEnter the new state name!!")
        self.newcity=input("\nEnter the new city name!!!")
        self.newAddr=input("\nEnter the new Address!!!")
        while(True):
            self.newPincode=int(input("\nEnter the new Pincode!!!"))
            if(len(str(self.newPincode))!=6):
                print("The pincode is wrong enter the correct one!!")
            else:
                break
        (cur,db)=create()
        try:
            cur.execute("""update custdetails set country=%s,state=%s,city=%s,addr=%s,pincode=%s where custid=%s""",(self.newcon,self.newstate,self.newcity,self.newAddrline1,self.newAddrline2,self.newPincode,self.customerid))
        except:
            print("Table update error redirecting wait")
            db.rollback()
            self.Addresschange()
        print("\nyour address has been changed!!!")
        db.commit()
        









#money depositting!!!    
    
    def Moneydeposit(self):
        self.date=str(datetime.date.today())
        self.transtype='credit'
        while(True):
                self.amount=int(input("\nEnter the Amount to be deposited"))
                self.accountno=input("\nEnter the account no to deposit")
                
                (cur,db)=create()
                try:
                    cur.execute("""select * from acctdetails where accountno=%s""",(self.acctno))
                except:
                    print("\nwrong account no")
                if(self.amount>0):
                        break
                else:
                        print("you amount is negative value")
        
        (cur,db)=create()
        #updating database
        
        try:
            cur.execute("update Acctdetails set money=money+%s where acctno=%s",(self.amount,self.acctno))
            cur.execute("select money from acctdetails where acctno=%s",(self.acctno))
            a=cur.fetchone()
            self.balance=int(a[0])
            cur.execute("insert into accttrans values(%s,%s,%s,%s,%s,%s)""",(self.custid,self.acctno,self.date,self.transtype,self.amount,self.balance))
        except:
            print("Deposit failed")
            db.rollback()
            a=mainmenu()
        db.commit()
        print("\nThe amount",self.amount, "has been successfully deposited to account no",self.acctno)
        while(True):
                a=input("\nif you want to continue press(y/n)")
                if(a=='y'):
                        self.Moneydeposit()
                else:
                        self.option()




    #withsrawal must have balance!!!

    def Moneywithdraw(self):
        self.transtype='debit'
        while(True):
                self.date=str(datetime.date.today())
                self.acctno=int(input("\nEnter the account no where the money to withdraw"))
                self.amount=int(input("\nEnter the Amount to withdraw"))
               
                
                (cur,db)=create()
                cur.execute("select acctno,money from accountdetails where custid=%s",(self.custid))
                a=cur.fetchone()
                i=int(a[0])
                j=int(a[1])
                if(i==self.accountno and self.amount<j):
                        break
                else:
                        print("\nyou have entered wrong accountno/you dont have suffient money in you account")
                        self.option()
        try:
            (cur,db)=create()
            cur.execute("update acctdetails set money=money-%s where cusid=%s",(self.amount,self.custid))
            cur.execute("select money from acctdetails where acctno=%s",(self.acctno))
            c=cur.fetchone()
            self.balance=int(c[0])
            cur.execute("insert into accttrans values(%s,%s,%s,%s,%s,%s)""",(self.custid,self.acctno,self.date,self.transtype,self.amount,self.balance))
        except:
            print("Withdraw failed")
            db.rollback()
        db.commit()
        db.close()
        print("\nThe amount",self.amount, "has been successfully withdrawed from your account no",self.acctno)
        print("\nyour new balance is",self.balance)
        while(True):
                a=input("\nif you want to continue press(y/n)")
                if(a=='y'):
                        self.Moneywithdraw()
                else:
                        self.option()

    




    def PrintStatement(self):
        while(True):
                self.acctno=int(input("\nEnter the account no...."))
                self.datefrom=input("\nDate from...")
                self.dateto=input("\ndate to(year-month-date)...")
                l=self.datefrom.split('-')
                r=self.dateto.split('-')
                d0=datetime.date(int(l[0]),int(l[1]),int(l[2]))
                d1=datetime.date(int(r[0]),int(r[1]),int(r[2]))
                delta=d1-d0
                (cur,db)=create()
                cur.execute("select acctno from acctdetails where custid=%s",(self.custid))
                a=cur.fetchone()
                i=a[0]
                if(delta.days>0 and i==self.acctno):
                        print("\n Welcome you trasaction are below")
                        break
                else:
                        print("\nWrong date input/invalid account no")
        try:
            cur.execute("select * from accttrans where acctno=%s and date>=%s and date<=%s",(self.acctno,self.datefrom,self.dateto))
            a=cur.fetchall()
        except:
            print("sorry the error will be cleared soon")
            a=mainmenu()
        print("|Customerid   |    Accountno   |  date  |   Amount  |transaction type|   balance  |\n")
        for i in a:
                self.custid=i[0]
                self.acctno=i[1]
                self.date=i[2]
                self.tras=i[3]
                self.amount=i[4]
                self.balance=i[5]
                print("|",self.custid,"",self.acctno,"|",self.date,"|",self.trans,"|",self.amount,"|",self.balance,"|")
        
        while(True):
                a=input("\nif you want to continue press(y/n)")
                if(a=='y'):
                        self.PrintSatement()
                else:
                        self.option()






    def TransferMoney(self):
        self.transtype='debit'
        self.transtype1='credit'
        while(True):
                self.amount=int(input("\nEnter the Amount to be withdrawed"))
                self.date=str(datetime.date.today())
                self.accountTo=int(input("\nEnter the account no where the money to transfered"))
                self.accountno=int(input("\nEnter you account no "))
                self.custid=input("\nEnter you customer id already given to you")
                (cur,db)=create()
                cur.execute("select acctno from acctdetails where custid=%s",(self.custid))
                a=cur.fetchone()
                i=a[0]
                cur.execute("select money from acctdetails where custid=%s",(self.custid))
                b=cur.fetchone()
                j=int(b[0])
                if(self.amount<j and a==self.acctno):
                    break
                else:
                    print("amount is not suffient to tansfer")
        (cur,db)=create()
        cur.execute("update Acctdetails set money=money-%s where cusid=%s",(self.amount,self.custid))
        cur.execute("update Acctdetails set money=money+%s where acctno=%s",(self.amount,self.accountTo))
        db.commit()
        cur.execute("select money from acctdetails where acctno=%s",(self.acctno))
        c=cur.fetchone()
        self.balance1=int(c[0])
        cur.execute("select money from acctdetails where acctno=%s",(self.accountTo))
        d=cur.fetchone()
        self.balance2=d[0]
        cur.execute("insert into accttrans values(%s,%s,%s,%s,%s,%s)",(self.custid,self.acctno,self.date,self.transtype,self.amount,self.balance1))
        cur.execute("select cusid from accountdetails where accountno=%s",(self.accountTo))
        a=cur.fetchone()
        cus=a[0]
        cur.execute("insert into accttrans values(%s,%s,%s,%s,%s,%s)",(cus,self.accountTo,self.date,self.transtype1,self.amount,self.balance2))

        print("\nThe amount",self.amount, "has been successfully transfered to your account no",self.accountTo)
        print("\nyour new balance is",self.balance1)
        print("\nThat account balance is",self.balance2)
        db.commit()
        
        while(True):
                a=input("\nif you want to continue press(y/n)")
                if(a=='y'):
                        self.TransferMoney()
                else:
                        self.option()




    def Accountclosure(self):
        
        try:          
            (cur,db)=create()
            self.date=str(datetime.date.today())
            cur.execute("select * from custdetails where custid=%s",(self.custid))
            a=cur.fetchone()
            self.acctno=int(a[1])
            cur.execute("insert into closedaccount values(%s,%s)",(self.acctno,self.date))
            cur.execute("select addr,pincode from custdetails where custid=%s",(self.custid))
            p=cur.fetchone()
            self.addr=p[0]
            self.pincode=p[1]
            cur.execute("select money from acctdetails where custid=%s",(self.custid))
            sup=cur.fetchone()
            self.money=sup[0]
            cur.execute("delete from custdetails where custid=%s",(self.custid))
            cur.execute("delete from acctdetails where custid=%s",(self.custid))
            cur.execute("delete from accttrans where custid=%s",(self.custid))
            print("\nyour account is successfully closed and your money ",self.money,"is trasfered to address",self.addr,self.pincode)
            print("thank you for banking also notify the bank on receiving!!!!!")
            db.commit()
        except:
            print("\error in closing account")
            self.option()
            
        
            




class admin(mainmenu):
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
                                    self.content()
                            else:
                                    self.tries-=1
                                    print("\nEnter the correct password you have",self.tries,"left")
                    print("your chance is over now try again later")
                    exit()
                except:
                    print("error")
                    print("redirecting")





   def content(self):                              
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
                                    self.acctno=row[0]
                                    self.deletedate=row[1]
                                    print("|",self.acctno,"|",self.deletedate,"|\n")
                                self.choose=input("type y if you want to continue or not")
                            except:
                                print("error we redirect")
                                db.rollback()
                                a=mainmenu()
                    if(self.choose==2):
                            a=mainmenu()
                            
                      
