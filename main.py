

class musswaschaun:

    def __init__(self, filename: str):
        with open(filename, encoding="UTF-8") as file:
            #self.words = set(file.read().split())
            self.letter = set(file.read().lower())
            print(self.map_primes_to_letters(self.letter))

    def map_primes_to_letters(self, letters):
        d = {}
        primes = self.gen_primes()
        print(dict(primes))
        for letter in letters:
            pass
        return d

    @ staticmethod
    def gen_primes():
        # Source: https://code.activestate.com/recipes/117119/
        """ Generate an infinite sequence of prime numbers."""
        # Maps composites to primes witnessing their compositeness.
        # This is memory efficient, as the sieve is not "run forward"
        # indefinitely, but only as long as required by the current
        # number being tested.
        #
        D = {}

        # The running integer that's checked for primeness
        q = 2

        while True:
            if q not in D:
                # q is a new prime.
                # Yield it and mark its first multiple that isn't
                # already marked in previous iterations
                # 
                yield q
                D[q * q] = [q]
            else:
                # q is composite. D[q] is the list of primes that
                # divide it. Since we've reached q, we no longer
                # need it in the map, but we'll mark the next 
                # multiples of its witnesses to prepare for larger
                # numbers
                # 
                for p in D[q]:
                    D.setdefault(p + q, []).append(p)


    def get_all_anagrams(self, word: str):
        pass

if __name__ == "__main__":
    a = musswaschaun("german.dic")
    print(a.letter)
