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

starting_choices()

print(cow)