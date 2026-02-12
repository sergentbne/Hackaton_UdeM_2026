import random

random.seed()
miss = 0
hit = 0


class alpha:
    instances = []

    def __init__(self):
        alpha.instances.append(self)
        with open("input_level_4.txt", "r") as f:
            n = int(f.readline())
            a = []
            for _ in range(n):
                line = f.readline()
                tokens = line.split()
                a.append(tokens)
            self.bits = a[0]
            self.bits_backup = self.bits.copy()
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
                numb = str(random.randint(0, 1))
                list_of_good[pos] = numb
        self.bits = list_of_good.copy()
        return self.bits

    def get_cadenas(self):
        return self.cadenas

    def get_real_and_compare(self, dict_of_value):
        global hit, miss
        # for i in dict_of_value:
        #     if self.bits_backup[i] == dict_of_value[i]:
        #         hit += 1
        #     else:
        #         miss += 1
        for i in dict_of_value:
            print(
                f"pos {i}: bit A: {self.bits_backup[i]}, bit B: {dict_of_value[i]} = {self.bits_backup[i] == dict_of_value[i]}"
            )
            if self.bits_backup[i] == dict_of_value[i]:
                hit += 1
            else:
                miss += 1


class sigma:
    instances = []

    def __init__(self):
        sigma.instances.append(self)
        self.alpha = None

    def guess(self):
        self.cadenas = [random.randint(0, 1) for i in range(83)]
        self.cadenas = ["Σ" if x == 0 else "ε" for x in self.cadenas]

        good_guess_alpha = {}
        for a in alpha.instances:
            bits = a.check_cadenas(self.cadenas)
            alpha_cadenas = a.get_cadenas()
            for pos, i in enumerate(alpha_cadenas):
                if i == self.cadenas[pos]:
                    good_guess_alpha[pos] = bits[pos]
        # good_guess_beta= {}
        # for b in beta.instances:
        #     for pos, ii in enumerate(b.get_cadenas()):
        #
        #             if ii == self.cadenas[pos]:
        #                  good_guess_beta[pos] = bits[pos]

    def final_check(self):
        for a in alpha.instances:
            a.get_real_and_compare(beta.instances[0].get_good_guess())
        print(f"{hit=}, {miss=}")


class beta:
    instances = []

    def __init__(self, a: alpha):
        beta.instances.append(self)
        self.cadenas = [random.randint(0, 1) for i in range(83)]
        self.cadenas = ["Σ" if x == 0 else "ε" for x in self.cadenas]
        self.intercept()
        self.bits = a.check_cadenas(self.cadenas)
        alpha_cadenas = a.get_cadenas()
        self.good_guess = {}
        for pos, i in enumerate(alpha_cadenas):
            if i == self.cadenas[pos]:
                self.good_guess[pos] = self.bits[pos]
        self.check()

    def get_cadenas(self):
        return self.cadenas

    def get_good_guess(self):
        return self.good_guess

    def check(self):
        for i in sigma.instances:
            i.final_check()

    def intercept(self):
        for i in sigma.instances:
            i.guess()


a = alpha()
o = sigma()
b = beta(a)
