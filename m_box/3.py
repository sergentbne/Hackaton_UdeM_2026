import random


class alpha:
    def __init__(self):

        with open("input_level_3.txt", "r") as f:
            n = int(f.readline())
            a = []
            for _ in range(n):
                line = f.readline()
                tokens = line.split()
                a.append(tokens)
            print(len(a[0]))
            self.bits = a[0]
            self.cadenas = a[1]

    def check_cadenas(self, cadenas_externe):
        list_of_good = []
        for pos, i in enumerate(cadenas_externe):
            if i == self.cadenas[pos]:
                list_of_good.append(True)
            else:
                list_of_good.append(False)
        for pos, i in enumerate(list_of_good):
            if i:
                list_of_good[pos] = self.bits[pos]
            else:
                list_of_good[pos] = random.randint(0, 1)
        return list_of_good

    def get_cadenas(self):
        return self.cadenas


class beta:
    def __init__(self, a: alpha):
        self.cadenas = [random.randint(0, 1) for i in range(83)]
        self.cadenas = ["Σ" if x == 0 else "ε" for x in self.cadenas]
        bits = a.check_cadenas(self.cadenas)
        alpha_cadenas = a.get_cadenas()
        good_guess = {}
        for pos, i in enumerate(alpha_cadenas):
            if i == self.cadenas[pos]:
                good_guess[pos] = bits[pos]
        print(good_guess)


a = alpha()
b = beta(a)
