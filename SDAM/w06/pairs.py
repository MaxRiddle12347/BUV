import random

rows1, cols1 = (4, 4)
rows2, cols2 = (5, 5)
row = range(rows1)
col = range(cols1)
numOfPairs = 0

#Get a random position for each card
def randomPos():
    rowPos = random.choice(row)
    colPos = random.choice(col)

    return rowPos, colPos


#Put 4 of a card into 4 random positions with no overlap
def randomCardPos(x):
    for a in range(4):
        rowPos, colPos = randomPos()
        if cardsPos[rowPos][colPos] != 0:
            while True:
                rowPos, colPos = randomPos()
                if cardsPos[rowPos][colPos] == 0:
                    cardsPos[rowPos][colPos] = x
                    break
        else:
            cardsPos[rowPos][colPos] = x

#Get the first chosen card
def getFirstCard(x):
    firstCardPos = [int(i) for i in x.split() if i.isdigit()]
    print(cardsPos[firstCardPos[0]][firstCardPos[1]])

    return firstCardPos

#Get the second chosen card
def getSecondCard(x):
    secondCardPos = [int(i) for i in x.split() if i.isdigit()]
    print(cardsPos[secondCardPos[0]][secondCardPos[1]])

    return secondCardPos

#Prepare the table with the number of rows and columes
cardsPos = [[0 for i in range(cols1)] for j in range(rows1)]


#Put all the cards into their positions
randomCardPos("Jack")
randomCardPos("Queen")
randomCardPos("King")
randomCardPos("Ace")

#Set up and print the display table
display = [["*" for i in range(cols2)] for j in range(rows2)]
display[0][0] = " "

for i in range(1,5):
    display[0][i] = "{cord}".format(cord = (i - 1))
for i in range(1,5):
    display[i][0] = "{cord}".format(cord = (i - 1))
for row in display:
    print(*row, sep="  ")

while True:
    firstCard = input("Enter the 1st card (row. col): ")
    firstCardPos = getFirstCard(firstCard)
    secondCard = input("Enter the 2nd card (row, col): ")
    secondCardPos = getSecondCard(secondCard)
    
    if display[firstCardPos[0] + 1][firstCardPos[1] + 1] == "X" or display[secondCardPos[0] + 1][secondCardPos[1] + 1] == "X":
        print("Card(s) already paired.")
    elif firstCard == secondCard:
        print("Can't pick the same card.")
    elif cardsPos[firstCardPos[0]][firstCardPos[1]] == cardsPos[secondCardPos[0]][secondCardPos[1]]:
        numOfPairs += 1
        display[firstCardPos[0] + 1][firstCardPos[1] + 1] = "X"
        display[secondCardPos[0] + 1][secondCardPos[1] + 1] = "X"
        print("You found a pair!")
        print("Number of pairs found: " + str(numOfPairs))
        for row in display:
            print(*row, sep="  ")
    else:
        print("Not a match.")

    if numOfPairs == 8:
        break