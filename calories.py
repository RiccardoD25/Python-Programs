def main():
    # Initialize constants
    COOKIES_PER_BAG = 40
    NUM_SERVINGS = 10
    CALORIES_PER_SERVING = 300

    # Intro
    print("Calorie Counter App ...")
    print()

    # Prompt user for number cookies consumed
    cookiesConsumed = eval(input("Please enter number of cookies consumed: "))

    # Calculate number of cookies per serving
    cookiesPerServing = COOKIES_PER_BAG / NUM_SERVINGS

    # Calculate number of  calories per cookie
    caloriesPerCookie = CALORIES_PER_SERVING / cookiesPerServing

    # Calculate total calories consumed
    caloriesConsumed = cookiesConsumed * caloriesPerCookie

    # Display calories consumed 
    print("\nYou consumed", caloriesConsumed, "calories.")

main()
    
