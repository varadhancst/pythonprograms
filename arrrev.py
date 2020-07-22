arr = []
n = int(input('Enter the limit: '))
print('Enter the elements: ')
for i in range(0, n):
    ele = int(input())
    arr.append(ele)
print('Entered values are: ')
print(arr, end='')


def reverse(arr):
    arr.reverse()
    return arr


print('\n Reversed values are: ', reverse(arr))
