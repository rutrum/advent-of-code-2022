import sys
sys.path.insert(1, '.')
import util

def main():
    text = open("day03/input.txt").read().strip()

    # part 1
    sum_priority = 0
    for line in text.split("\n"):
        l = len(line)
        first = line[:l//2]
        second = line[l//2:]
        first_chars = characters(first)
        for char in second:
            if char in first_chars:
                sum_priority += priority(char)
                break
    print(sum_priority)

    # part 2
    sum_priority = 0
    lines = text.split("\n")
    for line_num in range(0, len(lines), 3):
        sacks = lines[line_num:line_num+3]
        chars = characters(sacks[0])
        for x in range(1, 3):
            next_sack = sacks[x]
            for char in next_sack:
                if char in chars and chars[char] == x-1:
                    chars[char] = x
        for char in chars:
            if chars[char] == 2:
                sum_priority += priority(char)
    print(sum_priority)

def characters(string):
    chars = {}
    for char in string:
        chars[char] = 0
    return chars

def priority(c):
    o = ord(c)
    return o - ord('A') + 27 if o <= ord('Z') else o - ord('a') + 1

if __name__ == "__main__":
    main()
