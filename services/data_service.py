import json
import os
from models.recipe import Recipe
from models.meal_plan import MealPlan

class DataService:
    def __init__(self, recipe_service, meal_plan_service):
        self.recipe_service = recipe_service
        self.meal_plan_service = meal_plan_service
        self.data_file = "recipe_data.json"

    def save_data(self):
        """Save recipes and meal plans to a JSON file"""
        data = {
            "recipes": [
                {
                    "id": recipe.id,
                    "name": recipe.name,
                    "ingredients": recipe.ingredients,
                    "category": recipe.category,
                    "tags": recipe.tags,
                    "calories": recipe.calories
                }
                for recipe in self.recipe_service.recipes
            ],
            "meal_plans": {
                day: {
                    "day": plan.day,
                    "breakfast_id": plan.breakfast.id if plan.breakfast else None,
                    "lunch_id": plan.lunch.id if plan.lunch else None,
                    "snack_id": plan.snack.id if plan.snack else None,
                    "dinner_id": plan.dinner.id if plan.dinner else None
                }
                for day, plan in self.meal_plan_service.meal_plans.items()
            }
        }

        try:
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=2)
            print("\nData saved successfully!")
        except Exception as e:
            print(f"\nError saving data: {str(e)}")

    def load_data(self):
        """Load recipes and meal plans from JSON file"""
        if not os.path.exists(self.data_file):
            print("\nNo saved data found.")
            return

        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)

            # Load recipes
            for recipe_data in data.get("recipes", []):
                recipe = Recipe(
                    recipe_data["name"],
                    recipe_data["ingredients"],
                    recipe_data["category"],
                    recipe_data["tags"],
                    recipe_data["calories"]
                )
                recipe.id = recipe_data["id"]  # Preserve the original ID
                self.recipe_service.recipes.append(recipe)

            # Load meal plans
            for day, plan_data in data.get("meal_plans", {}).items():
                breakfast = self.recipe_service.get_recipe_by_id(plan_data["breakfast_id"])
                lunch = self.recipe_service.get_recipe_by_id(plan_data["lunch_id"])
                snack = self.recipe_service.get_recipe_by_id(plan_data["snack_id"])
                dinner = self.recipe_service.get_recipe_by_id(plan_data["dinner_id"])

                meal_plan = MealPlan(day, breakfast, lunch, snack, dinner)
                self.meal_plan_service.meal_plans[day] = meal_plan

            print("\nData loaded successfully!")
        except Exception as e:
            print(f"\nError loading data: {str(e)}")