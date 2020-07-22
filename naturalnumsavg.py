n = int(input('Enter the limit:'))
sum = int(0)

for i in range(1, n+1):
    print(i)
    sum = sum + i
print('Average of first ' , n , ' numbers is :', sum / n)


