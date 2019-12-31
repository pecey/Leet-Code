mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def romanToInt(s: str) -> int:
    aggregator = 0
    while len(s) > 1:
        first_letter = s[0]
        second_letter = s[1]
        if first_letter == "I" and second_letter in ["V", "X"]:
            aggregator += -1 + mapping[second_letter]
            s = s[2:]
        elif first_letter == "X" and second_letter in ["L", "C"]:
            aggregator += -10 + mapping[second_letter]
            s = s[2:]
        elif first_letter == "C" and second_letter in ["D", "M"]:
            aggregator += -100 + mapping[second_letter]
            s = s[2:]
        else:
            aggregator += mapping[first_letter]
            s = s[1:]
    if len(s) == 1:
        aggregator += mapping[s]
    return aggregator


print(romanToInt("IV"))
