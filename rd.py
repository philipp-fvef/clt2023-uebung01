# -*-coding:utf-8 -*-
# Date: 2022-10-24 15:16:00


# Input
word = "ein Kaesebrot isst Hans"
word = word.split(" ")

# Grammatik
T = ["Hans", "isst", "Kaesebrot", "ein"]
N = ["S", "NP", "VP", "V", "N", "Det"]
S = ["S"]
P = ["S → NP VP", "NP → Det N", "VP → V NP", "V → isst", "NP → Hans", "Det → ein", "N → Kaesebrot"]


def parse_S(sentence: list) -> bool:

    for j in range(1, len(sentence)):
        print("S", j)
        print(f"trying <{P[0]}> on")
        print(sentence[:j], sentence[j:])
        if parse_NP(sentence[:j]) and parse_VP(sentence[j:]):
            print("returned True")
            return True

    print("Failed S Parse")
    return False


def parse_NP(sentence: list) -> bool:
    print("parsing NP")

    if len(sentence) > 1:
        for j in range(1, len(sentence)):
            print(f"{j} - trying <{P[1]}> on")
            print(sentence[:j], sentence[j:])
            if parse_Det(sentence[:j]) and parse_N(sentence[j:]):
                print("returned True")
                return True
            print("returned False")

    if len(sentence) == 1:
        print(f"trying <{P[4]}> on {sentence}")
        if len(sentence) == 1 and sentence[0] == "Hans":
            print("returned True")
            return True
        print("returned False")

    print("Failed NP Parse")
    return False


def parse_VP(sentence: list) -> bool:
    print("parsing VP")

    if len(sentence) > 1:
        for j in range(1, len(sentence)):
            print(f"trying <{P[2]}> on")
            print(sentence[:j], sentence[j:])
            if parse_V(sentence[:j]) and parse_NP(sentence[j:]):
                print("returned True")
                return True

    print("Failed VP Parse")
    return False


def parse_N(sentence: list) -> bool:
    print("parsing N")

    print(f"trying <{P[6]}> on {sentence}")
    if len(sentence) == 1 and sentence[0] == "Kaesebrot":
        print("returned True")
        return True
    print("returned False")

    print("Failed N Parse")
    return False


def parse_V(sentence: list) -> bool:
    print("parsing V")

    print(f"trying <{P[3]}> on {sentence}")
    if len(sentence) == 1 and sentence[0] == "isst":
        print("returned True")
        return True
    print("returned False")

    print("Failed V Parse")
    return False


def parse_Det(sentence: list) -> bool:
    print("parsing Det")

    print(f"trying <{P[5]}> on {sentence}")
    if len(sentence) == 1 and sentence[0] == "ein":
        print("returned True")
        return True
    print("returned False")

    print("Failed Det Parse")
    return False


print(f"\nRESULT - {parse_S(word)}")
