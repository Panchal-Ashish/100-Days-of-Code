class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "two_hundred": 200,
        "hundred": 100,
        "fifty": 50,
        "twenty": 20,
        "ten": 10,
        "five": 5
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"Total collection: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert the money.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print(f"Sorry that's not enough money. Money refunded {self.CURRENCY} {self.money_received}.")
            self.money_received = 0
            return False
