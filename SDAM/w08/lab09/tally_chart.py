candidates = [{"Name": "Lisa", "Votes": 0},
              {"Name": "Barbara", "Votes": 0},
              {"Name": "Jean", "Votes": 0},
              {"Name": "Eula", "Votes": 0},
              {"Name": "Klee", "Votes": 0}]

def print_candidates(list):
    for candidate in list:
        print(f"{candidate['Name']}: {candidate['Votes']}")

def vote(list):
    print("List of candidates and their vote totals:")
    print_candidates(list)
    while True:
        choice = input("Vote for a candidate (1-5) or -1 to stop voting: ")
        if choice == str(-1):
            break
        elif not str.isdigit(choice):
            print("That's not a valid vote.")
        elif not 1 <= int(choice) <= 5:
            print("That's not a valid vote.")
        elif 1 <= int(choice) <= 5:
            list[int(choice) - 1]["Votes"] += 1

        print("List of candidates and their vote totals:")
        print_candidates(list)

    return list

def check_if_tie(list):
    tie = all(item["Votes"] == list[0]["Votes"] for item in list)

    return tie

def find_winner(list):
    winner = max(list, key=lambda x: x["Votes"])

    return winner

candidates = vote(candidates)

if check_if_tie(candidates):
    print("IT'S A TIE!")
else:
    print("THE WINNER IS {}".format(find_winner(candidates)["Name"]))