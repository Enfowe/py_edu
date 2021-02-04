money = 550
water = 400
milk = 540
coffee_beans = 120
disposable_cups = 9
machine_info = ""


def update_info():
    global machine_info
    machine_info = f"""The coffee machine has:
{water} ml of water
{milk} ml of milk
{coffee_beans} g of coffee beans
{disposable_cups} of disposable cups
{money} of money
"""


update_info()
print(machine_info)
print()


def buy():
    global money
    global water
    global milk
    global coffee_beans
    global disposable_cups
    # tuple decoding in dict "drinks":
    # (drink name, ml of water, ml of milk, g of coffee beans, cost in $)
    drinks = {"1": ("espresso", 250, 0, 16, 4),
              "2": ("latte", 350, 75, 20, 7),
              "3": ("cappuccino", 200, 100, 12, 6)}
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    choice = input("> ")
    drink = drinks[choice]
    water -= drink[1]
    milk -= drink[2]
    coffee_beans -= drink[3]
    money += drink[4]
    disposable_cups -= 1


def fill():
    global water
    global milk
    global coffee_beans
    global disposable_cups
    print("Write how many ml of water do you want to add:")
    water += int(input("> "))
    print("Write how many ml of milk do you want to add:")
    milk += int(input("> "))
    print("Write how many grams of coffee beans do you want to add:")
    coffee_beans += int(input("> "))
    print("Write how many disposable cups of coffee do you want to add:")
    disposable_cups += int(input("> "))


def take():
    global money
    print(f"I gave you ${money}")
    money = 0


actions = {"buy": buy, "fill": fill, "take":take}
print("Write action (buy, fill, take):")
action = input("> ")
actions[action]()
print()
update_info()
print(machine_info)
