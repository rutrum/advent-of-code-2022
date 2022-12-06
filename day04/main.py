import sys
sys.path.insert(1, '.')
import util

def main():
    text = open("day04/input.txt").read().strip()

    # overlap entirely
    total = 0
    for line in text.split("\n"):
        elves = [assignment.split("-") for assignment in line.split(",")]
        for elf in elves:
            elf[0] = int(elf[0])
            elf[1] = int(elf[1])
        if elves[0][0] <= elves[1][0] and elves[0][1] >= elves[1][1]:
            total += 1
        elif elves[0][0] >= elves[1][0] and elves[0][1] <= elves[1][1]:
            total += 1
    print(total)

    # overlap at all
    total = 0
    for line in text.split("\n"):
        elves = [assignment.split("-") for assignment in line.split(",")]
        for elf in elves:
            elf[0] = int(elf[0])
            elf[1] = int(elf[1])
        if elves[0][1] < elves[1][0] or elves[0][0] > elves[1][1]:
            total += 1
    print(len(text.split("\n")) - total)

if __name__ == "__main__":
    main()
