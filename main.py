from src.Deck import Deck
from src.DeckUtil import DeckUtil
from src.Score import Score
from src.OptimalPlacement import OptimalPlacement
from src.MonteCarlo import MonteCarlo as mc
from deuces import Card, Evaluator
import time
import os
import statistics


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
                   or to input 14 of their own in a specific format.
    """
    opt = input(
        "Please enter 'r' if you want the 14 cards randomly generated.\n"
        "Otherwise, enter 14 cards in the form `(R)ank(s)uit`"
        "and don't add a space in between the commas.\n")

    deck = Deck()
    hand = DeckUtil(deck)

    if opt == "r":
        print("Random generation selected.")
        start = time.time()
        mc.monte_carlo_simulation(10000)
        end = time.time()
        print(end-start)
    else:
        print("User generation selected.")
        hand.parse(opt)    

if __name__ == "__main__":
    printWelcome()
    printPineapple()
    printOptions()