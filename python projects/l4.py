#Switch statement (match case)
#array
#constants 
#while
#continue/break



#constant
#install pconst --> pip install pconst

from pconst import const

name='harry'
const.name =''

name='mike'
#print(name)
#print(const.name)



#continue  
# it will skip the condition and print all other values


for i in range(0,10):
    if (i==7) :
        continue
    print(i)  


#break
# it will break the loop after the condition met 
#output is :- 0,1,2
for i in range(0,10):
    if (i==3) :
        break
    #print(i)  

#pass
#it is used when we want to write a code but not using that part of our program.
for i in range(0,10):
  pass

#Q.1  # output --> 
'''
animals = ['Beetles', 'Giraffes', 'Lions']

for animal in animals:
    match animal:
        case "Beetles":
            print('insects')
        case "Giraffes":
            print('herbivores')
        case "Lions":
            print('Carnivores')
'''
        

#Q.2  # output --> opt.2
'''
from pconst import const

feeling  = 'normal'
const.STATE = 'water'

match const.STATE:
    case 'water':
        feeling = 'cold'
    case 'hot water':
        feeling ='hot'
print(const.STATE + 'is' + feeling)
'''

#Q.3  # output --> opt.2
'''
from pconst import const

const.MAX = 10
num=1

while num < const.MAX:
    num = num * 2
    if num > const.MAX:
        break
    print(num)
'''
#Q.4  # output -->  opt1
'''
oceanList = ['pacific','sea of japan','atlantic','indian']

for ocean in oceanList:
    if ocean == 'sea of japan':
        continue
    print(ocean)
'''

#Q.5 ---> opt.4
'''
from pconst import const

border =30
scores =[50,20,10,80,60]
pass1 =0 
const.PASS2 =20

for i in range(0,len(scores)):
    if (scores[i] < border):
        continue
    pass1 = pass1 + 1

    
print('you have passed' + str(pass1) + 'test')
print('The class as a whole has passed' + str(pass1 + const.PASS2) + 'test')
'''

#Q.6  # output --> opt 2
'''
state = "water"
temperature = 0

match state:
    case "Ice":
        temperature = 0
    case "water":
        temperature = 5
    case "Hot water":
        temperature = 40

for i in range(0,50):
    if i != temperature:
        print('measuring ...')
        continue
    print(str(i) + "c")
    break

'''

#Q.7 # output --> 1
'''
cakeCount = 3

while cakeCount > 1:
    cakeCount = cakeCount - 1

    #cakeCount = 3 - 1  --> 2
    #--> it will be skip due to continue statement inside if condition

    #cakeCount = 2 - 1  --> 1
    if cakeCount > 1:
        continue
    print('There is/are ' + str(cakeCount) + ' cake(s) left')
'''

#Q.8 --> 
'''
money=500
foods = ['melon','buff','bread','fish','strawberries']
prices = [100,300,400,100,80]

for i in range(0,5):
    if money >= prices[i]:
        print('Buy' + foods[i])
        money=money-prices[i]
    else:
        print("you can't buy it ")
        continue
'''
        
#Q.9 # 
# firtst loop go to case 1 and print rock and go to next then there it matches to case 
# and then print tie and break.
'''
myHand ="Scissors"

for i in range(0,3):
    match i:
        case  0 :
            hand = 'Rock'
        case  1 :
            hand = 'Scissors'
        case  2 :
            hand = 'Paper'
    if hand == myHand:
        print('its a tie')
        break
    print(hand)

'''
#Q.10 #output --> 50
'''
i = 1
num = 2
while True:
    ans = num * i

    if ans >= 50:
        break
    i = i + 1
print(ans)
'''

#Q.11 
'''
count = 0
BOXSIZE =3
box=[]
fruits = ['apples','oragnes','watermelons','grapes']

for fruit in fruits:
    if len(box) < BOXSIZE:
        box.append(fruit)
        count= count+1
print(box)
print('Fruit was added ' + str(count) + ' times')
'''

#Q.12  # output --> opt.3
#Q.13  # output --> opt.1

#Q.14  # output --> opt.4
'''
fruits1=['apples','bananas','oranges']
fruits2=['grapes','strawberries','melons']

for i in range(0, len(fruits1)):
    if len(fruits2) ==5:
        break
    fruits2.append(fruits1[i])
print(fruits2)
'''

#Q.15  # output --> opt.2
#Q.16  # output --> opt.4
#Q.17  # output --> opt.4

#Q.18  # output --> opt.3
'''
shapes=['circle', 'triangle','sqaure','rect']
for i in range(0,4):
    if i ==2:
        print('to here')
        break
    shapes.pop()
print(shapes)
'''

#Q.19 #output --> opt.1

#Q.20 #output --> opt.3
'''
dictionary = ['dog', 'cat', 'zebra']
searchWords = ["dog", "dolphin", 'cat']

for word in searchWords:
    match word in dictionary:
        case True:
            print(' is in dict')
        case False:
            print('not')
'''

#Q.21 #ouput --< opt.3
#In this example, the loop prints 'football' and 'basketball', 
# which are the sports that appear before #'baseball' in the list. 
# The loop stops when it reaches the selected sport.
'''
sports = ['football', 'basketball', 'baseball', 'volleyball']
select = 'baseball'
i=0

while i < sports.index(select):
    print(sports[i])
    i = i + 1
'''

#Q.22 #ouput --> opt.4

#Q.23 #output -->  opt. 4
'''
def search(arr, num):
    print(arr[num] + 'is the ' + str(num+1) + 'in the list')

animals = ['elephant', 'tiger', 'horse', 'monkey']
place = animals.index('monkey')


search(animals, place)

for i in range(0,len(animals)):
    if animals[i] == 'horse':
        continue
    search(animals, i)
   ''' 

#Q.24 #ouptut --> 
'''
saleList = ['potatoes','bell peppers']

for time in range(3,6):
    print(str(time) + 'PM')
    if time ==4:
        print('limited time scale')
        saleList.append('carrots')
    elif 'carrots' in saleList:
        saleList.pop()
    print(saleList)

'''
#Q.25 --> 3
'''
bag=['handkerchief', 'cell phone','scissors']
object=bag.index('scissors')
bag.pop(object)
print('the following items')
print(bag)
'''

