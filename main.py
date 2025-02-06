from src.Deck import Deck
from src.DeckUtil import DeckUtil
from src.Score import Score


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
    opt = input(
        "Please enter 'r' if you want the 15 cards randomly generated.\n"
        "Otherwise, enter 15 cards in the from `(R)ank(s)uit`"
        "and don't add a space inbetween the commas.\n")

    deck = Deck()
    hand = DeckUtil(deck)

    if opt == "r":
        print("Random generation selected.")
        hand.generateRandom(15)

    else:
        print("User generation selected.")
        hand.parse(opt)
    score = Score("","","")
    # score.checkThreeCardScore(["Ah", "Ac", "Ad"])
    # score.checkFiveCardScore(["As","Kh","Qh","Jh","Th"], True)
    # score.checkFiveCardScore(["Ah","Kh","Qh","Jh","Th"], False)
    score.isFoul([],["Ac","Ah","Jc","Td","9h"],["Kd","Kc","Qh","Js","9s"])
    score.convertThreeCardRank(["As","Ad","Qs"])
    

printWelcome()
printPineapple()
printOptions()
