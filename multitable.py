a = int(input('Enter a value :'))
b = int(input('Enter b value :'))

for i in range(a, b+1):
    for j in range(a, b+1):
        print(i * j, end=' ')
    print("\n")


