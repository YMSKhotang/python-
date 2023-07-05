
#1. write a program to check whether a number is odd or even.
#2. write a program to check whether a number is postive or negative or zero.
#3. write a program to input two different numbers and find the greatest number among them.
#4. write a program to input three different numbers and find sum and product.
#5. write a program to find simple interest.[ si = (principal*time*rate)/100 ] 

#3. write the output of the following program:

appleWeight = 400
orangeWeight =300

if appleWeight > orangeWeight:
    print('apples are heavier')
else:
    print('oranges are heavier')

#4. write the output of the following program:
score = 60
average = 65
if score > average:
    print('you did well')
else:
    print('try little harder')


#5. write the output of the program:
youme=[6,12,18,20]
for i in range(0,len(youme)):
    if not youme[i] ==18: 
        print(youme[i])

#.6 Write the output of the following program:
players=['dembele','messi','haland']
clubs=['barcelona','inter miami','manchester city']

for i in range(0,3):
    print(players[i] + ' plays for ' + clubs[i]) 

#7. write the output of the following program.
num1=7
num2=9
ans=0 

if num1 > num2 :
    ans= num1
elif num1 == num2:
    ans=num1+num2
else:
    ans=num2

print(ans)

#.8 write the output of the following program.

def output(value1, value2):
    print(value1 + value2)

output(5,10) #--> 5 + 10 = 15
output('5','10') #--> ' 22'+ ' 56 ' = 2256

#.9 write the output of the following program.
ageList=[23, 16, 18, 17]
for age in range(0, len(ageList)):
    if ageList[age] >= 18:
        print('you are eligible for vote')
    else:
        print('you are not eligible for vote')


#10. Write the output of the following program:

goal=[1,3,9,7]
goalCount=0
max_goal=0
	 
for i in range(0,len(goal)):
    goalCount = goalCount + goal[i]
    if max_goal < goal[i]:
        max_goal = goal[i]

print(goalCount) 
print(max_goal)  

if max_goal>10 and goalCount>20:
    print('greatest football player')
else:
    print('average football player')

def output():
    
    for name in names:
        print(name)

names=["ken","yeto"]
print("the group has" +str(len(names)) +  " members")
output()

score = 60
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
print (grade)