arr = []
n = int(input('Enter the limit: '))
print('Enter the elements: ')
for i in range(0, n):
    ele = int(input())
    arr.append(ele)
print('Entered values are: ')
print(arr, end='')
print('\nThe positive elements are: ')
for x in arr:
    if x > 0:
        print(x)


