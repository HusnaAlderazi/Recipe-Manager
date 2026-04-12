data = """name,category,ingredients,serving,last_cooked,rating,preparation_time,cooking_instructions,difficulty_level
Pancakes,Breakfast,flour:2:cup;milk:1.5:cup;egg:1:unit;sugar:2:spoon,2,2026-04-01,8.5,15,Mix ingredients;Heat pan;Cook both sides,3 
Chicken Salad,Lunch,chicken:200:gram;lettuce:100:gram;tomato:2:unit;olive_oil:2:spoon,3,2026-03-28,7.8,20,Chop vegetables;Grill chicken;Mix all,4 
Spaghetti Bolognese,Dinner,pasta:200:gram;beef:150:gram;tomato_sauce:1:cup;onion:1:unit,4,2026-04-03,9.2,30,Boil pasta;Cook beef;Add sauce;Mix together,5 
Chocolate Cake,Dessert,flour:2:cup;cocoa:0.5:cup;sugar:1.5:cup;eggs:3:unit,6,2026-03-20,9.5,45,Mix dry ingredients;Add eggs;Bake in oven,6 
Omelette,Breakfast,eggs:2:unit;milk:0.25:cup;cheese:50:gram,1,2026-04-05,7.0,10,Beat eggs;Pour in pan;Add cheese;Fold omelette,2 
Grilled Fish,Dinner,fish:300:gram;lemon:1:unit;garlic:2:clove,2,2026-03-30,8.8,25,Season fish;Grill for 15 minutes;Serve hot,4 
Fruit Salad,Dessert,apple:1:unit;banana:1:unit;orange:1:unit;honey:1:spoon,2,2026-04-02,6.5,10,Cut fruits;Mix together;Add honey,1 """

with open("recipes2.csv", "w", encoding="utf-8") as file: 
    file.write(data)


import csv
import random
from datetime import datetime

# build a class for the objects recipes
class Recipe:
    def __init__ (self, name,category,ingredients,serving,last_cooked,rating,preparation_time,cooking_instructions,difficulty_level):
        self.name = name
        self.category = category
        self.ingredients = ingredients
        self.serving = int(serving)
        self.last_cooked = datetime.strptime(last_cooked, "%Y-%m-%d")
        self.rating = int(rating)
        self.preparation_time = int(preparation_time)
        self.cooking_instructions = cooking_instructions
        self.difficulty_level = float(difficulty_level)


# build a class for the book as object
class RecipesBook:
    
    def __init__ (self, filename):
        self.recipes = [] #create a list for the class
        self.load_from_file (filename)
        

    def load_from_file (self, filename):
        
        with open (filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                recipe = Recipe(row["name"],           #make object for each recipe
                                row["category"],
                                row["ingredients"],
                                int(row["serving"]),
                                row["last_cooked"],
                                float(row["rating"]),
                                int(row["preparation_time"]),
                                row["cooking_instructions"],
                                float(row["difficulty_level"]) )
                self.recipes.append(recipe)
                


    def view_random_recipes(self):
        random_recipe = random.choice(self.recipes)
        print(random_recipe.name)
       
    def track_cooking_history(self):
        self.recipes.sort(key=lambda recipe: recipe.last_cooked, reverse= True)

    def sort_recipes_by_rate(self):
        reated_recipes = sorted(self.recipes, key=lambda recipe: recipe.rating)
        for recipe in reated_recipes:
            print(recipe.rating, "---->", recipe.name)
       
    def generate_shopoing_list(self):
        for recipe in self.recipes:
            print(recipe.name)
            
        recipe_shopoing_list = input("\nEnter Name of The recipe From The List Above\n:")
        
        for recipe in self.recipes:
            if recipe.name == recipe_shopoing_list:
                print(recipe.name, recipe.ingredients)
            
# choose a number from the menu

def main():
 
    book = RecipesBook("recipes2.csv")  #create an object from RecipesBook class
    
    while True:
        try:
            selection = int(input("""\nSelect A Number From The List Below:\n
            0. Leave The Program
            1. List All Recipes
            2. View A Random Recipes
            3. Sort Recipes By Date Preparation
            4. Sort Recipes By Rating
            5. Search By Ingredients
            6. Add New Recipe
            7. Scale Ingredients Quantity By Number Of Servings
            8. Generate Shopping List \n\n"""))
    

            if selection == 0:
                print("\n_____ Goodbye _____")
                break 
                
            if selection == 1:
                print("\n_____ List Of All Available Recipes: _____\n ")
                for recipe in book.recipes:
                    print(recipe.name)

                
            elif selection == 2:
                print("\n_____ Three Randomly Suggested Recipes: _____ \n")
                for i in range(1,4):
                    book.view_random_recipes()
                
                
            elif selection == 3:
                book.track_cooking_history()
                print("\n_____ Cooking History: _____\n")
                for recipe in book.recipes:
                    print(recipe.name, recipe.last_cooked)
                    
            elif selection == 4:
                print("\n_____ List Of Recipes Sorted By Rating: _____\n")
                book.sort_recipes_by_rate()
                
#            elif selection == 5:
#                book.search_by_ingredients()
                
#            elif selection == 6:
#                book.add_new_recipe()
                
#            elif selection == 7:
#                scale_ingredients_by_serving()
                
            elif selection == 8:
               book.generate_shopoing_list()
                
            else:
                print("Inccorect Selection\n")
                
        except ValueError:
            print("Please Enter A NUMBER Only!\n")