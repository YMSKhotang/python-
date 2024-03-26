'''
class Item:

    pay_rate = 0.8  # the pay rate after 20% discount

    all= []

    def __init__(self, name:str, price:float, quantity=0):

        #Run validations to the received arguments
        assert price >=0, f"price {price} is not greater than or equal to zero !"

        assert quantity >=0, f"quantity {quantity} is not greater than or equal to zero !"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        #Assign to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"
       

item1 = Item("phone", 100, 6)
item1.apply_discount()
print(item1.price)

item2 = Item("laptop", 1000, 2)

print(item1.calculate_total_price())
print(item2.calculate_total_price())

print(Item.all)

for instance in Item.all:
    print(instance.name)


'''

'''
# function
def person(name,age):
    return (name + str(age) )

p1= person('john', 35)
print(p1)



#class --> Always use capital letter while creating a class
class Person:
    x=99  
    y=100

p1=Person()
print(p1.x)


#The __init__() Function
#All classes have a function called __init__(), which is always executed when the class is being initiated. It is also called constructor.It assign values to object properties.
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1)
#print(p1.name)
#print(p1.age)

#The self Parameter
#The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
#It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

# __str__() Function
#The __str__() function controls what should be returned when the class object is represented as a string.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} {self.age}"


p1 = Person("John", 36)

#modifying Objects properties 
#p1.age = 40
p1.name = 'presan'
print(p1)

'''

class Youme:

    def __init__(self, students, activity):
        self.students = students
        self.activity = activity

    def __str__(self):
        return f" total students are {self.students} and main activity is {self.activity}"

abc = Youme(250, 'web development')

print(abc)