from src.ScoreConstants import ScoreConstants as sc
from src.ScoreConstants import RankOrder as ro
from deuces import Card, Evaluator
import math


class Score:
    
    def __init__(self, top, middle, bottom):
        self.top = top
        self.middle = middle
        self.bottom = bottom
        self.total = 0

        if not self.isFoul(self.top, self.middle, self.bottom):
            self.checkThreeCardScore(self.top)
            self.checkFiveCardScore(self.middle, True)
            self.checkFiveCardScore(self.bottom, False)
            print(f"Score : {self.total}. You did not foul!")
        else:
            print(f"Score : {self.total}. You fouled!!!!")

    def checkThreeCardScore(self, top):
        top_joined = " ".join(top)
        top_nums = "".join(x for x in top_joined if x.isupper() or x.isdigit())
       
        top_score = 0
        for key in sc.topHand.keys():
            if key in top_nums:
                top_score = sc.topHand[key]

        self.total += top_score
        return top_score


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
        score = 0
        if isMiddle:
            score = sc.middleHand[hand_type]
        else:
            score = sc.bottomHand[hand_type]

        self.total += score
        
        return score, hand_type



    def convertThreeCardRank(self, top):
        
        top_joined = " ".join(top)
        top_nums = "".join(x for x in top_joined if x.isupper() or x.isdigit())
              
        if len(set(top_nums)) == 1:
            
            out = ro.cardRank[top_nums[0]] * 66 + 1609
            return ("Three of a Kind", out, True)
       
        elif len(set(top_nums)) == 2:
            freq = {}
            
            for char in top_nums:
                freq[char] = freq.get(char, 0) + 1
            
            pair = ""
            kicker = None
            
            for char, count in freq.items():
                if count == 2:
                    pair = char
                elif count == 1:
                    kicker = char

            kickerRank = {}
            n = 11

            for key in ro.cardRank.keys():
                if len(kickerRank) < 10:                    
                    if pair == key:
                        pass
                    else:
                        kickerRank[key] = n
                        n -= 1
            
            out = ro.cardRank[pair] * 220 + 3105
            
            for key in kickerRank.keys():
                out += math.comb(kickerRank[key], 2)
                if key == kicker:
                    break
            return ("Pair", out, True)
        
        else:
            return ("High Card", 0, False)
    
    
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
        
        if middlescore < bottomscore: return True
      
        if self.convertThreeCardRank(top)[2] == False:
            if self.checkFiveCardScore(middle, True)[1] == "High Card":
                
                top_no_suit = []
                for t in top:
                    top_no_suit.append(t[0])

                sorted_ranks = [ro.cardRank[str(rank)] for rank in top_no_suit]
                sorted_ranks.sort()
                sorted_top = [str(key) for key, value in ro.cardRank.items() if value in sorted_ranks]
                
                middle_no_suit = []
                for m in middle:
                    middle_no_suit.append(m[0])

                sorted_mid_ranks = [ro.cardRank[str(rank)] for rank in middle_no_suit]
                sorted_mid_ranks.sort()

                sorted_mid = [str(key) for key, value in ro.cardRank.items() if value in sorted_mid_ranks]
                sorted_mid = sorted_mid[0:3]

                bust = False
                for i in range(3):
                    if ro.cardRank[sorted_mid[i]] > ro.cardRank[sorted_top[i]]:
                        bust = True
                        break
                    elif ro.cardRank[sorted_mid[i]] == ro.cardRank[sorted_top[i]]:
                        continue
                    else:
                        break
                if bust: return True
            else:
                return False
        else:
            return self.convertThreeCardRank(top)[1] < middlescore