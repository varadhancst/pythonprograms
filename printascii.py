from array import *

nu = int()
print("ASCII chart for characters: ")
for nu in range(65, 123):
    if 90 < nu < 97:
        continue
    print(nu, "\t", end=' ')
