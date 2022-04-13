class Numbers:
    Multiplier = 2

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    @classmethod
    def multiply(cls, a):
        return a * Numbers.Multiplier

    @staticmethod
    def subtract(b, c):
        return b - c

    @property
    def value(self):
        return self.x, self.y

    @value.setter
    def value(self, xy_tup):
        self.x, self.y = xy_tup

    @value.deleter
    def value(self):
        del self.x
        del self.y


n = Numbers(2, 3)
print(n.value)
