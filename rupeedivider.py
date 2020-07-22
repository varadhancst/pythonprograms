rupee = float(input('Enter the rupee:'))
print('The amount is :', rupee)
while rupee >= 1:
    rupee = rupee - (rupee % 1)
    print('The no of one rupees are :', rupee / 1 )
    break
while rupee >= 2:
    rupee = rupee - (rupee % 2)
    print('The no of two rupees are :', rupee / 2 )
    break
while rupee >= 5:
    rupee = rupee - (rupee % 5)
    print('The no of five rupees are :', rupee / 5 )
    break
while rupee >= 10:
    rupee = rupee - (rupee % 10)
    print('The no of ten rupees are :', rupee / 10 )
    break
while rupee >= 50:
    rupee = rupee - (rupee % 50)
    print('The no of fifty rupees are :', rupee / 50 )
    break
while rupee >= 100:
    rupee = rupee - (rupee % 100)
    print('The no of hundred rupees are :', rupee / 100 )
    break
while rupee >= 200:
    rupee = rupee - (rupee % 200)
    print('The no of two hundred rupees are :', rupee / 200 )
    break
while rupee >= 500:
    rupee = rupee - (rupee % 500)
    print('The no of five hundred rupees are :', rupee / 500 )
    break
while rupee >= 2000:
    rupee = rupee - (rupee % 2000)
    print('The no of two thousands rupees are :', rupee / 2000 )
    break
