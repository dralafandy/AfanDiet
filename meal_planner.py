import streamlit as st
import random

class SessionState:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

def calculate_meal_nutrition(selected_recipes, portion_sizes):
    total_nutrition = {"calories": 0, "carbs": 0, "protein": 0, "fat": 0}
    for recipe, portion_size in zip(selected_recipes, portion_sizes):
        for ingredient in recipe["ingredients"]:
            quantity = ingredient["quantity"] * portion_size
            total_nutrition["calories"] += ingredient["calories"] * quantity
            total_nutrition["carbs"] += ingredient["carbs"] * quantity
            total_nutrition["protein"] += ingredient["protein"] * quantity
            total_nutrition["fat"] += ingredient["fat"] * quantity
    return total_nutrition

def main():
    session_state = SessionState(user_info_submitted=False)

    st.title("Personalized Meal Planner")

    # First page for user input
    if not session_state.user_info_submitted:
        st.header("Welcome to the Personalized Meal Planner")
        st.write("Please provide some information about yourself and your dietary preferences to get started.")
        user_name = st.text_input("Enter your name:")
        user_age = st.number_input("Enter your age:", min_value=1, max_value=150, step=1)
        user_gender = st.radio("Select your gender:", options=["Male", "Female"])
        user_weight = st.number_input("Enter your weight in kg:", min_value=1.0, step=0.1)
        user_height = st.number_input("Enter your height in cm:", min_value=1.0, step=0.1)
        user_activity_level = st.selectbox("Select your activity level:",
                                           options=["Sedentary", "Lightly active", "Moderately active", "Very active", "Extra active"])

        # Customization options for dietary preferences and portion sizes
        dietary_preferences = st.multiselect("Select your dietary preferences:", ["Vegetarian", "Vegan", "Gluten-free"])
        portion_size_options = ["Small", "Medium", "Large"]
        portion_sizes = st.multiselect("Select portion sizes for meals:", portion_size_options, default=portion_size_options)

        if st.button("Generate Meal Plan"):
            # Once the user submits their information, proceed to the meal planning section
            session_state.user_info_submitted = True

    # Meal planning section
    else:
        st.write("Generating personalized meal plan...")

        # Expanded recipe database with detailed nutritional information
        recipes_data = [
            {
                "name": "Scrambled eggs with spinach",
                "category": "breakfast",
                "ingredients": [
                    {"name": "Eggs", "quantity": 2, "unit": "large", "calories": 140, "carbs": 2, "protein": 13, "fat": 9},
                    {"name": "Spinach", "quantity": 100, "unit": "grams", "calories": 23, "carbs": 3, "protein": 3, "fat": 0}
                ]
            },
            {
                "name": "Oatmeal with berries",
                "category": "breakfast",
                "ingredients": [
                    {"name": "Oats", "quantity": 40, "unit": "grams", "calories": 150, "carbs": 27, "protein": 5, "fat": 3},
                    {"name": "Berries", "quantity": 50, "unit": "grams", "calories": 30, "carbs": 8, "protein": 1, "fat": 0},
                    {"name": "Milk", "quantity": 200, "unit": "ml", "calories": 120, "carbs": 12, "protein": 8, "fat": 5}
                ]
            },
            # Add more recipes with detailed ingredient information
        ]

        # Generate random meal plan
        random_breakfast = random.choice([recipe["name"] for recipe in recipes_data if recipe["category"] == "breakfast"])
        random_lunch = random.choice([recipe["name"] for recipe in recipes_data if recipe["category"] == "lunch"])
        random_dinner = random.choice([recipe["name"] for recipe in recipes_data if recipe["category"] == "dinner"])
        random_snacks = random.choice([recipe["name"] for recipe in recipes_data if recipe["category"] == "snacks"])

        # Display random meal plan
        st.write("## Random Meal Plan")
        st.write("### Breakfast:", random_breakfast)
        st.write("### Lunch:", random_lunch)
        st.write("### Dinner:", random_dinner)
        st.write("### Snacks:", random_snacks)

if __name__ == "__main__":
    main()
