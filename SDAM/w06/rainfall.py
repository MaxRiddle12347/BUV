month = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
monthRain = []
count = 0
while count < 12:
    try:
        num = int(input(f'Enter the amount of rainfall of {month[count]}: '))
        monthRain.append(num)
        count += 1
    except:
        print("Input not accepted.")
highNum = max(monthRain)
blank = "   "
star = " * "
for x in range(highNum):
    for y in range(len(monthRain)):
        if y == 11:
            if (monthRain[y] - highNum) < 0:
                print(blank)
                highNum = highNum - 1
            else:
                print(star)
                highNum = highNum - 1
        else:
            if (monthRain[y] - highNum) < 0:
                print(f'{blank} ', end="")
            else:
                print(f'{star} ', end="")
print(" ".join(month))
