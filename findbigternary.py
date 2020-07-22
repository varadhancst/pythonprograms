a = int(input('Enter the num1 value :'))
b = int(input('Enter the num2 value :'))
c = int(input('Enter the num3 value :'))

#big = a > b  (a > c ? a : c)  (b > c ? b : c)
if a > b:
    if a > c:
        print('num1 is the biggest number: ', a)
    else:
        print('Num3 is the biggest number: ', c)
else:
    if b > c:
        print('num2 is the biggest number: ', b)
    else:
        print('num3 is the biggest number: ', c)
