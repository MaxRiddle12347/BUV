Cost_to_produce_each_item = int(input("Cost to produce each item: "))
Sale_price_for_each_item = int(input("Sale price for each item: "))
Fixed_cost = int(input("Fixed cost: "))

break_even = round(Fixed_cost / (Sale_price_for_each_item - Cost_to_produce_each_item))

print("Break even: ", break_even)