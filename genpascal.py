p = int(input('Enter the number of rows: '))
b = int(1)
q = int(0)
x = int
r = int
print("\nPascal's triangle is : \n\n")
while q < p:
    for r in range(37*q, 0, -1):
        print(' ')
    for x in range(0, q+1, +1):
        if x ==0 or q == 0:
            b = 1
        else:
            b = (b * (q - x + 1)) / x
            print(b, end=' ')
        print("\n")
        ++q
        break





