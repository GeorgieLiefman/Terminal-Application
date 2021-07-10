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
    "highland cow": ["bagpipes", "Loch Ness monster", "rugby ball"], 
    "texas longhorn cow": ["guitar", "Trump", "tumbleweed"], 
    "limousin cow": ["bike", "skiis", "Effiel Tower"], 
}

# Dictionary for cow's food
food_dictionary = {
    "highland cow": ["haggis", "shortbread", "bacon butty"], 
    "texas longhorn cow": ["barbeque", "chilli", "anything fried"], 
    "limousin cow": ["baguette", "cigarette", "croissant"], 
}

# Function for user to select breed of cow they want
def starting_choices():
    cow_choice = ""

    breed_list = list(food_dictionary.keys())

    #validate user input
    while cow_choice not in breed_list:
        print("Pick something from the list!")
        for option in breed_list:
            print(option)
        cow_choice = input("Which breed of cow would you like to adopt? ")

starting_choices()