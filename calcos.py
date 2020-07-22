x = float(input('Enter the value for x: '))
n = int(input('Enter the value for n: '))
sum = int(1)
t = int(1)
val = int
val = x
x = x * 3.14159 / 180
for i in range(1, n+1):
    t = t * pow((float) (-1), (float) (2 * i - 1)) * x * x / (2 * i * (2 * i - 1))
    sum = sum + t
print("\nCosine value of ", val , "is : ",  sum)


