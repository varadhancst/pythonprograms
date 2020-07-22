n = int(input('Enter the number: '))
r = int(0)
s = int(0)
while n > 1:
    r = int(n) % 10
    s = s + r
    n = n / 10
print('The sum of digits is : ', int(s))
