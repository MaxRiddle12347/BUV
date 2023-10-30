from tabulate import tabulate
import math

n = float(input("Input number: "))

def convert(sec):
    sec = round(sec % (24 * 3600))
    hour = round(sec // 3600)
    sec %= 3600
    min = round(sec //60)
    sec %= 60
    mydata = [
        ["Input", "Hours", "Minutes", "Seconds"],
        [n, hour, min, sec]
    ]
    print(tabulate(mydata, tablefmt='grind'))

print(convert(n))