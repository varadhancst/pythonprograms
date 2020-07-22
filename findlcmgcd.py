n1 = int(input('Enter the n1 value: '))
n2 = int(input('Enter the n2 value: '))
prod = n1 * n2
while n1 != n2:
    if n1 > n2:
        n1 = n1 - n2
    if n2 > n1:
        n2 = n2 - n1
gcd = n1
lcm = prod/gcd
print('The GCD is: ', gcd)
print('The LCM is: ', int(lcm))
