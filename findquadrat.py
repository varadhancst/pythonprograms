import math
a = float(input('Enter the values of A: '))
b = float(input('Enter the values of B: '))
c = float(input('Enter the values of C: '))
d = float()
e = float()
real = float()
imag = float()
r1 = float()
r2 = float()
n = float()
if a != 0:
    d = b * b - 4 * a * c
    if d < 0:
        print("Roots are imaginary")
        real = - b / (2 * a)
        e = - d
        n = pow(d, 0.5)
        imag = n / (2 * a)
        print("\nr1 = ", real, imag)
        print("r2 = ", real, imag)
    if d == 0:
        print("Roots are real and equal")
        r1 = - b / (2 * a)
        print("r1 = r2 = ", r1)

    if d > 0:
        print("Roots are real and unequal")
        r1 = (- b + math.sqrt(d)) / (2 * a)
        r2 = (- b - math.sqrt(d)) / (2 * a)
        print("r1 = ",r1)
        print("r2 = ",r2)
else:
    print("Equation is linear")
