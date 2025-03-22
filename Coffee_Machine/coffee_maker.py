class CoffeeMaker:
    resources = {"Water":300, "Milk":200, "Coffee":100}

    def report(self):
        return f"Water: {self.resources['Water']}ml\nMilk: {self.resources["Milk"]}ml\nCoffee: {self.resources['Coffee']}g"
    
    def is_resource_sufficient(self, drink):
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry, there is not enough {item}")
                return False
        return True
    
    def make_coffee(self, order):
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name}. Enjoy!")