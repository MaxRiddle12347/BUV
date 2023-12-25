def initial():
    name = input("Enter your name here: ")
    name = symbolRemoval(name)
    name = name.split(" ")
    print("Initials output: ", end=" ")
    for x in range(len(name)):
        if name[x] == " ":
            name.pop(x) #pop() is to remove the element at the specified position
    for y in range(len(name)):
        middleNameInit(name[y])


def middleNameInit(string):
    string = string.split("-")

    if len(string) >= 2:
        for names in string:
            if names == string[-1]:
                print(names[0].capitalize(),end=".")
            else:
                print(names[0].capitalize(), end="-")
    elif len(string) == 1:
        init = string[0][0]
        init = init.capitalize()
        print(init, end=".")

def symbolRemoval(string):
    string = [*string]
    list = []
    for x in string:
        if x.isalpha() or x == "-" or x==" ":
            list.append(x)
    return "".join(list)

initial()