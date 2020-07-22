r = int(input('Enter the number of rows: '))
c = int(1)
print("\nFloyd's triangle is : \n")
for i in range(0, r):
    for j in range(0, i+1):
        print(c, end=' ')
        c += 1
    print("\n")


