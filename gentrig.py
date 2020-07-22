import math
r = float()
i = int()
ch = str()
print("- - - - - - - - - - - - - - - - - -")
print("Angle \t Sin \t Cos \t Tan ")
print("- - - - - - - - - - - - - - - - - -")
for i in range(0, 181, 30):
    r = i * 3.14 / 180
    print(i, math.sin(r), math.cos(r), math.tan(r))
print("- - - - - - - - - - - - - - - - - -")
