from src.ScoreConstants import ScoreConstants as sc
from deuces import Card, Evaluator


class Score:
    
    
    def __init__(self, top, middle, bottom):
        self.top = top
        self.middle = middle
        self.bottom = bottom
        self.total = 0

    def checkMiddleScore(self, middle):
        board = [
            Card.new(middle[0]), 
            Card.new(middle[1]),
            Card.new(middle[2])
            ]
        hand = [
            Card.new(middle[3]),
            Card.new(middle[4])
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

        print(f"Hand type: {hand_type}")

    def checkTopScore(self, top):
        top_joined = " ".join(top)
        top_nums = "".join(x for x in top_joined if x.isupper() or x.isdigit())
       
        top_score = 0
        for key in sc.topHand.keys():
            if key in top_nums:
                top_score = sc.topHand[key]

        self.total += top_score
        
        print(self.total)
        print(top_nums)
        pass
    
    def checkBottomScore(self, bottom):
        pass
    
