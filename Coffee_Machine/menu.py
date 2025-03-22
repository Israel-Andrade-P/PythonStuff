from menu_item import MenuItem


class Menu:

    menu_items = {
                    MenuItem("Latte", 2.5, {"Water":200, "Milk":100, "Coffee":20}),
                    MenuItem("Cappuccino", 3.0, {"Water":150, "Milk":200, "Coffee":15}),
                    MenuItem("Espresso", 1.5, {"Water":100, "Coffee":22})
                  }

    
    def get_items(self):
        item_names = ""
        for item in self.menu_items:
            item_names += item.name + "/"

        return item_names
    
    def find_drink(self, order_name):
        for item in self.menu_items:
            if item.name == order_name:
                return item

        return None
    











        
                