
#welcome to our new computer lab
''' jhjbv bbvcx
mnbvhjvhjvcxz
hjghgfcx
hgfvc
hgfghfgx
hgvghvxhjghds
hjvhds
'''

#Variable
khusab=nelson=5

grade_7 = 'verygood'
grade_7 ='nelson'
grade_7 ='khusi'
age =9.7

#data type
'''print(type(age))'''

#string concatenation
'''var1='lismika'
var2="rai"
print(var1 + var2)
print(var1*5)'''



#list 
g7=['nelson', 'bibesh','prajwol']

print(g7)

'''
#List methods 
#1. append(data)  --> add items at last
g7.append('roshan')
print(g7)
#2. insert(index, data) --> add the items in your desired position
g7.insert(3,'govinda')
print(g7)
#3. pop()  --> removes the last items in a list
g7.pop()
print(g7)
#4. remove(data) --> reove the metioned item
g7.remove(10)
print(g7)
'''


#tuples
c7=('verygood', 'khusi')

#Dictionary
dict={'key':'value'}
dict1={'khusab':28, 'class':'seven'}

#input
'''a=int(input('enter a number:'))
print(type(a))'''

# output
'''print('it gives us output')'''

#operators
'''
score1 =70
score2= 60

if (score1>50) and (score2>50):
    print('pass')
else:
    print('fail')
'''

# if else
#check whether a number is positive or negative
'''
number = int(input('enter a number:'))


if number >= 0:
    print(' the number is positive')
else:
    print('the number is negative')
    '''


# level 1 practice
'''
apple=5
orange=7
if apple>orange:
    print('more apple')
else:
    print('more oraanges')
    '''

#Q.2
'''
time=8

if time ==8:
    print('good morning')

if time > 7:
    print('i dont eat break fast')


print('i eat breakfast')
print('i go to school at 9 am')

'''
#Q.3
'''
score = 70
average = 65

if  score > average:
    print('try little harder')
else:
    print('you did well')    

    '''

# if elif else
# postive or negative or zero
'''
num=int(input('enter a number'))

if num > 0:
    print('positive')

elif num < 0:
    print('negative')

else:
    print('the num is zero')
'''
'''
time = 8

if time==8:
    print('good morning')

if time >7:
    print('i dont eat breakfast')
else:
    print('i eat breakfast')

print('i go to school at 9 am')
'''
'''
num1= 5
num2 =5
ans = 0

if num1 > num2:
    ans = num1
elif num1 == num2:
    ans = num1 + num2
else:
    ans= num2 

print(ans)
'''

# write a program to check the number is odd or even.
'''
k =int(input("enter a number"))
remainder=k%2
if remainder==0:
    print("even")
else:
    print("odd")
    '''

#write a program to input the marks of three subject and check whether a student is pass
# or fail?

#write a program to input and check whether a number is divisible by three or not?
'''
num=int(input('enter a number: ' ))

reminder = num % 3

if reminder== 0:
    print('divisible')
else:
    print('not divisible')

'''

#loops
#while loop 
'''
i=0
while i<5:
    print(i)
    i=i+1
    #i = 0
    #i=0+1 =1
    #i= 1+1 =2
    #i= 2+1 =3
    #i = 3+1 =4
'''
#For Loops
'''
list=[1,2,3,4,5]
for i in list:
   print(i)
   '''
# range in for loop
'''
for i in range(0,10):
    if i >2 and i<8:
        if  (i!=5):
            print(i)
'''
# write a program to input two different numbers and 
# check whether a number is greater or not.
'''
num1=int(input('enter a first number: '))
num2=int(input('enter a 2nd number: '))

if num1>num2:
    print('first number is greater')
else:
    print('second num is greater')
'''

#Write a program to check whether a student has passed
#  on a computer or not. [pass mark = 40] 


#functions


def grade7(firstName, lastName ):
    print('my name is ' + firstName +' ' + lastName )

grade7('bibesh','rai')


def grade7(total_students):
    return total_students * 10

print(grade7(10))

#talking about git and github