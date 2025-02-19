import random
from models.meal_plan import MealPlan

class MealPlanService:
    def __init__(self, recipe_service):
        self.recipe_service = recipe_service
        self.meal_plans = {}
        self.days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

    def display_recipes_by_category(self, category):
        """Display recipes of a specific category"""
        category_recipes = self.recipe_service.get_recipes_by_category(category)
        if not category_recipes:
            print(f"No {category} recipes found!")
            return None
        
        print(f"\nAvailable {category} recipes:")
        for recipe in category_recipes:
            print(f"ID: {recipe.id} - {recipe.name} ({recipe.calories} calories)")
        return category_recipes

    def create_manual_meal_plan(self, day):
        """Create a meal plan manually for a specific day"""
        print(f"\n=== Creating Meal Plan for {day.title()} ===")
        
        # Get breakfast
        print("\nLet's select breakfast:")
        breakfast_recipes = self.display_recipes_by_category("breakfast")
        breakfast = None
        if breakfast_recipes:
            while True:
                breakfast_id = input("Enter recipe ID for breakfast: ").strip()
                breakfast = self.recipe_service.get_recipe_by_id(breakfast_id)
                if breakfast and breakfast.category == "breakfast":
                    break
                print("Invalid recipe ID! Please choose from the list above.")
        
        # Get lunch
        print("\nLet's select lunch:")
        lunch_recipes = self.display_recipes_by_category("lunch")
        lunch = None
        if lunch_recipes:
            while True:
                lunch_id = input("Enter recipe ID for lunch: ").strip()
                lunch = self.recipe_service.get_recipe_by_id(lunch_id)
                if lunch and lunch.category == "lunch":
                    break
                print("Invalid recipe ID! Please choose from the list above.")
        
        # Get snack
        print("\nLet's select snack:")
        snack_recipes = self.display_recipes_by_category("snack")
        snack = None
        if snack_recipes:
            while True:
                snack_id = input("Enter recipe ID for snack: ").strip()
                snack = self.recipe_service.get_recipe_by_id(snack_id)
                if snack and snack.category == "snack":
                    break
                print("Invalid recipe ID! Please choose from the list above.")
        
        # Get dinner
        print("\nLet's select dinner:")
        dinner_recipes = self.display_recipes_by_category("dinner")
        dinner = None
        if dinner_recipes:
            while True:
                dinner_id = input("Enter recipe ID for dinner: ").strip()
                dinner = self.recipe_service.get_recipe_by_id(dinner_id)
                if dinner and dinner.category == "dinner":
                    break
                print("Invalid recipe ID! Please choose from the list above.")
        
        meal_plan = MealPlan(day, breakfast, lunch, snack, dinner)
        self.meal_plans[day] = meal_plan
        self.display_meal_plan(meal_plan)

    def create_automatic_meal_plan(self, day):
        """Create an automatic meal plan for a specific day"""
        while True:
            breakfast = self.get_random_recipe("breakfast")
            lunch = self.get_random_recipe("lunch")
            snack = self.get_random_recipe("snack")
            dinner = self.get_random_recipe("dinner")
            
            meal_plan = MealPlan(day, breakfast, lunch, snack, dinner)
            print("\nGenerated Meal Plan:")
            self.display_meal_plan(meal_plan)
            
            choice = input("\nIs this meal plan okay? (yes/no): ").lower().strip()
            if choice == 'yes':
                self.meal_plans[day] = meal_plan
                break
            print("\nGenerating a new meal plan...")

    def get_random_recipe(self, category):
        """Get a random recipe from a specific category"""
        category_recipes = self.recipe_service.get_recipes_by_category(category)
        return random.choice(category_recipes) if category_recipes else None

    def display_meal_plan(self, meal_plan):
        """Display a meal plan with calorie information"""
        total_calories = 0
        print(f"\nMeal Plan for {meal_plan.day.title()}:")
        print("-" * 40)
        
        if meal_plan.breakfast:
            print(f"Breakfast: {meal_plan.breakfast.name} ({meal_plan.breakfast.calories} calories)")
            total_calories += meal_plan.breakfast.calories
        else:
            print("Breakfast: No recipe selected")
            
        if meal_plan.lunch:
            print(f"Lunch: {meal_plan.lunch.name} ({meal_plan.lunch.calories} calories)")
            total_calories += meal_plan.lunch.calories
        else:
            print("Lunch: No recipe selected")
            
        if meal_plan.snack:
            print(f"Snack: {meal_plan.snack.name} ({meal_plan.snack.calories} calories)")
            total_calories += meal_plan.snack.calories
        else:
            print("Snack: No recipe selected")
            
        if meal_plan.dinner:
            print(f"Dinner: {meal_plan.dinner.name} ({meal_plan.dinner.calories} calories)")
            total_calories += meal_plan.dinner.calories
        else:
            print("Dinner: No recipe selected")
            
        print("-" * 40)
        print(f"Total Calories: {total_calories}")

    def plan_meals(self):
        """Plan meals for a specific day"""
        if not self.recipe_service.recipes:
            print("\nNo recipes available! Please add some recipes first.")
            return
            
        print("\n=== Meal Planning ===")
        print("Available days:", ", ".join(day.title() for day in self.days))
        
        # Get day
        while True:
            day = input("Enter day of the week: ").lower().strip()
            if day in self.days:
                break
            print("Invalid day! Please choose from the available days.")
        
        # Get planning method
        print("\nHow would you like to plan your meals?")
        print("1. Manually select recipes")
        print("2. Auto-generate meal plan")
        
        while True:
            choice = input("Enter your choice (1-2): ").strip()
            if choice in ["1", "2"]:
                break
            print("Invalid choice! Please enter 1 or 2.")
        
        if choice == "1":
            self.create_manual_meal_plan(day)
        else:
            self.create_automatic_meal_plan(day)

    def view_meal_plans(self):
        """View all meal plans"""
        if not self.meal_plans:
            print("\nNo meal plans found!")
            return
            
        print("\n=== Meal Plans ===")
        for day in self.days:
            if day in self.meal_plans:
                self.display_meal_plan(self.meal_plans[day])