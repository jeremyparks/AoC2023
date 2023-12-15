""" Day 1 Advent of Code - 2023.

The newly-improved calibration document consists of lines of text; 
each line originally contained a specific calibration value that the 
Elves now need to recover. On each line, the calibration value can 
be found by combining the first digit and the last digit (in that order) 
to form a single two-digit number.
"""

def get_value(filepath):
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            digits = [s for s in line if s.isdigit()]
            first, last = digits[0], digits[-1]
            value = first + last
            yield int(value)


if __name__ == '__main__':
    print(sum(get_value('day1-input.txt')))
