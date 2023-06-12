#while loop
'''
i=1
while i<11:
    print(i)
    i=i+1
else:
    print("i is more than 10")
   ''' 


#print string and integer
'''name= "sangam"
age=26
print("my name is" +" " + name )

print(f'my name is  {name}  my age is  {age}') '''

#check the data type
#print(type(age))

#What is the output of the following code?

'''list1=['a','b','g',1,5]

list1.pop(4)
print(list1)'''

# demo question list
'''fruits=['banana','apple','orange']

for i in range(0,3):
    if not(i==1):
        print(fruits[i])'''

# if inside if
'''for i in range(0,10):
    if (i>2) and (i<8):
        if not(i==5):
            print(i)'''

# iteration in corresponding index

#example1:
'''
ages=[10,30,80]
name=['mike','hannah','john']

for i in range(0,3):
    if (ages[i] < 20) or (ages[i] > 60):
        print(name[i] + "use discount coupen")
    else:
        print(name[i] + "cannot use") 
        '''

#example 2
'''
fruits1 = ['apple','lemon','orange']
fruits2= ['banana','lemon','litchi']

for i in range(0,3):
    if fruits1[i] == fruits2[i]:
        print("fruits in both list is" + fruits1[i]) '''

#length and range in list 
'''arr=[1,2,3]
for i in range(0,len(arr)):
    if arr[i] !=2:
        print(arr[i])'''

#list comparision
'''
colors1 = ['red', 'white', 'white', 'red', 'white'] 
colors2 = ['red', 'red', 'white', 'white', 'red'] 
count=0
for i in range(0,5):
    if not  colors1[i]==colors2[i]:
        count=count+1   
        # red != red ==> 
        #white != red ==> count = 0+1 =1
        #white != white ==> 
        #red != white ==> count = 1+1 =2
        #white != red ==> count = 2+1=3

       
print(count)
print('pairs have diff colors')
'''

#Q.19 
'''
hits=[70,100,120,210]
hitCount=0
maxHit=0

for i in range(0,len(hits)):
    hitCount = hitCount + hits[i]
    #hitCount= 0 + 70 =70
    #hitCount= 70 + 100 = 170
    #hitCount= 170  + 120 = 290
    #hitCount= 290 + 210 = 500

    if maxHit < hits[i]:
        maxHit = hits[i]

        #   0 < 70 --> 70
        #   70 <100 --> 100
        #   100 < 120 --> 120
        #   120 < 210 --> 210

print(maxHit)

if maxHit>200 and hitCount>400:
    print('great baseball player')
else:
    print('baseball player')

# ans:- the output of the following program is: 
# 500
# 210
# great baseball player

'''

# Program to generate a random number between 0 and 9

# importing the random module
'''import random

print(random.randint(0,9)) '''



 


     
