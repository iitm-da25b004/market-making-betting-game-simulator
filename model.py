"""
Market-Making & Betting-Game Simulator

Assembled from your step-by-step solutions.
"""

import numpy as np

# Step 1 - expected_value
def expected_value(values, probabilities):
    # TODO: return the expected value of the discrete distribution (values, probabilities).
    ev = 0.0
    for i in range(len(values)):
        ev += values[i] * probabilities[i]
    return ev

# Step 2 - one_reroll_die_value
def one_reroll_die_value(sides):
    # TODO: return {'value': expected winnings under optimal reroll policy, 'reroll_faces': sorted faces to reroll}
    arr = np.arange(1, sides + 1)
    mid = sides // 2
    right = ((mid + (sides % 2)) / sides) * np.mean(arr[mid:])
    left = (mid / sides) * np.mean(arr)
    value = float(left + right)
    faces = arr[:mid].tolist()
    return {'value': value, 'reroll_faces': faces}

# Step 3 - pay_per_reroll_die_game
import numpy as np
def pay_per_reroll_die_game(sides, reroll_cost):
    # TODO: return {'threshold': t, 'value': V} for the pay-per-reroll die game under the optimal threshold policy.
    if reroll_cost == 0:
        return {'threshold': sides, 'value': float(sides)}
    val = (sides + 1 - np.sqrt(2 * sides * reroll_cost))
    thresh_1 = max(1, min(sides, int(np.ceil(val))))
    thresh_2 = max(1, min(sides, int(np.floor(val))))
    ev_1 = (thresh_1 + sides) / 2 - ((thresh_1 - 1) / (sides - thresh_1 + 1)) * reroll_cost
    ev_2 = (thresh_2 + sides) / 2 - ((thresh_2 - 1) / (sides - thresh_2 + 1)) * reroll_cost
    min_ev, min_thresh = max([(ev_1, thresh_1), (ev_2, thresh_2)], key=lambda x: (x[0], -x[1]))
    return {'threshold': min_thresh, 'value': float(min_ev)}

# Step 4 - red_black_card_game_value
from functools import lru_cache
def red_black_card_game_value(num_red, num_black):
    # TODO: return {'value': expected payout under optimal stopping, 'stop_now': whether to stop immediately}.
    total = num_black + num_red
    if num_red < num_black or (total == 0):
        return {'value': 0.0, 'stop_now': True}
    @lru_cache(None)
    def rec(r, b):
        if r == 0:
            return 0.0
        if b == 0:
            return float(r)
        if r == 1 and b == 1:
            return 0.5
        total = (r + b)
        return max(0.0, (r / total) * (1 + rec(r-1, b)) + (b / total) * (-1 +rec(r, b-1)))
    val = rec(num_red, num_black)
    return {'value': val, 'stop_now': False}

# Step 5 - make_quotes
def make_quotes(fair_value, spread_width):
    # TODO: return a dict with 'bid' and 'ask' symmetric around fair_value with total width spread_width
    return {
        'bid': fair_value - (spread_width / 2.0),
        'ask': fair_value + (spread_width / 2.0)
    }

# Step 6 - execute_trade (not yet solved)
# TODO: implement

# Step 7 - mark_to_market_pnl (not yet solved)
# TODO: implement

# Step 8 - adverse_selection_loss (not yet solved)
# TODO: implement

# Step 9 - uncertainty_spread (not yet solved)
# TODO: implement

# Step 10 - inventory_skewed_quotes (not yet solved)
# TODO: implement

# Step 11 - update_fair_value_from_trade (not yet solved)
# TODO: implement

# Step 12 - update_remaining_card_value (not yet solved)
# TODO: implement

# Step 13 - run_market_making_episode (not yet solved)
# TODO: implement

# Step 14 - summarize_episode_pnls (not yet solved)
# TODO: implement

