from typing import List
import json

class Runner:

    def __init__(self, db='recipe_data.json'):
        # TODO: parse DB into memory
        self.groceries = []
        self.standard = ["milk","cereal","fruit","frozen"]
        self.recipes = self._get_recipes_into_memory(db)

    def _get_recipes_into_memory(self, db) -> List:
        with open(db) as json_file:
            return json.load(json_file).get("data")
    
    def show_recipes(self) -> None:
        for recipe in self.recipes:
            print(f'{recipe.get("number")}: {recipe.get("name")}')
            for ingredient in recipe.get("ingredients"):
                print(f'{ingredient}')
            if recipe.get("extra_instructions"):
                print(f'{recipe.get("extra_instructions")}')
            print("")
    
    def add_recipe_to_list(self, search:str) -> None:
        try:
            if int == type(int(search)):
                number = search
            for recipe in self.recipes:
                if number == recipe.get("number"):
                    self.groceries.append(recipe)
                    return
        except ValueError:
            pass
        
        lowercase = search.lower()
        for recipe in self.recipes:
            if lowercase == recipe.get("name").lower():
                self.groceries.append(recipe)
                return
        print("Not found:", search)

    def remove_latest_recipe(self) -> None:
        try:
            self.groceries.pop()
        except IndexError:
            return 

    def show_grocery_list(self) -> None:
         for recipe in self.groceries:
            print(f'{recipe.get("number")}: {recipe.get("name")}')
            for ingredient in recipe.get("ingredients"):
                print(f'{ingredient}')
            print("")
    
    def finalize_list(self) -> None:
        print("")
        print("Grocery")

        for std in self.standard:
            print(std)

        print("")
        for recipe in self.groceries:
            print(f'{recipe.get("number")}: {recipe.get("name")}')
            for ingredient in recipe.get("ingredients"):
                print(f'{ingredient}')
            print("")

    def reset_list(self) -> None:
        self.groceries = []


    def start(self):
        while True:
            print("""
                Grocery manager:
                1) Show recipes
                2) Add recipe to grocery list
                3) Remove recipe from list
                4) Show list
                5) Finalize list
                6) Reset list

                e) exit
                h) help
            """)
            action = input("Enter action: ")
            if action == "1":
                self.show_recipes()
            if action == "2":
                search = input("Enter recipe :")
                self.add_recipe_to_list(search)
            if action == "3":
                self.remove_latest_recipe()
            if action == "4":
                self.show_grocery_list()
            if action == "5":
                self.finalize_list()
            if action == "6":
                self.reset_list()

            if action == "h":
                pass
            if action == "e":
                exit()

if __name__ == "__main__":
    runner  = Runner()
    runner.start()