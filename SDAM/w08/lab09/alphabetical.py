def get_letter():
    letters = []
    for i in range(5):
        letter = input("Enter string number {}: ".format(i + 1))
        letters.append(letter)

    return letters

def sort_list(list):
    list = sorted(list)

    return list

print(sort_list(get_letter()))