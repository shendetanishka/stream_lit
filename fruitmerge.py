class Fruit:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __str__(self):
        return f"{self.name} (Level {self.level})"


class FruitMergeGame:
    def __init__(self):
        self.inventory = []

    def add_fruit(self, fruit):
        self.inventory.append(fruit)
        print(f"Added {fruit}")

    def merge_fruits(self, fruit1, fruit2):
        if fruit1.level == fruit2.level:
            new_fruit = self.create_new_fruit(fruit1)
            if new_fruit:
                self.inventory.remove(fruit1)
                self.inventory.remove(fruit2)
                self.inventory.append(new_fruit)
                print(f"Merged {fruit1} and {fruit2} to create {new_fruit}")
            else:
                print("Cannot merge these fruits.")
        else:
            print("Fruits must be of the same level to merge.")

    def create_new_fruit(self, fruit):
        fruit_map = {
            "Blueberry": "Strawberry",
            "Strawberry": "Orange",
            "Orange": "Apple",
            "Apple": "Melon",
            "Melon": "Watermelon",
        }
        new_fruit_name = fruit_map.get(fruit.name)
        if new_fruit_name:
            return Fruit(new_fruit_name, fruit.level + 1)
        return None

    def show_inventory(self):
        if self.inventory:
            print("Your Inventory:")
            for fruit in self.inventory:
                print(f"- {fruit}")
        else:
            print("Your inventory is empty.")

    def play(self):
        while True:
            print("\n1. Add Fruit")
            print("2. Merge Fruits")
            print("3. Show Inventory")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                fruit_name = input("Enter the fruit name (Blueberry, Strawberry, Orange, Apple, Melon): ")
                level = int(input("Enter the fruit level (1 for new fruits): "))
                if fruit_name in ["Blueberry", "Strawberry", "Orange", "Apple", "Melon", "Watermelon"]:
                    self.add_fruit(Fruit(fruit_name, level))
                else:
                    print("Invalid fruit name.")
            elif choice == '2':
                if len(self.inventory) < 2:
                    print("You need at least two fruits to merge.")
                    continue
                print("Select two fruits to merge:")
                self.show_inventory()
                fruit1_index = int(input("Enter the index of the first fruit (0-indexed): "))
                fruit2_index = int(input("Enter the index of the second fruit (0-indexed): "))
                if (0 <= fruit1_index < len(self.inventory)) and (0 <= fruit2_index < len(self.inventory)):
                    self.merge_fruits(self.inventory[fruit1_index], self.inventory[fruit2_index])
                else:
                    print("Invalid indices.")
            elif choice == '3':
                self.show_inventory()
            elif choice == '4':
                print("Thank you for playing!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    game = FruitMergeGame()
    game.play()
