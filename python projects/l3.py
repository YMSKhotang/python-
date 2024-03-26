
# Tofas level 3  Questions:
#1. Write the output of the following program:

def student(name,age):
    print('my name is' + name + 'and my age is ' + age)

student('verygood', '12')
student('sabitra', '14')
student('deepa','14')

# Q.2 Write the output of the following program:
def side():
    if False:
        print('to the right of the bookstore')
    else:
        print('to the left of the floorsheet')

print('the post office is')
side()

#Q.3 Write the output of the following program:

def say(word):
    print(word + '!')
    
if False:
    a = 'welcome'
else:
    a = 'thank you'
    
say(a) 

#Q.5 Write the output of the following program:

def discount():
    print('sanjeev get a discount')
    return 230

price=1000

price=price-discount()

print('the price after discount is' + str(price))

#Q.6 Write the output of the following program:

def order(num):
    total=0
    for i in range(0,num):
        total=total+prices[i]
    return total
    
menuList=['pizza','momo','thakali khana']
prices=[500,200,900]
menuCount=0

for menu in menuList:
    print(menu)
    menuCount=menuCount+1
print("that's" + str(menuCount) + "item(s) for a total of" + str(order(menuCount)) + 'yen')

#Q.7 Write the output of the following program:

age=30
name='kedar'
print(name + str(age) + ' years old.')

#Q.8 Write the output of the following program:

def agedifference(age1,age2):
    fatherAge =30
    total=age1+age2

    if int(total)<fatherAge:
        return fatherAge - int(total)
    else:
        return int(total)-fatherAge
    
suprince=6
supriya=2
difference=agedifference(suprince,supriya)
print("the age diff. is"+str(difference) + "year(s)")

#Q.9 Write the output of the following program:

def add(num1,num2):
    text='calculated result'
    return num1+num2

text='is the answer'
ans=add(5,7)
print(str(ans) + text)


#Q.10 Write the output of the following program:

def sumTotal():
    total=food+drink
    print('total is' + str(total))
    

food=1200
drink=500
if True:
    sumTotal()

#Q.11 Write the output of the following program:

def comparison(num1,num2):
    if num1>num2:
        maxNum=num1
    else:
        maxNum=num2

    print(maxNum)

comparison(120,80)

#Q.12 Write the output of the following program:

def total():
    paisa1="170"
    paisa2="330"

    return int(paisa1) + int(paisa2)

print('I have ' + str(total()) + 'money')


#Q.13 Write the output of the following program:
def connect(text1, text2):
    return text1 + text2

day=str(1)+str(5)
text='is fifteen '

print(connect(day, text))


#Q.14 Write the output of the following program:
def output():
    for name in names:
        print(name)
names=['Abhi','bibek','samir']
print(str(len(names)))
output()

#15. Write the output of the following program:

import random 
import math

number = random.random()
result = math.floor(number *10 + 1)

if True:
    print(result)
else:
    print(number)

#16. Write the output of the following program:
import random 
import math

def output(name):
    num=math.floor(random.random() * 2)

    if num == 0:
        print(name + 'is 60 years old')
    else:
        print(name + 'is 170 cm tall')
    # for minimum value of random.random() i.e  0.1
    #num = math.floor(0.1 *2) = math.floor(0.2) = 0 
    # output is  -->  sonam is 60 years old

    # for maximum value of random.random() i.e  0.9
    #num = math.floor(0.9 *2) = math.floor(1.8) = 1
    # output is  -->  sonam is 170 cm tall

output('Sonam')

#17. Write the output of the following program:

import random 
import math

def add(num):
    number = 1
    print(number + num)

random = math.floor(random.random()*10)
#random = 1
#random = 9
add(random)

#ans_ 2 to 10

#18. Write the output of the following program:
import random
import math
randNum = '' 

for i in range(0,3):
    randNum = randNum + str(math.floor(random.random() * 9) +1 )
    #randNum = '' + '1' ==> '1'
    #randNum = '1' + '1'==> '11'
    #randNum = '11' + '1' ==>'111'


    #randNum = '' + '9'  => '9'
    #randNum = '9' + '9' ==>'99'
    #randNum = '99' + '9' ==>'999'

print(randNum)

#19. Write the output of the following program:
import random
import math
def createRandom():
    num = math.floor(random.random()*10) + 1
    return num

ans = 0
arr = [1,2,3]
randNum = createRandom()

for element in arr:
    ans = ans + element * randNum 

print(ans)


    #ans = 0 + 1 * 2 --> 2
    #ans = 2 + 2* 2 --> 6
    #ans = 6 + 3* 2 --> 12

     #ans = 0 + 1 * 10 --> 10
      #ans = 10 + 2 * 10 --> 30
       #ans = 30 + 3 * 10 --> 60









# ~~~~~~~~~~~~~~~~~~~ RANDOM NUMBERS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

'''
a=''
for i in range(0,3):
    a=  a+ str(math.floor(random.random() * 9) +1)
print(a)
'''







