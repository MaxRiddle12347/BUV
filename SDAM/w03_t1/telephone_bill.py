min = int(input("Enter number of minutes: "))

def cost():
    rate = 0.15
    vat = 0.2
    call_rate = min * rate
    vat_due = min * rate * vat
    total = call_rate + vat_due
    print("Number of minutes used: ", min)
    print("Basic call charge: ", call_rate)
    print("Vat due: ", vat_due)
    print("Total bill: ", total)

cost()