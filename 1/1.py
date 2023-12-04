import re
import argparse
from enum import Enum

def part_one(filename):
    total = 0

    with open(filename, 'r') as f:
        for line in f:
            first, second = '', ''
            for cha in line:
                if cha.isdigit():
                    if first == '':
                        first = cha
                    else:
                        second = cha
            if first == '':
                continue
            second = second if second != '' else first 
            number = int(first+second)
            total += number
    return total


DIGITS = {"one": '1',
     "two": '2',
     "three": '3',
     "four": '4',
     "five": '5',
     "six": '6',
     "seven": '7',
     "eight": '8',
     "nine": '9'}

numeric_re = re.compile(r'\d')
spelled_re = re.compile(r'one|two|three|four|five|six|seven|eight|nine')

def first_numeric_digit(line):
    match = re.search(numeric_re, line)
    if match is None:
        return None, None
    return match.start(), match.group(0) 

def first_spelled_digit(line):
    match = re.search(spelled_re, line)
    if match is None:
        return None, None
    return match.start(), DIGITS[match.group(0)]

def last_numeric_digit(line):
    line = line[::-1]
    match = re.search(numeric_re, line)
    if match is None:
        return None, None
    reversed_idx = match.start()
    idx = (len(line) - 1) - reversed_idx
    return idx, match.group(0)
    
spelled_reversed_re = re.compile(r'eno|owt|eerht|ruof|evif|xis|neves|thgie|enin')
def last_spelled_digit(line):
    line = line[::-1]

    match = re.search(spelled_reversed_re, line)
    if match is None:
        return None, None

    reversed_idx = match.end()
    idx = (len(line) - 1) - (match.end() - 1)
    return idx, DIGITS[match.group(0)[::-1]]

def get_first_digit(line):
    numeric_idx, numeric_digit = first_numeric_digit(line)
    spelled_idx, spelled_digit = first_spelled_digit(line)

    if numeric_idx is None and spelled_idx is None:
        return ''
    if numeric_idx is None and spelled_idx is not None:
        return spelled_digit
    if spelled_idx is None and numeric_idx is not None:
        return numeric_digit
    if numeric_idx < spelled_idx:
        return numeric_digit
    return spelled_digit

def get_last_digit(line):
    numeric_idx, numeric_digit = last_numeric_digit(line)
    spelled_idx, spelled_digit = last_spelled_digit(line)

    if numeric_idx is None and spelled_idx is None:
        return ''
    if numeric_idx is None and spelled_idx is not None:
        return spelled_digit
    if spelled_idx is None and numeric_idx is not None:
        return numeric_digit
    if numeric_idx > spelled_idx:
        return numeric_digit
    return spelled_digit

def get_number_in_line(line):
    first = get_first_digit(line)
    last = get_last_digit(line)
    if first == '' and last == '':
        return 0
    return int(first + last)


def run_tests():
    test_string = "abcone1"
    r = first_numeric_digit(test_string)
    assert(r == (6, 1))

    r = first_spelled_digit(test_string)
    assert(r == (3, 1))


    r = last_numeric_digit(test_string)
    assert(r == (6, 1))

    test_string = "ab12356"
    r = last_numeric_digit(test_string)
    assert(r == (6, 6))

    test_string = "onetwothreefour"
    r = last_spelled_digit(test_string)
    assert(r == (11, 4))

    return "Success"


def part_two(filename):
    total = 0

    with open(filename, 'r') as f:
        for line in f:
            number = get_number_in_line(line.strip())
            total += number
    return total


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
