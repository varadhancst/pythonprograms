x = int(input('Enter the value of X: '))
n = int(input('Enter the value of n: '))
count = 1
sum = 1
while count<=n:
    sum = sum * x
    count+=1
    #print(count)
print('The power of', x,'^',n , 'is: ', sum)

