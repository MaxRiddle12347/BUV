def character_print():
    char = input("Enter your string of texts: ")
    while True:
        try:
            inp = int(input("Enter your number(Must be a positive integer): "))
            break
        except:
            print("Input not accepted")
    return f"{char}\n"*inp

print(character_print())