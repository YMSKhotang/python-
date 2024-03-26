# Tofas level 2  Questions:

#1. Write the output of the following program:
months = ['jan','feb','march']
lastDay =['29','30','29']

for i in range (0,3):
    if lastDay[i]!= '30':  
        print(months[i] +'end on the' + lastDay[i])


#2. Write the output of the following program:
score1 =70
score2 = 40

if score1 >50 and score2>50:
    result = 'pass'
else:
    result = 'fail'

print('the test result is' + result)

#3.Write the output of the following program:
weather = 'sunny'
ticket ='yes'
seat ='B'

if (weather =='sunny') or (weather =='cloudy'):
    print('event will be held')
else:
    print('event will not be held')

if(ticket =='yes') and (seat =='B'):
    print('sit in seat A')
else:
    print('sit in seat B')

#4.Write the output of the following program:
fruits = [ 'apples', 'oranges','bananas']

for i in range(0,3):
    if not(i==1):
        print(fruits[i])

#5.Write the output of the following program:

for i in range(0,15):
    if(i>4) and (i<13):
        if not(i==9):
            print(i)

#6. Write the output of the following program: ****
num =0 

for i in range(0,6):
    num = num + 1
print(num)

 # 0 --> num = 0 + 1  ==>1
 # 1 --> num = 1 + 1  ==>2
 # 2 --> num = 2 + 1  ==>3
 # 3 --> num = 3 + 1  ==>4
 # 4 --> num = 4 + 1  ==>5
 # 5 --> num = 5 + 1  ==>6



#7. Write the output of the following program:
foods = ['curry','ramen','steak']

for i in range(0,3):
    print('I want to eat '+ foods[i])

#8. Write the output of the following program:
total = 0
weightList = [50,60,70,80,90]
count = len(weightList)

for i in range (0,count):
    total = total + weightList[i]

print(total)
if (total < 300) or (count< 6):
    print('can ride')
else:
    print('cannot ride')

#9. Write the output of the following program:

players = ['mbappe', 'neymar','ronaldo','messi']
print(players[1])

#10. Write the output of the following program:
stocks =[5, 0, 9]
items = ['Ipad','Macbook','Iphone']
for i in range(0,3):
    if stocks[i] == 0:
        print(items[i] + 'are not in stock')

#11. Write the output of the following program:
ages= [10,30,80]
names=['mike','hannah','john']

for i in range(0,3):
    if ages[i]<20 or ages[i]>60:
        print(names[i] + ' can use discounts coupens')
    else:
        print(names[i] + ' cannot use discounts coupens')
        
#12. Write the output of the following program:

array = [1,2,3]
for i in range(0, len(array)):
    if array[i] != 2:
        print(array[i])

#13. Write the output of the following program: ****

height= [161, 163, 165, 167, 169]

for i in range(0,5):
    if(height[i] ==165) or (height[i]==167):
        print(height[i])

#14. Write the output of the following program: ****

colors1 = ['red', 'white', 'white', 'red', 'red','white'] 
colors2 = ['red', 'white', 'white', 'white', 'red','red'] 
count=0
for i in range(0,6):

    if   colors1[i]!=colors2[i]:
        count=count+1   

print(count)
print('pairs have diff colors')

#15. Write the output of the following program:
fruits=['mango','apple','grapes']
colors=['yellow','red','green']

for i in range(0,3):
    print(fruits[i] + ' color is ' + colors[i])

#16. Write the output of the following program:

hits = [70,100,80,110]
hitCount = 0
maxHits = 0 

for i in range (0,4):
    hitCount = hitCount + hits[i]
    #hitCount = 0 + 70 ==> 70
    #hitCount = 70 + 100 ==> 170
    #hitCount = 170 + 80  ==> 250
    #hitCount = 250 + 110 = 360

    if maxHits < hits[i]:
        maxHits = hits[i]

    #if 0 < 70:
    #   maxHits = 70
    
    #if 70 < 100:
    #   maxHits = 100

    #if 100 < 80:
     pass

    # #if 100 < 110:
    #   maxHits = 110


   
print(hitCount)  #=> 360
print(maxHits)  #==> 110

if maxHits > 100 and hitCount > 350 :
    print('greatest player')
else:
    print('average player')
     
#17. Write the output of the following program:
ageList=(23, 16, 18, 17)

for i in range(0,4):

    if ageList [i]>= 18:
        print('you are eligible for vote')
    else:
        print('you are not eligible for vote')
