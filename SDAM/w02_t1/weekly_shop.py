nameList = ["Peaches","Beans","Chicken Pieces","Socks","Bottles of water"]
totalAmt = 0
totalCost = 0
for name in nameList:
    print(f'Item: {name}')
    amt = int(input("Amount: "))
    totalAmt += amt
    cost = float(input("Individual cost: "))
    totalCost += amt*cost
print(f'Total amount: {totalAmt} \nTotal cost: {totalCost}')