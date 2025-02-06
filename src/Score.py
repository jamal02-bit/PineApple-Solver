from src.ScoreConstants import ScoreConstants as sc
from deuces import Card, Evaluator


class Score:
    
    
    def __init__(self, top, middle, bottom):
        self.top = top
        self.middle = middle
        self.bottom = bottom
        self.total = 0
        self.top_rank = self.setThreeCardRank(self.top)

    def checkThreeCardScore(self, top):
        top_joined = " ".join(top)
        top_nums = "".join(x for x in top_joined if x.isupper() or x.isdigit())
       
        top_score = 0
        for key in sc.topHand.keys():
            if key in top_nums:
                top_score = sc.topHand[key]

        self.total += top_score
        
        print(self.total)
        print(top_nums)


    def checkFiveCardScore(self, row, isMiddle):
        
        board = [
            Card.new(row[0]), 
            Card.new(row[1]),
            Card.new(row[2])
            ]
        hand = [
            Card.new(row[3]),
            Card.new(row[4])
            ]

        # Instantiate evaluator
        evaluator = Evaluator()

        # Evaluate the hand (rank is returned as a number, with lower numbers being better hands)
        hand_rank = evaluator.evaluate(board, hand)

        # Get the hand type
        if hand_rank == 1:
            hand_type = "Royal Flush"
        else:
            hand_type = evaluator.class_to_string(evaluator.get_rank_class(hand_rank))

        if isMiddle:
            self.total += sc.middleHand[hand_type]
        else:
            self.total += sc.bottomHand[hand_type]
        print(f"Hand type: {hand_type}")
        print(self.total, isMiddle)



    def setThreeCardRank(self, top):
        
        top_joined = " ".join(top)
        top_nums = "".join(x for x in top_joined if x.isupper() or x.isdigit())
        if len(set(top_nums)) == 1:
            return "Three of a Kind"
        elif len(set(top_nums)) == 2:
            return "Pair"
        else:
            return "High Card"
    
    def convertThreeCardRank(self, rank):
        if rank == "Three of a Kind":
            pass
        elif rank == "Pair":
            pass
        else:
            pass
    
    
    
    
    def isFoul(self, top, middle, bottom):
        

        # Comparing middle to bottom
        middle_board = [
            Card.new(middle[0]), 
            Card.new(middle[1]),
            Card.new(middle[2])
            ]
        middle_hand = [
            Card.new(middle[3]),
            Card.new(middle[4])
            ]
        bottom_board = [
            Card.new(bottom[0]), 
            Card.new(bottom[1]),
            Card.new(bottom[2])
            ]
        bottom_hand = [
            Card.new(bottom[3]),
            Card.new(bottom[4])
            ]
        
        
        evaluator = Evaluator()
        middlescore = evaluator.evaluate(middle_board, middle_hand)
        bottomscore = evaluator.evaluate(bottom_board, bottom_hand)

        print(middlescore)











        if bottomscore <= middlescore:
            # print("Did not Foul")
            pass
        else:
            # print("You Fouled")
            return True
        
        
        return False