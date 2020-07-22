n = int(input('Enter the number:'))
s = int(0)
r = int()
t = int()
t = n
while n > 0:
    r = n % 10
    s = int(s) + int(int(r) * int(r) * int(r))
    n = n / 10

if s == t:
    print(t , " is an armstrong number")
else:
    print(t , " is not an armstrong number")
