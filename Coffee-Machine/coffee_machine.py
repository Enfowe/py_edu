money = 550
water = 400
milk = 540
coffee_beans = 120
disposable_cups = 9
working = True


def remaining():
    print()
    print(f"""The coffe machine has:
{water} ml of water
{milk} ml of milk
{coffee_beans} g of coffee beans
{disposable_cups} of disposable cups
{money} of money
""")


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
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    choice = input()
    if choice == "back":
        return None
    drink = drinks[choice]
    if water >= drink[1]:
        if milk >= drink[2]:
            if coffee_beans >= drink[3]:
                if disposable_cups >= 1:
                    print("I have enough resources, making you a coffee!")
                    water -= drink[1]
                    milk -= drink[2]
                    coffee_beans -= drink[3]
                    money += drink[4]
                    disposable_cups -= 1
                else:
                    print("Sorry, no disposable cups")
            else:
                print("Sorry, not enough coffee beans")
        else:
            print("Sorry, not enough milk")
    else:
        print("Sorry, not enough water")


def fill():
    global water
    global milk
    global coffee_beans
    global disposable_cups
    print("Write how many ml of water do you want to add:")
    water += int(input())
    print("Write how many ml of milk do you want to add:")
    milk += int(input())
    print("Write how many grams of coffee beans do you want to add:")
    coffee_beans += int(input())
    print("Write how many disposable cups of coffee do you want to add:")
    disposable_cups += int(input())


def take():
    global money
    print(f"I gave you ${money}")
    money = 0


def exit_():
    global working
    working = False


actions = {"buy": buy, "fill": fill, "take": take, "remaining": remaining, "exit": exit_}

while working:
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()
    actions[action]()
    print()
