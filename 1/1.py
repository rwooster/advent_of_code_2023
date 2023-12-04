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
            # import pdb; pdb.set_trace()
            total += number
    return total


def main():
    parser = argparse.ArgumentParser("day 1")
    parser.add_argument("filename")
    args = parser.parse_args()


    result = part_one(args.filename)
    print(result)

if __name__ == "__main__":
    main()
