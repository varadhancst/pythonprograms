n = int(input('Enter the limit:'))
a = int(-1)
b = int(1)
c = int(0)
sum = int(0)

for i in range(1, n+1):
    c = a + b
    print(c)
    sum = sum + c
    a = b
    b = c
print('Sum of fibonacci series is: ', sum)
