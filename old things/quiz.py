import math
import random

questions = [
    "Do you prefer cats or dogs? ",
    "If you could live anywhere in the world, where would it be? ",
    "Are you gay?", 
    "Can birds sing?",
    "What is the capital of South Korea?",
    "Would you rather have no hands or no legs? ",
    "What is 5+5?" ,
    "Bye", 
]

answers = [
    "Dogs",
    "Australia",
    "Yes",
    "Yes",
    "Seoul",
    "No hands",
    "10",
    "Bye",
]

def ask_question ():
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



