#variables
'''
Variables are the names which stores the value.
eg: susam = 9
'''

'''
name="merisha"
grade=6
students_of_grade6 = 16.5
allPass = False
'''
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



#Tofas Test
'''
#1. Write the output of the following program:
productPrice =1230

print("Items over 1000 yen are 50 percent off !!")

if productPrice > 1000:
    print('so items are half price')

#2. Write the output of the following programs:
apple=15
orange=19

if apple>orange :
    print('more apples')
else:
    print('more oranges')

#3. Write the output of the following programs:

time=12

if time>12:
    print('i am hungry right now')

if time <11:
    print('its third period')
else:
    print('second period')

print('learning python')
 
#4. write the outputs of the following program.
books=9
price=135
money=1500

money=money -books*price

if money != 0 :
    print('i can buy chocolates')
else:
    print('i dont have any money')

#Q.5 Write the output of the following program: 
grade = 5

grade=6

print(grade)

#Q.6 Write the output of the following program:
name1 = 'jisan'
name2='tavis'

name1=name2 
print(name2)

#Q.7 Write the output of the following program:
name1 = 'jisan'
name2= 'tavis'

name1=name2
print(name1)

#8. write the output of the following program:
marks = 45
average = 60
if marks > average:
    print('you did well')
else:
    print('try little harder')

#9. write the output of the following program:
num1= 12
num2= 20

num1= num1 + num1
if num1 == num2 :
    print('num1 and num2 are same')
else:
    print('num1 and num2 are different')

#10. Write the output of the following program: 

Address = 'kathamandu'
Address = 'khotang'
print (Address)
print (Address)

#11. Write the output of the following program:

books = 2
if books < 6:
    books = books + 6 
    print('you bought more books')

print(books)

#12. Write the output of the following program:

piece = 4

if piece > 4:
    print('enough')
else:
    print('not enough')
    piece = piece + 1

print(piece)
'''

grade6 = [1,2,3,4]

#for item in grade6:
  # print(item)

#for i in range(0,4):
    #print(grade6[i])

#for i in range(0,11):
    #print(i)

# write a program to print all even numbers from zero to ten. 
#for i in range(1,10,2):
 #   print(i)

'''
# List and Tuples :

List  are the containers to store a set of values of any type. It is mutable(changeable).
Eg: 
L = [ “halesi”, “youme”, 50, False]

L [  : 2 ]  →  “youme”
L [ 1 : 3 ]  →  “youme”, 50

List methods:
		  Consider a list ;

	L1=[1,5,3,7,10,9]

sort():  sorting the data in a sequence
reverse(): reverse the data inside a list
append(data): add the data at last
insert(index, data): add the data in a desired index position
pop():  remove the data placed at last
pop(index): remove the data at given index 
remove(data): remove the given data

AtLast, print(L1) for output after using above method
L1.sort	→  [1,3,5,7,9,10]
L1.reverse 	→  [9,10,7,3,5,1]
L1.append(8)  → adds 8 at the end of the list
L1.insert(3,11)  → add 11 at index 3 –(position, data)	
L1.pop(2)	   →  will remove element at index 2 and returns its value
L1.remove(9)   → remove 9 from the list


'''
# make a report card of your third term exam
# 80 --> distinction
# 60 --> first division
#50 --> second
#40 --> third division
#fail
'''
english = int(input('enter marks of english:'))
computer = int(input('enter marks of computer:'))
math = int(input('enter marks of math:'))



total = english + computer + math

#print(f'the total marks is : {total} ' )

print( 'the total marks is:' + str(total))

average = total / 3
print( 'the average marks is:' + str(average))



if english >=40 and computer>=40 and math>=40:
    print('pass')

    if average>=90:
        print('pass in grade A+ ')
    elif  average>=80:
        print('pass in grade A')
    elif  average>=70:
        print('pass in grade B+')
    elif  average>=60:
        print('pass in grade B')
    elif  average>=50:
        print('pass in grade C+')
    else:
        print('pass in grade C')
        
else:
    print('fail')

'''

name = 'youme'
students = 250

print('my name is ' + name + " and total students is " +  str(students))

print(f" my name is {name} and total students is {students} ")