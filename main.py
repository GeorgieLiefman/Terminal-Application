# Dictionary for cows's status
status = {
    "Name": "", 
    "Type": "", 
    "Age": 0, 
    "Hunger": 0,
    "Happiness": 100, 
    "Owned Toys": []
}

# Dictionary for cow's toys
toy_dictionary = {
    "Highland": ["bagpipes", "Loch Ness monster", "rugby ball"], 
    "Texas Longhorn": ["guitar", "Trump", "tumbleweed"], 
    "Limousin": ["bike", "skiis", "Effiel Tower"], 
}

# Dictionary for cow's food
food_dictionary = {
    "Highland": ["haggis", "shortbread", "bacon butty"], 
    "Texas lLnghorn": ["barbeque", "chilli", "anything fried"], 
    "Limousin": ["baguette", "cigarette", "croissant"], 
}

# Function for user to select breed of cow they want
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