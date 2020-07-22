x = float(input('Enter the value for x: '))
n = int(input('Enter the value for n: '))
sum = float(1)
t = float(1)
for i in range(1, n+1):
    exp = i
    t = t * x / exp
    sum = sum + t
print("Exponential value of ", x, " is: ", sum)


