def get_shop_list():
    shop_list = []
    for i in range(5):
        shop_item = input("Enter shopping item {}: ".format(i+1))
        item_n_price = shop_item.split()
        item = item_n_price[0]
        price = item_n_price[1]
        shop_item_dict = {"Item": item, "Price": price}
        shop_list.append(shop_item_dict)

    return shop_list

def sort_price(list):
    sort = sorted(list, key=lambda x: x["Price"], reverse=True)  #lamba is a anonymouse function

    return sort

for item in sort_price(get_shop_list()):
    print(f"{item['Item']}: ${item['Price']}")

#Lambda functions are similar to user-defined functions but without a name. They're commonly referred to as anonymous functions.
#Lambda functions are efficient whenever you want to create a function that will only contain simple expressions – that is, expressions that are usually a single line of a statement.