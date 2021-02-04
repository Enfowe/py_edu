print("Write how many ml of water the coffee machine has:")
water = int(input("> "))
print("Write how many ml of milk the coffee machine has:")
milk = int(input("> "))
print("Write how many grams of coffee beans the coffee machine has:")
coffee = int(input("> "))
print("Write how many cups of coffee you will need:")
need_cups = int(input("> "))
can_make = min([water // 200, milk // 50, coffee // 15])
if can_make < need_cups:
    print(f"No, I can make only {can_make} cups of coffee")
elif can_make == need_cups:
    print("Yes, I can make that amount of coffee")
else:
    print(f"Yes, I can make that amount of coffee (and even {can_make - need_cups} more than that)")
