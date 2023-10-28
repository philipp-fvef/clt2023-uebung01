# -*-coding:utf-8 -*-
# Date: 2022-10-24 15:16:00


# Grammatik
T = ["Hans", "isst", "Kaesebrot", "ein"]
N = ["S", "NP", "VP", "V", "N", "Det"]
S = ["S"]
P = ["S → NP VP", "NP → Det N", "VP → V NP", "V → isst", "NP → Hans", "Det → ein", "N → Kaesebrot"]


def parse_S(sentence: list, start, end) -> bool:
    print(f"S von {start} bis {end}?")

    for j in range(start+1, end):
        print(f"trying < {P[0]} > on <", sentence[start:j], sentence[j:end], ">")
        if parse_NP(sentence, start, j) and parse_VP(sentence, j, end):
            print(f"Found S von {start} bis {end}")
            return True

    print(f"No S von {start} bis {end}")
    return False


def parse_NP(sentence: list, start, end) -> bool:
    print(f"NP von {start} bis {end}?")

    print(f"trying < {P[4]} > on < {sentence[start:end]} >")
    if sentence[start:end] == ["Hans"]:
        print(f"Found NP von {start} bis {end}")
        return True

    for j in range(start+1, end):
        print(f"trying < {P[1]} > on <", sentence[start:j], sentence[j:end], ">")
        if parse_Det(sentence, start, j) and parse_N(sentence, j, end):
            print(f"Found NP von {start} bis {end}")
            return True

    print(f"No NP von {start} bis {end}")
    return False


def parse_VP(sentence: list, start, end) -> bool:
    print(f"VP von {start} bis {end}?")

    for j in range(start+1, end):
        print(f"trying <{P[2]}> on <", sentence[start:j], sentence[j:end], ">")
        if parse_V(sentence, start, j) and parse_NP(sentence, j, end):
            print(f"Found VP von {start} bis {end}")
            return True

    print(f"No VP von {start} bis {end}")
    return False


def parse_N(sentence: list, start, end) -> bool:
    print(f"N von {start} bis {end}?")

    print(f"trying <{P[6]}> on {sentence[start:end]}")
    if sentence[start:end] == ["Kaesebrot"]:
        print(f"Found N von {start} bis {end}")
        return True

    print(f"No N von {start} bis {end}")
    return False


def parse_V(sentence: list, start, end) -> bool:
    print(f"V von {start} bis {end}?")

    print(f"trying <{P[3]}> on {sentence[start:end]}")
    if sentence[start:end] == ["isst"]:
        print(f"Found V von {start} bis {end}")
        return True

    print(f"No V von {start} bis {end}")
    return False


def parse_Det(sentence: list, start, end) -> bool:
    print(f"Det von {start} bis {end}?")

    print(f"trying <{P[5]}> on {sentence[start:end]}")
    if sentence[start:end] == ["ein"]:
        print(f"Found Det von {start} bis {end}")
        return True

    print(f"No Det von {start} bis {end}")
    return False


if __name__ == "__main__":
    word = "Kaesebrot isst Hans".split(" ")
    print(f"\nRESULT: {parse_S(word, 0, len(word))}")
