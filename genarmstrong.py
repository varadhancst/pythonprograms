n = int(input('Enter the limit: '))
print("The armstrong numbers are: ")
for i in range(0, n+1):
    a = i
    s = 0
    while a > 0:
        r = a % 10
        s = s + (r * r * r)
        a = a / 10
        if i == s:
            print(i)
