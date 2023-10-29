from nltk.parse import RecursiveDescentParser
from nltk import Nonterminal, nonterminals, Production, CFG

S, NP, VP, V, N, Det = nonterminals("S, NP, VP, V, N, Det")

T = ["Hans", "isst", "Kaesebrot", "ein"]
NT = ["S", "NP", "VP", "V", "N", "Det"]
P = ["S → NP VP", "NP → Det N", "VP → V NP", "V → isst",
     "NP → Hans", "Det → ein", "N → Kaesebrot"]

nt1 = Nonterminal('S')
nt2 = Nonterminal('NP')
nt3 = Nonterminal('VP')
nt4 = Nonterminal('V')
nt5 = Nonterminal('N')
nt6 = Nonterminal('Det')

prod1 = Production(S, [NP, VP])
prod2 = Production(NP, [Det, N])
prod3 = Production(NP, ["Hans"])
prod4 = Production(VP, [V, NP])
prod5 = Production(N, ["Kaesebrot"])
prod6 = Production(V, ["isst"])
prod7 = Production(Det, ["ein"])

grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
NP -> "Hans"
VP -> V NP
N -> "Kaesebrot"
V -> "isst"
Det -> "ein"
""")

rd = RecursiveDescentParser(grammar)

sentence = "isst ein Kaesebrot".split()

for t in rd.parse(sentence):
     print(t)
