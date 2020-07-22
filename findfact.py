n = int(input('Enter a number: '))
s = int(0)
t = int(1)
for i in range(n, 0, -1):
    s = i
    t = t * s
    print(i)

print('The factorial of ', n, ' is ', t)

