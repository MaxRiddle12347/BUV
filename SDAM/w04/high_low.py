import random

number = random.randint(1, 13)
number2 = random.randint(1, 13)

def card_checker(num):
    match num:
        case 1:
            return "Ace"
        case 11: 
            return "Jack"
        case 12:
            return "Queen"
        case 13:
            return "King"
        case default:
            return num
        
def game():
    card_1 = number
    print("Ther first card is ", card_1)
    user = input("Is the next card higher or lower?( higher / lower) ")
    card_2 = number2
    print("The second card is ",card_2)

    if card_1 == card_2:
        print("Game end")
    elif (user == "higher" and card_2 > card_1 or user == "lower" and card_2 < card_1):
        print("You win")
    else:
        print("You lose")

game()