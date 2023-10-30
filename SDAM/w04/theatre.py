def ticket():
    adlt = int(input("Number of adults: "))
    elder = int(input("Number of olders: "))
    child = int(input("Number of childrens: "))

    while child > adlt + elder:
        print("Every child must be accompanied by at least one adult. Not an acceptable number.")
        child = int(input("Number of childrens: "))
    opt = input("Delivery option? (type 1 if you want your tickets to be delivered (fee included), type 2 if you want to collect them by yourself):")
    option = {
        "1": 2.54,
        "2": 0,
    }
    print(f'=======================')
    print(f'Children: {child}')
    print(f'Adult(<65): {adlt}')
    print(f'Adult(>65): {elder}')
    discount = (adlt+elder)/10
    if discount > 10:
        discount = 10
    adlt = adlt - discount
    if adlt < 0:
         elder = elder + adlt
         adlt = 0
    ticketPrice = adlt*10.5 + elder*8.4 + child*7.3 + option.get(opt)
    if ticketPrice >100:
        ticketPrice = (ticketPrice - option.get(opt))*0.9 + option.get(opt)
    print(f'Total price: £{round(ticketPrice,2)}')
    print(f'=======================')
ticket()