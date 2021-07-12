from data import status, toy_dictionary, food_dictionary, breed_dictionary

# Function for user to select breed of cow they want and name said cow
def starting_choices():
    cow_choice = ""

    breed_list = list(breed_dictionary.keys())
    #validate user input
    while cow_choice not in breed_list:
        print("""Here are the breeds availabe for adoption. 
Make sure you type the letter which corresponds with the breed you want!""")
        for key in breed_list:
            print(key + ":\t" + breed_dictionary[key]["text"])
        cow_choice = input("Which type of cow would you like to adopt? ").upper()
        print(" ")

    # User input to name pet
    name = input(f"Woohoo! You've adopt a {cow_choice} cow as your pet. What will you name them? ")
    print(f"{name} is a great name for such a cool {cow_choice} cow!")
    print(" ")

starting_choices()


# Print menu
    def printMenu(menuOptions):
        optionKeys = list(menuOptions.keys())

        print("Here are your options:")
        print("-------")
        for key in optionKeys:
            print(key + ":\t" + menuOptions[key]["text"])




def main():

    starting_choices()

    printMenu(menuOptions)

main() 

# Function to play with cow's toys

# Function to get new toys for user's cow

# Function to quit simulator 

# Function to feed user's cow

# Function to play rock, paper, scissors 
 
# Function to print out the updated status of the user's cow each "day"


# Function for the main menu game loop