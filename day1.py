""" Day 1 Advent of Code - 2023.

The newly-improved calibration document consists of lines of text; 
each line originally contained a specific calibration value that the 
Elves now need to recover. On each line, the calibration value can 
be found by combining the first digit and the last digit (in that order) 
to form a single two-digit number.
"""

WORDS = 'one two three four five six seven eight nine'.split()
DIGITS = '1 2 3 4 5 6 7 8 9'.split()
WORD_TO_DIGIT_MAP = dict(zip(WORDS, DIGITS))


def gen_line(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            yield line.strip()


def gen_digits(lines):
    for line in lines:
        for word in WORDS:
            line = line.replace(word, WORD_TO_DIGIT_MAP[word])
        yield [s for s in line if s.isdigit()]


def gen_values(digits_list):
    for digits in digits_list:
        value = digits[0] + digits[-1]
        yield int(value)


def main(filepath):
    lines = gen_line(filepath)
    digits = gen_digits(lines)
    values = gen_values(digits)
    total = sum(values)
    return total


if __name__ == '__main__':
    total = main('day1-input.txt')
    print(total)
