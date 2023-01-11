#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor can execute
only two operations in this file: Copy All and Paste. Given a number n,
write a method that calculates the fewest number of operations needed to
result in exactly n H characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
"""


def minOperations(n):
    """calculates fewest number of operations needed to
    result in exactly 'n' 'H' cahracters in this file
    Returns:
        Integer: if n is impossible to achieve, return 0
    """
    pasted_chars = 1  # how many chars in a file
    clipboard = 0  # how many H's copied
    counter = 0  # operations counter

    while pasted_chars < n:

        # if did not copy anything yet

        if clipboard == 0:

            # copyall

            clipboard = pasted_chars

            # increment operations count

            counter += 1

        # if hav'nt pasted anything yet

        if pasted_chars == 1:

            # paste

            pasted_chars += clipboard

            # increment operations counter

            counter += 1

            # continue to next loop

            continue

        remaining = n - pasted_chars  # remaining chars to paste

        # check if impossible by checking if clipboard has more
        # than needed to reach the desired number
        # this also means num of chars in file is equal or more than
        # in the clipboard.
        # in both situations it's impossible to achieve n of chars

        if remaining < clipboard:
            return 0

        # if can't be divided

        if remaining % pasted_chars != 0:

            # pasted current clipboard

            pasted_chars += clipboard

            # increment operations counter

            counter += 1
        else:

            # copyall

            clipboard = pasted_chars

            # paste

            pasted_chars += clipboard

            # increment operations counter

            counter += 2

        # if got the desired result

        if pasted_chars == n:
            return counter
        else:
            return 0
