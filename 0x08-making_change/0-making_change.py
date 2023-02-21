#!/usr/bin/python3
"""Change comes from within"""


def makeChange(coins, total):
    """GIven a pile of coins of different values, determine the fewest
        number of coins needed to meet a given amount
    """
    if total <= 0:
        return 0

    curr_total = 0
    coin_used = 0
    coins = sorted(coins, reverse=True)
    for coin in coins:
        r = (total - curr_total)//coin
        curr_total += r*coin
        coin_used += r
        if curr_total == total:
            return coin_used
    return -1
