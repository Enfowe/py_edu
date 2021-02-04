class Machine:

    def __init__(self):
        self.money = 550
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.disposable_cups = 9
        self.working = True
        # tuple decoding in dict "drinks":
        # (drink name, ml of water, ml of milk, g of coffee beans, cost in $)
        self.drinks = {"1": ("espresso", 250, 0, 16, 4),
                       "2": ("latte", 350, 75, 20, 7),
                       "3": ("cappuccino", 200, 100, 12, 6)}
        self.actions = {"buy": self.buy,
                        "fill": self.fill,
                        "take": self.take,
                        "remaining": self.remaining,
                        "exit": self.exit}

    def remaining(self):
        print()
        print(f"""The coffee machine has:\n{self.water} ml of water\n{self.milk} ml of milk
{self.coffee_beans} g of coffee beans\n{self.disposable_cups} of disposable cups\n{self.money} of money""")

    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        choice = input()
        if choice == "back":
            return None
        drink = self.drinks[choice]
        if self.water >= drink[1]:
            if self.milk >= drink[2]:
                if self.coffee_beans >= drink[3]:
                    if self.disposable_cups >= 1:
                        print("I have enough resources, making you a coffee!")
                        self.water -= drink[1]
                        self.milk -= drink[2]
                        self.coffee_beans -= drink[3]
                        self.money += drink[4]
                        self.disposable_cups -= 1
                    else:
                        print("Sorry, no disposable cups")
                else:
                    print("Sorry, not enough coffee beans")
            else:
                print("Sorry, not enough milk")
        else:
            print("Sorry, not enough water")

    def fill(self):
        print("Write how many ml of water do you want to add:")
        self.water += int(input())
        print("Write how many ml of milk do you want to add:")
        self.milk += int(input())
        print("Write how many grams of coffee beans do you want to add:")
        self.coffee_beans += int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        self.disposable_cups += int(input())

    def take(self):
        print(f"I gave you ${self.money}")
        self.money = 0

    def exit(self):
        self.working = False

    def work(self):
        while self.working:
            print("Write action (buy, fill, take, remaining, exit):")
            action = input()
            self.actions[action]()
            print()


coffee_machine = Machine()
coffee_machine.work()
