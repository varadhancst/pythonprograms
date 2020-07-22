import array
c = int(0)
r = int(0)
b = []
n = int(input('Enter a decimal number: '))
while n > 0:
    for i in range(0, n):
        r = int(n) % 2
        b[i] = r
        n = n / 2
        c+=1
    print("\nThe binary equivalent is : ", c)
for i in range(c-1, 0, -1):
    print(b[i])


