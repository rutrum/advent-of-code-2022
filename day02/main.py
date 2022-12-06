import sys
sys.path.insert(1, '.')
import util

def main():
    text = open("day02/input.txt").read()
    # A rock, B paper, C scissors
    # X rock, Y paper, Z scissors
    # 0 lost, 3 draw, 6 won
    matches = create_matches(text)
    print("Suspected strat:", sum([result(m[0], m[1]) for m in matches]))
    print("Actual strat:", sum([new_strat(m[0], m[1]) for m in matches]))

def create_matches(text):
    def map_letter(letter):
        o = ord(letter) - 65
        if o > 10:
            o -= 23
        return o

    matches = []
    for line in text.split("\n"):
        if line:
            letters = line.split()
            matches += [tuple(map_letter(x.strip()) for x in letters)]
    return matches

def new_strat(opponent, result):
    if result == 0:
        # loss
        you = (opponent + 2) % 3
        score = 0
    elif result == 1:
        # tie
        you = opponent
        score = 3
    else:
        you = (opponent + 1) % 3
        score = 6

    return you + 1 + score

def result(opponent, you):
    if opponent == you:
        # tie
        return 3 + you + 1
    elif (you + 1) % 3 == opponent:
        # loss
        return you + 1
    else:
        # win
        return 6 + you + 1


if __name__ == "__main__":
    main()
