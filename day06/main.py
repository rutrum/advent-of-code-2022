import sys
sys.path.insert(1, '.')
import util

def main():
    text = open("day06/input.txt").read().strip()

    start_of_packet = find_distinct(text, 4)
    print(start_of_packet)
    start_of_message = find_distinct(text[start_of_packet:], 14)
    print(start_of_message + start_of_packet)


def find_distinct(text, l):
    for i in range(len(text) - l):
        d = {}
        for x in range(l):
            d[text[i + x]] = 0
        if len(d.keys()) == l:
            return i + l


if __name__ == "__main__":
    main()
