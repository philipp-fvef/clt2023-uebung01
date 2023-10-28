# -*-coding:utf-8 -*-
# Date: 2022-10-24 15:16:00


# Input
word = "Hans isst ein Käsebrot"
word = word.split(" ")

# Grammatik
T = ["Hans", "isst", "Käsebrot", "ein"]
N = ["S", "NP", "VP", "V", "N", "Det"]
S = ["S"]
P = ["S → NP VP", "NP → Det N", "VP → V NP", "V → isst", "NP → Hans", "Det → ein", "N → Käsebrot"]


# for production in P:
#     print("")
#
#     sides = production.split("→")
#     left_side = sides[0].strip()
#     right_side = sides[1].strip()
#
#     print(f"<{left_side}> geht nach <{right_side}>")
#
#     if left_side in S: print("Start")
#     elif right_side in T: print("Terminal")
#     else: print("Expansion")


def parse_S(sentence: list, start: int, end: int) -> bool:

    for j in range(start, end):
        print(j)
        print(f"trying <{P[0]}> on")
        print(sentence[start:j], sentence[j:end])
        if parse_NP(sentence[start:j], 0, j) and parse_VP(sentence[j:end], j, end):
            print("returned True")
            return True

    print("Failed S Parse")
    return False


def parse_NP(sentence: list, start: int, end: int) -> bool:
    print("parsing NP")

    for j in range(start, end):
        print(j)
        print(f"trying <{P[1]}> on")
        print(sentence[start:j], sentence[j:end])
        if parse_Det(sentence[start:j], 0, j) and parse_N(sentence[j:end], j, end):
            print("returned True")
            return True
        print("returned False")

    for j in range(start, end):
        print(j)
        print(f"trying <{P[4]}> on")
        print(sentence[start:j], sentence[j:end])
        if str(sentence) in "Hans":
            print("returned True")
            return True
        print("returned False")

    print("Failed NP Parse")
    return False


def parse_VP(sentence: list, start: int, end: int) -> bool:
    print("parsing VP")

    for j in range(start, end):
        print(j)
        print(f"trying <{P[2]}> on")
        print(sentence[start:j], sentence[j:end])
        if parse_V(sentence[start:j], 0, j) and parse_NP(sentence[j:end], j, end):
            print("returned True")
            return True

    print("Failed VP Parse")
    return False


def parse_N(sentence: list, start: int, end: int) -> bool:
    print("parsing N")

    for j in range(start, end):
        print(j)
        print(f"trying <{P[6]}> on")
        print(sentence[start:j], sentence[j:end])
        if str(sentence) in "Kaesebrot":
            print("returned True")
            return True

    print("Failed N Parse")
    return False


def parse_V(sentence: list, start: int, end: int) -> bool:
    print("parsing V")

    for j in range(start, end):
        print(j)
        print(f"trying <{P[3]}> on")
        print(sentence[start:j], sentence[j:end])
        if str(sentence) in "isst":
            print("returned True")
            return True

    print("Failed V Parse")
    return False


def parse_Det(sentence: list, start: int, end: int) -> bool:
    print("parsing Det")

    for j in range(start, end):
        print(j)
        print(f"trying <{P[5]}> on")
        print(sentence[start:j], sentence[j:end])
        if str(sentence) in "ein":
            print("returned True")
            return True

    print("Failed Det Parse")
    return False


print(f"\nRESULT - {parse_S(word, 0, len(word))}")
