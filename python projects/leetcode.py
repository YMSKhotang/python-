#1. Input : = [0,1,0,3,12]  --> Output: [1,3,12,0,0]

array = [0,1,0,3,12]

for i in range(0,5):
    if array[i]==0:
        array.remove(array[i])
        array.append(0)

        
print(array)

    