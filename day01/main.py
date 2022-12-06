import sys
sys.path.insert(1, '.')
import util

def main():
    text = open("day01/input.txt").read()
    totals = []
    for elf_idx, elf in enumerate(text.split("\n\n")):
        elf = elf.strip()
        total = 0
        for snack in elf.split("\n"):
            total += int(snack.strip())
        totals += [total]

    print(sum(sorted(totals)[:-4:-1]))

if __name__ == "__main__":
    main()
