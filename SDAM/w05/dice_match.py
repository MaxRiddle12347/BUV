from random import randrange
print("Welcome to the game")


def main():
    inp = int(input("Enter the target: "))
    sum = 0
    if inp < 2 or inp >= 13:
            print("Please enter a valid number")
            main()
    while sum != inp:
        dice1 = randrange(1,7)
        dice2 = randrange(1,7)
        sum = dice1 + dice2
        output = "Roll: {} and {}, sum is {}".format (dice1,dice2,sum)
        print(output)
    if sum == inp:
        print("Successful")

main()