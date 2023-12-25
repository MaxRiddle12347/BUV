def entry():
    num = str(input("Enter 2 integer: "))
    data = num.split()
    print("Your entry: ", data[0], data[1])
    def swap():
        reverse = list(reversed(data))
        print ("Swapped result: ", reverse[0], reverse[1])
    swap()
entry()