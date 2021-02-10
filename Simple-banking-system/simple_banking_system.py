# JetBrains Academy
# Project: Simple Banking System
# Stage 4/4

import random
import sqlite3

conn = sqlite3.connect('card.s3db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS card (id INTEGER, number TEXT, pin TEXT, balance INTEGER DEFAULT 0);')
conn.commit()


class Bank:
    def __init__(self):
        self.current_user = None
        self.is_run = True

    def start_page(self):
        if self.is_run:
            commands = {"1": self.create_an_account,
                        "2": self.log_into_account,
                        "0": self.exit}
            print("1. Create an account\n2. Log into account\n0. Exit")
            command = input()
            return commands.get(command, self.start_page)()
        else:
            return

    @staticmethod
    def luhn_checksum(card_number):
        numbers = list(map(int, list(card_number)))
        for i in range(len(numbers)):
            if i % 2 == 0:
                numbers[i] *= 2
        return (60 - sum(list(map(lambda x: x - 9 if x > 9 else x, numbers)))) % 10

    def create_an_account(self):
        id_num = str(random.randint(1, 999999999)).rjust(9, "0")
        card_number = "400000" + id_num
        card_number += str(self.luhn_checksum(card_number))
        in_db = cur.execute(f"SELECT number FROM card WHERE number = '{card_number}'").fetchall()
        if not in_db:
            card_pin = str(random.randint(1, 9999)).rjust(4, "0")
            print(f"Your card has been created\nYour card number:\n{card_number}\nYour card PIN:\n{card_pin}")
            cur.execute(f'INSERT INTO card (id, number, pin) VALUES ({id_num}, "{card_number}", "{card_pin}")')
            conn.commit()
            return self.start_page()
        else:
            return self.create_an_account()

    def add_income(self):
        income = int(input("Enter income:"))
        cur.execute(f"SELECT balance FROM card WHERE number = '{self.current_user}'")
        balance = cur.fetchone()[0]
        balance += income
        cur.execute(f"UPDATE card SET balance = {balance} WHERE number = '{self.current_user}'")
        conn.commit()
        print("Income was added!")
        return self.account_page()

    def do_transfer(self):
        receiver_card = input("Transfer\nEnter card number:")
        luhn_checksum = self.luhn_checksum(receiver_card[0: -1])
        all_cards = [card[0] for card in cur.execute("SELECT number FROM card;").fetchall()]
        if str(luhn_checksum) != receiver_card[-1]:
            print("Probably you made a mistake in the card number. Please try again!")
        elif receiver_card not in all_cards:
            print("Such a card does not exist.")
        elif receiver_card == self.current_user:
            print("You can't transfer money to the same account!")
        else:
            money_to_transfer = int(input("Enter how much money you want to transfer:"))
            user_balance = cur.execute(f"SELECT balance FROM card WHERE number = '{self.current_user}';").fetchone()[0]
            receiver_balance = cur.execute(f"SELECT balance FROM card WHERE number = '{receiver_card}';").fetchone()[0]
            if money_to_transfer > user_balance:
                print("Not enough money!")
            else:
                user_balance -= money_to_transfer
                receiver_balance += money_to_transfer
                cur.execute(f"UPDATE card SET balance = {user_balance} WHERE number = '{self.current_user}';")
                cur.execute(f"UPDATE card SET balance = {receiver_balance} WHERE number = '{receiver_card}';")
                conn.commit()
                print("Success!")
        return self.account_page()

    def close_account(self):
        cur.execute(f"DELETE FROM card WHERE number = '{self.current_user}'")
        conn.commit()
        print("The account has been closed!")
        return self.start_page()

    def account_page(self):
        commands = {"1": self.check_balance,
                    "2": self.add_income,
                    "3": self.do_transfer,
                    "4": self.close_account,
                    "5": self.log_out,
                    "0": self.exit}
        print("1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit")
        command = input()
        return commands.get(command, self.account_page)()

    def log_into_account(self):
        card_number = input("Enter your card number:")
        user_pin = input("Enter your PIN:")
        in_db = cur.execute(f"SELECT number FROM card WHERE number = '{card_number}'").fetchall()
        if in_db:
            card_pin = cur.execute(f"SELECT pin FROM card WHERE number = '{card_number}'").fetchone()[0]
        else:
            print("Wrong card number or PIN!")
            return self.start_page()
        if card_pin == user_pin:
            print("You have successfully logged in!")
            self.current_user = card_number
            return self.account_page()
        else:
            print("Wrong card number or PIN!")
            return self.start_page()

    def check_balance(self):
        balance = cur.execute(f"SELECT balance FROM card WHERE number = '{self.current_user}'").fetchone()[0]
        print(f"Balance: {balance}")
        return self.account_page()

    def log_out(self):
        self.current_user = None
        print("You have successfully logged out!")
        return self.start_page()

    def exit(self):
        self.is_run = False
        print("Bye!")
        return


bank = Bank()
bank.start_page()
