from data import cow, toy_dictionary, food_dictionary, breed_dictionary

# Function for user to select breed of cow they want and name said cow
def starting_choices():
    cow["breed"] = ""

    breed_list = list(breed_dictionary.keys())
    # verify user input
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

    print("""Make sure you type the letter which corresponds with the feature you want to use!
These are the activities that are currently on offer to do:""")
    print("---------")
    for key in optionKeys:
        print(key + ":\t" + menu_dictionary[key]["text"])

# Function to play with cow's toys
def play_toys():
    print("You played with your toys")

# Function to get new toys for user's cow
def new_toys():
    print("You got some new toys!")

# Function to quit simulator 
def quit_app():
    print("You quit the app!")

# Function to feed user's cow
def feed_cow():
    print("You fed your cow!")

# Function to play rock, paper, scissors 
def rps_game():
    print("You played RPS!")
 
# Function to print out the updated status of the user's cow each "day"


# Function for the main menu game loop
def primary_loop():
    #intialise out pet
    starting_choices()

    #menu options for printing and access
    menu_dictionary = {
        "F": {"function": feed_cow, "text": "Feed " + cow["name"] + "."},
        "T": {"function": new_toys, "text": "Get a new toy for " + cow["name"] + "."},
        "P": {"function": play_toys, "text": "Have " + cow["name"] + " play with their toys."},
        "R": {"function": rps_game, "text": "Play Rock, Paper, Scissors against " + cow["name"] + "!"},
        "Q": {"function": quit_app, "text": "Stop playing with " + cow["name"] + " and quit the application."}
    }   

    continue_game = True
    while continue_game:
        # display game menu
        feature_choice = ""

        # verify user input
        while feature_choice not in menu_dictionary.keys():
            menu_display(menu_dictionary)
            print(" ")
            feature_choice = input("Which of these activities would you like to do with " + cow["name"] + "? ").upper()

        # quit the application if the user picks option from menu
        if feature_choice == "Q":
            continue_game = False

        # add functionality to main game menu
        menu_dictionary[feature_choice]["function"]()


primary_loop()