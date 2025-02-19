class ShoppingListService:
    def __init__(self, meal_plan_service):
        self.meal_plan_service = meal_plan_service

    def generate_shopping_list(self):
        """Generate a shopping list for a specific day's meal plan"""
        if not self.meal_plan_service.meal_plans:
            print("\nNo meal plans found! Please create a meal plan first.")
            return
    
        print("\n=== Generate Shopping List ===")
        print("Available days:", ", ".join(day.title() for day in self.meal_plan_service.meal_plans.keys()))
    
        while True:
            day = input("Enter day of the week: ").lower().strip()
            if day in self.meal_plan_service.meal_plans:
                break
            print("Invalid day! Please choose from the available days.")
    
        meal_plan = self.meal_plan_service.meal_plans[day]
        shopping_list = {}
        
        def add_recipe_ingredients(recipe):
            if recipe:
                for ingredient, quantity in recipe.ingredients:
                    ingredient = ingredient.lower()
                    shopping_list[ingredient] = shopping_list.get(ingredient, 0) + quantity
    
        # Add ingredients from all meals
        add_recipe_ingredients(meal_plan.breakfast)
        add_recipe_ingredients(meal_plan.lunch)
        add_recipe_ingredients(meal_plan.snack)
        add_recipe_ingredients(meal_plan.dinner)
    
        # Display shopping list
        print(f"\nShopping List for {day.title()}:")
        print("-" * 40)
        for ingredient, quantity in sorted(shopping_list.items()):
            print(f"{ingredient.title()}: {quantity}g")
        print("-" * 40)