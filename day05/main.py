import sys
sys.path.insert(1, '.')
import util

def main():
    text = open("day05/input.txt").read().strip()

    parts = text.split("\n\n")
    crates = get_crates(text)
    crates_1 = move_crates(text, crates)
    print("".join(top_of_crates(crates_1)))
    crates = get_crates(text)
    crates_2 = move_crates_bulk(text, crates)
    print("".join(top_of_crates(crates_2)))

def parse_instruction(line):
    p = line.split(" ")
    return (int(p[1]), int(p[3]) - 1, int(p[5]) - 1)

def move_crates(text, crates):
    text = text.split("\n\n")[1].strip()

    for line in text.split("\n"):
        ins = parse_instruction(line)
        for i in range(ins[0]):
            c = crates[ins[1]].pop()
            crates[ins[2]].append(c)

    return crates

def move_crates_bulk(text, crates):
    text = text.split("\n\n")[1].strip()

    for line in text.split("\n"):
        ins = parse_instruction(line)
        new = []
        for i in range(ins[0]):
            c = crates[ins[1]].pop()
            new.append(c)
        for c in new[::-1]:
            crates[ins[2]].append(c)

    return crates

def get_crates(text):
    text = text.split("\n\n")[0][2:]
    print(text)
    crates = [ [] for x in range(9) ]
    for line in text.split("\n")[:-1]:
        for i in range(1, 4*9, 4):
            if line[i] != " ":
                crates[i // 4].append(line[i])
    for crate in crates:
        crate = crate.reverse()
    return crates

def top_of_crates(crates):
    return [ stack[-1] for stack in crates ]

if __name__ == "__main__":
    main()
