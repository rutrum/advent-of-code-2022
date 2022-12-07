import sys
sys.path.insert(1, '.')
import util

class file:
    def new_root():
        f = file("/")
        return f

    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = None
        self.size = None

    def mkdir(self, name):
        child = file(name)
        child.parent = self
        self.children.append(child)
        return child

    def touch(self, name, size):
        child = file(name)
        child.parent = self
        child.size = size
        self.children.append(child)

    def get_size(self):
        if self.size:
            return self.size
        else:
            return sum([ c.get_size() for c in self.children ])


    def get_size_less_than_100k(self):
        total = 0
        for d in self.dirs():
            if d.get_size() < 100000:
                total += d.get_size()
        return total

    def dirs(self):
        if len(self.children) > 0:
            yield self
        for c in self.children:
            yield from c.dirs()


    def abspath(self):
        parts = [self.name]
        p = self.parent
        while p:
            if p.name != "/":
                parts.append(p.name)
            p = p.parent
        return "/" + "/".join(parts[::-1])

    def root(self):
        p = self
        while True:
            if p.parent:
                p = p.parent
            else:
                return p


def main():
    text = open("day07/input.txt").read().strip()
    root = explore(text)
    print(f"Sum of size of all dirs < 100k: {root.get_size_less_than_100k()}")

    total_size = root.get_size()
    free_space = (70000000 - total_size)
    space_to_delete = 30000000 - free_space

    print(f"Need to delete {space_to_delete}")

    sizes = []
    for d in root.dirs():
        sizes.append((d.get_size(), d.abspath()))
    sizes = sorted(sizes)

    for size in sizes:
        if size[0] > space_to_delete:
          print(f"Need to delete {size[1]} of size {size[0]}")
          break;


def explore(text):
    pwd = None

    for line in text.split("\n"):
        if line.startswith("$"):
            # command
            command = line.split()[1]
            args = line.split()[2:]

            if command == "cd":
                if args[0] == "/":
                    pwd = file.new_root()
                elif args[0] == "..":
                    pwd = pwd.parent
                else:
                    pwd = pwd.mkdir(args[0])
            else:
                # ls? dont care
                pass
        else:
            # list of stuff
            dir_or_size = line.split()[0]
            name = line.split()[1]
            try:
                size = int(dir_or_size)
            except:
                continue
            pwd.touch(name, size)

    return pwd.root()

if __name__ == "__main__":
    main()
