print("1.Admin\n2.User")
x=int(input("Enter 1 For Admin or 2 For User:"))
if x==1:
    print("Welcome Admin For FoodApp")
    print("Please Select an Option:")
    print("'a1':Admin to login\n'a2':Admin to add newitem\n'a3':Admin to see menucard\n'a4':Admin to remove an item\n'a5':Admin to edit an item")
    n=input("Enter a Number:")
if x==2:
    print("Welcome to FoodCourtApp")
    print("Please Select an Option:")
    print("'u1':User For Signup\n'u2':User For Login")
    n=input("Enter a Number:")
class Admin:
    foodlist=[{'id': 1, 'name': 'chicken lolipop', 'quantity': '4 pieces', 'price': 'Rs:300', 'discount': 'Rs:25', 'stock': '200 pieces'},{'id': 2, 'name': 'apple juice', 'quantity': '250 ml', 'price': 'Rs:35', 'discount': 'Rs:4', 'stock': '50000 ml'}]
    dict1={'Admin1':"password147"}
    def adminlogin(self):
        self.username=input("Enter Admin username:")
        self.password=input("Enter Admin Password:")
        if self.username in self.dict1:
            if self.dict1[self.username]==self.password:
                return "login sucessfull"
        else:
            return "Please use UNIQUE username and password for Admin to login in FoodApp\n For Username and Password Please see in Admin.dict1"
    def addingitem(self,na,q,p,d,s):
    	item={'id':len(self.foodlist)+1,'name':na,'quantity':q,'price':p,'discount':d,'stock':s}
	
    	self.foodlist.append(item)
    	print(self.foodlist)
    	return "Item added sucessfully"
        
    def menucard(self):
        print("Item Id : Item :   Quantity  :    Price  :    Discount   :   Stock")
        for i in self.foodlist:
            print(f"{i['id']}. {i['name']} : {i['quantity']} : {i['price']} : {i['discount']} : {i['stock']}")
        
            
    def removeitem(self,n1):
        for i in self.foodlist:
            if i['id']==n1:
                self.foodlist.remove(i)
                print("Menu card After removing an item")
                print(self.foodlist)
                return "Item removed from menu"
        else:
            return "foodId doesnot exit"
        
        
    def editItem(self,n1):
        for i in self.foodlist:
            if i['id']==n1:
                self.na=input("Enter item name:")
                self.q=input("Enter Quantity:")
                self.p=input("Enter Price:")
                self.d=input("Enter Discount:")
                self.s=input("Enter Stock:")
                i['name']=self.na
                i['quantity']=self.q
                i['price']=self.p
                i['discount']=self.d
                i['stock']=self.s
                print("Menu card After Editing An Item")
                for i in self.foodlist:
                    print(i)
                return "Edit an Item is sucessfull"
        else:
            return 'Id doesnot exit'
class user(Admin):
    def __init__(self,foodlist):
        Admin.__init__(self)
    ulist=[{'name': 'mani', 'phonenumber': 8919702354, 'email': 'mani@gmail.com', 'Address': 'k.samudram', 'Password': 'mani@144'},{'name': 'manisankar', 'phonenumber': 7013245319, 'email': 'sankar@gmail.com', 'Address': 'kkr-2', 'Password': 'sankar'}]
    orderedlist=[{'username': 'mani', 'Id': 2, 'name': 'apple juice', 'quantity': 1, 'Amount': 35},{'username': 'mani', 'Id': 1, 'name': 'chicken lolipop', 'quantity': 2, 'Amount': 600}]
    noworderedlist=[]
    def signup(self):
        self.fn=input("Enter FullName:")
        self.ph=int(input("Enter phoneNumber:"))
        self.em=input("Enter Email:")
        self.ad=input("Enter Address:")
        self.pd=input("Enter Password:")
        user={'name':self.fn,'phonenumber':self.ph,'email':self.em,'Address':self.ad,'Password':self.pd}
        self.ulist.append(user)
        print(self.ulist)
        return "signup sucessfully"
    def userlogin(self,u,p):
        for i in self.ulist:
            if i['name']==u and i['Password']==p:
                print("logined sucessfull")
                print("1.place neworder\n2.orderhistory\n3.updateprofile")
                m=int(input("Select An Option:"))
                return m
        else:
            return "Please enter correct credientials to login"
    def placeorder(self,foodlist):
        for i in self.foodlist:
            print("{}.{}({})[INR{}]".format(i['id'],i['name'],i['quantity'],i['price']))
        print("Please select Fooditems from menu card")
        self.n=input("Enter an foodId seperated by comma to place an food item:").split(",")
        self.n=list(map(int,self.n))
        self.na=input("Enter Name:")
        for j in self.n:
            self.q=int(input("Enter Number of Items For FoodId:"))
            for i in self.foodlist:
                if j==i['id']:
                    d={'username':self.na,'Id':i['id'],'name':i['name'],'quantity':self.q,'Amount':(int(i['price'][3:]))*self.q}
                    self.orderedlist.append(d)
                    self.noworderedlist.append(d)
        for i in self.noworderedlist:
            print(i)
        p=input("Enter 'yes' to place order or 'no' not to place order :")
        if p=='yes':
            return "you are placed order"
        if p=='no':
            return "you are not placed order"
    def orderhistory(self):
        self.c=0
        self.username=input("Enter an username:")
        for i in self.orderedlist:
            if i['username']==self.username:
                print(i)
                self.c+=1
        if self.c==0:
            print("username doesnot exist")
            print("Please refer user.orderedlist")
    def updateprofile(self):
        self.c=0
        self.username=input("Enter an username:")
        for i in self.ulist:
            if i['name']==self.username:
                self.na=input("Enter a new name:")
                self.phone=int(input("Enter a newphonenumber:"))
                self.Email=input("Enter a newEmail :")
                self.newaddress=input("Enter a new Address:")
                self.newpassword=input("Enter a new password:")
                i['name']=self.na
                i['phonenumber']=self.phone
                i['email']=self.Email
                i['Address']=self.newaddress
                i['Password']=self.newpassword
                self.c+=1
                print(i)
                print("updated sucessfully")
        if self.c==0:
            print("user doesnot exist")
            print("Please refer user.ulist")
                    
A1=Admin()
u1=user('foodlist')

if n=='a1':
    print("For Admin to login into App use UNIQUE login and password which have given to U")
    print(A1.adminlogin())
if n=='a2':
    na=input("Enter item name:")
    q=input("Enter Quantity:")
    p=input("Enter Price:")
    d=input("Enter Discount:")
    s=input("Enter Stock:")
    print(A1.addingitem(na,q,p,d,s))
if n=='a3':
    A1.menucard()
if n=='a4':
    n1=int(input("Enter an foodId to remove an item from menu:"))
    print(A1.removeitem(n1))
if n=='a5':
    n1=int(input("Enter an foodId to Edit an item from menu:"))
    print(A1.editItem(n1))


if n=='u1':
    print(u1.signup())
if n=='u2':
    u=input("Enter an username:")
    p=input("Enter an password:")
    m1=u1.userlogin(u,p)
    if type(m1)==str:
        print(m1)
        print("Please refer user.ulist and Signup")
    elif m1==1:
        print(u1.placeorder('foodlist'))
    elif m1==2:
        u1.orderhistory()
    elif m1==3:
        u1.updateprofile()
    else:
        print("please select correct option")
else:
    print("please select correct option")
