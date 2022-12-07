import sys
from pathlib import Path

CWD = []
N = '\n'
T = '\t'

class File():
    def __init__(self, filename, size):
        self.filename = filename
        self.size_ = size
        return

    def __repr__(self):
        return f"File({repr(self.filename)}, {self.size_})"

    def size(self):
        return self.size_

class Directory():
    def __init__(self, path):
        self.path = path
        self.dirs = []
        self.files = []
        self.size_ = None
        return

    def size(self):
        if self.size_ == None:
            self.size_ = sum(t.size() for t in self.files) + sum(t.size() for t in self.dirs)
        return self.size_

    def __repr__(self):
        return f"{self.path}\n{N.join(T + repr(t) for t in self.dirs)}\n{N.join(T + repr(t) for t in self.files)}"


for line in sys.stdin:
    line = line.rstrip() 

    if line.startswith('$'):
        parts = line.split(' ')
        if len(parts) == 2:
            _, command = parts
            assert command == 'ls'
        elif len(parts) == 3:
            _, command, path = parts
            assert command == 'cd'
            if path == '..':
                CWD.pop(-1)
            else:
                d = Directory(path)
                if len(CWD) > 0:  # start case
                    CWD[-1].dirs.append(d)
                CWD.append(d)
        # COMMAND
        pass
    elif line.startswith('dir'):
        # DIR
        pass
    else:
        # FILE
        size_str, filename = line.split(' ')
        f = File(filename, int(size_str))
        CWD[-1].files.append(f)

def part1(directory):
    total = 0
    s = directory.size()
    if directory.size() <= 100_000:
        total += s
    for d in directory.dirs:
        total += part1(d)
    return total

print(part1(CWD[0]))
