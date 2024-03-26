#print("my name is don didi")

name = 'don'
last_name='didi'
#concatinate
#print(name + last_name)

# repeat
#print(name * 5)
 

#data types 
'''
1. string --> str  
ex:- "apple"

2. integer --> int
ex:- 510

3. Floating number  --> float
ex:- 4.7

4. Boolean  --> bool
ex:- True, False
'''

age = 13.7
present = False


#print(age)

# how to find out data type
'''print(type(name))
print(type(age))
print(type(present)) '''

#list # mutable/changeable
'''
vowel1=['a','e','i','o','u', 5, 7.9, False]
print(vowel1)

vowel1 '''

#Tuples # not changeable
'''vowel2=('a','e','i','o', 'u')
print(vowel2) '''

#list method 
abc=[1,4,7,3,5,2,6]
#print(abc)

#append(data) --> add the item at last
'''abc.append(8)
print(abc) '''

#sort()  --> keep the data in a sequence
'''abc.sort()
print (abc) '''

#reverse()
'''abc.reverse()
print(abc) '''

#insert(index, data) --> add data at desire location or position inside list
abc.insert(2, 10)
#print(abc)

#pop(index) --> remove data of last index
abc.pop()

#remove(data) -->
abc.remove(10)
#print(abc)

#Dictionary
'''dict={'key':'value'}

grade9 = {'id1':'aaisa','id2':'bhawana','id3':'deepa','id4':'hebindra'}

print(grade9['id3']) '''

#operators

#if else
#check whether a number is positive or negative
'''
num=int(input('enter a number:'))

if  num > 0:
    print('positive')
elif num == 0:
    print('the num is zero')



else:
    print('negative')
    '''

#LOOP
#while loop
'''
i=1
while i<11:
   
   i=i+1
   print(i)
'''
#for loop
'''
total=0
weightlist=[50,60,70,80,90]
count=len(weightlist) #--> 5

for i in range(0,count):
    total=total+weightlist[i]
 
    
print(total)
'''


#write a program to input marks in three subjects and check whether
#  a student is passed in all subject or not. [pass marks is 40]
'''
sub1 = int(input('enter your marks in english  '))
sub2 = int(input('enter your marks in maths  '))
sub3= int(input('enter your marks in science  '))

if sub1 >=40 and sub2>=40 and sub3>=40:
    print('pass')
else:
    print('fail')
    '''

#there are more oranges
'''
appleCount = 5
orangeCount = 7

if appleCount > orangeCount :
    print('there are more apples')
else:
    print('there are more oranges')
    '''

# odd or even
'''
M=int(input("enter a number"))
reminder=M%2
if reminder==0:
 print("number is even")
else:
 print("number is odd")

 a=10
 b=6

if a>b:
  print('true')
else:
  print('false')
'''

#level 2
'''
weather = 'cloudy'


if weather != 'sunny':
    print('tha day is not sunny')
else:
    print('the day is sunny')

'''
'''
list = ['a','b','c','d','e','f']

for i in range(0,5):
    print(list[i])
'''
'''
score1 =70
score2 = 60

if score1 >50 and score2>50:
    print('pass')
else:
    print('fail')
'''
'''
num =0 

for i in range(0,5):
    num = num + i
    # num = 0 + 0 = 0
    # num = 0 + 1 = 1
    # num = 1 + 2 = 3
    # num = 3 + 3 = 6 
    #num  = 6 + 4 = 10
    #num  = 10 +5= 15
print(num)
'''
# ouput # grapes # persimmon
'''
stocks=[3,0,5]
fruits=['grapes', 'apple','persimmon']

for i in range(0,3):
    if  stocks[i] !=0:
        print(fruits[i] + '   are in stock')
'''

#tofas question
'''
ages= [10,30,80]
names=['mike','hannah','john']

for i in range(0,3):
    if ages[i]<20 or ages[i]>60:
        print(names[i] + ' can use discounts coupens')
    else:
        print(names[i] + ' cannot use discounts coupens')

'''
#functions
'''
def grade9(firstname, lastname):
    print('my name is ' + firstname + ' ' + lastname)

grade9('khamosh','rai')

def grade10(name):
    return (name) * 5

print(grade10(5))

def sushila():
    print('jishan is clever')

print('hello')
print('its so hot')
print('its over')
sushila()
print('aaisa lai makhhai pardim')
'''
#
'''
def order(num):
    total=0
    for i in range(0,num):
        total= total + prices[i]
    return total


prices=[900,300,700]

menuList=['ramen','potstickers','fried rice']
menuCount =0
for menu in menuList:
    print(menu)
    menuCount=menuCount + 1

print('thats'+ str(menuCount) + 'items for a  total of' + str(order(menuCount)) + 'yen')
'''
#

'''
def comparision(num1,num2):
    if num1>num2:
        maxNum= num1
    else:
        maxNum=num2
    return maxNum

print(comparision(10,100))


'''


#
'''
def output():
    print('you have money left over')

prices = [100,500,100]

money =1000

for i in prices:
    money = money - i
    print(money)
'''

#random integer
import random
import math

#random.randint(0,9) will print random number in range of 0 to 9
grade9= random.randint(1,13)
#print(grade9)

#random.random() will print a random floating number between 0 and 1.
number=random.random()
#print(number)

#math.floor() will rounds a number DOWN to the nearest integer, if necessary,
#  and returns the result.

result=math.floor(number)
#print(result)

'''
import random
import math

a=''

for i in range(0,3):
    a= a + str(math.floor(random.random() *9 +1 ))
    #a = '' + '1'  --> '1'
    #a = '1' + '2' -->  '12'
    #a = '12' + '3' --> '123'   
    
print(a)

'''

hits = [70,100,80,110]
hitCount = 0
maxHits = 0

for i in range (0,4):
    hitCount = hitCount + hits[i]
    #--> hitCount = 0 + 70 --> 70
    #--> hitCount = 70 + 100 --> 170
    #--> hitCount = 170 + 80 --> 250
    #--> hitCount = 290 + 60  --> 310

    if maxHits < hits[i]:
        maxHits = hits[i]

    #  if 0 < 70 :
    #    maxHits = 70

    # if 70 < 100 :
    #   maxHits = 100

    #if 100 < 80:
    #   nothing

    #if 100 < 110:
    #   110


#hitCount= 500
#maxHits = 210
'''
    if maxHits > 200 and hitCount > 400 :
        print('greatest player')
    else:
        print('average player')

    '''

#
'''
def say(susana):
    print(susana + '!')

if False:
    greeting = 'welcome'
else:
    greeting = 'thank you'

say(greeting)

'''
#ggg
'''
def output():
    print('you have money left over')

prices = [100, 500, 1000]
money = 1000

for price in prices:
    money = money - price
    if money > 0:
        print('you have '+ str(money) + 'yen left')
        output()
    else:
        print('i am done shopping')
       ''' 

import random
import math

grade9= random.randint(1,1000)
#print(grade9)

# zero to 1
number=random.random()
#print(number)

#print(math.floor(4.5))

randNum = ' '

for i in range(0,3):
    randNum = randNum + str(math.floor(random.random()* 9) + 1)
    #index 0--> randNum = ' ' +  str(9) --> '9'
    #index 1 --> randNum = '9 ' + str(9)  --> '99'
    #index 2 --> randNum = ' 99' +  str(9)  -> '999'

    print(randNum)





