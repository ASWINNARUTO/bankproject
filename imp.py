class Addresschange(Signin):
    def __init__(self):
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
        db=pymysql.connect("localhost","root","aswin","bank")
        cur=db.cursor()
        try:
            cur.execute("""update cusdetails set country=%s,state=%s,city=%s,addline1=%s,addline=%s,pincode=%s where cusid=%s""",(self.newcon,self.newstate,self.newcity,self.newAddrline1,self.newAddrline2,self.newPincode,Signin.customerid))
        except:
               print("Table update error redirecting wait")
               db.rollback()
               a=Addresschange()
        print("\nThank You vey much your address has been changed successfully")
        db.comit()
class MoneyWithdraw(Signin):
    date=str(datetime.date.today())
    try:
        db=pymysql.connect("localhost","root","aswin","bank")
        cur=db.cursor()
    except:
        print("sorry connecting with database error")
    def __init__(self):
        self.transtype='debit'
        while(True):
                self.amount=input("\nEnter the Amount to be withdrawed")
                self.accountno=input("\nEnter the account no where the money to withdrawed")
                cur.execute("select accountno form accountdetails where cusid=%s",(Signin.customerid))
                a=cur.fetchone()
                i=a[0]
                cur.execute("select money from accountdetails where cusid=%s",(Signin.customerid))
                b=cur.fetchone()
                j=b[0]
                if(i==self.accountno and self.amount<j):
                        break
                else:
                        print("\nyou have entered wrong accountno/you dont have suffient money in you account")
        try:
            cur.execute("update Accountdetails set money=money-%s where cusid=%s",(self.amount,Signin.customerid))
            cur.execute("select money form accountdetails where accountno=%s",(self.accountno))
            c=fetchone()
            self.balance=c[0]
            cur.execute("\ninsert into accounttransaction values(%s,%s,%s,%s,%s,%s)""",(Sigin.customerid,self.accountno,self.date,self.transtype,self.amount,self.balance))
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
                        y=MoneyWithdraw()
                else:
                        Signin.options()

class PrintStatement(Signin):
    try:
        db=pymysql.connect("localhost","root","aswin","bank")
        cur=db.cursor()
    except:
        print("sorry connecting with database error")
    def __init__(self):
        while(True):
                self.accountno=input("\nEnter the account no....")
                self.datefrom=input("\nDate from(year-month-date)...")
                self.dateto=input("\ndate to(year-month-date)...")
                l=self.datefrom.split('-')
                r=self.dateto.split('-')
                d0=datetime.date(int(l[0]),int(l[1]),int(l[2]))
                d1=datetime.date(int(r[0]),int(r[1]),int(r[2]))
                delta=d0-d1
                cur.execute("select accountno form accountdetails where cusid=%s",(Signin.customerid))
                a=cur.fetchone()
                i=a[0]
                if(delta.days>0 and i==self.accountno):
                        print("\n Welcome you trasaction are below")
                        break
                else:
                        print("\nWrong date input/invalid account no")
        try:
            cur.execute("select * from accounttrasaction where date>=%s and date<=%s and cusid=%s",(self.dateform,self.dateto,Signin.customerid))
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
                        y=PrintStatement()
                else:
                        Signin.options()
      
class TransferMoney(Signin):
    try:
        db=pymysql.connect("localhost","root","aswin","bank")
        cur=db.cursor()
    except:
        print("sorry connecting with database error")
    def __init__(self):
        self.transtype='debit'
        self.transtype1='credit'
        while(True):
                self.amount=input("\nEnter the Amount to be withdrawed")
                self.accountTo=input("\nEnter the account no where the money to transfered")
                self.accountno=input("\nEnter you account no ")
                cur.execute("select accountno form accountdetails where cusid=%s",(Signin.customerid))
                a=cur.fetchone()
                i=a[0]
                cur.execute("select money from accountdetails where cusid=%s",(Signin.customerid))
                b=cur.fetchone()
                j=b[0]
                cur.execute("select money from accountdetails",(signin.customerid))
                k=cur.fetchall()
                for row in k:
                     if(row[0]==self.accountTo):
                            break
                     else:
                            pass
                else:
                     print("account no which money going to transfered is invalid")
                if(i==self.accountno and self.amount<j):
                     print("Welcome")
                else:
                     print("\nyou have entered wrong accountno/you dont have suffient money in you account")
        cur.execute("update Accountdetails set money=money-%s where cusid=%s",(self.amount,Signin.customerid))
        cur.execute("update Accountdetails set money=money+%s where accountno=%s",(self.amount,self.accountTo))
        cur.execute("select money form accountdetails where accountno=%s",(self.accountno))
        c=fetchone()
        self.balance1=c[0]
        cur.execute("select money form accountdetails where accountno=%s",(self.accountTo))
        d=fetchone()
        self.balance2=d[0]
        cur.execute("\ninsert into accounttransaction values(%s,%s,%s,%s,%s,%s)""",(Sigin.customerid,self.accountno,self.date,self.transtype,self.amount,self.balance))
        print("\nThe amount",self.amount, "has been successfully transfered to your account no",self.accountTo)
        print("\nyour new balance is",self.balance1)
        print("\nThat account balance is",self.balance2)
        
        while(True):
                a=input("\nif you want to continue press(y/n)")
                if(a=='y'):
                        y=TransferMoney()
                else:
                        Signin.options()
        
class AccountClosure(Signin):
        date=str(datetime.date.today())
        try:
            db=pymysql.connect("localhost","root","aswin","bank")
            cur=db.cursor()
        except:
            print("sorry connecting with database error")
        def __init__(self):
                try:
                    cur.execute("select cusdetails where cusid=%s",(Signin.customerid))
                    a=fetchone()
                    self.accountno=row[1]
                    cur.execute("insert into closureaccount values(%s,%s)",(self.accountno,self.date))
                    cur.execute("select addline1,addline2,pincode form cusdetails where cusid=%s",(Signin.customerid))
                    p=cur.fetchone()
                    self.addrline1=p[0]
                    self.addrline2=p[1]
                    self.pincode=p[2]
                    cur.execute("select money from accountdetails where cusid=%s",(Signin.customerid))
                    sup=cur.fetchone()
                    self.money=sup[0]
                    cur.execute("delete from cusdetails where cusid=%s",Signin.customerid)
                    cur.execute("delete from accountdetails where cusid=%s",Signin.customerid)
                    print("\nyour account is successfully closed you money ",self.money,"is trasfered to address",self.addrline1,self.addrline1,self.pincode)
                except:
                    print("\nclosing error occured wait redirecting")
                    a=Signin()
                    a.choose()
class Admin:
   def __init__(self):
                try:
                    self.adminid=input("\nEnter the admin id...")
                    self.password=input("\nEnter the password..")
                    db=pymysql.connect("localhost","root","aswin","bank")
                    cur=db.cursor()
                    cur.execute("select adminpassword from admindetails where adminid=%s",self.adminid)
                    passs=cur.fetchone()
                    self.pas=passs[0]
                    self.tries=3
                    while(self.tries>0):
                            self.password=input("\nEnter the password...")
                            if(self.datas==self.password):
                                    print("\nWelcome Admin please choose the operation below")
                                    self.options1()
                            else:
                                    self.tries-=1
                                    print("\nEnter the correct password you have",self.tries,"left")
                    print("your chance is over now try again later")
                    exit()
                except:
                    print("error")
   def options1(self):                              
                while(True):
                    print("\nEnter your choice \n1.colsure account\n2.logout\n")
                    self.choose=int(input("Enter you choice"))
                    if(self.choose==1):
                            print("the closed accounts are ")
                            print("|accountno|deletedate|\n")
                            try:
                                db=pymysql.connect("localhost","root","aswin","bank")
                                cur=db.cursor()
                            except:
                                print("sorry connecting with database error")
                            try:
                                cur.execute("select * from accountclosure")
                                r=cur.fetchall()
                                for row in r:
                                    self.accountno=row[0]
                                    self.deleteddate=row[1]
                                    print("|",self.accountno,"|",self.deletedate,"|\n")
                            except:
                                print("retry later")
                    else:
                            print("thank you")
                            a=menu()


                    
                        
               
                
            

        





        
        
        
