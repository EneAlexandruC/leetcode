import random

class RandomizedSet:
    def __init__(self):
        self.s = set()

    def insert(self, val: int) -> bool:
        flag = val not in self.s
        if flag:
            self.s.add(val)
        return flag

    def remove(self, val: int) -> bool:
        flag = val in self.s
        if flag:
            self.s.remove(val)
        return flag

    def getRandom(self) -> int:
        return random.choice(list(self.s))

def main():
    obj = RandomizedSet()
    val = 2
    print(obj.insert(val))
    print(obj.getRandom())

if __name__ == '__main__':
    main()