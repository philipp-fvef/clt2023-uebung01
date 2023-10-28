# -*-coding:utf-8 -*-
# Date: 2022-10-24 15:16:00


# Grammatik
T = ["Hans", "isst", "Kaesebrot", "ein"]
N = ["S", "NP", "VP", "V", "N", "Det"]
S = ["S"]
P = ["S → NP VP", "NP → Det N", "VP → V NP", "V → isst", "NP → Hans", "Det → ein", "N → Kaesebrot"]


def parse_S(sentence: list, start, end) -> bool:
    print("s ", sentence[start:end])
    for j in range(start+1, end):
        print(f"trying <{P[0]}> on")
        print(sentence[start:j], sentence[j:end])
        if parse_NP(sentence, start, j) and parse_VP(sentence, j, end):
            print("returned True")
            return True

    print("Failed S Parse")
    return False


def parse_NP(sentence: list, start, end) -> bool:
    print("np ", sentence[start:end])

    for j in range(start+1, end):
        print(f"{j} - trying <{P[1]}> on")
        print(sentence[start:j], sentence[j:end])
        if parse_Det(sentence, start, j) and parse_N(sentence, j, end):
            print("returned True")
            return True
        print("returned False")

    print(f"trying <{P[4]}> on {sentence[start:end]}")
    if sentence[start:end] == ["Hans"]:
        print("returned True")
        return True
    print("returned False")

    print("Failed NP Parse")
    return False


def parse_VP(sentence: list, start, end) -> bool:
    print("vp ", sentence[start:end])
    for j in range(start+1, end):
        print(f"trying <{P[2]}> on")
        print(sentence[start:j], sentence[j:end])
        if parse_V(sentence, start, j) and parse_NP(sentence, j, end):
            print("returned True")
            return True

    print("Failed VP Parse")
    return False


def parse_N(sentence: list, start, end) -> bool:
    print("n ", sentence[start:end])
    print(f"trying <{P[6]}> on {sentence[start:end]}")
    if sentence[start:end] == ["Kaesebrot"]:
        print("returned True")
        return True

    print("Failed N Parse")
    return False


def parse_V(sentence: list, start, end) -> bool:
    print("v ", sentence[start:end])
    print(f"trying <{P[3]}> on {sentence[start:end]}")
    if sentence[start:end] == ["isst"]:
        print("returned True")
        return True

    print("Failed V Parse")
    return False


def parse_Det(sentence: list, start, end) -> bool:
    print("det ", sentence[start:end])
    print(f"trying <{P[5]}> on {sentence[start:end]}")
    print(sentence[start:end])
    if sentence[start:end] == ["ein"]:
        print("returned True")
        return True

    print("Failed Det Parse")
    return False


if __name__ == "__main__":
    word = "ein Kaesebrot isst Hans".split(" ")
    print(f"\nRESULT - {parse_S(word, 0, len(word))}")
    print(" ".join(word))
