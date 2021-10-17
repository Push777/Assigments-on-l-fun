class book_my_show:
    def __init__(self):
        
        print("welcome to book my show,book your ticket and enjoy your Show")
        self.row= input('enter the number of row :' );
        self.coloum= input('enter the number of coloum :' );
        self.s=[0]*int(self.row);
        self.t=[' ']+[str(i+1) for i in range(int(self.coloum))];
        for i in range(int(self.row)):
            self.s[i]=[str(i+1)]+['v']*int(self.coloum);
            
        # calculating Total income and making current income zero
        if int(self.row)*int(self.coloum)<=60:
            self.total=10*int(self.row)*int(self.coloum)
            if int(self.row)*int(self.coloum)>=60:
                if int(self.row)%2==0:
                    self.total=10*(self.row)*(self.coloum)
            else:
                f=(int(self.row)//2)
                self.total=(8*f*int(self.coloum))+(10*(int(self.coloum)-f)*int(self.coloum))
        self.currentincome=0
        self.userinfo= {}
        self.options()
    
    def options(self):
        print('/n')
        print('Select your option')
        print('1. Show the seats')
        print('2.Buy a Ticket')
        print('3.Statistics')
        print('4.Show booked ticket user Info')
        print('0.Exit')
        print('Type corresponding option number for selecting your Option')
        print('===========================')
        
        x=input()
        if x=='1':
            self.showtickets()
        elif x=='2':
            self.buyticket()
        elif x=='3':
            self.statistics()
        elif x=='4':
            self.show_booked_ticket_n_userinfo()
        elif x==0:
            Exit()
        
        else:
            print('choose your Option')
            self.options()
            
    def showtickets(self):
        print('/n')
        print('cinema: ')
        print(' '.join(self.t))
        for i in self.s:
            print(' '.join(i))
        print('/n')
        print(['v= Vacant              B=Booked/n'])
        
        self.options()
        
    def buyticket(self):
        print('\n')
        x1=input('Row Number :')
        x2=input('Coloum Number :')
        
        price=0
        
        if int(self.row)*int(self.coloum)<=60:
            price= 10
        if int(self.row)*int(self.coloum)>=60:
            if int(x1)>int(self.row)/2:
                price = 8
            if int(x1)<=int(self.row)/2:
                price=10
                
        print('\n')
        print('price for the seat is '+str(price))
        print('\n')
        print('would you like to proceed')
        print('type "yes"for Booking \n "no" for options')
        yorn=input()
        if yorn=='yes':
            self.currentincome+=price
            self.userinfo[x1+x2]={}
            print('\n')
            self.userinfo[x1+x2]['Name']=input('Name - ')
        
            self.userinfo[x1+x2]['Gender']=input('Gender - ')
            if self.userinfo[x1+x2]['Gender']=='M'or self.userinfo[x1+x2]['Gender']=='F' or self.userinfo[x1+x2]['Gender']=='m' or self.userinfo[x1+x2]['Gender']=='f':
                pass
            else:
                print('Type correct Gender')
                self.userinfo[x1+x2]['Gender']=input('Gender - ')
                
            self.userinfo[x1+x2]['Age']=input('Age - ')
            if self.userinfo[x1+x2]['Age'].isnumeric() and int(self.userinfo[x1+x2]['Age'])>=0 and int(self.userinfo[x1+x2]['Age'])<=100:
                pass
            else:
                print('Type correct Age')
                self.userinfo[x1+x2]['Age']=input('Age - ')
            self.userinfo[x1+x2]['TicketPrice']=price
            
            self.userinfo[x1+x2]['Phone no']=input('Phone no - ')
            if self.userinfo[x1+x2]['Phone no'].isnumeric() and len(self.userinfo[x1+x2]['Phone no'])==10:
                pass
            else:
                print('Number is Invalied')
                self.userinfo[x1+x2]['Phone no']=input('Phone no - ')
                
            print('Ticket Booked Sucessfully')
            self.s[int(x1)-1][int(x2)]='B'
            if yorn=='no':
                print('\n')
                print('Thank you')
            self.options()
            
    def statistics(self):
        print('\n')
        print('Number of Purches Tickets : '+str(len(self.userinfo)))
        print('Percentage : ',str((self.currentincome*100)/self.total)+'%')
        print('current Income : ','$'+str (self.currentincome))
        print('Total Income : ','$'+str(self.total))
        print('******************************')
        print('\n')
        
        self.options()
        
    def show_booked_ticket_n_userinfo(self):
        print('\n')
        if len(self.userinfo)==0:
            print('Movie Theater is Completely Vacant :(')
            self.options()
            
        i=input('Row Number : ')
        j=input('Coloum Number : ')
        if i+j in self.userinfo:
            print('/n')
            
            print('Name : ',self.userinfo[i+j]['Name'])
            print('Gender : ',self.userinfo[i+j]['Gender'])
            print('Age : ',self.userinfo[i+j]['Age'])
            print('TicketPrice : ','$'+str(self.userinfo[i+j]['Gender']))
            print('Phone no : ',self.userinfo[i+j]['Phone no'])
            print('******************************************')
            print('\n')
            
        else:
            print('\n')
            print(i+j+' is not booked yet')
            
        self.options()
        
    def exit(self):
        pass
    
x=book_my_show()

    
            
            
                 
         
            
        
        
            
