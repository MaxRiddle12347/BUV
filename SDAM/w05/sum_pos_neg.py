pos = []
neg = []
count = 0
while count < 10:
    num = int(input("Enter interger numbers: "))
    if num > 0:
        pos.append(num)
    else:
        neg.append(num)
    count += 1
print("Sum of possitive numbers: ", sum(pos))
print("Sum of negative numbers: ", sum(neg))