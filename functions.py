# Function to calculate BMI and return a category and response
def calculate_bmi(weight, height, age):
    """
    Calculates BMI based on weight and height, and returns a BMI category and response message.

    Args:
        weight (float): Weight in kilograms.
        height (float): Height in meters.
        age (int): Age of the user (not used in calculation but can be used for future extensions).

    Returns:
        list: A list containing a response message and the BMI category.
    """
    bmi = weight / (height * height)  # BMI formula: weight (kg) / height^2 (m^2)

    # Determine BMI category and response
    if bmi < 19:
        bmi_category = "Underweight"
        response = ("Based on your BMI, it seems like you're underweight. "
                    "I can help you create a personalized diet plan and workout routine to help you gain weight in a healthy way.")
    elif bmi < 25:
        bmi_category = "Healthy Weight"
        response = ("Congratulations! Based on your BMI, it seems like you're at a healthy weight. "
                    "I can help you maintain this weight and improve your overall fitness with a personalized diet and workout plan.")
    elif bmi < 30:
        bmi_category = "Overweight"
        response = ("Based on your BMI, it seems like you're overweight. "
                    "I can help you create a personalized diet plan and workout routine to help you achieve your weight loss goals in a healthy way.")
    else:
        bmi_category = "Obese"
        response = ("Based on your BMI, it seems like you're obese. "
                    "I can help you create a personalized diet plan and workout routine to help you achieve your weight loss goals in a healthy way. "
                    "It's important to start making changes as soon as possible to improve your health.")

    return [response, bmi_category]


# Function to create a workout plan based on BMI and fitness level
def create_workout_plan_with_BMI(fitness_level, bmi_category):
    """
    Creates a personalized workout plan based on the user's BMI category and fitness level.

    Args:
        fitness_level (str): User's fitness level ('beginner', 'intermediate', 'advanced').
        bmi_category (str): User's BMI category ('Underweight', 'Healthy Weight', 'Overweight', 'Obese').

    Returns:
        str: A detailed workout plan tailored to the user's BMI and fitness level.
    """
    print(bmi_category)  # Debugging: Print the BMI category
    response = ""

    # Workout plan for "Underweight" category
    if bmi_category.lower() == "underweight":
        if fitness_level.lower() == 'beginner':
            response = ("Based on your BMI, it's important to focus on gaining weight in a healthy way. "
                        "As a beginner, I recommend the following workout plan:\n\n"
                        "1. Resistance Training: 3 days per week (Monday, Wednesday, and Friday)\n"
                        "   - Bodyweight squats: 3 sets of 10 reps\n"
                        "   - Push-ups: 3 sets of 10 reps\n"
                        "   - Dumbbell curls: 3 sets of 10 reps\n"
                        "   - Dumbbell shoulder press: 3 sets of 10 reps\n\n"
                        "2. Cardiovascular Exercise: 2-3 days per week (Tuesday, Thursday, and Saturday)\n"
                        "   - 20-30 minutes of low-intensity cardio, such as walking, cycling, or swimming.")
        elif fitness_level.lower() == 'intermediate':
            response = ("Based on your BMI, it's important to focus on gaining weight in a healthy way. "
                        "As an intermediate, I recommend the following workout plan:\n\n"
                        "1. Resistance Training: 4 days per week (Monday, Tuesday, Thursday, and Friday)\n"
                        "   - Barbell squats: 3 sets of 8 reps\n"
                        "   - Barbell bench press: 3 sets of 8 reps\n"
                        "   - Barbell rows: 3 sets of 8 reps\n"
                        "   - Barbell shoulder press: 3 sets of 8 reps\n"
                        "   - Barbell curls: 3 sets of 8 reps\n"
                        "   - Tricep pushdowns: 3 sets of 8 reps\n\n"
                        "2. Cardiovascular Exercise: 3-4 days per week (Wednesday, Saturday, and Sunday)\n"
                        "   - 30-40 minutes of moderate-intensity cardio, such as running, cycling, or swimming.")
        elif fitness_level.lower() == 'advanced':
            response = ("Based on your BMI, it's important to focus on gaining weight in a healthy way. "
                        "As an advanced individual, I recommend the following workout plan:\n\n"
                        "1. Resistance Training: 5 days per week (Monday, Tuesday, Wednesday, Thursday, and Friday)\n"
                        "   - Barbell squats: 4 sets of 8 reps\n"
                        "   - Barbell bench press: 4 sets of 8 reps\n"
                        "   - Barbell rows: 4 sets of 8 reps\n"
                        "   - Barbell shoulder press: 4 sets of 8 reps\n"
                        "   - Barbell curls: 4 sets of 8 reps\n"
                        "   - Tricep pushdowns: 4 sets of 8 reps\n\n"
                        "2. Cardiovascular Exercise: 3-4 days per week (Wednesday, Saturday, and Sunday)\n"
                        "   - 40-60 minutes of high-intensity cardio, such as sprinting, cycling, or swimming.")

    # Workout plan for "Healthy Weight" category
    elif bmi_category.lower() == "healthy weight":
        if fitness_level.lower() == 'beginner':
            response = ("Based on your BMI, it's important to focus on maintaining your weight to stay healthy. "
                        "As a beginner, I recommend the following workout plan:\n\n"
                        "1. Resistance Training: 3 days per week (Monday, Wednesday, and Friday)\n"
                        "   - Bodyweight squats: 4 sets of 10 reps\n"
                        "   - Push-ups: 3 sets of 20 reps\n"
                        "   - Dumbbell curls: 3 sets of 20 reps\n"
                        "   - Dumbbell shoulder press: 3 sets of 20 reps\n\n"
                        "2. Cardiovascular Exercise: 2-3 days per week (Tuesday, Thursday, and Saturday)\n"
                        "   - 20-30 minutes of low-intensity cardio, such as walking, cycling, or swimming.")
        elif fitness_level.lower() == 'intermediate':
            response = ("Based on your BMI, it's important to focus on maintaining your weight to stay healthy. "
                        "As an intermediate, I recommend the following workout plan:\n\n"
                        "1. Resistance Training: 4 days per week (Monday, Tuesday, Thursday, and Friday)\n"
                        "   - Barbell squats: 4 sets of 8 reps\n"
                        "   - Barbell bench press: 4 sets of 8 reps\n"
                        "   - Barbell rows: 4 sets of 8 reps\n"
                        "   - Barbell shoulder press: 4 sets of 8 reps\n"
                        "   - Barbell curls: 4 sets of 8 reps\n"
                        "   - Tricep pushdowns: 4 sets of 8 reps\n\n"
                        "2. Cardiovascular Exercise: 3-4 days per week (Wednesday, Saturday, and Sunday)\n"
                        "   - 30-40 minutes of moderate-intensity cardio, such as running, cycling, or swimming.")
        elif fitness_level.lower() == 'advanced':
            response = ("Based on your BMI, it's important to focus on maintaining your weight to stay healthy. "
                        "As an advanced individual, I recommend the following workout plan:\n\n"
                        "1. Resistance Training: 5 days per week (Monday, Tuesday, Wednesday, Thursday, and Friday)\n"
                        "   - Barbell squats: 4 sets of 8 reps\n"
                        "   - Barbell bench press: 4 sets of 8 reps\n"
                        "   - Barbell rows: 4 sets of 8 reps\n"
                        "   - Barbell shoulder press: 4 sets of 8 reps\n"
                        "   - Barbell curls: 4 sets of 8 reps\n"
                        "   - Tricep pushdowns: 4 sets of 8 reps\n\n"
                        "2. Cardiovascular Exercise: 3-4 days per week (Wednesday, Saturday, and Sunday)\n"
                        "   - 40-60 minutes of high-intensity cardio, such as sprinting, cycling, or swimming.")

    # Workout plan for "Overweight" category
    elif bmi_category.lower() == "overweight":
        if fitness_level.lower() == 'beginner':
            response = ("Based on your BMI, it's important to focus on losing weight in a healthy way. "
                        "As a beginner, I recommend the following workout plan:\n\n"
                        "1. Circuit Training: 2-3 days per week (Tuesday, Thursday, and optionally Saturday)\n"
                        "   - 3 circuits of 10-12 reps each of the following exercises:\n"
                        "     - Bodyweight squats\n"
                        "     - Push-ups\n"
                        "     - Dumbbell rows\n"
                        "     - Dumbbell shoulder press\n"
                        "     - Plank\n\n"
                        "2. Cardiovascular Exercise: 3-4 days per week (Monday, Wednesday, and Friday)\n"
                        "   - 20-30 minutes of low-intensity cardio, such as walking, cycling, or elliptical machine.")
        elif fitness_level.lower() == 'intermediate':
            response = ("Based on your BMI, it's important to focus on losing weight in a healthy way. "
                        "As an intermediate, I recommend the following workout plan:\n\n"
                        "1. Resistance Training: 3-4 days per week (Monday, Tuesday, Thursday, and Friday)\n"
                        "   - Barbell squats: 3 sets of 10 reps\n"
                        "   - Barbell bench press: 3 sets of 10 reps\n"
                        "   - Dumbbell rows: 3 sets of 10 reps\n"
                        "   - Dumbbell shoulder press: 3 sets of 10 reps\n"
                        "   - Plank: 3 sets of 30 seconds\n\n"
                        "2. Cardiovascular Exercise: 4-5 days per week (Monday, Wednesday, Friday, and optionally Sunday)\n"
                        "   - 30-40 minutes of moderate-intensity cardio, such as jogging, cycling, or elliptical machine.")
        elif fitness_level.lower() == 'advanced':
            response = ("Based on your BMI, it's important to focus on losing weight in a healthy way. "
                        "As an advanced individual, I recommend the following workout plan:\n\n"
                        "1. Strength Training: 4-5 days per week (Monday, Tuesday, Thursday, and Friday)\n"
                        "   - Barbell squats: 4 sets of 8 reps\n"
                        "   - Barbell bench press: 4 sets of 8 reps\n"
                        "   - Barbell rows: 4 sets of 8 reps\n"
                        "   - Barbell shoulder press: 4 sets of 8 reps\n"
                        "   - Deadlifts: 4 sets of 8 reps\n\n"
                        "2. Cardiovascular Exercise: 5-6 days per week (Monday, Wednesday, Friday, and optionally Sunday)\n"
                        "   - 45-60 minutes of high-intensity cardio, such as running, cycling, or rowing machine.")

    # Workout plan for "Obese" category
    elif bmi_category.lower() == "obese":
        if fitness_level.lower() == 'beginner':
            response = ("Based on your BMI, it's important to focus on seriously losing weight in a healthy way. "
                        "As a beginner, I recommend the following workout plan:\n\n"
                        "1. Resistance Training: 2-3 days per week (Tuesday, Thursday, and optionally Saturday)\n"
                        "   - 3 sets of 12-15 reps each of the following exercises:\n"
                        "     - Leg press machine\n"
                        "     - Chest press machine\n"
                        "     - Lat pulldown machine\n"
                        "     - Seated row machine\n"
                        "     - Shoulder press machine\n\n"
                        "2. Cardiovascular Exercise: 3-4 days per week (Monday, Wednesday, and Friday)\n"
                        "   - 20-30 minutes of low-intensity cardio, such as walking, cycling, or elliptical machine.")
        elif fitness_level.lower() == 'intermediate':
            response = ("Based on your BMI, it's important to focus on seriously losing weight in a healthy way. "
                        "As an intermediate, I recommend the following workout plan:\n\n"
                        "1. Resistance Training: 3-4 days per week (Monday, Tuesday, Thursday, and Friday)\n"
                        "   - Dumbbell squats: 3 sets of 12 reps\n"
                        "   - Dumbbell bench press: 3 sets of 12 reps\n"
                        "   - Dumbbell rows: 3 sets of 12 reps\n"
                        "   - Dumbbell shoulder press: 3 sets of 12 reps\n"
                        "   - Plank: 3 sets of 30 seconds\n\n"
                        "2. Cardiovascular Exercise: 4-5 days per week (Monday, Wednesday, Friday, and optionally Sunday)\n"
                        "   - 30-40 minutes of moderate-intensity cardio, such as jogging, cycling, or elliptical machine.")
        elif fitness_level.lower() == 'advanced':
            response = ("Based on your BMI, it's important to focus on seriously losing weight in a healthy way. "
                        "As an advanced individual, I recommend the following workout plan:\n\n"
                        "1. Resistance Training: 4-5 days per week (Monday, Tuesday, Thursday, and Friday)\n"
                        "   - Barbell squats: 4 sets of 8 reps\n"
                        "   - Barbell bench press: 4 sets of 8 reps\n"
                        "   - Barbell rows: 4 sets of 8 reps\n"
                        "   - Barbell shoulder press: 4 sets of 8 reps\n"
                        "   - Crunches: 3 sets of 1 minute\n\n"
                        "2. Cardiovascular Exercise: 5-6 days per week (Monday, Wednesday, Friday, and optionally Sunday)\n"
                        "   - 45-60 minutes of high-intensity cardio, such as running, cycling, or rowing machine.")

    return response


# Function to create a diet plan based on BMI and fitness level
def create_diet_plan_with_BMI(fitness_level, bmi_category):
    """
    Creates a personalized diet plan based on the user's BMI category and fitness level.

    Args:
        fitness_level (str): User's fitness level ('beginner', 'intermediate', 'advanced').
        bmi_category (str): User's BMI category ('Underweight', 'Healthy Weight', 'Overweight', 'Obese').

    Returns:
        str: A detailed diet plan tailored to the user's BMI and fitness level.
    """
    # Diet plan for "Underweight" category
    if bmi_category.lower() == "underweight":
        if fitness_level.lower() == "beginner":
            return ("Here is a sample diet plan to gain weight for a beginner who is underweight:\n\n"
                    "Breakfast: Oatmeal with milk, banana, and walnuts.\n"
                    "Snack: Greek yogurt with mixed berries and honey.\n"
                    "Lunch: Grilled chicken wrap with avocado, tomato, and spinach.\n"
                    "Snack: Hummus with carrots and whole-grain crackers.\n"
                    "Dinner: Baked salmon with quinoa and roasted vegetables (such as broccoli and sweet potato).\n"
                    "Snack: Apple slices with almond butter.")
        elif fitness_level.lower() == "intermediate":
            return ("Here is a sample diet plan to gain weight for an intermediate person who is underweight:\n\n"
                    "Breakfast: Whole-grain toast with avocado and a boiled egg.\n"
                    "Snack: Mixed nuts and dried fruit.\n"
                    "Lunch: Grilled chicken breast with brown rice and roasted vegetables (such as carrots and zucchini).\n"
                    "Snack: Greek yogurt with mixed berries and honey.\n"
                    "Dinner: Baked salmon with quinoa and roasted vegetables (such as broccoli and sweet potato).\n"
                    "Snack: Apple slices with almond butter.")
        elif fitness_level.lower() == "advanced":
            return ("Here is a sample diet plan to gain weight for an advanced person who is underweight:\n\n"
                    "Breakfast: Avocado toast with smoked salmon and a poached egg.\n"
                    "Snack: Protein shake with mixed berries and almond milk.\n"
                    "Lunch: Grilled chicken breast with quinoa and roasted vegetables (such as broccoli, cauliflower, and sweet potato).\n"
                    "Snack: Greek yogurt with mixed nuts and honey.\n"
                    "Dinner: Baked salmon with quinoa and roasted vegetables (such as broccoli, cauliflower, and sweet potato).\n"
                    "Snack: Apple slices with almond butter.")

    # Diet plan for "Healthy Weight" category
    elif bmi_category.lower() == "healthy weight":
        if fitness_level.lower() == "beginner":
            return ("Here is a sample diet plan to maintain weight for a beginner who has a healthy weight:\n\n"
                    "Breakfast: Greek yogurt with mixed berries and honey.\n"
                    "Snack: Apple slices with almond butter.\n"
                    "Lunch: Grilled chicken breast with roasted vegetables (such as broccoli, carrots, and zucchini) and brown rice.\n"
                    "Snack: Carrots and hummus.\n"
                    "Dinner: Baked salmon with roasted sweet potatoes and green beans.\n"
                    "Snack: Mixed nuts and dried fruit.")
        elif fitness_level.lower() == "intermediate":
            return ("Here is a sample diet plan to maintain weight for an intermediate person who has a healthy weight:\n\n"
                    "Breakfast: Scrambled eggs with spinach and whole-grain toast.\n"
                    "Snack: Greek yogurt with mixed nuts and honey.\n"
                    "Lunch: Grilled chicken salad with mixed greens, tomatoes, and vinaigrette dressing.\n"
                    "Snack: Apple slices with almond butter.\n"
                    "Dinner: Baked salmon with quinoa and roasted vegetables (such as asparagus and bell peppers).\n"
                    "Snack: Carrots and hummus.")
        elif fitness_level.lower() == "advanced":
            return ("Here is a sample diet plan to maintain weight for an advanced person who has a healthy weight:\n\n"
                    "Breakfast: Quinoa breakfast bowl with avocado, poached egg, and mixed greens.\n"
                    "Snack: Protein shake with mixed berries and almond milk.\n"
                    "Lunch: Grilled chicken breast with mixed vegetables (such as bell peppers, onions, and mushrooms) and sweet potato.\n"
                    "Snack: Carrots and hummus.\n"
                    "Dinner: Baked salmon with quinoa and roasted vegetables (such as asparagus and bell peppers).\n"
                    "Snack: Mixed nuts and dried fruit.")

    # Diet plan for "Overweight" category
    elif bmi_category.lower() == "overweight":
        if fitness_level.lower() == "beginner":
            return ("Here is a sample diet plan to lose weight for a beginner who is overweight:\n\n"
                    "Breakfast: Greek yogurt with mixed berries and honey.\n"
                    "Snack: Apple slices with almond butter.\n"
                    "Lunch: Grilled chicken breast with roasted vegetables (such as broccoli, carrots, and zucchini) and brown rice.\n"
                    "Snack: Carrots and hummus.\n"
                    "Dinner: Baked salmon with roasted sweet potatoes and green beans.\n"
                    "Snack: Mixed nuts and dried fruit.")
        elif fitness_level.lower() == "intermediate":
            return ("Here is a sample diet plan to lose weight for an intermediate person who is overweight:\n\n"
                    "Breakfast: Scrambled eggs with spinach and whole-grain toast.\n"
                    "Snack: Greek yogurt with mixed nuts and honey.\n"
                    "Lunch: Grilled chicken salad with mixed greens, tomatoes, and vinaigrette dressing.\n"
                    "Snack: Carrots and hummus.\n"
                    "Dinner: Baked salmon with quinoa and roasted vegetables (such as asparagus and bell peppers).\n"
                    "Snack: Apple slices with almond butter.")
        elif fitness_level.lower() == "advanced":
            return ("Here is a sample diet plan to lose weight for an advanced person who is overweight:\n\n"
                    "Breakfast: Quinoa breakfast bowl with avocado, poached egg, and mixed greens.\n"
                    "Snack: Protein shake with mixed berries and almond milk.\n"
                    "Lunch: Grilled chicken breast with mixed vegetables (such as bell peppers, onions, and mushrooms) and sweet potato.\n"
                    "Snack: Carrots and hummus.\n"
                    "Dinner: Baked salmon with quinoa and roasted vegetables (such as asparagus and bell peppers).\n"
                    "Snack: Mixed nuts and dried fruit.")

    # Diet plan for "Obese" category
    elif bmi_category.lower() == "obese":
        if fitness_level.lower() == "beginner":
            return ("Here is a sample diet plan to seriously lose weight for a beginner who is obese:\n\n"
                    "Breakfast: Greek yogurt with mixed berries and honey.\n"
                    "Snack: Apple slices with almond butter.\n"
                    "Lunch: Grilled chicken breast with mixed vegetables (such as broccoli, carrots, and zucchini) and brown rice.\n"
                    "Snack: Carrots and hummus.\n"
                    "Dinner: Baked salmon with roasted sweet potatoes and green beans.\n"
                    "Snack: Mixed nuts and dried fruit.")
        elif fitness_level.lower() == "intermediate":
            return ("Here is a sample diet plan to seriously lose weight for an intermediate person who is obese:\n\n"
                    "Breakfast: Scrambled eggs with spinach and whole-grain toast.\n"
                    "Snack: Greek yogurt with mixed nuts and honey.\n"
                    "Lunch: Grilled chicken salad with mixed greens, tomatoes, and vinaigrette dressing.\n"
                    "Snack: Carrots and hummus.\n"
                    "Dinner: Baked salmon with quinoa and roasted vegetables (such as asparagus and bell peppers).\n"
                    "Snack: Apple slices with almond butter.")
        elif fitness_level.lower() == "advanced":
            return ("Here is a sample diet plan to seriously lose weight for an advanced person who is obese:\n\n"
                    "Breakfast: Quinoa breakfast bowl with avocado, poached egg, and mixed greens.\n"
                    "Snack: Protein shake with mixed berries and almond milk.\n"
                    "Lunch: Grilled chicken breast with mixed vegetables (such as bell peppers, onions, and mushrooms) and sweet potato.\n"
                    "Snack: Carrots and hummus.\n"
                    "Dinner: Baked salmon with quinoa and roasted vegetables (such as asparagus and bell peppers).\n"
                    "Snack: Mixed nuts and dried fruit.")

    # If no valid BMI category is provided
    return "No diet plan available for the given inputs."


# Function to create a general workout plan based on fitness level
def create_workout_plan(fitness_level):
    """
    Creates a general workout plan based on the user's fitness level without considering BMI.

    Args:
        fitness_level (str): User's fitness level ('beginner', 'intermediate', 'advanced').

    Returns:
        str: A general workout plan tailored to the user's fitness level.
    """
    # Workout plan for "Beginner" fitness level
    if fitness_level.lower() == 'beginner':
        return ("Great! As a beginner, it's important to start with simple exercises and gradually build up your strength and endurance.\n"
                "Here's a sample workout plan:\n\n"
                "Monday: 10 push-ups, 10 squats, 10 lunges (each leg), 10 minutes of jogging\n"
                "Tuesday: Rest day\n"
                "Wednesday: 15 push-ups, 15 squats, 15 lunges (each leg), 15 minutes of jumping jacks\n"
                "Thursday: Rest day\n"
                "Friday: 20 push-ups, 20 squats, 20 lunges (each leg), 20 minutes of cycling\n"
                "Saturday: Rest day\n"
                "Sunday: 30 minutes of walking or hiking.\n\n"
                "Remember to listen to your body and take rest days as needed. As you get stronger, you can gradually increase the intensity and duration of your workouts.")

    # Workout plan for "Intermediate" fitness level
    elif fitness_level.lower() == 'intermediate':
        return ("Awesome! As an intermediate exerciser, you've already built a foundation of strength and endurance.\n"
                "Here's a sample workout plan:\n\n"
                "Monday: 20 push-ups, 20 squats, 20 lunges (each leg), 20 minutes of jogging\n"
                "Tuesday: Rest day\n"
                "Wednesday: 30 push-ups, 30 squats, 30 lunges (each leg), 30 minutes of jumping jacks\n"
                "Thursday: Rest day\n"
                "Friday: 40 push-ups, 40 squats, 40 lunges (each leg), 40 minutes of cycling\n"
                "Saturday: Rest day\n"
                "Sunday: 60 minutes of walking or hiking.\n\n"
                "Remember to challenge yourself but also listen to your body and take rest days as needed. You can also consider adding new exercises or activities to keep your workouts interesting and varied.")

    # Workout plan for "Advanced" fitness level
    elif fitness_level.lower() == 'advanced':
        return ("Impressive! As an advanced exerciser, you have a high level of fitness and strength.\n"
                "Here's a sample workout plan:\n\n"
                "Monday: 30 push-ups, 30 squats, 30 lunges (each leg), 30 minutes of high-intensity interval training (HIIT)\n"
                "Tuesday: Rest day\n"
                "Wednesday: 40 push-ups, 40 squats, 40 lunges (each leg), 40 minutes of cycling or running\n"
                "Thursday: Rest day\n"
                "Friday: 50 push-ups, 50 squats, 50 lunges (each leg), 50 minutes of swimming or rowing\n"
                "Saturday: Rest day\n"
                "Sunday: 60 minutes of hiking or rock climbing.\n\n"
                "Remember to always warm up before exercising and cool down after, and to listen to your body and take rest days as needed. You can also consider working with a personal trainer to help you set and achieve new fitness goals.")

    # Invalid fitness level
    else:
        return "I'm sorry, I didn't understand. Can you please enter 'beginner', 'intermediate', or 'advanced' to indicate your fitness level?"


# Function to create a general diet plan based on fitness level
def create_diet_plan(fitness_level):
    """
    Creates a general diet plan based on the user's fitness level without considering BMI.

    Args:
        fitness_level (str): User's fitness level ('beginner', 'intermediate', 'advanced').

    Returns:
        str: A general diet plan tailored to the user's fitness level.
    """
    # Diet plan for "Beginner" fitness level
    if fitness_level.lower() == 'beginner':
        return ("Great! As a beginner, it's important to start with small, manageable changes to your diet.\n"
                "Here are some tips to get you started:\n\n"
                "1. Focus on whole, nutrient-dense foods such as fruits, vegetables, whole grains, lean protein, and healthy fats.\n"
                "2. Drink plenty of water throughout the day to stay hydrated.\n"
                "3. Avoid processed foods and sugary drinks.\n"
                "4. Plan your meals and snacks ahead of time to avoid impulsive eating.\n"
                "5. Consider working with a registered dietitian to help you set and achieve your goals.\n\n"
                "Here's a sample meal plan you can follow:\n\n"
                "Breakfast: Greek yogurt with berries and honey\n"
                "Snack: Apple slices with almond butter\n"
                "Lunch: Grilled chicken salad with mixed greens, tomatoes, and avocado\n"
                "Snack: Carrot sticks with hummus\n"
                "Dinner: Baked salmon with roasted vegetables.\n\n"
                "Remember to listen to your body and make changes as needed. Small, sustainable changes are more effective than drastic ones that are difficult to maintain.")

    # Diet plan for "Intermediate" fitness level
    elif fitness_level.lower() == 'intermediate':
        return ("Great! As an intermediate dieter, you already have some experience with healthy eating habits.\n"
                "Here are some tips to take your diet to the next level:\n\n"
                "1. Focus on whole, nutrient-dense foods such as fruits, vegetables, whole grains, lean protein, and healthy fats.\n"
                "2. Consider tracking your food intake to ensure you're meeting your macronutrient and calorie goals.\n"
                "3. Plan your meals and snacks ahead of time to avoid impulsive eating.\n"
                "4. Try new healthy recipes to keep your meals interesting and varied.\n"
                "5. Consider working with a registered dietitian to help you set and achieve your goals.\n\n"
                "Here's a sample meal plan you can follow based on your goals:\n\n"
                "Goal: Weight loss\n"
                "Breakfast: Oatmeal with berries and almond milk\n"
                "Snack: Greek yogurt with chopped nuts\n"
                "Lunch: Grilled chicken breast with roasted vegetables\n"
                "Snack: Apple slices with peanut butter\n"
                "Dinner: Baked salmon with quinoa and steamed broccoli\n\n"
                "Goal: Muscle gain\n"
                "Breakfast: Scrambled eggs with whole wheat toast and avocado\n"
                "Snack: Protein shake with banana\n"
                "Lunch: Grilled chicken breast with sweet potato and green beans\n"
                "Snack: Cottage cheese with pineapple chunks\n"
                "Dinner: Beef stir-fry with brown rice and mixed vegetables.\n\n"
                "Remember to listen to your body and make changes as needed. Consistency and balance are key to achieving your goals.")

    # Diet plan for "Advanced" fitness level
    elif fitness_level.lower() == 'advanced':
        return ("Impressive! As an advanced dieter, you've already developed healthy eating habits.\n"
                "Here are some tips to maintain your progress and continue achieving your goals:\n\n"
                "1. Focus on whole, nutrient-dense foods such as fruits, vegetables, whole grains, lean protein, and healthy fats.\n"
                "2. Consider tracking your food intake to ensure you're meeting your macronutrient and calorie goals.\n"
                "3. Plan your meals and snacks ahead of time to avoid impulsive eating.\n"
                "4. Try new healthy recipes to keep your meals interesting and varied.\n"
                "5. Consider periodic refeeds or cheat meals to help you stay on track and avoid feeling deprived.\n\n"
                "Here's a sample meal plan you can follow:\n\n"
                "Breakfast: Quinoa breakfast bowl with avocado, poached egg, and mixed greens\n"
                "Snack: Protein shake with mixed berries and almond milk\n"
                "Lunch: Grilled chicken breast with mixed vegetables (such as bell peppers, onions, and mushrooms) and sweet potato\n"
                "Snack: Carrots and hummus\n"
                "Dinner: Baked salmon with quinoa and roasted vegetables (such as asparagus and bell peppers).\n\n"
                "Remember to listen to your body and make changes as needed. Consistency and balance are key to maintaining your progress and achieving your goals.")

    # Invalid fitness level
    else:
        return "I'm sorry, I didn't understand. Can you please enter 'beginner', 'intermediate', or 'advanced' to indicate your fitness level?"