list = ['One for sorrow', 'Two for joy', 'Three for a girl', 'Four for a boy',
        'Five for silver', 'Six for gold', 'Seven for a secret nver to be told']

num = int(input('Enter a number: '))

if num >=1 and num <=7:
    print(list[num-1])
else:
    print("Not a permitted number")