n = int(input('Enter the limit:'))
esum = int()
for i in range(1, n+1):
    if i % 2 == 0:
        print(i)
        esum = esum + i
print('The result is: ', esum)
osum = int()
for i in range(1, n+1):
    if i % 2 == 1:
        print(i)
        osum = osum + i
print('The result is: ', osum)
