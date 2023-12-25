lit = []
count = 0

def slicing(s):
    return s[::-1]

def reverse():
    global lit
    global count
    while count < 5:
        user = int(input("Enter interger numbers: "))
        lit.append(user)
        count += 1
    else:
        print(slicing(lit))

reverse()

#Create a slice that starts at the end of the string, and moves backwards.
#In this particular example, the slice statement [::-1] means start at the end of the string and end at position 0, move with the step -1, negative one, which means one step backwards.