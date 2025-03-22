from coffee_maker import CoffeeMaker
from money_machne import MoneyMachine
from menu import Menu

class CoffeeMachineApp:

    def get_order(self):
        while True:
            user_input = input(f"What would you like?  {Menu.get_items(Menu())}")
            if user_input == "report":
                print(CoffeeMaker.report())
                print(MoneyMachine.report())
                continue
            elif user_input == "off":
                print("Goodbye!")
                break
            elif Menu.find_drink(Menu() ,user_input) in Menu.menu_items:
                drink = Menu.find_drink(user_input)
                if CoffeeMaker.is_resource_sufficient(drink):
                    payment = MoneyMachine.proccess_coins()
                    if MoneyMachine.make_payment(payment, drink.cost):
                        CoffeeMaker.make_coffee(drink)
                        continue
                else:
                    continue
            else:
                print(f"Sorry, we don't have {user_input} in our menu.")
                continue

my_app = CoffeeMachineApp()

my_app.get_order()
