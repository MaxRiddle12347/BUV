from tabulate import tabulate

rent = float(input("Rent per month: "))
gas = float(input("Gas payment per month: "))
electricity = float(input("Electricity payment per month: "))
water = float(input("Water payment per month: "))
council =float(input("Council tax payment per month: "))

print("Rent: ", rent)
print("Gas: ", gas)
print("Electricity: ", electricity)
print("Water: ", water)
print("Council: ", council)
table = [["Rent","€",rent], ["Gas","€",gas], ["Electricity","€",electricity], ["Water","€",water], ["Council","€",council]]
total = rent + gas + electricity + water + council

print(tabulate(table))
print("Total: ", total)