# Hybrid Inheritance 
'''
class University:
    def __init__(self,uname):
        self.uname=uname
    def detail(self):
        print("University name : ",self.uname)
        
class Course(University):
    def __init__(self,uname,cname):
        University.__init__(self,uname)
        self.cname=cname
        
    def detail(self):
        print(f"I did {self.cname} course from {self.uname}")
        
class Branch(University):
    def __init__(self,uname,branch):
        University.__init__(self,uname)
        self.branch=branch
    def detail(self):
        print(f"I studied {self.branch} from {self.uname}")
        
class Student(Branch,Course):
    def __init__(self,uname,branch, cname,name):
        self.name=name
        Branch.__init__(self,uname,branch)
        Course.__init__(self,uname,cname)
    def detail(self):
        print(f"I am {self.name} of {self.branch} branch and my  course is {self.cname} from {self.uname} university")
        
class Faculty(Branch):
    def detail(self):
        print("faculty")
        
u1=University("MDU")
u1.detail()

c1=Course("MDU","WebDev")
c1.detail()

b1=Branch(" MDU ","CSE")
b1.detail()

s1=Student("MDU","CSE","WebDev","sangam")
s1.detail()
'''



#Output:
'''
University name :  MDU
I did WebDev course from MDU
I studied CSE from  MDU
I am sangam of CSE branch and my  course is WebDev from MDU university

'''

#Assignment
# overload > operator which create a class of 2 person   with name and age. one who is elder going to pay the bill. compare the age of two person.

# method 1 
'''
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    

p1= Person('kedar',31)
p2= Person('Sonam', 25)

if p1.age > p2.age:
    print(f"{p1.name} pays the bill")
else:
    print(f"{p2.name} pays the bill")
'''

#method 2 operator overloading
'''   
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __gt__(self,x):
        if self.age > x.age:
            return True
        else:
            return False

    

p1= Person('kedar',31)
p2= Person('Sonam', 25)

if p1 > p2:
    print(f"{p1.name} pays the bill")
else:
    print(f"{p2.name} pays the bill")

'''

#********** Assignment OOP *********
# Create a Bank Account Class having
#-->  two attributes: Account Holder & Balance
#--> and two methods: Deposit and Withdraw
#Make some deposit and withdraw operations but withdraw amount can not exceed the availiable balance.

class Bank_Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance


    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f" deposited {amount} !!!")

    def withdraw(self,amount):
        if amount<self.balance:
            self.balance = self.balance - amount
            print(f" withdrawn {amount}  !!!")

        else:
            print("Insufficient Balance!")

    # Daunting / magic method ( used to print the object directly)
    def __str__(self):
        return f'Account of {self.name}, Balance={self.balance}'

n1 = Bank_Account('sangam', 500)
print(n1)
n1.deposit(600)
print(n1)
n1.withdraw(900)
print(n1)