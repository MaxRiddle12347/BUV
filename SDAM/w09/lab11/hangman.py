from random_word import RandomWords

word = RandomWords().get_random_word()

def letterAssess(letter, word,count):
    winCount = 0
    hangman = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
    if letter[-1] in word:
        print("Successful guess!")
    else:
        print("Sorry. Your letter isn't in the word.")
        print(hangman[count])
        print(f'Remaining attempts: {6-count}')
        count += 1
    for a in range(len(word)):
        if a == len(word) -1 :
            if word[a] in letter:
                print(word[a])
                winCount += 1
            else:
                print("-")
        else:
            if word[a] in letter:
                print(word[a], end="")
                winCount += 1
            else:
                print("-", end="")
    if winCount != len(word):
        return count
    else:
        return "won"


def play(word):
    word = [*word]
    list = []
    count = 0
    for x in range(len(word)):
        if x == len(word) - 1:
            print(f'-    Number of letters: {len(word)}')
        else:
            print("-",end="")
    while count < 7 :
        inp = input("Enter your letter: ")
        if len(inp) == 1:
            if inp.isalpha():
                if inp not in list:
                    list.append(inp)
                    count = letterAssess(list,word,count)
                    try:
                        if count.isalpha():
                            return f'You {count}!'
                    except:
                        continue
                else:
                    print("Letter has already been played.")
            else:
                print("Not an acceptable input.")
        else:
            print("Not an acceptable input.")
    print("".join(word))
    return "You lost :("


print(play(word))