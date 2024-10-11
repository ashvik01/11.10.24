# Maximum number of ones
a= [1,0,1,0,1,1,0,1,0,0,0,0,0,0,1,1,1,1,1,1,1,0,1]
size= len(a)

def Maxlen(a, size):
    counter= 0
    maxones= 0
    for i  in range(0, size):
        if a[i]==0:
            counter=0
        else:
            counter+=1
            maxones= max(maxones,counter)
            
    return maxones

print("Maximum number of ones in '1,0,1,0,1,1,0,1,0,0,0,0,0,0,1,1,1,1,1,1,1,0,1' =" ,Maxlen(a, size))

# Maximum number of zeroes
a= [1,0,1,0,1,1,0,1,0,0,0,0,0,1,1,1,0,1]
size= len(a)

def Maxlen(a, size):
    counter= 0
    maxones= 0
    for i  in range(0, size):
        if a[i]==1:
            counter=0
        else:
            counter+=1
            maxones= max(maxones,counter)
            
    return maxones

print("Maximum number of zeroes in '1,0,1,0,1,1,0,1,0,0,0,0,0,1,1,1,0,1' =" ,Maxlen(a, size))