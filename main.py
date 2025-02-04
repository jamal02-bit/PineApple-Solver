def printWelcome():
    """
    printWelcome() greets the user.
    """

    print("Welcome to the PineAppleSolver!")

def printPineapple():
    """
    printPineapple() prints ascii art of a pineapple.
    """
    pineapple = """
        ⠀⠀⠀⣀⡀⠀⠀⠀⣠⠶⡄⠀⢀⣀⣠⠄⠀⠀
    ⠀⠀⠀⠉⠻⡓⢄⢰⠃⠀⢹⡴⢩⠏⠁⠀⠀⠀
    ⠀⠀⠈⠳⣶⢷⣈⡏⢀⣤⡀⣇⡧⠴⡲⠟⠀⠀
    ⠀⠀⠀⠀⠈⢣⠈⢳⡎⠀⢳⠋⢀⠞⠁⠀⠀⠀
    ⠀⠀⠀⠈⠳⣦⣇⢸⠁⣀⠈⡇⡾⣶⠏⠀⠀⠀
    ⠀⠀⠀⠀⢀⣹⡎⢻⡼⠈⣧⠋⣴⣁⡄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠹⡝⠦⡇⠀⣸⠞⡽⠋⠀⠀⠀⠀
    ⠀⠀⠀⠀⣠⠖⢻⠟⠛⠛⣿⠓⠳⣄⠀⠀⠀⠀
    ⠀⠀⢠⠞⢇⡠⠁⠱⡀⡰⠁⠑⢤⡋⠱⡄⠀⠀
    ⠀⢠⣇⡠⠊⢆⠀⢀⠜⠣⡀⢀⠎⠈⠢⣼⡆⠀
    ⢀⡟⠩⡀⠀⠀⠱⡂⠀⠀⢨⠮⣀⠀⢠⠃⠸⡄
    ⢸⠁⠀⣑⡔⠈⠀⠈⢢⣔⠁⠀⠀⢱⠣⢄⡀⡇
    ⢸⢖⠈⠀⠈⠢⣀⠔⠁⠈⠑⢤⡔⠁⠀⠀⡘⣷
    ⢸⡈⠢⣀⠤⠊⠉⠢⢀⠀⡠⠊⠀⠁⢒⠼⢀⡇
    ⠈⣇⠉⠈⠢⡀⠀⡀⠔⠉⠢⠄⣀⡠⠂⠀⢰⠃
    ⠀⠸⣄⡀⠤⠚⠙⠄⡀⠀⢀⠤⠊⠉⠀⣲⠏⠀
    ⠀⠀⠘⢗⠤⡀⠀⡀⠬⠓⠃⠤⣀⣠⣪⠏⠀⠀
    ⠀⠀⠀⠈⠑⢮⣙⠢⢄⣀⠤⣂⡥⠚⠁⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀
    """
    print(pineapple)

def printOptions():
    """
    printOptions() allows the user to select whether to randomly generate 15 cards
                   or to input 15 of their own in a specific format.
    """
    isRandom = input("Please enter 'r' if you want the 15 cards randomly generated.\nOtherwise, enter 15 cards in the from `(R)ank(s)uit` and don't add a space inbetween the commas.\n")

    if (isRandom == "r"):
        print("Random generation selected.")
        # send a call to randomGeneration()
        # and print generated cards DeckGenerator::generateFantasyLandDeck()
    else:
        print("User generation selected.")
        # Send cards to a parser

# Call to functions
printWelcome()
printPineapple()
printOptions()
