"""
dadad
"""
import json


def adjust_recipe(recipe, num_people):
    """
    Adjusts the ingredient quantities in the recipe based on the desired number of servings.

    :param recipe: Dictionary with recipe details including ingredients and servings
    :param num_people: Desired number of servings
    :return: New dictionary with adjusted ingredient quantities
    """
    # Calculate adjustment factor based on original servings
    factor = num_people / recipe['servings']

    # Adjust each ingredient quantity by the factor
    adjusted_ingredients = {
        ingredient: quantity * factor
        for ingredient, quantity in recipe['ingredients'].items()
    }

    # Return a new recipe dictionary with adjusted ingredients and updated servings
    return {
        'title': recipe['title'],
        'ingredients': adjusted_ingredients,
        'servings': num_people
    }


def load_recipe(json_string):
    """
    Converts a JSON string to a Python dictionary.

    :param json_string: JSON string representing a recipe
    :return: Python dictionary with recipe details
    """
    return json.loads(json_string)


def recipe_to_json(recipe):
    """
    Converts a Python dictionary to a JSON string.

    :param recipe: Dictionary representing a recipe
    :return: JSON string of the recipe
    """
    return json.dumps(recipe, indent=4)


if __name__ == '__main__':
    # Example JSON recipe
    recipe_json = (
        '{"title": "Spaghetti Bolognese", "ingredients": '
        '{"Spaghetti": 400, "Tomato Sauce": 300, "Minced Meat": 500}, '
        '"servings": 4}'
    )

    # Load the recipe from JSON
    original_recipe = load_recipe(recipe_json)

    # Adjust the recipe for a new number of people
    new_num_people = 2
    adjusted_recipe = adjust_recipe(original_recipe, new_num_people)

    # Print the original and adjusted recipes
    print('Original Recipe (for 4 servings):')
    print(recipe_to_json(original_recipe))

    print('\nAdjusted Recipe (for 2 servings):')
    print(recipe_to_json(adjusted_recipe))
