n = int(input('Enter the value for N: '))
r = int(input('Enter the value for R: '))
ncr = int()
def fact(i):
    x = int()
    if i==0:
        return 1
    else:
        x = i * fact(i-1)
        return x
if n>=r:
    ncr = fact(n) / (fact(n-r) * fact(r))
    print('The NCR value is : ', int(ncr))
else:
    print('Calculating NCR value is not possible')


