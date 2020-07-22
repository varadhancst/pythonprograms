n = int(input('Enter the limit: '))
print('The prime numbers are:')
for i in range(1,n+1):
    if i <= 3:
        print(i)
    else:
        z = i/2
        for j in range(2, int(z)):
            if i % j == 0:
                continue
    print(i)
