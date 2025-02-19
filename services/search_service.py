class SearchService:
    def __init__(self, recipe_service):
        self.recipe_service = recipe_service

    def search_recipes(self):
        """Search recipes by name, tags, or ingredients"""
        if not self.recipe_service.recipes:
            print("\nNo recipes found in the database!")
            return

        print("\n=== Search Recipes ===")
        print("1. Search by name")
        print("2. Search by tag")
        print("3. Search by ingredient")
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == "1":
            self._search_by_name()
        elif choice == "2":
            self._search_by_tag()
        elif choice == "3":
            self._search_by_ingredient()
        else:
            print("Invalid choice!")

    def _search_by_name(self):
        """Search recipes by name"""
        search_term = input("Enter recipe name to search: ").strip().lower()
        if not search_term:
            print("Search term cannot be empty!")
            return
            
        matching_recipes = [
            recipe for recipe in self.recipe_service.recipes 
            if search_term in recipe.name.lower()
        ]
        self._display_search_results(matching_recipes, f"name containing '{search_term}'")

    def _search_by_tag(self):
        """Search recipes by tag"""
        print(f"Available tags: {', '.join(self.recipe_service.valid_tags)}")
        search_tag = input("Enter tag to search: ").strip().lower()
        
        if not search_tag:
            print("Search tag cannot be empty!")
            return
            
        if search_tag not in self.recipe_service.valid_tags:
            print("Invalid tag! Please choose from the available tags.")
            return
            
        matching_recipes = [
            recipe for recipe in self.recipe_service.recipes 
            if search_tag in recipe.tags
        ]
        self._display_search_results(matching_recipes, f"tag '{search_tag}'")

    def _search_by_ingredient(self):
        """Search recipes by ingredient"""
        search_ingredient = input("Enter ingredient to search: ").strip().lower()
        if not search_ingredient:
            print("Search ingredient cannot be empty!")
            return
            
        matching_recipes = [
            recipe for recipe in self.recipe_service.recipes 
            if any(search_ingredient in ingredient[0].lower() for ingredient in recipe.ingredients)
        ]
        self._display_search_results(matching_recipes, f"ingredient containing '{search_ingredient}'")

    def _display_search_results(self, matching_recipes, search_criteria):
        """Helper function to display search results"""
        if not matching_recipes:
            print(f"\nNo recipes found with {search_criteria}!")
            return
            
        print(f"\nFound {len(matching_recipes)} recipe(s) with {search_criteria}:")
        for recipe in matching_recipes:
            print(f"\nID: {recipe.id}")
            print(f"Name: {recipe.name}")
            print(f"Category: {recipe.category}")
            print(f"Tags: {', '.join(recipe.tags)}")
            print(f"Calories: {recipe.calories}")
            print("Ingredients:")
            for ingredient, quantity in recipe.ingredients:
                print(f"- {ingredient}: {quantity}g")
            print("-" * 30)