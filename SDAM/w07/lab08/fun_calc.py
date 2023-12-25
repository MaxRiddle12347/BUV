def arithmaticEquation():
    list = []
    while True:
        inp = int(input("Enter your number: "))
        print(inp)
        list.append(inp)
        if len(list) == 2:
            break
    while True:
        inp = int(input("Choose your arithmatic evaluator (1 to add, 2 to subtract, 3 to divide, 4 to multiply, 5 for the remainder after dividing the 1st number with the 2nd): "))
        if inp < 0 or inp > 5:
            print("Option not avaliable.")
        else:
            break
    try:
        match inp:
            case 1:
                return list[0] + list[1]
            case 2:
                return list[0] - list[1]
            case 3:
                return list[0] / list[1]
            case 4:
                return list[0] * list[1]
            case 5:
                return (list[0] % list[1])
    except:
        print("Can't divide by 0.")
print(arithmaticEquation())