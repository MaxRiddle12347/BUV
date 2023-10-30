list1 = []
list2 = []
positive_number = 0
negative_number = 0
count = 0
total_num = 0
average = 0

user = None

while user != 0:
    try:
        user = int(input("Enter a number: "))
    except ValueError:
        user = 0

    if user > 0:
        total_num += 1
        positive_number += 1
        count += 1
        list1.insert(1, user)
    elif user < 0:
        total_num += 1
        negative_number += 1
        count += 1
        list2.insert(1, user)

if count==0:
    print("You didn't enter any number, closing program")
else:
    average = total_num / count
    print("\nThe number of positives: ", positive_number)
    print("The number of negatives: ", negative_number)
    print("Total amount of number used: ", count)
    print("The average is ", format(average, ".2f"), "which is", str(total_num), "/", str(count))
    print("Sum of positive numbers: ", sum(list1))
    print("Sum of negative numbers: ", sum(list2))