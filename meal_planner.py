import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Define the data
data = [
    {
        "Meal": "Oatmeal",
        "Ingredients": "Oats, Milk, Banana, Honey, Cinnamon",
        "Ingredients Weight (grams)": "50, 100, 50, 10, 2",
        "Meal Type": "Breakfast",
        "Calories": 250,
        "Fat (grams)": 4,
        "Carbohydrates (grams)": 45,
        "Protein (grams)": 8,
        "Calcium (mg)": 150,
        "Vitamin C (mg)": 5,
        "Type": "Maintain weight",
        "Dietary Restrictions": ["Vegetarian"]
    },
    {
        "Meal": "Egg Salad Sandwich",
        "Ingredients": "Eggs, Bread, Mayonnaise, Mustard, Lettuce, Tomato",
        "Ingredients Weight (grams)": "100, 50, 20, 10, 20, 20",
        "Meal Type": "Lunch",
        "Calories": 320,
        "Fat (grams)": 18,
        "Carbohydrates (grams)": 25,
        "Protein (grams)": 14,
        "Calcium (mg)": 90,
        "Vitamin C (mg)": 8,
        "Type": "Maintain weight",
        "Dietary Restrictions": []
    },
    {
        "Meal": "Chicken Curry with Rice",
        "Ingredients": "Chicken, Onion, Tomato, Coconut Milk, Curry Powder, Rice",
        "Ingredients Weight (grams)": "100, 50, 50, 100, 10, 150",
        "Meal Type": "Dinner",
        "Calories": 400,
        "Fat (grams)": 20,
        "Carbohydrates (grams)": 35,
        "Protein (grams)": 22,
        "Calcium (mg)": 60,
        "Vitamin C (mg)": 10,
        "Type": "Maintain weight",
        "Dietary Restrictions": []
    },
    {
        "Meal": "Greek Yogurt with Honey and Nuts",
        "Ingredients": "Greek Yogurt, Honey, Almonds, Walnuts",
        "Ingredients Weight (grams)": "150, 20, 15, 15",
        "Meal Type": "Snack",
        "Calories": 200,
        "Fat (grams)": 10,
        "Carbohydrates (grams)": 15,
        "Protein (grams)": 15,
        "Calcium (mg)": 200,
        "Vitamin C (mg)": 0,
        "Type": "Maintain weight",
        "Dietary Restrictions": ["Vegetarian"]
    },
    {
        "Meal": "Pancakes with Maple Syrup",
        "Ingredients": "Flour, Milk, Eggs, Butter, Maple Syrup",
        "Ingredients Weight (grams)": "50, 100, 2, 10, 30",
        "Meal Type": "Breakfast",
        "Calories": 350,
        "Fat (grams)": 10,
        "Carbohydrates (grams)": 55,
        "Protein (grams)": 8,
        "Calcium (mg)": 100,
        "Vitamin C (mg)": 0,
        "Type": "Maintain weight",
        "Dietary Restrictions": ["Vegetarian"]
    },
    {
        "Meal": "Caprese Salad",
        "Ingredients": "Tomatoes, Mozzarella Cheese, Fresh Basil, Balsamic Vinegar, Olive Oil",
        "Ingredients Weight (grams)": "100, 50, 10, 10, 10",
        "Meal Type": "Lunch",
        "Calories": 250,
        "Fat (grams)": 18,
        "Carbohydrates (grams)": 8,
        "Protein (grams)": 15,
        "Calcium (mg)": 200,
        "Vitamin C (mg)": 20,
        "Type": "Maintain weight",
        "Dietary Restrictions": ["Vegetarian"]
    },
    {
        "Meal": "Grilled Salmon with Asparagus",
        "Ingredients": "Salmon Fillet, Asparagus, Lemon, Olive Oil, Salt, Black Pepper",
        "Ingredients Weight (grams)": "150, 100, 10, 10, 2, 2",
        "Meal Type": "Dinner",
        "Calories": 400,
        "Fat (grams)": 25,
        "Carbohydrates (grams)": 8,
        "Protein (grams)": 35,
        "Calcium (mg)": 100,
        "Vitamin C (mg)": 20,
        "Type": "Maintain weight",
        "Dietary Restrictions": []
    },
    {
        "Meal": "Hummus with Veggie Sticks",
        "Ingredients": "Chickpeas, Tahini, Lemon Juice, Garlic, Carrot Sticks, Cucumber Sticks, Bell Pepper Sticks",
        "Ingredients Weight (grams)": "100, 30, 10, 5, 50, 50, 50",
        "Meal Type": "Snack",
        "Calories": 180,
        "Fat (grams)": 10,
        "Carbohydrates (grams)": 20,
        "Protein (grams)": 6,
        "Calcium (mg)": 60,
        "Vitamin C (mg)": 10,
        "Type": "Maintain weight",
        "Dietary Restrictions": ["Vegetarian", "Vegan"]
    },
    {
        "Meal": "Ful Medames",
        "Ingredients": "Fava Beans, Olive Oil, Garlic, Lemon Juice, Cumin, Salt",
        "Ingredients Weight (grams)": "100, 10, 5, 10, 2, 2",
        "Meal Type": "Breakfast",
        "Calories": 300,
        "Fat (grams)": 8,
        "Carbohydrates (grams)": 45,
        "Protein (grams)": 15,
        "Calcium (mg)": 100,
        "Vitamin C (mg)": 4,
        "Type": "Maintain weight",
        "Dietary Restrictions": ["Vegetarian", "Vegan"]
    },
    {
        "Meal": "Mahshi",
        "Ingredients": "Zucchini, Eggplant, Bell Peppers, Tomatoes, Rice, Onion, Garlic, Parsley, Dill, Tomato Sauce",
        "Ingredients Weight (grams)": "100, 100, 50, 100, 50, 50, 10, 10, 10, 100",
        "Meal Type": "Dinner",
        "Calories": 350,
        "Fat (grams)": 7,
        "Carbohydrates (grams)": 60,
        "Protein (grams)": 10,
        "Calcium (mg)": 80,
        "Vitamin C (mg)": 25,
        "Type": "Maintain weight",
        "Dietary Restrictions": ["Vegetarian", "Vegan"]
    },
    {
        "Meal": "Molokhia",
        "Ingredients": "Jute Leaves, Garlic, Coriander, Chicken Broth, Olive Oil, Lemon Juice",
        "Ingredients Weight (grams)": "100, 5, 5, 200, 10, 10",
        "Meal Type": "Dinner",
        "Calories": 250,
        "Fat (grams)": 15,
        "Carbohydrates (grams)": 10,
        "Protein (grams)": 20,
        "Calcium (mg)": 150,
        "Vitamin C (mg)": 30,
        "Type": "Maintain weight",
        "Dietary Restrictions": ["Halal"]
    },
    {
        "Meal": "Kebda Iskandarani",
        "Ingredients": "Liver, Onion, Garlic, Vinegar, Cumin, Coriander, Butter",
        "Ingredients Weight (grams)": "100, 50, 5, 10, 2, 2, 10",
        "Meal Type": "Dinner",
        "Calories": 280,
        "Fat (grams)": 12,
        "Carbohydrates (grams)": 5,
        "Protein (grams)": 25,
        "Calcium (mg)": 30,
        "Vitamin C (mg)": 2,
        "Type": "Maintain weight",
        "Dietary Restrictions": []
    },
    {
        "Meal": "Mulukhiyah Soup",
        "Ingredients": "Jute Leaves, Chicken, Garlic, Coriander, Lemon, Olive Oil",
        "Ingredients Weight (grams)": "100, 100, 5, 5, 10, 10",
        "Meal Type": "Dinner",
        "Calories": 320,
        "Fat (grams)": 18,
        "Carbohydrates (grams)": 10,
        "Protein (grams)": 28,
        "Calcium (mg)": 150,
        "Vitamin C (mg)": 30,
        "Type": "Maintain weight",
        "Dietary Restrictions": ["Halal"]
    },
    {
        "Meal": "Roz Bel Laban",
        "Ingredients": "Rice, Milk, Sugar, Vanilla",
        "Ingredients Weight (grams)": "100, 150, 30, 2",
        "Meal Type": "Dessert",
        "Calories": 280,
        "Fat (grams)": 5,
        "Carbohydrates (grams)": 55,
        "Protein (grams)": 6,
        "Calcium (mg)": 200,
        "Vitamin C (mg)": 0,
        "Type": "Maintain weight",
        "Dietary Restrictions": ["Vegetarian"]
    },
    {
        "Meal": "Shakshuka",
        "Ingredients": "Tomatoes, Bell Peppers, Onions, Eggs, Garlic, Cumin, Paprika, Chili Flakes",
        "Ingredients Weight (grams)": "200, 100, 50, 4, 5, 2, 2, 2",
        "Meal Type": "Breakfast",
        "Calories": 320,
        "Fat (grams)": 18,
        "Carbohydrates (grams)": 15,
        "Protein (grams)": 15,
        "Calcium (mg)": 80,
        "Vitamin C (mg)": 30,
        "Type": "Maintain weight",
        "Dietary Restrictions": ["Vegetarian"]
    },
    {
        "Meal": "Feseekh",
        "Ingredients": "Salted Fish, Bread",
        "Ingredients Weight (grams)": "150, 100",
        "Meal Type": "Breakfast",
        "Calories": 220,
        "Fat (grams)": 10,
        "Carbohydrates (grams)": 15,
        "Protein (grams)": 20,
        "Calcium (mg)": 100,
        "Vitamin C (mg)": 2,
        "Type": "Maintain weight",
        "Dietary Restrictions": []
    },
    {
        "Meal": "Ta'meya (Falafel)",
        "Ingredients": "Fava Beans, Coriander, Parsley, Garlic, Onion, Cumin, Flour",
        "Ingredients Weight (grams)": "100, 20, 20, 5, 50, 2, 20",
        "Meal Type": "Lunch",
        "Calories": 250,
        "Fat (grams)": 10,
        "Carbohydrates (grams)": 35,
        "Protein (grams)": 10,
        "Calcium (mg)": 60,
        "Vitamin C (mg)": 6,
        "Type": "Maintain weight",
        "Dietary Restrictions": ["Vegetarian", "Vegan"]
    },
    {
        "Meal": "Macarona Bechamel",
        "Ingredients": "Macaroni, Bechamel Sauce (Butter, Flour, Milk), Ground Beef, Tomato Sauce",
        "Ingredients Weight (grams)": "100, 150, 100, 50",
        "Meal Type": "Dinner",
        "Calories": 450,
        "Fat (grams)": 20,
        "Carbohydrates (grams)": 40,
        "Protein (grams)": 25,
        "Calcium (mg)": 150,
        "Vitamin C (mg)": 8,
        "Type": "Maintain weight",
        "Dietary Restrictions": []
    },
    {
        "Meal": "Kunafa",
        "Ingredients": "Kataifi Dough, Cheese, Sugar Syrup, Butter",
        "Ingredients Weight (grams)": "100, 100, 50, 20",
        "Meal Type": "Dessert",
        "Calories": 400,
        "Fat (grams)": 22,
        "Carbohydrates (grams)": 40,
        "Protein (grams)": 10,
        "Calcium (mg)": 200,
        "Vitamin C (mg)": 0,
        "Type": "Maintain weight",
        "Dietary Restrictions": ["Vegetarian"]
    },
    {
        "Meal": "Baladi Bread with Fava Beans",
        "Ingredients": "Baladi Bread, Fava Beans, Olive Oil, Lemon Juice, Salt",
        "Ingredients Weight (grams)": "100, 100, 10, 5, 2",
        "Meal Type": "Breakfast",
        "Calories": 300,
        "Fat (grams)": 8,
        "Carbohydrates (grams)": 45,
        "Protein (grams)": 12,
        "Calcium (mg)": 50,
        "Vitamin C (mg)": 6,
        "Type": "Maintain weight",
        "Dietary Restrictions": ["Vegetarian", "Vegan"]
    },
    {
        "Meal": "Vegetarian Kushari",
        "Ingredients": "Rice, Lentils, Pasta, Chickpeas, Tomato Sauce, Fried Onions",
        "Ingredients Weight (grams)": "100, 50, 50, 50, 100, 20",
        "Meal Type": "Lunch",
        "Calories": 400,
        "Fat (grams)": 10,
        "Carbohydrates (grams)": 70,
        "Protein (grams)": 15,
        "Calcium (mg)": 50,
        "Vitamin C (mg)": 10,
        "Type": "Maintain weight",
        "Dietary Restrictions": ["Vegetarian"]
    },
    {
        "Meal": "Vegan Mahshi",
        "Ingredients": "Zucchini, Eggplant, Bell Peppers, Tomatoes, Rice, Onion, Garlic, Parsley, Dill, Tomato Sauce",
        "Ingredients Weight (grams)": "100, 100, 50, 100, 50, 50, 10, 10, 10, 100",
        "Meal Type": "Dinner",
        "Calories": 350,
        "Fat (grams)": 7,
        "Carbohydrates (grams)": 60,
        "Protein (grams)": 10,
        "Calcium (mg)": 80,
        "Vitamin C (mg)": 25,
        "Type": "Maintain weight",
        "Dietary Restrictions": ["Vegetarian", "Vegan"]
    },
    {
        "Meal": "Gluten-Free Kebda Iskandarani",
        "Ingredients": "Liver, Onion, Garlic, Vinegar, Cumin, Coriander, Olive Oil",
        "Ingredients Weight (grams)": "100, 50, 5, 10, 2, 2, 10",
        "Meal Type": "Dinner",
        "Calories": 280,
        "Fat (grams)": 12,
        "Carbohydrates (grams)": 5,
        "Protein (grams)": 25,
        "Calcium (mg)": 30,
        "Vitamin C (mg)": 2,
        "Type": "Maintain weight",
        "Dietary Restrictions": ["Gluten-Free"]
    },
    {
        "Meal": "Halal Molokhia",
        "Ingredients": "Jute Leaves, Chicken Broth, Garlic, Coriander, Olive Oil, Lemon Juice",
        "Ingredients Weight (grams)": "100, 200, 5, 5, 10, 10",
        "Meal Type": "Dinner",
        "Calories": 250,
        "Fat (grams)": 15,
        "Carbohydrates (grams)": 10,
        "Protein (grams)": 20,
        "Calcium (mg)": 150,
        "Vitamin C (mg)": 30,
        "Type": "Maintain weight",
        "Dietary Restrictions": ["Halal"]
    },
    {
        "Meal": "Low-Carb Shakshuka",
        "Ingredients": "Tomatoes, Bell Peppers, Onions, Eggs, Garlic, Cumin, Paprika, Chili Flakes",
        "Ingredients Weight (grams)": "200, 100, 50, 4, 5, 2, 2, 2",
        "Meal Type": "Breakfast",
        "Calories": 320,
        "Fat (grams)": 18,
        "Carbohydrates (grams)": 10,
        "Protein (grams)": 15,
        "Calcium (mg)": 80,
        "Vitamin C (mg)": 30,
        "Type": "Maintain weight",
        "Dietary Restrictions": ["Low-Carb"]
    }

]

# Create DataFrame
df = pd.DataFrame(data)


# Define color mappings for each meal type
color_mapping = {
    "Breakfast": "#FFA07A",  # Light Salmon
    "Lunch": "#87CEEB",      # Sky Blue
    "Dinner": "#90EE90",     # Light Green
    "Snack": "#FFD700"       # Gold
}

@st.cache  # Cache the function result based on input parameters
def generate_meal_data(df, min_calories, max_calories, min_fat, max_fat, num_breakfast, num_lunch, num_dinner, num_snacks, dietary_restrictions, excluded_ingredients):
    return generate_meals(df, min_calories, max_calories, min_fat, max_fat, num_breakfast, num_lunch, num_dinner, num_snacks, dietary_restrictions, excluded_ingredients)
# Filter meals based on user preferences
def filter_meals(df, min_calories, max_calories, min_fat, max_fat):
    filtered_df = df[(df['Calories'] > min_calories) & (df['Calories'] < max_calories)
                     & (df['Fat (grams)'] > min_fat) & (df['Fat (grams)'] < max_fat)]
    return filtered_df

def generate_meals(df, min_calories, max_calories, min_fat, max_fat, num_breakfast, num_lunch, num_dinner, num_snacks, dietary_restrictions, excluded_ingredients):
    st.write("Input values:")
    st.write(f"min_calories: {min_calories}, max_calories: {max_calories}, min_fat: {min_fat}, max_fat: {max_fat}")
    
    # Filter meals based on calorie and fat restrictions
    filtered_df = df[(df['Calories'] >= min_calories) & (df['Calories'] <= max_calories) & (df['Fat (grams)'] >= min_fat) & (df['Fat (grams)'] <= max_fat)]
    
    # Filter out meals based on dietary restrictions
    for restriction in dietary_restrictions:
        filtered_df = filtered_df[~filtered_df['Ingredients'].str.contains(restriction, case=False)]
    
    # Exclude meals based on specified ingredients
    if excluded_ingredients:
        excluded_ingredients_list = [ingredient.strip().lower() for ingredient in excluded_ingredients.split(',')]
        for ingredient in excluded_ingredients_list:
            filtered_df = filtered_df[~filtered_df['Ingredients'].str.contains(ingredient, case=False)]
    
    suggested_meals = {}
    for meal_type, num_meals in zip(["Breakfast", "Lunch", "Dinner", "Snack"], [num_breakfast, num_lunch, num_dinner, num_snacks]):
        meals_available = filtered_df[filtered_df['Meal Type'] == meal_type]
        if len(meals_available) > 0:
            if len(meals_available) >= num_meals:
                suggested_meals[meal_type] = meals_available.sample(n=num_meals, replace=False)
            else:
                st.warning(f"Not enough {meal_type} meals available. Showing all available.")
                suggested_meals[meal_type] = meals_available
        else:
            st.warning(f"No {meal_type} meals available.")
            suggested_meals[meal_type] = pd.DataFrame(columns=df.columns)  # Empty DataFrame
    return suggested_meals

def main():
    st.title("Daily Meal Planner")

    min_calories = st.sidebar.number_input("Minimum Calories", min_value=0, value=0)
    max_calories = st.sidebar.number_input("Maximum Calories", min_value=0, value=2500)
    num_breakfast = st.sidebar.number_input("Number of Breakfast Meals", min_value=0, value=2)
    num_lunch = st.sidebar.number_input("Number of Lunch Meals", min_value=0, value=2)
    num_dinner = st.sidebar.number_input("Number of Dinner Meals", min_value=0, value=3)
    num_snacks = st.sidebar.number_input("Number of Snack Meals", min_value=0, value=1)
    
    min_fat = st.sidebar.number_input("Minimum Fat (grams)", min_value=0, value=0)
    max_fat = st.sidebar.number_input("Maximum Fat (grams)", min_value=0, value=100)

    dietary_restrictions = st.sidebar.multiselect("Dietary Restrictions", ["Vegetarian", "Vegan", "Gluten-Free"])
    
    excluded_ingredients = st.sidebar.text_input("Excluded Ingredients (comma-separated)")

    if min_calories > max_calories:
        st.warning("Minimum calories cannot be greater than maximum calories. Please adjust the values.")
        return

    if st.button("Generate Meals"):
        suggested_meals = generate_meals(df, min_calories, max_calories, min_fat, max_fat, num_breakfast, num_lunch, num_dinner, num_snacks, dietary_restrictions, excluded_ingredients)
        # Display generated meals...
        total_calories = sum(meal['Calories'].sum() for meal in suggested_meals.values())
        if total_calories > max_calories:
            st.warning("Total calories of selected meals exceed the maximum calories. Please adjust the meal quantities.")
            return

        st.info(f"Total calories of selected meals: {total_calories} kcal (Maximum: {max_calories} kcal)")

        st.subheader("Generated Meals")
        for meal_type, meal_data in suggested_meals.items():
            st.subheader(meal_type)
            meal_data_styled = meal_data.style.apply(lambda row: [f"background-color: {color_mapping.get(meal_type, '#FFFFFF')}" for _ in row], axis=1)
            st.write(meal_data_styled)

        # Pie chart for meal type distribution
        meal_counts = {meal_type: len(meal_data) for meal_type, meal_data in suggested_meals.items()}
        labels = list(meal_counts.keys())
        values = list(meal_counts.values())

        st.write("Meal Type Distribution:")
        st.pyplot(values, labels=labels, autopct='%1.1f%%', startangle=90)

        st.subheader("Generated Meals")
        for meal_type, meal_data in suggested_meals.items():
            st.subheader(meal_type)
            meal_data_styled = meal_data.style.apply(lambda row: [f"background-color: {color_mapping.get(meal_type, '#FFFFFF')}" for _ in row], axis=1)
            st.write(meal_data_styled)

if __name__ == "__main__":
    main()
