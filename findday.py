month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
s = int()
print('Enter the DOB')
date = int(input('Date: '))
mon = int(input('Month: '))
year = int(input('Year: '))
if (year / 4 == 0) and (year % 400 == 0) and (year % 100 != 0):
    month[1] = 29
for i in range(0, mon-1):
    s = int(s) + month[i]
s = int(s) + (date + year + (year / 4) - 2)
s = int(s) % 7
print('The day is : ', week[s])

