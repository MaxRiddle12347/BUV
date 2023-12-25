name = input("Enter your name here: ")
name = name.split()

match len(name):
    case 1:
        print(f'First name: {name[0][0]}')
        print(f'Last name: {name[1][1]}')
    case 2:
        print("No family name retard")
    case _:
        print(f'First name: {name[0][0]}')
        print(f'Middle name: {" ".join(name[1:-1])}')
        print(f'Family name: {name[-1][0]}')