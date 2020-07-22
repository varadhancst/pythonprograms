arr = []
arrpos = int()
arrneg = int()
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
        arrpos = arrpos + x
        print(x)
print('\nThe sum of positive elements are: ', arrpos)
print('\nThe negative elements are: ')
for x in arr:
    if x < 0:
        arrneg = arrneg + x
        print(x)
print('\nThe sum of negative elements are: ', arrneg)

