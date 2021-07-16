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
    # handle happiness levels if they dip into the negative or exceed 100
    postive_happiness = random.randint(16, 32)
    updated_happiness = cow["happiness"] + postive_happiness
    if updated_happiness <= 0:
        updated_happiness = 0
    if updated_happiness >= 100:
        updated_happiness = 100
    # increase cow's happiness level by having it play with toys 
    cow["happiness"] = updated_happiness
    # print out options of toys to for user's cow to play with
    print("_________________________________________________________________________________")
    print("Here are the options of foods you can feed your cow: ")
    toy_choices = ["big red ball", "cow figurine", "chicken", "bagpipes", "country guitar", "bicycle"]
    print(toy_choices)
    #specific location number to select from the list
    toy_number = -1
    #get a valid location to input
    while toy_number < 0 or toy_number > len(toy_choices) -1:
        for x in range(len(toy_choices)):
            print(str(x) + ": " + toy_choices[x])
        toy_number = int(input("Enter the number which corresponds with the food you'd like to feed your cow: "))
        selected_toy = toy_choices[toy_number]
        # output happiness levels and user's input
        print("Yipee! " + cow["name"] + " had a lot of fun playing with the " + selected_toy + " you picked for them.")
        print("Their happiness increased by " + str(postive_happiness) + ".") 

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
    # handle hunger levels if they dip into the negative or exceed 100
    negative_hunger = random.randint(16, 32)
    updated_hunger = cow["hunger"] - negative_hunger
    if updated_hunger <= 0:
        updated_hunger = 0
    if updated_hunger >= 100:
        updated_hunger = 100
    # decrease cow's hunger level by feeding it
    cow["hunger"] = updated_hunger
    # print out options of food to feed user's cow
    print("_________________________________________________________________________________")
    print("Here are the options of foods you can feed your cow: ")
    food_choices = ["grass", "hay", "salt lick", "haggis", "anything fried", "baguette"]
    print(food_choices)
    #specific location number to select from the list
    number_food = -1
    #get a valid location to input
    while number_food < 0 or number_food > len(food_choices) -1:
        for x in range(len(food_choices)):
            print(str(x) + ": " + food_choices[x])
        number_food = int(input("Enter the number which corresponds with the food you'd like to feed your cow: "))
        picked_food = food_choices[number_food]
        # output hunger levels and user's input
        print("Yummy! " + cow["name"] + " enjoyed the " + picked_food + " you fed them.")
        print("Their hunger decreased by " + str(negative_hunger) + ".") 

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
        # random event which will occur while your cow is on its walk
        random_event = random.choice(["$31,250, unfortunately it was Iranian Rial so it's only worth about $1 AUD.", "other cows to play with and I now have new friends.", "an angus beef cheeseburger. Luckily I realised what angus beef was before I took a bite o_o"])
        # output statements for walk
        print()
        print(cow["name"] + " had a great time walking to the " + picked_location + "!")
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