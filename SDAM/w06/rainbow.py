rainbow = ['red', 'orange', 'yelow', 'green', 'blue', 'indigo', 'violet']

while True:
    user = int(input("Enter a number: "))
    if user >= 1 and user <= 7:
        print(rainbow[user -1])
    else:
        user == -1
        print("Quiting program")
        break