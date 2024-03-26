#Practical Assignment
#1. write a program to check whether a number is odd or even.
#2. write a program to check whether a number is postive or negative or zero.   <----
#3. write a program to input two different numbers and 
#   find the greatest number among them.     ~~~~~~~~~~~
#4. Write a program to find the area of rectangle.  [ area = lenght * breadth] ---> 
#5.	Write a program to find simple interest.   <------
#[ SI= ( principal * time * rate ) /100 ]
#6.	Write a program to input two different numbers and find sum and product. --->
#7. write a program to input and check whether a number is divisible by three or not?  
# ~~~~~~
#8. write a program to input marks in three subjects and check whether
#   a student is passed in all subject or not. [pass marks is 40]


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

# for minimum value of random.random() i.e  0.0
#num = math.floor(0.0 *10)  + 1 = math.floor(0) + 1 = 1
# for element in arr:
#ans = ans + element * randNum
#ans = 0   +    1    *  1      =  1  #repeat this process
#ans = 1   +    2    *  1      =  3  
#ans = 3   +    3    *  1      =  6  
# output for minimum number is 6 

#agin do it for maximum number
# for maximum value of random.random() i.e  0.9
#num = math.floor(0.9 *10) + 1 = math.floor(9) + 1 = 10
# for element in arr:
#ans = ans + element * randNum
#ans = 0   +    1    *  10      =  10  #repeat this process
#ans = 10   +   2    *  10      = 30  
#ans = 30   +   3    *  10      =  60  
# output for minimum number is 60 

# The final output is in between 6 to 60. 





  