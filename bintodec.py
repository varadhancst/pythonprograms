import math
j= int()
n = int(input('Enter the binary number: '))
if n != 0:
    i = n % 10
    if i == 0 or i == 1:
        while n != 0:
            i = n % 10
            
            sum = sum + i * math.pow(2, j)
            n = n / 10
            j += 1

if sum == 0:
    print("\nThe number is not a binary number")
else:
    print("\nThe equivalent decimal number is : %d", sum)


