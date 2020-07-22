x = float(input('Enter the value for x: '))
n = float(input('Enter the value for n: '))
i = float()
val = float()
sum = float()
t = float()
val = x
x = x * 3.14159 / 180
t = x
sum = x
for i in range(1, int(n+1)):
    t = (t * pow((float) (-1), (float) (2 * i - 1)) * x * x) / (2 * i * (2 * i + 1))
    sum = sum + t
print("\nSine value of ", val,  " is : ", sum)
