import random
from constants import QUESTIONS


def getRandomQuestion() -> str:
    rand = random.randint(0, len(QUESTIONS))
    return getQuestion(rand), rand

def createFullQuestion() -> str:
    rand = random.randint(1, 10)
    question, index = getRandomQuestion()
    print(len(QUESTIONS))
    if question:
        removeQuestion(index)
        print(f"Removing question from list...")
        print(len(QUESTIONS))
        return f"They're a {rand} but {question}."
    else:
        return f"Woah @hughjassvibes, i'm broken come fix me!"


def getQuestion(index: int) -> str:
    return QUESTIONS[index]


def removeQuestion(index: int) -> None:
    QUESTIONS.pop(index)

    
