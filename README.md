# Recipe Organizer

A comprehensive Python-based recipe management and meal planning system that helps users organize recipes, plan meals, and generate shopping lists.

## How to Run

To start the Recipe Organizer, simply run the following command in your terminal:

```bash
python3 main.py
```

## Features

### 1. Recipe Management

#### Add Recipes
- Create new recipes with unique IDs
- Specify recipe name, ingredients with quantities (in grams)
- Assign recipe categories (breakfast, lunch, dinner, snack)
- Add dietary tags (veg, vegan, non-veg, dairy)
- Include calorie information
- Prevent duplicate recipe names
- Ensure valid ingredient quantities
x
#### List Recipes
- View all stored recipes
- Display comprehensive recipe details:
  - Unique ID
  - Recipe name
  - Category
  - Tags
  - Calories
  - Ingredients with quantities

#### Delete Recipes
- Remove recipes using their unique ID
- Automatic validation to prevent deletion of non-existent recipes

#### Search Recipes
Three search methods available:
1. **Search by Name**
   - Case-insensitive partial name matching
   - Returns all recipes containing the search term

2. **Search by Tag**
   - Search using predefined dietary tags
   - Shows all recipes matching the selected tag

3. **Search by Ingredient**
   - Find recipes containing specific ingredients
   - Case-insensitive ingredient matching

### 2. Meal Planning

#### Manual Meal Planning
- Create meal plans for specific days of the week
- Select recipes for each meal type:
  - Breakfast
  - Lunch
  - Snack
  - Dinner
- View available recipes by category
- Validate recipe selections
- Calculate total daily calories

#### Automatic Meal Planning
- Generate random meal plans
- Include all meal types automatically
- Preview generated plans
- Accept or regenerate plans
- Calculate total daily calories
- Store approved meal plans

### 3. Shopping List Generation
- Generate ingredient shopping lists for specific days
- Combine ingredients from all meals in the day's plan
- Automatically sum quantities for matching ingredients
- Present sorted list of ingredients with total quantities
- Display measurements in grams
- Clear organization of shopping needs

#### Recipe
- Properties:
  - Unique ID (UUID-based)
  - Name
  - Ingredients list with quantities
  - Category
  - Tags
  - Calories

#### MealPlan
- Properties:
  - Day
  - Breakfast recipe
  - Lunch recipe
  - Snack recipe
  - Dinner recipe

### 4. Data Storage
- Data storage using a JSON file.
- Ensuring that recipes and meal plans are saved locally.
- Allowing users to retain their data even after exiting the program.

#### RecipeOrganizer
- Main management class
- Handles all operations and user interactions
- Maintains recipe and meal plan collections

### Data Validation
- Input validation for all numeric values
- Category validation against predefined lists
- Tag validation against predefined options
- Ingredient quantity validation
- Recipe ID validation
- Day of week validation

### User Interface
- Clear console-based menu system
- Organized display of information
- Error handling with user-friendly messages
- Interactive prompts for data entry
- Consistent formatting of output

### Getting Started
1. Run the program
2. Use the main menu to navigate features
3. Start by adding some recipes
4. Create meal plans
5. Generate shopping lists as needed

### Main Menu Options
1. Add Recipe
2. List Recipes
3. Delete Recipe
4. Search Recipes
5. Plan Meals
6. View Meal Plans
7. Generate Shopping List
8. Save Data
9. Exit

## Requirements
- Python 3.x
- No external dependencies required
- Standard library modules used:
  - uuid (for unique IDs)
  - random (for automatic meal planning)