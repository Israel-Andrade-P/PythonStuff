class MoneyMachine:
    money = 0.0

    def report(self):
        print(self.money)

    def proccess_coins():
        while True:
            try:
                print("Please insert coins")
                total = int(input("How many quarters? ")) * 0.25
                total += int(input("How many dimes? ")) * 0.1
                total += int(input("How many nickels? ")) * 0.05
                total += int(input("How many pennies? ")) * 0.01
                return round(total, 2)
            except ValueError:
                print("Invalid input. Please type in a digit.")  
                continue      

    def make_payment(self, drink_cost):
        money_received = self.proccess_coins()
        if  money_received >= drink_cost:
            change = round(money_received - drink_cost, 2)
            print(f"Here is ${change} in change")
            self.money += drink_cost
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False
