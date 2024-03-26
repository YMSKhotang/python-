
'''
print('Welcome to Python Quiz')
answer=input('Are you ready to play the Quiz ? (yes/no) :')
score=0
total_questions=3
 
if answer.lower()=='yes':
    print('Question 1: Which programming language is popular?')
    print('options 1. python 2. java')
    answer=input("ans:" + "     ") 
    if answer.lower()=='python':
        score =  score + 1
        print('correct')
    else:
        print('Wrong Answer :')
 
    print('Question 2: Computer understands only 0 & 1?')
    print(' options 1. yes 2. no ')
    answer=input("ans:" + "     ")
    if answer.lower()=='yes':
        score += 1
        print('correct')
    else:
        print('Wrong Answer : ')
   
    print('Question 3: Python is  ____________ programming language.')
    print(' options 1. Low level 2. High level ')
    answer=input("ans:" + "     ")
    if answer.lower()=='High level':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
else:
    print('see you next time ')
 
print('Thankyou for Playing this small quiz game, you attempted  '+ str(score) + "  questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('BYE!')
'''

print('welcome to quiz game')
answer = input('are you ready? (yes/no) ')
score=0

if answer=='yes':
    # Q.1
    print("Q1. capital city of nepal?")
    print(" options : 1. kathmandu  2. pokhara")
    answer=input("your answer is:")
    if answer == '1':
        score=score + 1
        print('correct answer')
    else:
        print('wrong answer')
    
    #Q.2
    print("Q1. Who will be the winner of tomorrow's program?")
    print(" options : 1. hitesh  2. thiren")
    answer=input("your answer is:")
    if answer == '1':
        score=score + 1
        print('correct answer')
    else:
        print('wrong answer')
    #Q.3
        print("Q1. is nikesh coming to khotang?")
    print(" options : 1. yes  2. no")
    answer=input("your answer is:")
    if answer == '1':
        score=score + 1
        print('correct answer')
    else:
        print('wrong answer')
    
    print('Thankyou for playing game')
    print('your final score is  ' + str(score) )
    
   
else:
    print('see you again')





 

