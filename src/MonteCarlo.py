import statistics
import math
import matplotlib.pyplot as plt
from src.Deck import Deck
from src.DeckUtil import DeckUtil
from src.OptimalPlacement import OptimalPlacement
from src.Score import Score

class MonteCarlo:
    """
    monte_carlo_simulation()
        Runs a monte carlo simulation on generated best_hands for a given n number of trials
    Args:
        n (int) : The number of trials

    Returns:
        (dict): {mean_score, standard_deviation, standard_error, confidence_interval, scores}
    """  
    def monte_carlo_simulation(n):
        deck = Deck()
        hand = DeckUtil(deck)
        results = []
        running_avg = []

        for _ in range(n):
            x = hand.generateRandom(14)
            op = OptimalPlacement(x, Score())
            res = op.threader(x)
            print(res)
            results.append(res["Score"])

            current_avg = statistics.mean(results)
            running_avg.append(current_avg)
        
        mean_score = statistics.mean(results)
        stdev_score = statistics.stdev(results)
        standard_error = stdev_score / math.sqrt(n)
        conf_interval = (mean_score - 1.96 * standard_error, mean_score + 1.96 * standard_error)

        print(f"\nEstimated EV: {mean_score:.3f}")
        print(f"Sample Standard Deviation: {stdev_score:.3f}")
        print(f"Standard Error: {standard_error:.3f}")
        print(f"95% Confidence Interval: ({conf_interval[0]:.3f}, {conf_interval[1]:.3f})")

        plt.figure(figsize=(10, 6))
        plt.plot(running_avg, label='Running Average EV')
        plt.axhline(mean_score, color='r', linestyle='--', label='Final EV')
        plt.xlabel('Number of Trials')
        plt.ylabel('Average Score')
        plt.title('Fantasyland EV Running Average')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
        
        return {
        "mean_score": mean_score,
        "standard_deviation": stdev_score,
        "standard_error": standard_error,
        "confidence_interval": conf_interval,
        "scores": results
    }

