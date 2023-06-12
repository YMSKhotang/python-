#variables
'''
Variables are the names which stores the value.
eg: susam = 9
'''


name="merisha"
grade=6
students_of_grade6 = 16.5
allPass = False

#data type
'''
print(type(name))
print(type(grade))
print(type(students_of_grade6))
print(type(allPass))
'''

#operators
#1. Arithmetic operators  +,-,/,*,%,**
#2. Comparision(relatives) operators ==,!=, >,>=,<,<=
#3. Logical operators not, and, or

#if else statements
'''
age =15

if age > 12:
    print("hhgggggn")
else:
    print('bbbbbb')

    '''
#Input methods

#strings
'''
name = input('enter your name: ')
print('my name is' + name)
'''

#integer 
'''
age=int(input('enter your age: '))
print( age)
'''

'''
# for string(str)
newMember = input('enter a name:')
print('my name is' + newMember)

# for integer(int)
num = int(input('enter a number:'))
print('the given number is' + num)
'''


#1. write a program to check a number is positive or negative.
'''
num=int(input('enter a number: '))
print( num)

if num > 0:
    print('number is positive')
else:
    print('negative')
    '''

#2.write a program to input the marks of three subject and find its total. 
#3.write a program to input the marks of three subject and find its total & average.
#4.write a program to input the marks of three subject and check whether a student is pass
#  or fail.
#5. write a program to find simple interest. [SI = (principal * time * rate ) / 100]
#6. write a program to input two different number and find out the greatest number.
#7. write a program to input two different number and find out the smaller number.
#8. write a program to input two differt numbers then find sum, products and difference.
#9. write a program to  check whether a number is positive or negative.
# 

 

'''
num1=int(input('enter first number:  '))
num2=int(input('enter second number:  '))

sum= num1 + num2
print(sum)

product= num1 * num2
print(product)

difference = num1 - num2
print(difference)
'''



#Tofas practice
'''
productPrice =1200

print("Items over 1000 yen are 50 percent off !!")

if productPrice > 1000:
    print('so items are half price')

'''
'''
apple=12
orange=7

if apple>orange :
    print('more apples')
else:
    print('more oranges')
'''

#practice
'''
time=12


if time>12:
    print('i am hungry right now')

if time <11:
    print('its third period')
else:
    print('second period')

print('learning python')

'''

#if elif else
#write a program to check whether a number is positive, negative or zero.
'''
num=int(input('enter a number:  '))

if num > 0:
    print('number is positive')
elif num ==0:
    print('the number is zero')
else:
    print('number is negative')
'''

#practice questions for students
# write the outputs of the following programs.
books=9
price=135
money=1500

money=money -books*price

if money !=0 :
    print('i can buy chocolates')
else:
    print('i dont have any money')
