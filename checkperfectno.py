s = int()
n = int(input('Enter the number:'))
for i in range(1, n):
    if n % i == 0:
        s = s + i
if s == n:
    print('the no is perfect', n)
else:
    print('The no is not perfect', n)
