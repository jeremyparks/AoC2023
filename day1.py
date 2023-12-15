""" Day 1 Advent of Code - 2023.

The newly-improved calibration document consists of lines of text; 
each line originally contained a specific calibration value that the 
Elves now need to recover. On each line, the calibration value can 
be found by combining the first digit and the last digit (in that order) 
to form a single two-digit number.
"""

def get_digits(char_list):
    return [s for s in char_list if s.isdigit()]


