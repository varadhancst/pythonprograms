n = int(input('Enter the number:'))
s = int(0);
r = int(0);

while n > 1:
    r = int(n) % 10
    s = int(r) + int(s) * 10
    n = int(n) / 10

print('The reverse number is :', s)


