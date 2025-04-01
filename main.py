from src.Deck import Deck
from src.DeckUtil import DeckUtil
from src.Score import Score
from src.OptimalPlacement import OptimalPlacement
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
        x = hand.generateRandom(14)
        print(x)
        op = OptimalPlacement(x, Score())
        op.threader(x)
        #{'Bottom': ['7d', '8s', '7s', '8d', '8c'], 'Middle': ['Jh', '5h', '6s', '5s', '6d'], 'Top': ('As', 'Qd', 'Qs'), 'Discard': ['Tc'], 'Score': 13
        end = time.time()
        print(end-start)
    elif opt == "r monte":
        results = []
        for _ in range(1000):
            x = hand.generateRandom(14)
            op = OptimalPlacement(x, Score())
            res = op.threader(x)
            print(res)
            results.append(res["Score"])
        print(statistics.mean(results))
    else:
        print("User generation selected.")
        hand.parse(opt)    

if __name__ == "__main__":
    printWelcome()
    printPineapple()
    printOptions()

      
    #op = OptimalPlacement(['8c', '8s', '6s', '8h', '6c','As', 'Ks', 'Qd', 'Jh', 'Td','4c', '4s', '7h','6h'], Score())
    #op.threader(['8c', '8s', '6s', '8h', '6c','As', 'Ks', 'Qd', 'Jh', 'Td','4c', '4s', '7h','6h'])
    #score = Score(('Kd', '5s', 'Kc'),('Jd', '9d', '2d', 'Ad', 'Qd'),('5d', '4d', '7d', '3d', '6d'))
    #top_score = Score.checkThreeCardScore(score, ('Kd', '5s', 'Kc'))
    #print(top_score)
    #op = OptimalPlacement(['8c', '8s', '6s', '8h', '6c','As', 'Ks', 'Qd', 'Jh', 'Td','4c', '4s', '7h','6h'], Score())
    #evaluator = Evaluator()
    #board = []
    #hand_strings = ['As', 'Ks', 'Qs', 'Js', 'Ts']
    #hand = [Card.new(card) for card in hand_strings]
    #print(evaluator.evaluate(board, hand))