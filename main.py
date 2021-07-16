from data import cow, toy_dictionary, food_dictionary, breed_dictionary
import random

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
        print()
    # User input to name pet
    print("_________________________________________________________________________________")
    cow["name"] = input("Woohoo! You've adopt a cow as your pet. What will you name them? ")
    print(cow["name"] + " is a great name for such a cool cow!")
    print()

# output the starting user's cow status
print(cow)

# print menu
def menu_display(menu_dictionary):
    shorthand_menu_choices = list(menu_dictionary.keys())
    print("_________________________________________________________________________________")
    print("""Make sure you type the letter which corresponds with the feature you want to use!
These are the activities that are currently on offer to do:""")
    for key in shorthand_menu_choices:
        print(key + ":\t" + menu_dictionary[key]["text"])

# Function to play with cow's toys
def play_toys():
    print("_________________________________________________________________________________")
    print("You played with your toys")

# Function to get new toys for user's cow
def new_toys():
    print("_________________________________________________________________________________")
    print("Hooray! " + cow["name"] + " is going to have some new toys to play with!")
    selectable_toys = ["pile of mulch", "obstacle course", "cow plushie"]
    print(selectable_toys)
    #specific toy number to select from the list
    number_toy = -1
    #get a valid toy to input
    while number_toy < 0 or number_toy > len(selectable_toys) -1:
        for x in range(len(selectable_toys)):
            print(str(x) + ": " + selectable_toys[x])
        number_toy = int(input("Enter the number which corresponds with the toy you'd like for your cow: "))
        #get the selected toy option from our list
        picked_toy = selectable_toys[number_toy]
        cow["toys"].append(picked_toy)
        print(cow["name"] + " loves the " + picked_toy + " you chose for them!")

# Function to quit simulator 
def quit_app():
    print("_________________________________________________________________________________")
    print("You have quit the application. Thank you for playing with " + cow["name"] + "!")

# Function to feed user's cow
def feed_cow():
    # handle hunger levels if they dip into the negative
    negative_hunger = random.randint(16, 32)
    update_hunger = cow["hunger"] - negative_hunger
    if update_hunger < 0:
        update_hunger = 0
    # decrease cow's hunger level by feeding it
    cow["hunger"] = update_hunger
    print("_________________________________________________________________________________")
    print("Yummy! " + pet["name"] + " enjoyed the food you fed them.")
    print("Their hunger decreased by " + str(negative_hunger)) 


# Function to walk cow 
def walk():
    print("_________________________________________________________________________________")
    print("Good choice! " + cow["name"] + " is really excited to go on a walk with you!")
    location = ["far left paddock", "down to the pond", "mountain"]
    print(location)
    #specific location number to select from the list
    number_location = -1
    #get a valid location to input
    while number_location < 0 or number_location > len(location) -1:
        for x in range(len(location)):
            print(str(x) + ": " + location[x])
        number_location = int(input("Enter the number which corresponds with where you'd like to walk your cow: "))
        #get the selected location option from the list
        picked_location = location[number_location]
        
        # output statements for walk
        print()
        print("On their walk " + cow["name"] + " found " + random_event)
























 
# Function to print out the updated status of the user's cow each "day"
def updated_status():
    print()
    print("_________________________________________________________________________________")
    print("Here is an update of how " + cow["name"] + " is progressing!")
    print("At the moment, your cow owns: " + str(len(cow["toys"])) + " toys. These toys are: ")
    for owned_toy in cow["toys"]:
        print(owned_toy)
    print(cow["name"] + "'s hunger level is presently " + str(cow["hunger"]) + " out of a maximum 100 and a minimum of 0.")
    print(cow["name"] + "'s happiness level is presently " + str(cow["happiness"]) + " out of a maximum 100 and a minimum of 0.")
    print("Currently, your cow is " + str(cow["age"]) + " " + "days old.")

# Function for the main menu game loop
def primary_loop():
    # print starting choices 
    starting_choices()
    #menu options for printing and access
    menu_dictionary = {
        "F": {"function": feed_cow, "text": "Feed " + cow["name"] + "."},
        "T": {"function": new_toys, "text": "Get a new toy for " + cow["name"] + "."},
        "P": {"function": play_toys, "text": "Have " + cow["name"] + " play with their toys."},
        "W": {"function": walk, "text": "Take " + cow["name"] + " for a walk!"},
        "Q": {"function": quit_app, "text": "Stop playing with " + cow["name"] + " and quit the application."}
    }   

    continue_game = True
    while continue_game:
        # display game menu
        feature_choice = ""
        # verify user input
        while feature_choice not in menu_dictionary.keys():
            menu_display(menu_dictionary)
            feature_choice = input("Which of these activities would you like to do with " + cow["name"] + "? ").upper()
            print()
        # quit the application if the user picks option from menu
        if feature_choice == "Q":
            continue_game = False
        # add functionality to main game menu
        menu_dictionary[feature_choice]["function"]()
        # increase/decrease cow's hunger, happiness and age
        cow["hunger"] += random.randint(3, 15)
        cow["happiness"] -= random.randint(4, 15)
        cow["age"] += 1
        #print cow's updated status
        updated_status()
        print()
 


primary_loop()