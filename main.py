from data import status, toy_dictionary, food_dictionary

# Function for user to select breed of cow they want and name said cow
def starting_choices():
    cow_choice = ""

    breed_list = list(food_dictionary.keys())
    #validate user input
    while cow_choice not in breed_list:
        print("Here are the breeds availabe for adoption. Make sure you pick something from the list!")
        for option in breed_list:
            print(option)
        cow_choice = input("Which type of cow would you like to adopt? ")

    # User input to name pet
    name = input(f"Woohoo! You've adopt a {cow_choice} cow as your pet. What will you name them? ")
    print(f"{name} is a great name for such a cool {cow_choice} cow!")

starting_choices()