import csv
import random
from datetime import date, datetime, timedelta
import re

def add_new_recipe():
    """Adding a new recipe into the recipe csv file"""
    # try to open the file. If the file does not exist, create one
    try:
        with open('recipes.csv', 'r', newline='') as file:
            reader = csv.DictReader(file)
            row_count = len(list(reader))
            for row in reader:
                row['no'] = int(row['no'])
                row['preparation_time'] = float(row['preparation_time'])
                row['serving'] = int(row['serving'])
                row['ratting'] = float(row['ratting'])
        print('\nrecipes.csv exist.')

    except:
        with open('recipes.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                'no', 'name', 'category', 'ingredients', 'serving',
                'preparation_time', 'cooking_instraction',
                'difficulty', 'last_cooked', 'ratting'
            ])
            print('\n\nnew recipes.csv created')
            row_count = 1

    print("\n=== Add a New Recipes ===")
    rec_no = row_count+1
    name = input("Enter recipe name: ")


    # Get category
    print("\nCategory examples: Breakfast', 'Lunch', 'Dinner','Dessert")
    category = input("Enter recipes categories: ")

    #Recipes ingredients
    print("\nWhat are the ingredients (Use ',' between the ingredients): ")
    ingredients = input("Enter the ingredients: ")

        
    # Validate serving people 
    while True:
        try:
            serving = int(input("Enter the number of servings (e.g., How many people will this recipe serve?): "))
            if serving > 0:
                break
            print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")

    #preparation_time(min)

    #Cooking instructions 
    cooking_instraction = input("Enter the cooking instructions: ")

    # Get difficulty
    print("\nRate the difficulty (Easy, Medium, Hard)")
    difficulty = input("Enter recipes difficulty: ")

    # Get last cooked 
    while True:
        last_cooked = input("Enter last cooked date (YYYY-MM-DD) or press Enter for today: ")
        if not start_date.strip():  # Use today's date
            start_date = date.today().strftime("%Y-%m-%d")
            break
        try:
            datetime.strptime(start_date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    # Get ratting
    print("\nRate the recipe out of ten (0: bad and 5: delicious)")
    ratting = input("Enter recipes rate: ")


    # Create new recipe
    new_recipe = {
        'no': rec_no,
        'name': name,
        'category': category,
        'ingredients': ingredients,
        'serving': serving,
        'preparation_time': start_date,
        'cooking_instraction': cooking_instraction,
        'difficulty': difficulty,
        'last_cooked':last_cooked,
        'ratting':ratting
    }
    try:
        with open('recipes.csv', 'a', newline='') as file:
            fn = ['no', 'name', 'category', 'ingredients', 'serving', 'preparation_time',
                             'cooking_instraction', 'difficulty', 'last_cooked', 'ratting']
            writer = csv.DictWriter(file, fieldnames=fn)
            writer.writerow(new_recipe)
            print(f"\nrecipe '{name}' added successfully!")
    except Exception as e:
        print(f'Error saving new recipe:{e}')

def open_recipe ():
    file = open("recipes.csv", "r", encoding="utf-8")
    reader = csv.DictReader(file)
    return reader 


def view_recipes():
    """View All Recipes"""
    reader = open_recipe()
    print("\n--- List Of Recipes ---")
    i = 1
    for row in reader:
        print(str(i) + ". " + row["name"] + " - " + row["preparation_time"])
        i += 1

def view_random_recipe():
    """View random Recipes"""
    reader = open_recipe()
    All_Recipes = list(reader)
    Recipes_no = len(All_Recipes)
    random_recipe = random.randint(1, Recipes_no)

    print("\n--- Suggested Recipe ---")
    print(All_Recipes[random_recipe])



def sort_recips_by_rate():
    """Sort Recipes By Rate"""
    reader = open_recipe()
    sorted_by_ratting = sorted(reader, key=lambda row: float(row["ratting"]), reverse=True)
    
    for i, row in enumerate(sorted_by_ratting, 1):
        print(f"{i}. {row['name']} - {row['ratting']}")

        
def search_by_ingredients():
    """Search For Recipes By Ingredients"""

    ingredient = input("Please enter the ingredient you are looking for:")
    reader = open_recipe()
    j=1
    for row in reader:
        ingredients = re.sub(r'[^\w]', '', row["ingredients"].lower())
        ingredients = ingredients.split()
        for i in ingredients:
            if i == ingredient:
                print(str(j) + ". " +row['name'])
                j += 1

def track_cooking_history():
    """Sort Recipes By Cooking History"""
    reader = open_recipe()
    sorted_by_last_date = sorted(reader, key=lambda row: datetime.strptime(row["last_cooked"], "%Y-%m-%d"), reverse=False)
        
    for i, row in enumerate(sorted_by_last_date, 1):
        print(f"{i}. {row['name']} - {row['last_cooked']}")
        
def search_by_category():
    """Sort Recipes By Category"""
    reader = open_recipe()
    valid_category = ['Breakfast', 'Lunch', 'Dinner','Dessert']

    print("Please enter a valid ategory: Breakfast', 'Lunch', 'Dinner','Dessert.")
    selceted_category = input("Choose Category Option: ")
    i = 1
    if selceted_category in valid_category:
        for row in reader:
            if selceted_category == row ['category']:
                print(f"{i}. {row['name']} - {row['ingredients']}")
                i += 1
    
    
def display_menu():
    """Display the main menu options."""
    print("\n=== Recipes Menu ===")
    print("1. List All Recipes")
    print("2. View A Random Recipes")
    print("3. Sort Recipes By Date Preparation")
    print("4. Sort Recipes By Rating")
    print("5. Search By Ingredients")
    print("6. Add New Recipe")
    print("7. Search by Category ")
    print("8. Exit")
    return int(input("\nSelect A Number From (1-8): "))
    

def main():
    """Main application function."""
    print("Welcome to Recipe Manager!")
    print("This app helps you build your own recipes.")

    while True:
        selection = display_menu()
    
        if selection == 1:
            view_recipes()
        elif selection == 2:
            view_random_recipe()
        elif selection == 3:
            track_cooking_history()
        elif selection == 4:
            sort_recips_by_rate()
        elif selection == 5:
            search_by_ingredients()
        elif selection == 6:
            add_new_recipe()
        elif selection == 7:
            search_by_category()
        elif selection == 8:
            print("Thank you for using Recipe Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")
