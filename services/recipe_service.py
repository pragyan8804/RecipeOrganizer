from models.recipe import Recipe
from utils.input_helpers import get_valid_number_input

class RecipeService:
    def __init__(self):
        self.recipes = []
        self.valid_categories = ["breakfast", "lunch", "dinner", "snack"]
        self.valid_tags = ["vegetarian", "vegan", "gluten-free", "dairy-free"]

    def get_ingredients(self):
        """Helper function to get ingredients and their quantities"""
        ingredients = []
        print("\nEnter ingredients (type 'done' when finished)")
        print("For each ingredient, you'll be asked to specify the quantity in grams")
        
        while True:
            ingredient_name = input("\nIngredient name (or 'done' to finish): ").strip()
            
            if ingredient_name.lower() == 'done':
                if not ingredients:
                    print("Recipe must have at least one ingredient!")
                    continue
                break
                
            if not ingredient_name:
                print("Ingredient name cannot be empty!")
                continue
                
            quantity = get_valid_number_input(f"Enter quantity for {ingredient_name} (in grams): ")
            ingredients.append((ingredient_name, quantity))
            
        return ingredients

    def add_recipe(self):
        """Add a new recipe with user input"""
        print("\n=== Add New Recipe ===")
        
        while True:
            name = input("Enter recipe name: ").strip()
            if not name:
                print("Recipe name cannot be empty!")
                continue
            if any(recipe.name.lower() == name.lower() for recipe in self.recipes):
                print("Error: Recipe with this name already exists!")
                continue
            break
        
        ingredients = self.get_ingredients()
        calories = get_valid_number_input("Enter total calories for this recipe: ")
        
        print(f"\nValid categories: {', '.join(self.valid_categories)}")
        while True:
            category = input("Enter category: ").lower().strip()
            if category in self.valid_categories:
                break
            print("Invalid category! Please choose from the list above.")
        
        print(f"\nValid tags: {', '.join(self.valid_tags)}")
        tags = []
        while True:
            tag = input("Enter tag (or 'done' to finish): ").lower().strip()
            if tag == 'done':
                if not tags:
                    print("Recipe must have at least one tag!")
                    continue
                break
            if not tag:
                print("Tag cannot be empty!")
                continue
            if tag in self.valid_tags:
                if tag in tags:
                    print("This tag is already added!")
                    continue
                tags.append(tag)
            else:
                print("Invalid tag! Please choose from the list above.")
        
        recipe = Recipe(name, ingredients, category, tags, calories)
        self.recipes.append(recipe)
        print(f"\nRecipe added successfully! Recipe ID: {recipe.id}")

    def delete_recipe(self):
        """Delete a recipe by ID"""
        if not self.recipes:
            print("\nNo recipes to delete!")
            return
            
        recipe_id = input("Enter recipe ID to delete: ").strip()
        
        if not recipe_id:
            print("Recipe ID cannot be empty!")
            return
            
        for i, recipe in enumerate(self.recipes):
            if recipe.id == recipe_id:
                del self.recipes[i]
                print(f"Recipe '{recipe.name}' deleted successfully!")
                return
        
        print("Recipe ID not found!")

    def list_recipes(self):
        """Display all recipes with their details"""
        if not self.recipes:
            print("\nNo recipes found!")
            return
        
        print("\n=== Recipe List ===")
        for recipe in self.recipes:
            print(f"\nID: {recipe.id}")
            print(f"Name: {recipe.name}")
            print(f"Category: {recipe.category}")
            print(f"Tags: {', '.join(recipe.tags)}")
            print(f"Calories: {recipe.calories}")
            print("Ingredients:")
            for ingredient, quantity in recipe.ingredients:
                print(f"- {ingredient}: {quantity}g")
            print("-" * 30)

    def get_recipe_by_id(self, recipe_id):
        """Get recipe object by ID"""
        for recipe in self.recipes:
            if recipe.id == recipe_id:
                return recipe
        return None

    def get_recipes_by_category(self, category):
        """Get all recipes of a specific category"""
        return [r for r in self.recipes if r.category == category]