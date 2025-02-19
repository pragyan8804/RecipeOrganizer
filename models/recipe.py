import uuid

class Recipe:
    def __init__(self, name, ingredients, category, tags, calories):
        self.id = str(uuid.uuid4())[:8]
        self.name = name
        self.ingredients = ingredients
        self.category = category
        self.tags = tags
        self.calories = calories