#function

nicknames='verygood'
def grade9(name,age):
    
    print('my name is' + name + ' and age is ' + age)


gprice=0
price= grade9('verygood', '12')
grade9('sabitra', '14')
grade9('deepa','14')

'''
def grade8(name):
    print('i am ' + name)
grade8('roshan')


def grade7(name):
    return 'i am ' + name
    
print(grade7('khusab'))
'''



# Q.2
'''
def side():
    if False:
        print('to the right of the bookstore')
    else:
        print('to the left of the floorsheet')

print('the post office is')
side()
'''

#Q.3 -->
'''
def say(word):
    print(word + '!')
    
if False:
    a = 'welcome'
else:
    a = 'thank you'
say(a) '''

#Q.5
'''
def discount():
    print('you get a discount')
    return 100

price=1000

price=price-discount()

print('the price after discount is' + str(price))
'''

#Q.6
'''
def order(num):
    total=0
    for i in range(0,num):
        total=total+prices[i]
    return total
    
menuList=['ramen','post sticker','fried rice']
prices=[900,300,700]
menuCount=0

for menu in menuList:
    print(menu)
    menuCount=menuCount+1
print("that's" + str(menuCount) + "item(s) for a total of" + str(order(menuCount)) + 'yen')
'''

#Q.8
''''
age=20
name='sangam'
print(name + str(age) + ' years old.')
'''
#Q.9
'''
def agedifference(age1,age2):
    fatherAge =35
    total=age1+age2

    if int(total)<fatherAge:
        return fatherAge - int(total)
    else:
        return int(total)-fatherAge
    
a=10
b=14
difference=agedifference(a,b)
print("the age diff. is"+str(difference) + "year(s)")
'''
#Q.11
'''
def sumTotal():
    total=food+drink
    print('total is' + str(total))
    

food=700
drink=200
if True:
    sumTotal()
'''
#Q.12
'''
def comparison(num1,num2):
    if num1>num2:
        maxNum=num1
    else:
        maxNum=num2
    print(maxNum)

comparison(10,100)
'''
#
'''
def total():
    str1="100"
    str2="200"
    return int(str1) + int(str2)

print('spent' + str(total()))
'''
#Q.16
'''
def connect(text1, text2):
    return text1 + text2

day=str(1)+str(5)
text='is fifteen '
print(connect(day, text))
'''

#Q.20
'''
def output():
    for name in names:
        print(name)
names=['a','b']
print(str(len(names)))
output()
'''
#random numbers
import random
import math

#random.randint(0,9) will print random number in range of 0 to 9
#print(random.randint(0,9))

#random.random() will print a random floating number between 0 and 1.
number=random.random()
#print(number)

#math.floor() will rounds a number DOWN to the nearest integer, if necessary,
#  and returns the result.
result=math.floor(number*10+1)
#print(result)


