add_mapper = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

sub_mapper = {
    "I": 1,
    "X": 10,
    "C": 100
}


class Solution(object):
    def romanToInt(self, word):
        """
        :type word: str
        :rtype: int
        """
        prev = ""
        acc = 0
        for s in word:
            acc += add_mapper[s]
            if s == "V" or s == "X":
                if prev == "I":
                    acc -= add_mapper[prev]
                    acc -= sub_mapper[prev]

            elif s == "L" or s == "C":
                if prev == "X":
                    acc -= add_mapper[prev]
                    acc -= sub_mapper[prev]

            elif s == "D" or s == "M":
                if prev == "C":
                    acc -= add_mapper[prev]
                    acc -= sub_mapper[prev]
                    
            prev = s


        return acc
        