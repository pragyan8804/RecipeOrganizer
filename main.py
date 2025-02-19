from services.recipe_service import RecipeService
from services.search_service import SearchService
from services.meal_plan_service import MealPlanService
from services.shopping_list_service import ShoppingListService
from services.data_service import DataService
from models.recipe import Recipe
from models.meal_plan import MealPlan

class RecipeOrganizer:
    def __init__(self):
        self.recipe_service = RecipeService()
        self.search_service = SearchService(self.recipe_service)
        self.meal_plan_service = MealPlanService(self.recipe_service)
        self.shopping_list_service = ShoppingListService(self.meal_plan_service)
        self.data_service = DataService(self.recipe_service, self.meal_plan_service)
        
        # Load saved data when starting the program
        self.data_service.load_data()

    def main_menu(self):
        """Display and handle the main menu"""
        while True:
            print("\n=== Recipe Organizer ===")
            print("1. Add Recipe")
            print("2. List Recipes")
            print("3. Delete Recipe")
            print("4. Search Recipes")
            print("5. Plan Meals")
            print("6. View Meal Plans")
            print("7. Generate Shopping List")
            print("8. Save Data")
            print("9. Exit")
            
            choice = input("Enter your choice (1-9): ").strip()
            
            if choice == "1":
                self.recipe_service.add_recipe()
            elif choice == "2":
                self.recipe_service.list_recipes()
            elif choice == "3":
                self.recipe_service.delete_recipe()
            elif choice == "4":
                self.search_service.search_recipes()
            elif choice == "5":
                self.meal_plan_service.plan_meals()
            elif choice == "6":
                self.meal_plan_service.view_meal_plans()
            elif choice == "7":
                self.shopping_list_service.generate_shopping_list()
            elif choice == "8":
                self.data_service.save_data()
            elif choice == "9":
                # Save data before exiting
                self.data_service.save_data()
                print("Goodbye!")
                break
            else:
                print("Invalid choice! Please try again.")

if __name__ == "__main__":
    organizer = RecipeOrganizer()
    organizer.main_menu()