import random

#Modeling the battlefield
Row1 = ["", "", "", "", ""]
Row2 = ["", "", "", "", ""]
Row3 = ["", "", "", "", ""]
Row4 = ["", "", "", "", ""]
Row5 = ["", "", "", "", ""]
Rows = [Row1, Row2, Row3, Row4, Row5]

missedlist = []
hitlist = []
shiplist = []

#Printing out the battlefield
def display(list):
    global hitlist
    global missedlist
    for element in range(len(list)):
        minilist = list[element]
        for value in range(len(minilist)):
            if [element,value] in hitlist:
                if value == 4:
                    print("[H]")
                else:
                    print("[H]", end=" ")
            elif [element,value] in missedlist:
                if value == 4:
                    print("[M]")
                else:
                    print("[M]", end=" ")
            else:
                if value == 4:
                    print("[ ]")
                else:
                    print("[ ]", end=" ")


#Checking to see if a number is < 0 or >5
def check(num):
    if num < 0 or num > 4:
        return True
    else:
        return False



#making sure the computer doesnt choose titles that dont exist
def PosAppend(a, b, c, d,e):
    global Rows
    if check(a) or check(b) or check(c) or check(d):
        RowOrCol(a,b,e)
    else:
        e.append([a, b])
        e.append([c, d])
        print(e)

#letting randomness choose whether the ship is vertical or horizontal
def RowOrCol(a,b,c):
    value = random.randrange(1,5)
    if value == 1:
        PosAppend(a,b,a+1,b,c)
    elif value ==2:
        PosAppend(a, b, a -1, b,c)
    elif value ==3:
        PosAppend(a,b,a,b+1,c)
    elif value == 4:
        PosAppend(a,b,a,b-1,c)

#Registering the full 1x2 /2x1 ship
def ComputerReg():
    global shiplist
    [row1,col1] =  [random.randrange(0,5) , random.randrange(0,5)]
    RowOrCol(row1,col1,shiplist)



#Starting the game (line 56 is a cheat code)
def ShipAttack(list):
    global hitlist
    global missedlist
    global shiplist
    ComputerReg()
    while len(hitlist) < 2:
        display(list)
        try:
            row1 = int(input("Enter your row: "))               #inputting attack row
            if check(row1-1):
                print("Number isn't a valid option.")
                continue
            col1 = int(input("Enter your column: "))            #inputting attack column
            if check(col1-1):
                print("Number isn't a valid option.")
                continue
            if [row1-1,col1-1] in hitlist or [row1-1,col1-1] in missedlist:     #checking to see if target has already been hit
                print("Target has already been picked")
                continue
            if [row1-1,col1-1] in shiplist:
                print("Critical hit!")                      #player hits
                hitlist.append([row1-1,col1-1])
            else:
                print("Missed...")                          #player misses
                missedlist.append([row1-1,col1-1])
        except:
            print("Invalid input.")
            continue
    if len(hitlist) == 2:
        display(list)
        print("You won!")
        print(f'Number of attempts: {len(missedlist) +len(hitlist)}')

ShipAttack(Rows)
