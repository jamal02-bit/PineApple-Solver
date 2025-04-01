from src.ScoreConstants import ScoreConstants as sc
from itertools import combinations
from deuces import Evaluator, Card
from src.ScoreConstants import RankOrder as ro
from src.Score import Score
import math
import heapq
import concurrent.futures
import os
from functools import partial
import time

class OptimalPlacement:
    def __init__(self, cards, score):
        self.cards = cards
        self.total = 0
        self.score = score
        #self.thread = self.threader(self.cards)
        #self.bottoms = self.get_best_bottoms(["Kd","5d","4d","7d","9d","Kc", "Ad", "Qd","2d","3d","4s","5s","6d","Jd"])
        #self.algorithm = self.bottom_algorithm(self.cards)
    
    def threader(self, cards):
        best_bottoms = self.get_best_bottoms(cards)
        chunk_size = len(best_bottoms) // os.cpu_count()
        chunks = [best_bottoms[i * chunk_size:(i + 1) * chunk_size] for i in range(os.cpu_count())]

        func = partial(self.bottom_algorithm, cards=cards)
        with concurrent.futures.ProcessPoolExecutor(max_workers=os.cpu_count()) as executor:
            best_hands = list(executor.map(func, chunks))
        
        best_hand = max(best_hands, key = lambda x: x["Score"])
        print(best_hand)
        return best_hand
        #print(best_hands, len(best_hands))

    def get_best_bottoms(self, cards):
        min_heap = []
        heapq.heapify(min_heap)
        #Hand = namedtuple("Hand", ["cards", "score", "rank"])
        for bottom in combinations(cards, 5):
            score, _, rank = self.score.checkFiveCardScore(bottom, 0)
            hand = (bottom, score, rank)
            #hand = Hand(cards = bottom, score = score, rank = rank)

            if len(min_heap) < 16:
                heapq.heappush(min_heap, (-rank, hand))
            else:
                heapq.heappushpop(min_heap, (-rank, hand))
        return [hand for _, hand in min_heap]
    
    def compare_unpaired_tops(self, current_top, new_top):
        new_no_suit = []
        for t in new_top:
            new_no_suit.append(t[0])
        sorted_new_ranks = [ro.cardRank[str(rank)] for rank in new_no_suit]
        sorted_new_ranks.sort()
        sorted_new = [str(key) for key, value in ro.cardRank.items() if value in sorted_new_ranks]
        
        current_no_suit = []
        for m in current_top:
            current_no_suit.append(m[0])
        sorted_current_ranks = [ro.cardRank[str(rank)] for rank in current_no_suit]
        sorted_current_ranks.sort()
        sorted_current = [str(key) for key, value in ro.cardRank.items() if value in sorted_current_ranks]

        newIsBetter = False
        for i in range(3):
            if ro.cardRank[sorted_new[i]] < ro.cardRank[sorted_current[i]]:
                newIsBetter = True
                break
            elif ro.cardRank[sorted_new[i]] == ro.cardRank[sorted_current[i]]:
                continue
            else:
                break
        return newIsBetter
        
    
    def check_tops(self, current_top, new_top):
        if self.score.convertThreeCardRank(current_top)[2] == False and self.score.convertThreeCardRank(new_top)[2] == False:
            return self.compare_unpaired_tops(current_top, new_top)
        elif self.score.convertThreeCardRank(current_top)[2] == False and self.score.convertThreeCardRank(new_top)[2] == True:
            return True
        elif self.score.convertThreeCardRank(current_top)[2] == True and self.score.convertThreeCardRank(new_top)[2] == False:
            return False
        else:
            return self.score.convertThreeCardRank(current_top)[1] > self.score.convertThreeCardRank(new_top)[1] 

    def bottom_algorithm(self, chunk, cards):
        best_setup = None
        best_score = 0
        #print(cards)
        for bottom in chunk:
            bottom_hand = list(bottom[0])
            #print(bottom_hand)
            remaining_middle = list(set(cards)-set(bottom_hand))

            for middle in combinations(remaining_middle, 5):
                middle = list(middle)
                middle_score, _, middle_rank = self.score.checkFiveCardScore(middle, 1)
                remaining_top = list(set(remaining_middle)-set(middle))
                if middle_rank < bottom[2]:
                    continue
                
                for top in combinations(remaining_top, 3):
                    top_score = self.score.checkThreeCardScore(top)
                    discard = list(set(remaining_top)-set(top))
                    
                    if not self.score.isFoul(top, middle, bottom_hand):
                        current_total = bottom[1] + middle_score + top_score
                    else:
                        current_total = 0

                    if best_setup == None:
                        best_score = current_total
                        best_setup = {
                            'Bottom' : bottom_hand,
                            'Middle' : middle,
                            'Top' : top,
                            'Discard' : discard,
                            'Score' : current_total
                        }
                    else:
                        if current_total > best_score or (current_total == best_score and self.check_tops(best_setup['Top'], top)):
                            best_score = current_total
                            best_setup = {
                                'Bottom' : bottom_hand,
                                'Middle' : middle,
                                'Top' : top,
                                'Discard' : discard,
                                'Score' : current_total
                            }
        #print(best_setup)
        return best_setup