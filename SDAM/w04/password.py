pwd = input("Enter password: ")
i = 0
while i <5:
    pwds = input("Enter your password: ")
    if pwds == pwd and i <5:
        print("Welcome")
        break
    elif pwds != pwd and i ==4:
        print("Out of attempts")
        break
    elif pwds != pwd and i <5:
        print("Try again")
        i += 1
        continue
