# we are learning to use comment in python

'''print('bell ring')
print('i dont like to do homeworks') '''


a="prayog"
#print(a[3])

#list --> changebale --> different data types
list1=['apple', 'ball', 4,10, 7.5, True, False]
#print(list1[1])
#print(len(list1))

#array --> changaebale --> only one data type 
'''import array as arr 
roll_number = arr.array('i',[10,11,12])
print(roll_number)
print(roll_number[2])
'''
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

#tuples --> not changeable
'''abc=('apple', 'cat', 10, 60,)
print(abc[2]) '''

#dictionary
'''dict={'key':'value'}
dict1={'id':1, 'name':'sangam'}

print(dict1['name'])
'''

#operators
#1. arithmetic operator  + - * /
#2. Relative or comparision operator  >, <, >=, <=, ==, !=
# 3. Logical operator and , or , not

#Conditional statements(if else)
#check whether a number is positive or negative or zero.
'''
num=int(input('enter a number:'))

if num > 0:
    print('positive')
elif num < 0:
    print('negative')
else:
    print('zero')
    '''

#check whether a number is odd or even
'''
num=int(input('enter a number:'))

remainder = num % 2

if remainder == 0:
    print('even')
else :
    print('odd')
    '''

#loops
#while loop 
# -->used when you want to repeat a block of code until a certain condition is met
'''
i=0

while i <5: # 0,1,2,3,4
    i=i+1  
    #i=0+1=1
    #i=1+1=2
    #i=2+1=3
    #i=3+1=4
    #i=4+1=5

    print(i)
    
'''


# For Loop
'''
num=0

for i in range(0,5):
    num=num+i
    #num= 0+0=0
    #num= 0+1=1
    #num= 1+2=3
    #num= 3+3=6
    #num= 6+4=10
   
print(num)

'''
'''
grade8=['aamka','anamol','govinda','muna','praasan','prayog','roshan','welcome']

for student in grade8:
    print(student)

for item in range(1,21,2):
    print(item)
    '''
#condition inside for loop
'''
for item in range(1,15):
    if not (item==10) and (item >7):
        print(item)

'''
# break statement 
'''
for i in range(0,20):
    
    if i==5:
        break
    print(i)
    '''

#continue statement
'''
for i in range(0,20):
    
    if i==5:
        continue

    print(i)
    '''
#pass
for i in range(0,20):
    pass

#practice
'''
for i in range(0,10):
    if i>2 and i <8:
        if not i ==5:
            print(i)
'''
#practice
'''
apple = 5
orange = 7

if apple>orange:   
    print('more apples')
else:
    print('more oranges')

    '''
'''
score1 = 70
score2 =40

if score1>50 or score2>50:
    result = 'pass'
else:
    result = 'fail'

print('the result is' + result )
'''
#and or
'''
a=10
b=20

if (a>15) and (b>25) :
    print('the condition is true')
else:
    print('the condition is false')
'''

food=['curry','ramen','steak']
'''
for b in food:
    print('i eat' + b)
    '''

'''
for i in range(0,3):
    print(f'i eat  {i}')
'''

#Q.9 write a program to input two different number 
# and check whether a number is greater or not.
'''
num1=int(input('enter a first number: '))
num2=int(input('enter second number: '))

if num1 > num2:
    print('num1 is greater')
else:
    print('number 2 is greater')
'''
# write a program to check whether a number is odd or even.

#write the output of the following program.

lis=[165,168,170,178]

for i in range(0,len(lis)): 
    if lis[i]==168 or lis[i]==178:
        print(lis[i])

         
      


#tofas
'''
fruits=['apple','banana']
colors=['red','yellow']

for i in range(0,2):
    print(fruits[i] + ' color is ' + colors[i])
'''
# function
# 1. built-in function  2. user defined function
'''
def grade8():
    print('there are alotogether 12 students')
grade8()
'''

#practice questions.
#1. write a program to input two different numbers and find the greatest among them.
#2. write a program to check whether a number is postive or negative or zero.
#3 write the output of the program:
youme=[2,7,8]
for i in range(0,len(youme)):
    if not youme[i] ==7: 
        print(youme[i])

#.4 Write the output of the following program:
fruits=['mango','apple','grapes']
colors=['yellow','red','green']

for i in range(0,3):
    print(fruits[i] + ' color is ' + colors[i])

#5.Write the output of the following program:
ageList=[23, 16, 18, 17]
for age in range(0,len(ageList)):
    if ageList[age] >= 18:
        print('you are eligible for vote')
    else:
        print('you are not eligible for vote') 


#6.
colors1 = ['red', 'white', 'white', 'red', 'red','white'] 
colors2 = ['red', 'white', 'white', 'white', 'red','red'] 
count=0
for i in range(0,5):
    if  not colors1[i]==colors2[i]:
        count=count+1   

print(count)
print('pairs have diff colors')

