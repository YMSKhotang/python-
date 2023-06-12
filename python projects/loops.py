#pattern
# print 5 star horizonatlly usnig loop
'''
n=5
for i in range(n):
    print('*', end=' ')
'''

#nested loops
# A loop within another loop is called nestde loop.
# A nested loop must have one outer loop and one inner loop.

#1. print star for 5 rowns and column
'''
n=5
for i in range(n):
    for j in range(n):
        print('*', end='') 
        #Inside the inner loop, the statement print('*', end='')
        # prints an asterisk without a newline character.

    print()
    #After the inner loop completes, the statement print() is called to 
    #print a newline character, which moves the output to the next line

    '''

#2. prints star from 1 to 5 rows with increasing columns (increasing traingles)
'''
n=5
for i in range(0,n): #The outer loop for i in range(0, n)
    for j in range(i+1): 
        #The inner loop for j in range(i+1):iterates from 0 to i(inclusive)
        # In the first iteration of the outer loop, i is 0, so the inner loop will 
        # iterate only once. In the second iteration of the outer loop, i is 1, 
        # so the inner loop will iterate twice, and so on.

        print('*' , end='')
        
    print()
    '''

#3. Decreasing traingle
n=5
for i in range(0,5):
    #for i in range(0, 5):: This line starts a loop that iterates over the numbers
    #0 to 4 (inclusive). The variable i represents the current row number.

    for j in range(i,n):
        #for j in range(i, n):: This line starts another loop that iterates over the numbers 
        #from i to n-1. The variable j represents the position within the current row.
    
        print('*' , end='')
        
    print()

#  
