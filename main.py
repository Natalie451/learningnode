import math
import random

questions = [
    "How many wheels does a car have?",
    "How old is a person?",
    "Name a famous gay rock band",
    "What is the capital of France?",
    "Are you dumb",
    "What is 2+2",
    "How many people are there in the world?",
    "Bye",
]

answers = [
    "4",
    "25",
    "The Beatles",
    "Paris",
    "No",
    "4",
    "100",
    "Bye",
]
    

def ask_question():
    score = 0
    index_number = math.floor(random.random() * len(questions))
    print(questions[index_number])
    answer = input()
    if answer == answers[index_number]:
        score = score + 1
        print("Correct! Your score is now " + str(score))
        print(" ")
        print(" ")
        print(" ")
        ask_question()
    elif answer != answers[index_number]:
        print("Wrong! Your score is still " + str(score))
        print(" ")
        print(" ")
        print(" ")
        ask_question()

def main ():
    ask_question()
    

if __name__ == "__main__":
    main()