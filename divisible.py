n = int(input('Enter the limit :'))
d = int(input('Enter the divisible number :'))
for i in range(1,n+1):
    if i % d == 0:
        print(i)

