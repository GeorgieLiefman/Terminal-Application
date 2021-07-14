from data import cow, toy_dictionary, food_dictionary, breed_dictionary

# Function for user to select breed of cow they want and name said cow
def starting_choices():
    cow["breed"] = ""

    breed_list = list(breed_dictionary.keys())
    #validate user input
    while cow["breed"] not in breed_list:
        print("""Here are the breeds availabe for adoption. 
Make sure you type the letter which corresponds with the breed you want!""")
        for key in breed_list:
            print(key + ":\t" + breed_dictionary[key]["text"])
        cow["breed"] = input("Which type of cow would you like to adopt? ").upper()
        print(" ")

    # User input to name pet
    cow["name"] = input("Woohoo! You've adopt a cow as your pet. What will you name them? ")
    print(cow["name"] + " is a great name for such a cool cow!")
    print(" ")

# output the starting user's cow status
print(cow)

# print menu
def menu_display(menu_dictionary):
    optionKeys = list(menu_dictionary.keys())

    print("Here are your options:")
    print("---------")
    for key in optionKeys:
        print(key + ":\t" + menu_dictionary[key]["text"])

# Function to play with cow's toys

# Function to get new toys for user's cow

# Function to quit simulator 

# Function to f(eed user's cow
def feed_cow():
    print("You fed your cow!")

# Function to play rock, paper, scissors 
 
# Function to print out the updated status of the user's cow each "day"


# Function for the main menu game loop
def primary_loop():
    #intialise out pet
    starting_choices()

    #menu options for printing and access
    menu_dictionary = {
        "F": {"function": feed_cow, "text": "Feed " + cow["name"] + "."},
    }   

    menu_display(menu_dictionary)

primary_loop()