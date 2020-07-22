

a = int(input('Enter a value :'))
b = int(input('Enter b value :'))
print ('Before swapping a = ' , a ,'and b = ', b)
a = a + b
b = a - b
a = a - b
print('After swapping a = ' , a ,'and b = ', b)


print(format('After swapping the values %a') %a)
