from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
sentence_0=And(AKnight, AKnave)
knowledge0 = And(
Or(AKnight, AKnave),
Not(And(AKnight, AKnave)),

Implication(AKnave, Not(sentence_0)),
Implication(AKnight, sentence_0)

)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
sentence_1=And(AKnave, BKnave)
knowledge1 = And(
#Both A and B cant be knaves
Or(AKnight, BKnight),
Or(AKnave, BKnave ),
Not(And(AKnave, AKnight)),
Not(And(BKnave, BKnight)),

Implication(AKnight, sentence_1),
Implication(AKnave, Not(sentence_1))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
sentence2_0 = Or(And(AKnight, BKnight), And(AKnave, BKnave))
sentence2_1= Or(And(AKnight, BKnave), And(AKnave, BKnight))
knowledge2 = And(
#A is either a knight or a knave
#B is either a knight or a knave
#A cannot be both
#B cannot be both
Or(AKnight, AKnave),
Or(BKnight, BKnave),
Not(And(AKnave, AKnight)),
Not(And(BKnave, BKnight)),

Implication(AKnight, sentence2_0),
Implication(AKnave, Not(sentence2_0)),

Implication(BKnave, Not(sentence2_1)),
Implication(BKnight, sentence2_1)

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
sentence3_0 = Or(AKnight, AKnave) # A says either "I am a knight." or "I am a knave.", but you don't know which.
sentence3_1 = AKnave # B says "A said 'I am a knave'."
sentence3_2 = CKnave # B says "C is a knave."
sentence3_3 = AKnight # C says "A is a knight."

knowledge3 = And(
Or(AKnight, AKnave),
Or(BKnight, BKnave),
Or(CKnight, CKnave),
Not(And(AKnight, AKnave)),
Not(And(BKnave, BKnight)),
Not(And(CKnave, CKnight)),

Implication(AKnave, Not(sentence3_0)),
Implication(AKnight, sentence3_0),
Implication(BKnight, sentence3_1),
Implication(BKnave, Not(sentence3_1)),
Implication(BKnight, sentence3_2),
Implication(BKnave,Not(sentence3_2)),
Implication(CKnight, sentence3_3),
Implication(CKnave, Not(sentence3_3))


)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
