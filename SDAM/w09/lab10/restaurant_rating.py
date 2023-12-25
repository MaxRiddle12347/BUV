def rating():
    counts = False
    data = ['1:', '2:', '3:', '4:', '5:']
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    vote_list = [one, two, three, four, five]
    ans = []
    repetition = 0
    sums = 0
    def count(z):
        vote_list[z-1] += 1
        return vote_list
    while counts == False:
        for i in range(len(data)):
            print(data[i], vote_list[i])
        vote = input("\n Vote for a restaurant 1-5 (-1 to cancel): ")
        if vote.isnumeric() == False:
            if vote == '-1':
                counts = True
            else:
                print("\n Input not accepted!")
        else:
            vote = int(vote)
            if vote >= 1 and vote <= 5:
                count(vote)
                repetition += 1
                sums += vote
                print("Added")
            elif vote == -1:
                counts = True
            else:
                print("\n Invalid input!")
    print("\n The result is: ")
    ans.append(data)
    ans.append(vote_list)
    for column in ans:
        print("{: <10} {: <10} {: <10} {: <10} {: <10} ".format(*column))
    if repetition == 0:
        print("No data entered")
    else:
        print("\n the average is: ", round(sums/repetition, 2))
rating()