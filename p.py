def play_toys():
    try:
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
            toy_number = int(input("Enter the number which corresponds with the toy you'd like to give your cow: "))

    except (IndexError, ValueError):
        print()
        print("""Sorry that was not a valid answer.
If you want to play with their toys you have to make sure you input the number that corresponds with the toy you want.""")
    
    else:
        selected_toy = toy_choices[toy_number]
        print("Yipee! cow had a lot of fun playing with the " + selected_toy + " you picked for them.")
       

            

play_toys()