""" Day 2: Cube Conundrum
In game 1, three sets of cubes are revealed from the bag (and then put back again). 
The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 
2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.

The Elf would first like to know which games would have been possible if the bag 
contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

answer for sample -> 8
answer for input, part1 -> 2176
answer for input, part2 -> 63700
"""
import functools
import operator


CUBES_IN_BAG = {'red': 12, 'blue': 14, 'green': 13}

def max_colors():
    temp = {}
    with open('day2-input.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            game, data = line.split(':')
            _, game_number = game.split()
            temp[game_number] = {'red': 0, 'blue': 0, 'green': 0}
            for revealed in data.split(';'):
                for cubes in revealed.split(','):
                    number_of_cubes, color = cubes.split()
                    temp[game_number][color] = max(int(number_of_cubes), temp[game_number][color])
    return temp

valid_attempts = []
powers = []
for number, attempt in max_colors().items():
    power = functools.reduce(operator.mul, attempt.values())
    powers.append(power)
    for color, number_of_cubes in attempt.items():
        if number_of_cubes > CUBES_IN_BAG[color]:
            print(f'attempt: {number} not valid, {color}: {number_of_cubes} > {CUBES_IN_BAG[color]}')
            break
    else:  # NO BREAK
        valid_attempts.append(int(number))
print('part1', sum(valid_attempts))
print('part2', sum(powers))
