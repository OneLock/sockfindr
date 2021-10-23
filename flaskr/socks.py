from random import randint, random
import sys


class SockFactory:

    def build(self):
        size = randint(32,49)
        left_or_right = randint(0, sys.maxsize)
        return Colorgenerator.color()[0], left_or_right, size

class Colorgenerator:

    def color(self, n=1):
        rand_colors = []
        for j in range(n):
            rand_colors = ["#" + ''.join(random.choice('ABCDEF0123456789')) for i in range(6)]
        return rand_colors

class Sock:
    color, left_or_right, size = SockFactory.build()
    found_pair = False

    def is_other(self, other):
        if type(other) is Sock:
            return all([ slf == oth for slf , oth in  zip(self.stream ,other.stream)])
        else:
            return False

