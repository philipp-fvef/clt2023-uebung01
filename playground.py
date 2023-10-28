sentence = ["Hans", "isst", "ein", "Kaesebrot"]
sentence = sentence[1:]


# print("True  - S  ", sentence[0:4])
# print("True  - NP ", sentence[2:4])
# print("False - N  ", sentence[0:1])
# print("True  - VP ", sentence[1:4])
# print("False - V  ", sentence[0:1])


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


def splits(sent, begin, end):

    if len(sent) == 1:
        print(sent)
    else:
        for i in range(begin+1, end):
            print(sent[begin:i], sent[i:end])


splits(sentence, 0, len(sentence))
print([i for i in range(1,2)])
