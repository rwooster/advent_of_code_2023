import argparse
import re

def update_game_result(game_result, draw_result):
    for key, val in draw_result.items():
        if key in game_result:
            game_result[key] = max(game_result[key], draw_result[key])
        else:
            game_result[key] = draw_result[key]

def parse_draw(draw):
    result = {}

    cubes = draw.split(',')
    for cube in cubes:
        count, color = cube.split()
        result[color] = int(count)
        
    return result


game_re = re.compile(r'.*Game (\d+): (.*)')
def parse_game(line):
    game_result = {}
    game_number = None

    if match := re.match(game_re, line):
        game_number = match.group(1)
        draws = match.group(2)
        draws = draws.split(';')
        for draw in draws:
            draw_result = parse_draw(draw)
            update_game_result(game_result, draw_result)
    return game_number, game_result


def part_one(filename):
    total = 0

    max_values = {'red': 12, 'green': 13, 'blue': 14}

    with open(filename, 'r') as f:
        for line in f:
            game_number, game_result = parse_game(line)

            valid = True
            for key, value in game_result.items():
                if key not in max_values or value > max_values[key]:
                    valid = False
                    break

            print(f"{valid} --- {line}")
            if valid:
                total += int(game_number)
    return total

def part_two(filename):
    pass

def run_tests():
    draw = '3 blue, 4 red, 1 green'
    result = parse_draw(draw)

    assert(result == {'blue': 3, 'red': 4, 'green': 1}) 

    game = 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'
    result = parse_game(game)
    assert(result == {'blue': 9, 'red': 5, 'green': 4})

    return "Success!"

def main():
    parser = argparse.ArgumentParser("day 1")
    parser.add_argument("part")
    parser.add_argument("filename")
    args = parser.parse_args()

    result = None
    if args.part == '1':
        result = part_one(args.filename)
    elif args.part == '2':
        result = part_two(args.filename)
    elif args.part == 'test':
        result = run_tests()
    print(result)

if __name__ == "__main__":
    main()
