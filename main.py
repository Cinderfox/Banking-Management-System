import os
import pickle
import random

class bank:                                        #Class for pre-requisites
    def __init__(self):
        self.bank_asset=100000
        self.mort=123
        self.stud_loan=123
        self.auto_loan=123
        self.s_b_a=123
        self.pers_loan=123
        self.credit_card=123
        self.debit_card=123

    def bank_details(self):
        self.bank_asset=input('Enter the bank asset- ')
        self.mort=input('Enter the mortgage loan rate- ')
        self.stud_loan=input('Enter the student loan rate- ')
        self.auto_loan=input('Enter the automobile loan rate- ')
        self.s_b_a=input('Enter the small bussiness loan rate- ')
        self.pers_loan=input('Enter the personal loan rate- ')
        self.credit_card=input('Enter the interest rate on credit card- ') 
        self.debit_card=input('Enter the maximum amount that can be withdrawn per day- ')


class customer(bank):                                        #Class for customer details
    def __init__(self):
        self.cust_id=1
        self.cust_name=''
        self.cust_email=''
        self.cust_category=''
        self.cust_balance=0
        self.cust_dep=0
        self.cust_withdraw=0
        self.cust_transfer=0
        self.cust_loan=0
        self.cust_credit=[0,0]
        self.cust_debit=[0,0]
        self.passw=0

    def customer_details(self,j):
        if j==0:
           self.cust_id=random.randint(100000,1000000)
           self.cust_name=input('Enter the customer name- ')
           self.cust_email=input('Enter customer email-id- ')
           s=input('Enter the customer category(General or Student)- ')
           self.passw=input('Enter your password-')
           print()
           print('YourID is- ',self.cust_id)
           self.cust_category=s.lower()
        if j==1:
           self.cust_name=input('Enter the customer name- ')
           self.cust_email=input('Enter customer email-id- ')
           self.cust_category=input('Enter the customer category(General or Student)- ')
            
    def customer_deposit(self):
        amt=input('Enter the amount to be deposited- ')
        self.balance+=amt
    def customer_withdraw(self):
        amt=input('Enter the amount to be withdrawn- ')
        self.balance-=amt
    def customer_transfer(self,account2):
        amt=input('Enter the amount to be transferred- ')
        self.balance-=amt


        
def main():
    
    print()
    print()
    print()
    print ('\t\t    *                   *                   *')
    print ('\t\t     *****             * *             ***** ')
    print ('\t\t      *****           *   *           ***** ')
    print ('\t\t       *****         *     *         ***** ')
    print ('\t\t        ********************************* ')
    print ('\t\t         *******WELCOME TO Z BANK*******  ')
    print ('\t\t           >Your Service,Our Priority<    ')
    print ('\t\t           ***************************    ')
    print ('\t\t          *****      *     *      *****   ')
    print ('\t\t         ****         *   *         ****  ')
    print ('\t\t        ***            * *            *** ')
    print ('\t\t       *                *                *')                              #Logo
    print()  
        
    
    while True:

      print()
      print()
      print ('\t\t\t\t____MAIN MENU____')
       
      print ('\t\t\t\t1 >> Administrator')
      print ('\t\t\t\t2 >> Customer')
      print ('\t\t\t\t3 >> Exit')
      print()
      choice0=input('Enter the choice- ')
      if choice0.isdigit():
       choice=int(choice0)
       if choice==1:                                           #Admin menu
            print ('\t\t\t\t1 >> Log in')
            print ('\t\t\t\t2 >> Return to main menu')
            print()
            choice0=input('Enter your choice- ')
            if choice0.isdigit():
             choice1=int(choice0)
             if choice1==1:
                 password=int(input('Enter password- '))
                 if password==123456789:
                    print()
                    print ('Access granted....')
                    print()
                    print ('\t\t\t\t1 >> Enter bank pre-requisites')
                    print ('\t\t\t\t2 >> View transactions')
                    print ('\t\t\t\t3 >> Log out')
                    print()
                    choice20=input('Enter your choice- ')
                    if choice20.isdigit():
                     choice2=int(choice20)
                     if choice2==1:                                          #Pre-requisites
                         b=bank()
                         b.bank_details()
                         dict_bank={}

                         dict_bank[123456789]=[b.bank_asset,b.mort,b.stud_loan,b.auto_loan,b.s_b_a,b.pers_loan,b.credit_card,b.debit_card]
                

                         try:
                            f=open("bankdetails0.dat","rb")
                            m=pickle.load(f)
                    
                            f.close()
                            m.update(dict_bank)
                            f=open("bankdetails0.dat","wb")
                            pickle.dump(m,f)
                            f.close()

                         except:
                            f=open("bankdetails0.dat","wb")
                            pickle.dump(dict_bank,f)
                            f.close()
                            
                     elif choice2==2:                          #Transactions
                         try:
                            trans=open("transaction.txt","r")
                            print()
                            print ('Transaction details....')
                            print()
                           
                            transread=trans.readlines()
                            try:
                              for i in transread:
                                 r=i
                                 o=r.split('$$')
                                 for j in o:
                                   h= j.split('#')
                                   for c in h:
                                      if c[1]=='d':
                                       
                                          print()
                                          print ('_________________________________________________________________________')
                                      print (c)
                            except IndexError:
                                 pass
                         except IOError:
                             print()
                             print('No Transactions have been made!')
                             print()
                            
                     elif choice2==3:
                         while True:
                             break
                        
                     else:
                         print()
                         print("-Invalid Option!-")
                         print()

                    else:
                        print()
                        print("-Invalid option!-")
                        print()
                        
                 else:
                     print()
                     print ('--Wrong password!--')
                     print()

             elif choice1==2:
                 while True:
                     break
                
             else:
                 print()
                 print("-Invalid Option!-")
                 print()

            else:
                print()
                print("-Invalid option!-")
                print()

                        
       elif choice==2:                                         #Customer Menu
          while True:
           print()
           print ('\t\t\t\t1 >> Log in')
           print ('\t\t\t\t2 >> Register')
           print ('\t\t\t\t3 >> Return to Main Menu')
           print()
           choice30=input('Enter your choice- ')
           if choice30.isdigit():
            choice3=int(choice30)

            if choice3==1:                                      #Customer login
                   try:
                    print()
                    print("-Available Accounts-")
                    print()
                    f11=open("customer0.dat","rb")
                    d=pickle.load(f11)
                   except:
                     print()
                     print("-No Accounts Available!-")
                     print()
                   cnt=1
                   for item in d:
                     print("  ",cnt,"-",item)
                     cnt+=1
                   print()
                   f11.close()
                   print()
                   id1=int(input("Enter customer id-"))
                   print()
                   if id1 in d.keys():
                     print()
                     password=input("Enter your password-")
                     if password==d[id1][10]:
                      while True :
                       status=1
                       print()
                       print()
                       print ('\t\t\t\t____________MENU____________')
                       print ('\t\t\t\t 1 >> Modify account details')
                       print ('\t\t\t\t 2 >> View account')
                       print ('\t\t\t\t 3 >> Delete account')
                       print ('\t\t\t\t 4 >> Transfer money')
                       print ('\t\t\t\t 5 >> Deposit money')
                       print ('\t\t\t\t 6 >> Withdraw money')
                       print ('\t\t\t\t 7 >> Take loan')
                       print ('\t\t\t\t 8 >> Repay loan')
                       print ('\t\t\t\t 9 >> Issue credit card')
                       print ('\t\t\t\t10 >> Issue debit card')
                       print ('\t\t\t\t11 >> Log Out')
                       print()
                       print()
                       choice40=input('Enter your choice- ')
                       if choice40.isdigit():
                        choice4=int(choice40)
                        print()

                        if choice4==1:                                          #Modifying account details
                            p=customer()
                            p.customer_details(1)
                            f110=open("customer0.dat","rb")
                            dict1=pickle.load(f110)
                            
                            dict1[id1][0]=p.cust_name
                            dict1[id1][1]=p.cust_email
                            dict1[id1][2]=p.cust_category
                            f110.close()
                            

                            try:
                                f=open("customer0.dat","rb")
                                detail=pickle.load(f)
                                f.close()
                                detail.update(dict1)
                                f=open("customer0.dat","wb")
                                pickle.dump(detail,f)
                                f.close()
                                
                            except: 
                                f=open("customer0.dat","wb")
                                pickle.dump(dict1,f)
                                f.close()
                                print()
                                print('-Details are modified!-')
                                print()

                        elif choice4==2:                                            #Viewing account
                            f=open("customer0.dat","rb")
                            dict1=pickle.load(f)
                            f.close()
                            print()
                            print ('-Details-')
                            print (' ID->          ',id1)
                            print (' Name->        ',dict1[id1][0])
                            print (' E-mail->      ',dict1[id1][1])
                            print (' Category->    ',dict1[id1][2].title())
                            print (' Balance->     ',dict1[id1][3])
                            print (' Pending loan->',dict1[id1][7])
                            if dict1[id1][9][0]!=0 and dict1[id1][9][1]!=0:
                                print()
                                print('Credit card number->',dict1[id1][9][0])
                                print('Pin Code->',dict1[id1][9][1])
                                print()

                            else:
                                print()
                                print('->Credit card not issued!<-')

                            if dict1[id1][8][0]!=0 and dict1[id1][8][1]!=0:
                                print()
                                print('Debit card number->',dict1[id1][8][0])
                                print('Pin Code->',dict1[id1][8][1])
                                print()

                            else:
                                print()
                                print('->Debit card not issued!<-')
                                print() 

                                      
                        elif choice4==3:                                            #Deleting account
                          while True:   
                           print("-Are you sure you wish to delete your Account-")
                           print()
                           print("-Yes or No-")
                           print()
                           choose=input("Enter your choice-")
                           print()
                           if choose.lower()=='yes':
                            f=open("customer0.dat","rb")
                            dict1=pickle.load(f)
                            f.close()
                            f=open("customer0.dat","wb")
                            del dict1[id1]
                            pickle.dump(dict1,f)
                            f.close()
                            print()
                            print ('-Your Account has successfully been deleted!-')
                            break
                        
                           elif choose.lower()=='no':
                               break
                            
                           else:
                               print()
                               print("-----------------------")
                               print()
                               print("-Please make a choice!-")
                               print()
                          if choose.lower()=='yes':
                              break
                        
                        elif choice4==4:                                            #Transferring money
                            print()
                            print("-Available Accounts-")
                            print()
                            f111=open("customer0.dat","rb")
                            d=pickle.load(f111)
                            cnt=1
                            for item in d:
                              print("  ",cnt,"-",item)
                              cnt+=1
                            print()
                            f111.close()
                            
                            f=open("customer0.dat","rb")
                            dict1=pickle.load(f)
                            f.close()
                            id2=int(input('Enter the account to which money is to be transferred- '))
                            print()
                            if id2 in dict1.keys():
                                print()
                                transfer=int(input('Enter the amount to be transferred- '))
                                if dict1[id1][3]>=transfer:
                                    dict1[id2][3]+=transfer
                                    dict1[id1][3]-=transfer
                                    print()
                                    print ('-Money transferred-')
                                    print()
                                    ft=open("transaction.txt","a")                                 #text file
                                    lt=list(range(3))
                                    lt[0]='Transferrer\'s ID-'+str(id1)+'#'
                                    lt[1]='Receiver\'s ID-'+str(id2)+'#'
                                    lt[2]='Money transferred-'+str(transfer)+'$$'
                                    ft.writelines(lt)
                                                                        
                                    ft.close()
                                  
                                  
                                  
                                else:
                                    print()
                                    print ('-Insufficient balance!-')
                                    print()
                            else:
                                print()
                                print ('-Account doesn\'t exist!-')
                                print()
                              

                            f=open("customer0.dat","wb")
                            pickle.dump(dict1,f)
                            f.close()
                            print()

                        elif choice4==5:                                            #Depositing money
                            f=open("customer0.dat","rb")
                            dict1=pickle.load(f)
                            f.close()
                            
                            depo=input('Enter the amount to be deposited- ')
                            if depo.isdigit():
                                dep=int(depo)
                                
                                dict1[id1][3]+=dep
                                ft=open("transaction.txt","a")                                          #text file
                            
                            
                                lt=list(range(2))
                                lt[0]='ID-'+str(id1)+'#'
                                lt[1]='Amount deposited-'+str(dep)+'$$'
                                ft.writelines(lt)
                                ft.close()
                                print()
                                print ('-Money deposited-')
                                f=open("customer0.dat","wb")
                                pickle.dump(dict1,f)
                                f.close()
                                print()
                            else:
                                print()
                                print("-Please try again-")
                                print()

                        elif choice4==6:                                        #Withdrawing money  
                            f=open("customer0.dat","rb")
                            dict1=pickle.load(f)
                            f.close()
                            withdraws=input('Enter the amount to be withdrawn- ')
                            if withdraws.isdigit():
                                withdraw=int(withdraws)
                                f1=open("customer0.dat","rb")
                                d1=pickle.load(f1)
                                s=d1[id1][3]
                                if s>withdraw:
                                    dict1[id1][3]-=withdraw
                                    print()
                                    ft=open("transaction.txt","a")                                          #text file
                            
                                    lt=list(range(2))
                                    lt[0]='ID-'+str(id1)+'#'
                                    lt[1]='Amount withdrawn-'+str(withdraw)+'$$'
                                    ft.writelines(lt)
                                    ft.close()
                                    print ('-Money withdrawn-')
                                    f=open("customer0.dat","wb")
                                    pickle.dump(dict1,f)
                                    f.close()
                                    print()
                                else:
                                    print()
                                    print("-Insufficient Balance!-")
                                    print()

                            else:
                                print()
                                print("-Please try again-")
                                print()    

                        elif choice4==7:                                            #Applying for loan
                           f1=open("bankdetails0.dat","rb")
                            
                           bank1=pickle.load(f1)
                           f1.close()
                           print()
                           print ('\t\t\t\t_______Loan Menu_________')
                           print ('\t\t\t\t1 >> Student loan')
                           print ('\t\t\t\t2 >> Mortgage loan')
                           print ('\t\t\t\t3 >> Small bussiness loan')
                           print ('\t\t\t\t4 >> Automobile loan')
                           print ('\t\t\t\t5 >> Personal loan')
                           print ('\t\t\t\t6 >> Exit')
                           print()

                           choice50=input('Enter your choice- ')
                           if choice50.isdigit():
                            choice5=int(choice50)
                            
                            if choice5==1:                    #Student loan(Only for Student category)
                                f=open("customer0.dat","rb")
                                dict1=pickle.load(f)
                                f.close()
                                if dict1[id1][2].lower()=='student':
                                    print()
                                    tem=bank1[123456789][2]
                                    print ('Interest will be compounded quarterly at',tem,'% rate.Maximum amount to be borrowed is twice the school fees per annum for a minimum time period of one year.Do you agree to the terms?(y/n) ')
                                    print()
                                    choice66=input('Enter your choice- ')
                                    print()
                                    if choice66.lower()=='y':
                                        fee=int(input('Enter the school fee per annum- '))
                                        amount=int(input('Enter the amount to be borrowed- '))
                                        time=int(input('Enter the time period(in years)- '))
                                        if amount<=fee:
                                            print ('loan is granted..')
                                            print()
                                            print ('Amount to be repaid:',(amount)+(amount*(float((bank1[123456789][2]))/100+1)**(time*4.0)))
                                            dict1[id1][7]+=(amount)+(amount*(float((bank1[123456789][2]))/100+1)**(time*4.0))
                                            ft=open("transaction.txt","a")

                                            lt=list(range(3))                                    
                                            lt[0]='ID-'+str(id1)+'#'
                                            lt[1]='type of loan-student'+'#'
                                            lt[2]='Amount taken-'+str(amount)+'$$'
                                            ft.writelines(lt)
                                            ft.close()                                       
                                            f=open("customer0.dat","wb")
                                            pickle.dump(dict1,f)
                                            f.close()
                                        else:
                                            print()
                                            print ('--Amount requested is not as per accepted criteria!--')

                                else:
                                    print()
                                    print ('-elligible!-')
                                    print()

                            elif choice5==2:                                          #Mortgage loan(Only for General category)
                                f=open("customer0.dat","rb")
                                dict1=pickle.load(f)
                                f.close()
                                if dict1[id1][2].lower()=='general':
                                    print()
                                    tem=bank1[123456789][1]
                                        
                                    print ('Interest will be compounded quarterly at',tem,'% rate.Maximum amount to be borrowed is half the value of the asset submitted to the bank for a minimum time period of one year.Do you agree to the terms?(y/n) ')
                                    print()
                                    choice66=input('Enter your choice- ')
                                    print()
                                    if choice66.lower()=='y':
                                        asset=int(input('Enter the value of the asset- '))
                                        amount=int(input('Enter the amount to be borrowed- '))
                                        time=int(input('Enter the time period(in years)- '))
                                        if amount<=(0.5*asset):
                                            print ('loan is granted..')
                                            print()
                                            print ('Amount to be repaid:',(amount)+(amount*(float((bank1[123456789][1]))/100+1)**(time*4.0)))
                                            dict1[id1][7]+=(amount)+(amount*(float((bank1[123456789][1]))/100+1)**(time*4.0))
                                            ft=open("transaction.txt","a")                                          #text file                            
                                            lt=list(range(3))                                     
                                            lt[0]='id-'+str(id1)+'#'
                                            lt[1]='type of loan-mortgage'+'#'
                                            lt[2]='Amount taken-'+str(amount)+'$$'
                                            ft.writelines(lt)
                                            ft.close()  
                                            f=open("customer0.dat","wb")
                                            pickle.dump(dict1,f)
                                            f.close()
                                        else:
                                            print()
                                            print ('--Amount requested is not as per accepted criteria!--')
                                else:
                                    print()
                                    print ('-You are not elligible!-')
                                    print()

                            elif choice5==3:                            #Small business loan(Only for General Category)
                                f=open("customer0.dat","rb")
                                dict1=pickle.load(f)
                                f.close()
                                if dict1[id1][2].lower()=='general':
                                    print()
                                    tem=bank1[123456789][4]
                                        
                                    print ('Interest will be compounded quarterly at',tem,'% rate.Maximum amount to be borrowed is half the value of the asset submitted to the bank for a minimum time period of one year.Do you agree to the terms?(y/n) ')
                                    print()
                                    choice66=input('Enter your choice- ')
                                    print()                 
                                    if choice66.lower()=='y':
                                        asset=int(input('Enter the value of the asset- '))
                                        amount=int(input('Enter the amount to be borrowed- '))
                                        time=int(input('Enter the time period(in years)- '))
                                        if amount<=(0.5*asset):
                                            print ('loan is granted..')
                                            print()
                                            print ('Amount to be repaid:',(amount)+(amount*(float((bank1[123456789][4]))/100+1)**(time*4.0)))
                                            dict1[id1][7]+=(amount)+(amount*(float((bank1[123456789][4]))/100+1)**(time*4.0))
                                            ft=open("transaction.txt","a")              #text file
                                                
                                            lt=list(range(3))                                  
                                            lt[0]='id-'+str(id1)+'#'
                                            lt[1]='type of loan-small bussiness loan'+'#'
                                            lt[2]='Amount taken-'+str(amount)+'$$'
                                            ft.writelines(lt)
                                            ft.close()  
                                            f=open("customer0.dat","wb")
                                            pickle.dump(dict1,f)
                                            f.close()
                                        else:
                                            print()
                                            print ('--Amount requested is not as per accepted criteria!--')

                                else:
                                    print()
                                    print ('-You are not elligible!-')
                                    print()
                                         
                            elif choice5==4:                          #Automobile loan(Only for General Category)
                                f=open("customer0.dat","rb")
                                dict1=pickle.load(f)
                                f.close()
                                if dict1[id1][2].lower()=='general':
                                    print()
                                    tem=bank1[123456789][3]
                                        
                                    print ('Interest will be compounded quarterly at',tem,'% rate.Maximum amount to be borrowed is half the value of the asset submitted to the bank for a minimum time period of one year.Do you agree to the terms?(y/n) ')
                                    print()
                                    choice66=input('Enter your choice- ')
                                    print()                
                                    if choice66.lower()=='y':
                                     asset=int(input('Enter the value of the asset- '))
                                     amount=int(input('Enter the amount to be borrowed- '))
                                     time=int(input('Enter the time period(in years)- '))
                                     if amount<=(0.5*asset):
                                        print ('loan is granted..')
                                        print
                                        print ('Amount to be repaid:',(amount)+(amount*(float((bank1[123456789][3]))/100+1)**(time*4.0)))
                                        dict1[id1][7]+=(amount)+(amount*(float((bank1[123456789][3]))/100+1)**(time*4.0))
                                        ft=open("transaction.txt","a")                                          #text file
                                                
                                        lt=list(range(3))                                    
                                        lt[0]='id-'+str(id1)+'#'
                                        lt[1]='type of loan-automobile loan'+'#'
                                        lt[2]='Amount taken-'+str(amount)+'$$'
                                        ft.writelines(lt)
                                        ft.close()  
                                        f=open("customer0.dat","wb")
                                        pickle.dump(dict1,f)
                                        f.close()
                                     else:
                                         print()
                                         print ('--Amount requested is not as per accepted criteria!--')

                                else:
                                    print()
                                    print ('-You are not elligible!-' )
                                    print()
                                          
                            elif choice5==5:             #Personal loan(Only for General Category)
                                f=open("customer0.dat","rb")
                                dict1=pickle.load(f)
                                f.close()
                                if dict1[id1][2].lower()=='general':
                                    print()
                                    tem=bank1[123456789][5]
                                        
                                    print ('Interest will be compounded quarterly at',tem,'% rate.Maximum amount to be borrowed is half the value of the asset submitted to the bank for a minimum time period of one year.Do you agree to the terms?(y/n) ')
                                    print()
                                    choice66=input('Enter your choice- ')
                                    print()              
                                    if choice66.lower()=='y':
                                        asset=int(input('Enter the value of the asset- '))
                                        amount=int(input('Enter the amount to be borrowed- '))
                                        time=int(input('Enter the time period(in years)- '))
                                        if amount<=(0.5*asset):
                                            print ('loan is granted..')
                                            print
                                            print ('Amount to be repaid:',(amount)+(amount*(float((bank1[123456789][5]))/100+1)**(time*4.0)))
                                            dict1[id1][7]+=(amount)+(amount*(float((bank1[123456789][5]))/100+1)**(time*4.0))
                                            ft=open("transaction.txt","a")                                          #text file
                                                
                                            lt=list(range(3))
                                            lt[0]='id-'+str(id1)+'#'
                                            lt[1]='type of loan-personal'+'#'
                                            lt[2]='Amount taken-'+str(amount)+'$$'
                                            ft.writelines(lt)
                                            ft.close()  
                                            f=open("customer0.dat","wb")
                                            pickle.dump(dict1,f)
                                            f.close()
                                        else:
                                           print()
                                           print ('--Amount requested is not as per accepted criteria!--')

                                else:
                                    print()
                                    print ('-You are not elligible!-')
                                    print()
                                    
                            elif choice5==6:
                                while True:
                                    break

                            else:
                                print()
                                print("-Invalid option123-")
                                print()
                            

                        elif choice4==8:                      #Repayment of loan
                           print()
                           try: 
                            f=open("customer0.dat","rb")
                            dict1=pickle.load(f)
                            f.close()
                            repay=int(input('Enter amount paid- '))                
                            if repay>dict1[id1][7]:
                                print()
                                print ('-----------Receipt-----------')
                                print ('Name->          ',dict1[id1][0])
                                print ('Amount paid->   ',dict1[id1][7])
                                print ('Balance amount->',repay-dict1[id1][7])
                                print ('-----------------------------')
                                print()
                                ft=open("transaction.txt","a")           #text file
                                                
                                lt=list(range(2))                         
                                lt[0]='id-'+str(id1)+'#'
                                lt[1]='amount of loan repaid-'+str(dict1[id1][7])+'$$'
                                ft.writelines(lt)
                                ft.close()  
                                f=open("customer0.dat","rb")
                                dict2=pickle.load(f)
                                f.close()
                                dict2[id1][7]=0
                                dict1=dict2
                                f=open("customer0.dat","wb")
                                pickle.dump(dict1,f)
                                f.close()
                                       
                            else:
                                print()
                                print ('-----------Receipt------------')
                                print ('Name->          ',dict1[id1][0])
                                print ('Amount paid->   ',repay)
                                print ('Balance amount->',0.0)
                                print ('Pending loan->  ',dict1[id1][7]-repay)
                                print()
                                ft=open("transaction.txt","a")           #text file
                                                
                                lt=list(range(2))                                           
                                lt[0]='id-'+str(id1)+'#'
                                lt[1]='amount of loan repaid-'+str(repay)+'$$'
                                ft.writelines(lt)
                                ft.close()
                                f=open("customer0.dat","rb")
                                dict2=pickle.load(f)
                                f.close()
                                dict2[id1][7]=(dict1[id1][7]-repay)
                                dict1=dict2
                                f=open("customer0.dat","wb")
                                pickle.dump(dict1,f)
                                f.close()
                                print()

                           except:
                               print("-No loan to repay!-")

                        elif choice4==9:                                 #Issuing credit card
                            f=open("customer0.dat","rb")
                            dict1=pickle.load(f)
                            f1=open("bankdetails0.dat","rb")
                            m=pickle.load(f1)
                    
                            f1.close()
                            f.close()
                            
                            if dict1[id1][2].lower()=='general':
                                print ('Credit card will be issued on an interest rate of',m[123456789][6],'%. Do you agree to the terms and conditions(y/n)?')
                                print()
                                c=input('Enter your choice-')
                                if c.lower()=='y':
                                    
                                   dict1[id1][9][0]=(random.randint(1000000000000000,10000000000000000))
                                   dict1[id1][9][1]=(random.randint(1000,10000))
                                   print('\nCredit card  issued\n')
                                   print()
                                   print ('Card Number->',dict1[id1][9][0])
                                   print ('Pin Code->   ',dict1[id1][9][1])
                                   ft=open("transaction.txt","a")                  #text file
                                                
                                   lt=list(range(2))                                             
                                   lt[0]='id-'+str(id1)+'#'
                                   lt[1]='Credit card issued'+'$$'
                                   ft.writelines(lt)
                                   ft.close() 
                                   f=open("customer0.dat","wb")
                                   pickle.dump(dict1,f)
                                   f.close()

                            else:
                                print()
                                print ('-You are not eligible!-')
                                print()

                        elif choice4==10:                     #Issuing debit card
                            f=open("customer0.dat","rb")
                            dict1=pickle.load(f)
                            f1=open("bankdetails0.dat","rb")
                            m=pickle.load(f1)
                    
                            f1.close()
                            f.close()
                            
                            if dict1[id1][2].lower()=='general':
                                print ('Debit card will be issued on the criteria that maximum amount that can be withdrawn per day is',m[123456789][7],'Do you agree to the terms and conditions(y/n)?')
                                print()
                                c=input('Enter your choice-')
                                if c.lower()=='y':
                                  f=open("customer0.dat","rb")
                                  dict1=pickle.load(f)
                                  dict1[id1][8][0]=(random.randint(1000000000000000,10000000000000000))
                                  dict1[id1][8][1]=(dict1[id1][9][1])
                                  print ('\n-Debit card successfully issued-\n')
                                  print()
                                  print ('Card Number->',dict1[id1][8][0])
                                  print ('Pin Code->   ',dict1[id1][8][1])
                                  ft=open("transaction.txt","a")                                            #text file
                                                
                                  lt=list(range(2))                                           
                                  lt[0]='id-'+str(id1)+'#'
                                  lt[1]='Debit card issued'+'$$'
                                  ft.writelines(lt)
                                  ft.close()
                                  f=open("customer0.dat","wb")
                                  pickle.dump(dict1,f)
                                  f.close()

                            else:
                                print()
                                print ('-You are not eligible!-')
                                print()
                                                       

                        elif choice4==11:                              #Logging out
                            print()
                            print("--You Have been Successfully logged out of the system!--")
                            print()
                            break
                            
                        else:
                            print()
                            print ("-Invalid Option!-")
                            print()

                       else:
                           print()
                           print("-Invalid option!-")
                           print()

                     else:
                         print()
                         print("--Wrong Password!--")
                         print()
                                
                   else:
                         print()
                         print("-Account doesn't exist!-")
                         print("-Please register an Account first to log in!-")
                         print()     
                     
            elif choice3==2:                    #Registering for new account

                s=customer()
                s.customer_details(0)
                dict_customer={}

                dict_customer[s.cust_id]=[s.cust_name,s.cust_email,s.cust_category,s.cust_balance,s.cust_dep,s.cust_withdraw,s.cust_transfer,s.cust_loan,s.cust_debit,s.cust_credit,s.passw]
                
                try:
                    f=open("customer0.dat","rb")
                    m=pickle.load(f)
                    f.close()
                    m.update(dict_customer)
                    f=open("customer0.dat","wb")
                    pickle.dump(m,f)
                    f.close()
                    
                except:
                    f=open("customer0.dat","wb")
                    pickle.dump(dict_customer,f)
                    f.close()

                print()  
                print ('Thank you for registering..')
                print()
                print()

            elif choice3==3:
                break

            else:
                print()
                print("-Invalid option!-")

           else:
               print()
               print("-Invalid option!-")
               print()

       elif choice==3:
            print ('Exiting..')
            exit()

       else:
            print()
            print("-Invalid option!ddd-")
            while True:
                break

      else:
           print()
           print("-Invalid option!-")

main() 