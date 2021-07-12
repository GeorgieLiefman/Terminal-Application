# Dictionary for cows's status
status = {
    "Name": "", 
    "Type": "", 
    "Age": 0, 
    "Hunger": 0,
    "Happiness": 100, 
    "Owned Toys": []
}

# Dictionary for cow breeds for user to select from
breed_dictionary = {
    "H": {"text": "Highland"}, 
    "T": {"text": "Texas Longhorn"}, 
    "L": {"text": "Limousin"}
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
    "Texas Longhorn": ["barbeque", "chilli", "anything fried"], 
    "Limousin": ["baguette", "cigarette", "croissant"], 
}

# Dictionary for menu options
menu_dictionary = {
        "F": {"function": feed_cow, "text": "Feed " + cow["name"] + "."},
        "T": {"function": new_toys, "text": "Get a new toy for " + cow["name"] + "."},
        "P": {"function": play_toys, "text": "Have " + cow["name"] + " play with their toys."},
        "R": {"function": rps_game, "text": "Play Rock, Paper, Scissors against " + cow["name"] + "!"},
        "Q": {"function": quit_app, "text": "Stop playing with " + cow["name"] + " and quit the application."}
}