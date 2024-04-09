import streamlit as st
import random

class Recipe:
    def __init__(self, name, category, ingredients, calories, carbs, protein, fat, weights, dietary_restrictions=None):
        self.name = name
        self.category = category
        self.ingredients = ingredients
        self.calories = calories
        self.carbs = carbs
        self.protein = protein
        self.fat = fat
        self.weights = weights
        self.dietary_restrictions = dietary_restrictions if dietary_restrictions else []

class User:
    def __init__(self, name, age, gender, weight_kg, height_cm, activity_level):
        self.name = name
        self.age = age
        self.gender = gender
        self.weight_kg = weight_kg
        self.height_cm = height_cm
        self.activity_level = activity_level

    def calculate_bmr(self):
        if self.gender.lower() == 'male':
            bmr = 10 * self.weight_kg + 6.25 * self.height_cm - 5 * self.age + 5
        elif self.gender.lower() == 'female':
            bmr = 10 * self.weight_kg + 6.25 * self.height_cm - 5 * self.age - 161
        else:
            raise ValueError("Gender should be 'male' or 'female'")
        return bmr

    def calculate_tdee(self):
        bmr = self.calculate_bmr()
        activity_multipliers = {
            'sedentary': 1.2,
            'lightly active': 1.375,
            'moderately active': 1.55,
            'very active': 1.725,
            'extra active': 1.9
        }
        activity_multiplier = activity_multipliers[self.activity_level.lower()]
        tdee = bmr * activity_multiplier
        return tdee

def load_recipes(dietary_restrictions=None):
    # Load recipes from a database or CSV file
    # For simplicity, I'll define some example recipes here
    recipes = [
        Recipe("Scrambled eggs with spinach", "breakfast", ["Eggs", "Spinach"], 210, 2, 13, 16, [100, 50], dietary_restrictions=["vegetarian"]),
        Recipe("Oatmeal with berries", "breakfast", ["Oats", "Berries", "Milk"], 280, 49, 8, 4, [50, 30, 100]),
        Recipe("Grilled chicken salad", "lunch", ["Chicken breast", "Lettuce", "Tomato", "Cucumber", "Olive oil"], 400, 10, 40, 20, [150, 100, 50, 50, 20]),
        Recipe("Quinoa and vegetable stir-fry", "lunch", ["Quinoa", "Broccoli", "Carrots", "Peppers", "Soy sauce"], 350, 60, 12, 8, [100, 100, 80, 50, 20]),
        Recipe("Salmon with roasted vegetables", "dinner", ["Salmon", "Broccoli", "Carrots", "Potatoes", "Olive oil"], 450, 20, 30, 25, [150, 100, 80, 100, 30]),
        Recipe("Vegetable curry with brown rice", "dinner", ["Chickpeas", "Spinach", "Tomato", "Coconut milk", "Brown rice"], 380, 60, 10, 12, [100, 80, 50, 100, 80]),
        Recipe("Greek yogurt with nuts", "snacks", ["Greek yogurt", "Almonds", "Walnuts", "Honey"], 250, 15, 15, 15, [100, 30, 30, 50]),
        Recipe("Carrot sticks with hummus", "snacks", ["Carrots", "Hummus"], 200, 30, 5, 10, [100, 50]),
        Recipe("Fruit salad", "breakfast", ["Apple", "Banana", "Orange", "Berries"], 200, 50, 2, 1, [100, 100, 100, 50]),
        Recipe("Chicken wrap", "lunch", ["Chicken", "Lettuce", "Tomato", "Cheese", "Whole wheat wrap"], 400, 40, 30, 15, [150, 100, 50, 50, 100]),
        Recipe("Pasta with marinara sauce", "dinner", ["Pasta", "Tomato sauce", "Garlic", "Onion", "Basil"], 450, 80, 10, 5, [100, 150, 50, 50, 10]),
        Recipe("Smoothie", "snacks", ["Spinach", "Banana", "Berries", "Almond milk", "Protein powder"], 300, 40, 20, 5, [50, 100, 50, 150, 30]),
        Recipe("Avocado toast", "breakfast", ["Avocado", "Whole wheat bread", "Tomato", "Egg"], 350, 25, 15, 20, [100, 50, 50, 50]),
        Recipe("Koshari", "lunch", ["Rice", "Lentils", "Pasta", "Tomato Sauce", "Chickpeas", "Fried Onions"], 450, 80, 20, 10, [100, 100, 100, 150, 100, 50]),
        Recipe("Ful Medames", "breakfast", ["Fava Beans", "Garlic", "Lemon Juice", "Olive Oil", "Salt"], 300, 40, 15, 10, [100, 20, 20, 20, 5]),
        Recipe("Mahshi", "dinner", ["Zucchini", "Tomatoes", "Rice", "Ground Beef", "Onion", "Garlic", "Spices"], 400, 60, 25, 15, [100, 100, 100, 150, 50, 20, 10]),
        Recipe("Hawawshi", "lunch", ["Pita Bread", "Ground Beef", "Onion", "Bell Pepper", "Tomato", "Spices"], 350, 40, 20, 15, [100, 150, 50, 50, 50, 10]),
        Recipe("Molokhia", "dinner", ["Molokhia Leaves", "Garlic", "Coriander", "Chicken", "Rice", "Vinegar"], 380, 50, 30, 10, [100, 20, 20, 150, 100, 10]),
        Recipe("Baba Ganoush", "snacks", ["Eggplant", "Tahini", "Garlic", "Lemon Juice", "Salt", "Olive Oil"], 250, 20, 10, 15, [150, 50, 20, 20, 5, 10]),
        Recipe("Basbousa", "dessert", ["Semolina", "Sugar", "Yogurt", "Coconut", "Butter", "Baking Powder"], 300, 40, 5, 15, [100, 100, 100, 50, 50, 20]),
        Recipe("Fattah", "lunch", ["Rice", "Bread", "Lamb", "Garlic", "Vinegar", "Tomato Sauce"], 500, 70, 30, 20, [100, 100, 150, 20, 20, 50]),
        Recipe("Baladi Bread", "breakfast", ["Whole Wheat Flour", "Water", "Yeast", "Salt"], 150, 30, 5, 2, [100, 100, 10, 5]),
        Recipe("Shakshuka", "breakfast", ["Tomatoes", "Bell Peppers", "Onion", "Garlic", "Eggs", "Spices"], 350, 15, 20, 25, [150, 100, 50, 20, 100, 10]),
        Recipe("Chocolate Smoothie", "snacks", ["Cocoa powder", "Banana", "Almond milk", "Honey"], 280, 40, 10, 5, [20, 100, 150, 30]),
        Recipe("Tofu Stir Fry", "dinner", ["Tofu", "Broccoli", "Carrots", "Bell peppers", "Soy sauce", "Garlic", "Ginger"], 320, 35, 20, 15, [100, 100, 80, 50, 30, 20, 10]),
        Recipe("Vegetarian Chili", "dinner", ["Kidney beans", "Black beans", "Tomatoes", "Bell peppers", "Onion", "Garlic", "Chili powder"], 380, 60, 20, 5, [100, 100, 150, 50, 50, 20, 10]),
        Recipe("Tuna Salad Sandwich", "lunch", ["Canned tuna", "Lettuce", "Tomato", "Mayonnaise", "Whole wheat bread"], 350, 40, 25, 15, [100, 50, 50, 30, 100]),
        Recipe("Caprese Salad", "lunch", ["Tomato", "Fresh mozzarella", "Basil", "Olive oil", "Balsamic vinegar"], 250, 10, 20, 15, [100, 100, 20, 30, 20]),
        Recipe("Peanut Butter Banana Sandwich", "snacks", ["Whole wheat bread", "Peanut butter", "Banana"], 300, 40, 10, 15, [100, 50, 100]),
        Recipe("Vegetable Soup", "dinner", ["Carrots", "Celery", "Onion", "Potatoes", "Vegetable broth", "Garlic", "Bay leaves"], 200, 30, 5, 2, [100, 100, 100, 100, 150, 20, 5]),
        Recipe("Cheese Quesadillas", "snacks", ["Tortillas", "Cheese", "Salsa", "Sour cream"], 350, 40, 15, 20, [50, 100, 30, 30]),
        Recipe("Banana Bread", "snacks", ["Bananas", "Flour", "Eggs", "Butter", "Sugar", "Baking soda"], 300, 50, 5, 15, [100, 200, 100, 50, 100, 5]),
        Recipe("Mushroom Risotto", "dinner", ["Arborio rice", "Mushrooms", "Parmesan cheese", "Vegetable broth", "Onion", "Garlic", "White wine"], 400, 60, 15, 10, [100, 200, 50, 150, 50, 20, 30]),
        Recipe("Berry Smoothie Bowl", "breakfast", ["Mixed berries", "Banana", "Greek yogurt", "Granola", "Honey"], 300, 50, 15, 5, [100, 100, 100, 50, 20]),
        Recipe("Tofu Scramble", "breakfast", ["Tofu", "Bell peppers", "Onion", "Spinach", "Turmeric", "Garlic powder"], 250, 10, 15, 15, [100, 50, 50, 50, 5, 5]),
        Recipe("Pesto Pasta", "dinner", ["Pasta", "Basil", "Pine nuts", "Parmesan cheese", "Garlic", "Olive oil"], 450, 60, 15, 20, [100, 50, 30, 50, 20, 30]),
        Recipe("Hummus Wrap", "lunch", ["Whole wheat wrap", "Hummus", "Lettuce", "Tomato", "Cucumber", "Red onion"], 300, 40, 10, 5, [100, 50, 20, 20, 20, 20]),
        Recipe("Veggie Burger", "dinner", ["Black beans", "Quinoa", "Mushrooms", "Onion", "Garlic", "Breadcrumbs", "Egg"], 350, 45, 20, 10, [100, 100, 100, 50, 20, 30, 50]),
        Recipe("Green Smoothie", "snacks", ["Spinach", "Banana", "Green apple", "Celery", "Cucumber", "Lemon juice"], 250, 40, 5, 5, [50, 100, 100, 100, 50, 20]),
        Recipe("Egg Salad", "snacks", ["Eggs", "Mayonnaise", "Mustard", "Dill pickles", "Onion", "Lettuce", "Bread"], 300, 30, 15, 15, [100, 50, 20, 30, 20, 20, 50]),
        Recipe("Stuffed Bell Peppers", "dinner", ["Bell peppers", "Quinoa", "Black beans", "Corn", "Tomatoes", "Onion", "Garlic", "Cheese"], 350, 50, 20, 10, [100, 100, 100, 50, 50, 20, 20, 50]),
        Recipe("Banana Pancakes", "breakfast", ["Bananas", "Flour", "Eggs", "Milk", "Baking powder", "Vanilla extract"], 300, 40, 10, 10, [100, 200, 100, 150, 10, 5]),
        Recipe("Cucumber Salad", "lunch", ["Cucumbers", "Tomatoes", "Red onion", "Feta cheese", "Olive oil", "Red wine vinegar"], 200, 15, 10, 15, [100, 50, 50, 50, 30, 30]),
        Recipe("Apple Chips", "snacks", ["Apples", "Cinnamon", "Sugar"], 150, 30, 2, 0, [100, 5, 5]),
        Recipe("Vegetarian Sushi Rolls", "snacks", ["Sushi rice", "Nori", "Cucumber", "Avocado", "Carrot", "Bell pepper"], 250, 50, 5, 5, [100, 100, 50, 50, 50, 20]),
        Recipe("Blueberry Muffins", "snacks", ["Flour", "Blueberries", "Sugar", "Eggs", "Milk", "Butter", "Baking powder"], 300, 40, 5, 15, [200, 100, 100, 100, 150, 50, 10]),
        Recipe("Chickpea Salad", "lunch", ["Chickpeas", "Cucumber", "Tomato", "Red onion", "Feta cheese", "Olive oil", "Lemon juice"], 300, 35, 15, 15, [150, 50, 50, 50, 50, 30, 20]),
        Recipe("Cheese Omelette", "breakfast", ["Eggs", "Cheese", "Milk", "Butter", "Salt", "Pepper"], 300, 5, 20, 25, [100, 50, 50, 20, 2, 2]),
        Recipe("Spinach Artichoke Dip", "snacks", ["Spinach", "Artichoke hearts", "Cream cheese", "Sour cream", "Mayonnaise", "Garlic", "Parmesan cheese"], 250, 10, 5, 20, [100, 100, 100, 50, 50, 20, 30]),
        Recipe("Stuffed Mushrooms", "snacks", ["Mushrooms", "Cream cheese", "Garlic", "Parmesan cheese", "Breadcrumbs", "Parsley"], 200, 10, 5, 15, [100, 50, 20, 20, 20, 5]),
        Recipe("Ratatouille", "dinner", ["Eggplant", "Zucchini", "Tomatoes", "Onion", "Garlic", "Olive oil", "Herbs de Provence"], 250, 30, 5, 20, [100, 100, 100, 50, 20, 30, 10]),
        Recipe("Cauliflower Fried Rice", "dinner", ["Cauliflower", "Carrots", "Peas", "Eggs", "Soy sauce", "Garlic", "Ginger"], 300, 40, 15, 10, [200, 100, 50, 100, 30, 20, 10]),
        Recipe("Lentil Soup", "dinner", ["Lentils", "Carrots", "Celery", "Onion", "Garlic", "Vegetable broth", "Tomatoes", "Bay leaves"], 250, 30, 20, 5, [150, 100, 100, 100, 20, 150, 100, 5]),
        Recipe("Baked Sweet Potato", "snacks", ["Sweet potato", "Olive oil", "Salt", "Pepper"], 200, 40, 2, 0, [150, 10, 2, 2]),
        Recipe("Pineapple Fried Rice", "dinner", ["Rice", "Pineapple", "Shrimp", "Carrots", "Peas", "Eggs", "Soy sauce", "Garlic", "Onion"], 400, 60, 20, 5, [150, 150, 150, 100, 50, 100, 30, 20, 50]),
        Recipe("Tomato Basil Bruschetta", "snacks", ["Tomatoes", "Basil", "Garlic", "Olive oil", "Balsamic vinegar", "Baguette"], 200, 30, 5, 5, [100, 20, 5, 20, 20, 100]),
        Recipe("Cabbage Soup", "dinner", ["Cabbage", "Carrots", "Celery", "Onion", "Garlic", "Tomatoes", "Vegetable broth", "Bay leaves"], 200, 30, 10, 2, [150, 100, 100, 100, 20, 100, 150, 5]),
        Recipe("Zucchini Bread", "snacks", ["Zucchini", "Flour", "Sugar", "Eggs", "Butter", "Cinnamon", "Baking powder"], 250, 40, 5, 10, [200, 100, 100, 100, 50, 10, 5]),
        Recipe("Stuffed Zucchini Boats", "dinner", ["Zucchini", "Ground beef", "Tomato sauce", "Onion", "Garlic", "Mozzarella cheese", "Parmesan cheese"], 350, 40, 30, 15, [150, 100, 100, 50, 20, 50, 30]),
        Recipe("Peanut Butter Cookies", "snacks", ["Peanut butter", "Sugar", "Egg"], 200, 20, 5, 10, [100, 100, 100]),
        Recipe("Lemon Garlic Shrimp Pasta", "dinner", ["Shrimp", "Pasta", "Garlic", "Lemon", "Olive oil", "Parsley"], 400, 60, 25, 10, [150, 100, 20, 50, 30, 5]),
        Recipe("Apple Crisp", "snacks", ["Apples", "Oats", "Brown sugar", "Flour", "Butter", "Cinnamon"], 300, 50, 5, 10, [200, 100, 100, 100, 50, 10]),
        Recipe("Cucumber Avocado Salad", "lunch", ["Cucumber", "Avocado", "Red onion", "Dill", "Lemon juice", "Olive oil"], 200, 15, 5, 20, [100, 100, 50, 5, 20, 30]),
        Recipe("Garlic Bread", "snacks", ["Baguette", "Butter", "Garlic", "Parsley"], 250, 30, 5, 10, [100, 50, 5, 5]),
        Recipe("Broccoli Cheddar Soup", "dinner", ["Broccoli", "Cheddar cheese", "Carrots", "Onion", "Garlic", "Vegetable broth", "Butter", "Flour", "Milk"], 350, 30, 20, 15, [150, 150, 100, 100, 20, 150, 20, 20, 150]),
        Recipe("Coconut Curry Chicken", "dinner", ["Chicken", "Coconut milk", "Red curry paste", "Onion", "Garlic", "Ginger", "Vegetables"], 450, 20, 35, 20, [150, 150, 50, 50, 20, 20, 100]),
        Recipe("Banana Chips", "snacks", ["Bananas", "Lemon juice"], 150, 30, 2, 0, [100, 20]),
        Recipe("Caesar Salad", "lunch", ["Romaine lettuce", "Chicken", "Parmesan cheese", "Croutons", "Caesar dressing"], 300, 10, 30, 15, [100, 150, 50, 50, 50]),
        Recipe("Tiramisu", "dessert", ["Ladyfingers", "Mascarpone cheese", "Eggs", "Sugar", "Coffee", "Cocoa powder"], 400, 50, 15, 20, [150, 200, 100, 100, 50, 10]),
        Recipe("Peanut Butter Banana Smoothie", "snacks", ["Banana", "Peanut butter", "Milk", "Honey"], 300, 40, 10, 15, [100, 50, 150, 30]),
        Recipe("Pulled Pork Sandwich", "lunch", ["Pork shoulder", "Barbecue sauce", "Hamburger buns", "Coleslaw"], 450, 40, 30, 20, [150, 100, 100, 100]),
        Recipe("Lemon Bars", "dessert", ["Flour", "Powdered sugar", "Butter", "Eggs", "Lemon juice", "Lemon zest"], 350, 40, 5, 20, [200, 150, 150, 100, 50, 10]),
        Recipe("Vegetable Lasagna", "dinner", ["Lasagna noodles", "Tomato sauce", "Zucchini", "Spinach", "Ricotta cheese", "Mozzarella cheese"], 400, 60, 20, 15, [100, 150, 100, 100, 150, 150]),
        Recipe("Lentil Salad", "lunch", ["Lentils", "Cucumber", "Tomato", "Red onion", "Feta cheese", "Olive oil", "Lemon juice"], 300, 35, 15, 15, [150, 50, 50, 50, 50, 30, 20]),
        Recipe("Fruit Smoothie", "snacks", ["Mixed berries", "Banana", "Orange juice", "Greek yogurt", "Honey"], 250, 50, 15, 5, [100, 100, 100, 100, 30]),
        Recipe("Cinnamon Rolls", "snacks", ["Flour", "Butter", "Milk", "Sugar", "Yeast", "Cinnamon", "Cream cheese"], 350, 45, 10, 15, [200, 100, 150, 100, 20, 20, 50]),
        Recipe("French Toast", "breakfast", ["Bread", "Eggs", "Milk", "Vanilla extract", "Cinnamon"], 300, 40, 15, 10, [100, 100, 150, 10, 5]),
        Recipe("Miso Soup", "snacks", ["Tofu", "Seaweed", "Green onions", "Miso paste", "Vegetable broth"], 200, 15, 10, 10, [100, 20, 20, 50, 150]),
        Recipe("Pumpkin Bread", "snacks", ["Pumpkin puree", "Flour", "Sugar", "Eggs", "Butter", "Cinnamon", "Nutmeg"], 300, 40, 5, 15, [150, 100, 100, 100, 50, 10, 5]),
        Recipe("Taco Salad", "lunch", ["Ground beef", "Lettuce", "Tomato", "Onion", "Cheddar cheese", "Salsa", "Sour cream", "Tortilla chips"], 400, 20, 25, 20, [150, 100, 50, 50, 100, 50, 30, 50]),
        Recipe("Peach Cobbler", "dessert", ["Peaches", "Flour", "Sugar", "Butter", "Baking powder", "Cinnamon", "Nutmeg"], 350, 50, 10, 15, [200, 100, 100, 100, 10, 5, 5]),
        Recipe("Margarita Pizza", "dinner", ["Pizza dough", "Tomato sauce", "Mozzarella cheese", "Basil", "Olive oil"], 400, 40, 20, 15, [150, 100, 100, 20, 30]),
        Recipe("Eggplant Parmesan", "dinner", ["Eggplant", "Flour", "Eggs", "Breadcrumbs", "Tomato sauce", "Mozzarella cheese", "Parmesan cheese"], 450, 60, 25, 20, [150, 100, 100, 100, 150, 100, 50]),
        Recipe("Chicken Noodle Soup", "dinner", ["Chicken", "Carrots", "Celery", "Onion", "Egg noodles", "Chicken broth", "Garlic"], 300, 30, 15, 10, [150, 100, 100, 100, 100, 150, 20]),
        Recipe("Potato Salad", "snacks", ["Potatoes", "Mayonnaise", "Mustard", "Celery", "Red onion", "Dill", "Salt", "Pepper"], 250, 20, 5, 15, [150, 50, 20, 50, 50, 5, 2, 2]),
        Recipe("Rice Krispie Treats", "snacks", ["Rice cereal", "Marshmallows", "Butter"], 200, 40, 2, 5, [100, 100, 50]),
        Recipe("Chicken Caesar Wrap", "lunch", ["Grilled chicken", "Romaine lettuce", "Parmesan cheese", "Caesar dressing", "Whole wheat wrap"], 400, 20, 35, 20, [150, 100, 50, 30, 100]),
        Recipe("Vegetable Tempura", "snacks", ["Vegetables (e.g., broccoli, sweet potato, bell pepper)", "Flour", "Cornstarch", "Water", "Soy sauce", "Mirin", "Sugar", "Oil"], 300, 40, 5, 15, [200, 100, 50, 100, 30, 30, 20, 30]),
        Recipe("Cabbage Rolls", "dinner", ["Cabbage leaves", "Ground beef", "Rice", "Onion", "Garlic", "Tomato sauce", "Broth", "Parsley"], 400, 60, 25, 15, [150, 100, 100, 50, 20, 150, 100, 5]),
        Recipe("Tofu Tacos", "dinner", ["Tofu", "Taco shells", "Lettuce", "Tomato", "Onion", "Salsa", "Avocado"], 350, 30, 20, 15, [150, 100, 50, 50, 50, 30, 50]),
        Recipe("Sausage and Peppers", "dinner", ["Italian sausage", "Bell peppers", "Onion", "Tomato sauce", "Garlic", "Olive oil", "Italian seasoning"], 400, 20, 25, 20, [150, 100, 50, 150, 20, 30, 10]),
        Recipe("Chocolate Chip Cookies", "snacks", ["Flour", "Butter", "Brown sugar", "White sugar", "Eggs", "Vanilla extract", "Chocolate chips"], 300, 40, 5, 15, [200, 100, 100, 100, 100, 5, 50]),
        Recipe("Garlic Knots", "snacks", ["Pizza dough", "Butter", "Garlic", "Parsley"], 250, 30, 5, 10, [100, 100, 5, 5]),
        Recipe("Fruit Tart", "dessert", ["Pie crust", "Pastry cream", "Assorted fruits (strawberries, kiwi, berries, etc.)", "Apricot glaze"], 350, 40, 5, 20, [150, 150, 100, 50]),
        Recipe("Honey Glazed Carrots", "snacks", ["Carrots", "Butter", "Honey", "Salt", "Pepper"], 200, 30, 5, 10, [150, 20, 20, 2, 2]),
        Recipe("Chicken Alfredo", "dinner", ["Chicken", "Fettuccine pasta", "Heavy cream", "Parmesan cheese", "Garlic", "Butter", "Parsley"], 450, 50, 20, 25, [150, 200, 150, 50, 20, 20, 5]),
        Recipe("Broccoli Salad", "snacks", ["Broccoli", "Bacon", "Red onion", "Raisins", "Sunflower seeds", "Mayonnaise", "Vinegar", "Sugar"], 300, 20, 10, 15, [150, 100, 50, 50, 30, 20, 20, 20]),
        Recipe("Pineapple Upside Down Cake", "dessert", ["Pineapple", "Cherries", "Butter", "Brown sugar", "Flour", "Sugar", "Eggs", "Baking powder", "Vanilla extract"], 400, 50, 15, 20, [150, 50, 100, 100, 200, 100, 100, 10, 5]),
        Recipe("Chicken Shawarma", "dinner", ["Chicken thighs", "Yogurt", "Lemon juice", "Garlic", "Cumin", "Paprika", "Cayenne pepper", "Olive oil", "Pita bread", "Tahini sauce"], 400, 10, 30, 20, [150, 100, 20, 20, 10, 10, 5, 30, 100, 50]),
        Recipe("Key Lime Pie", "dessert", ["Graham cracker crust", "Sweetened condensed milk", "Key lime juice", "Egg yolks", "Lime zest", "Whipped cream"], 350, 40, 5, 20, [150, 200, 100, 100, 20, 50]),
        Recipe("Ratatouille Grilled Cheese", "snacks", ["Ratatouille", "Sourdough bread", "Mozzarella cheese", "Butter"], 350, 30, 15, 20, [200, 100, 100, 50]),
        Recipe("Pumpkin Soup", "snacks", ["Pumpkin puree", "Vegetable broth", "Onion", "Garlic", "Coconut milk", "Curry powder", "Cinnamon", "Nutmeg"], 250, 20, 5, 10, [200, 150, 50, 20, 100, 20, 5, 5]),
        Recipe("Quiche", "breakfast", ["Pie crust", "Eggs", "Milk", "Cheese", "Bacon", "Spinach", "Onion", "Salt", "Pepper"], 350, 20, 25, 20, [150, 150, 150, 100, 100, 100, 50, 2, 2]),
        Recipe("Tomato Basil Soup", "snacks", ["Tomatoes", "Vegetable broth", "Onion", "Garlic", "Olive oil", "Fresh basil", "Heavy cream"], 250, 20, 5, 20, [200, 150, 50, 20, 20, 20, 50]),
        Recipe("Pancakes", "breakfast", ["Flour", "Milk", "Eggs", "Butter", "Sugar", "Baking powder", "Salt", "Vanilla extract"], 350, 40, 10, 15, [200, 150, 100, 100, 50, 10, 2, 5]),
        Recipe("Mango Salsa", "snacks", ["Mango", "Red bell pepper", "Red onion", "Cilantro", "Lime juice", "Salt"], 150, 10, 5, 2, [100, 50, 50, 5, 20, 2]),
        Recipe("Chicken Pot Pie", "dinner", ["Pie crust", "Chicken", "Carrots", "Peas", "Corn", "Onion", "Celery", "Butter", "Flour", "Chicken broth", "Milk"], 400, 40, 20, 15, [150, 150, 100, 100, 100, 100, 100, 50, 20, 150, 150]),
        Recipe("Chocolate Cake", "dessert", ["Flour", "Sugar", "Cocoa powder", "Baking powder", "Baking soda", "Salt", "Eggs", "Milk", "Vegetable oil", "Vanilla extract", "Boiling water"], 400, 50, 20, 25, [200, 150, 100, 10, 5, 2, 100, 150, 100, 10, 150]),
        Recipe("Cobb Salad", "lunch", ["Romaine lettuce", "Chicken", "Bacon", "Eggs", "Tomato", "Avocado", "Blue cheese", "Red wine vinaigrette"], 400, 20, 30, 25, [100, 150, 100, 100, 50, 100, 50, 30]),
        Recipe("Gazpacho", "snacks", ["Tomatoes", "Cucumber", "Red bell pepper", "Red onion", "Garlic", "Olive oil", "Red wine vinegar", "Bread", "Salt", "Pepper"], 200, 10, 5, 5, [200, 100, 100, 50, 20, 30, 30, 100, 2, 2]),
        Recipe("Fish Tacos", "dinner", ["Fish fillets", "Flour tortillas", "Cabbage", "Tomato", "Cilantro", "Lime", "Sour cream", "Salsa"], 350, 30, 20, 15, [150, 100, 50, 50, 20, 20, 20, 30]),
        Recipe("Chocolate Mousse", "dessert", ["Chocolate", "Butter", "Eggs", "Sugar", "Whipping cream", "Vanilla extract"], 300, 30, 15, 20, [200, 50, 100, 100, 150, 5]),
        Recipe("Shakshuka", "breakfast", ["Eggs", "Tomatoes", "Red bell pepper", "Onion", "Garlic", "Paprika", "Cumin", "Cayenne pepper", "Olive oil", "Parsley", "Feta cheese", "Bread"], 300, 20, 15, 20, [100, 150, 50, 50, 20, 5, 5, 5, 30, 5, 50, 50]),
        Recipe("Meatball Subs", "lunch", ["Meatballs", "Sub rolls", "Marinara sauce", "Mozzarella cheese", "Parmesan cheese"], 450, 30, 35, 25, [150, 100, 150, 100, 50]),
        Recipe("Blueberry Pancakes", "breakfast", ["Flour", "Milk", "Eggs", "Butter", "Blueberries", "Sugar", "Baking powder", "Salt", "Vanilla extract"], 350, 40, 10, 15, [200, 150, 100, 100, 100, 50, 10, 2, 5]),
        Recipe("Beef Stir Fry", "dinner", ["Beef", "Broccoli", "Bell peppers", "Onion", "Garlic", "Ginger", "Soy sauce", "Sesame oil", "Cornstarch", "Rice"], 400, 40, 30, 20, [200, 150, 100, 100, 20, 20, 30, 30, 30, 200]),
        Recipe("Black Bean Soup", "dinner", ["Black beans", "Onion", "Garlic", "Bell pepper", "Vegetable broth", "Cumin", "Chili powder", "Lime", "Cilantro", "Sour cream"], 250, 30, 15, 5, [200, 100, 20, 50, 150, 5, 5, 20, 5, 20]),
        Recipe("Chicken Enchiladas", "dinner", ["Chicken", "Tortillas", "Black beans", "Corn", "Bell peppers", "Onion", "Enchilada sauce", "Cheddar cheese", "Sour cream", "Cilantro"], 400, 30, 25, 20, [150, 100, 100, 50, 50, 50, 150, 100, 20, 5]),
        Recipe("Caramelized Onion Tart", "snacks", ["Pie crust", "Onion", "Butter", "Olive oil", "Thyme", "Eggs", "Heavy cream", "Gruyere cheese"], 350, 60, 15, 20, [200, 200, 100, 30, 5, 100, 150, 150]),
        Recipe("Shakshuka", "breakfast", ["Tomatoes", "Bell Peppers", "Onion", "Garlic", "Eggs", "Spices"], 350, 15, 20, 25, [150, 100, 50, 20, 100, 10])
    ]
    return recipes


def generate_meal_plan(user, recipes, num_days):
    for day in range(1, num_days+1):
        meal_plan = {'breakfast': None, 'lunch': None, 'dinner': None, 'snacks': None}

        # Calculate target calories for each meal based on user's TDEE
        tdee = user.calculate_tdee()
        target_calories = {
            'breakfast': tdee * 0.25,  # 25% of TDEE for breakfast
            'lunch': tdee * 0.35,      # 35% of TDEE for lunch
            'dinner': tdee * 0.30,     # 30% of TDEE for dinner
            'snacks': tdee * 0.10      # 10% of TDEE for snacks
        }

        for meal_type in meal_plan.keys():
            # Filter recipes based on meal type
            meal_recipes = [recipe for recipe in recipes if recipe.category == meal_type]

            # Select a random recipe that meets the target calories
            valid_recipes = [recipe for recipe in meal_recipes if recipe.calories <= target_calories[meal_type]]
            if valid_recipes:
                meal_plan[meal_type] = random.choice(valid_recipes)
            else:
                # If no recipe meets the target calories, select the one closest to the target
                closest_recipe = min(meal_recipes, key=lambda x: abs(x.calories - target_calories[meal_type]))
                meal_plan[meal_type] = closest_recipe

        st.write(f"Day {day}")
        for meal_type, recipe in meal_plan.items():
            st.write(f"### {meal_type.capitalize()}: {recipe.name}")
            st.write(f"Calories: {recipe.calories} kcal | Carbs: {recipe.carbs} g | Protein: {recipe.protein} g | Fat: {recipe.fat} g")
            st.write("Ingredients:")
            for ingredient, weight in zip(recipe.ingredients, recipe.weights):
                st.write(f"- {ingredient}: {weight} g")

def main():
    st.title("Personalized Meal Planner")

    st.header("Welcome to the Personalized Meal Planner")
    st.write("Please provide some information about yourself and your dietary preferences to get started.")
    user_name = st.text_input("Enter your name:")
    user_age = st.number_input("Enter your age:", min_value=1, max_value=150, step=1)
    user_gender = st.radio("Select your gender:", options=["Male", "Female"])
    user_weight = st.number_input("Enter your weight in kg:", min_value=1.0, step=0.1)
    user_height = st.number_input("Enter your height in cm:", min_value=1.0, step=0.1)
    user_activity_level = st.selectbox("Select your activity level:",
                                       options=["Sedentary", "Lightly active", "Moderately active", "Very active", "Extra active"])

    user = User(user_name, user_age, user_gender, user_weight, user_height, user_activity_level)
    
    # Dietary restrictions filter
    dietary_restrictions = st.multiselect("Select your dietary restrictions:", options=["vegetarian", "vegan", "gluten-free", "dairy-free"])

    recipes = load_recipes(dietary_restrictions)

    num_days = st.number_input("Enter the number of days for meal plan generation:", min_value=1, max_value=7, step=1)

    if st.button("Generate Meal Plan"):
        st.write("Generating personalized meal plan...")
        generate_meal_plan(user, recipes, num_days)

if __name__ == "__main__":
    main()
