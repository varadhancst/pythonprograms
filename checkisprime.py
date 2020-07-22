n = int(input('Enter the number:'))
m = int(n/2)
flag = int(0)
if(n <= 3):
    flag = 0
else:
    for i in range(2, m):
        if(n % i == 0):
            flag = 1
            break
if flag == 1:
    print("\nThe number is not prime")
else:
    print("\nThe number is prime")
