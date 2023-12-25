def reverse(x):
    str = ""
    for i in x:
        str = i + str
    return str

x = input("Enter your text:")

print("The orginal string is: ", end="")
print(x)

print("The reversed string is: ", end="")
print(reverse(x))