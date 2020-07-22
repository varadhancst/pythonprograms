import array
n = int(input('Enter a number: '))
a = array[10]
c = int(0)

while n > 0:
    a[c] = n % 10

    n = n / 10
    c=+1

print(c)

for i in range(c-1, 0, -1):
    if a[i] == 0:
        print('Zero')
    if a[i] == 1:
        print('ONE')
    if a[i] == 2:
        print('TWO')
    if a[i] == 3:
        print('THREE')
    if a[i] == 4:
        print('FOUR')
    if a[i] == 5:
        print('FIVE')
    if a[i] == 6:
        print('SIX')
    if a[i] == 7:
        print('SEVEN')
    if a[i] == 8:
        print('EIGHT')
    if a[i] == 9:
        print('NINE')
    if a[i] == 10:
        print('TEN')


