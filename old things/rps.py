# This is a rock paper scissors game. New version
# imports the python random module and sqlite3 module
import random
import sqlite3

# creates a tuple of options
options = ("rock", "paper", "scissors")

class DatabaseHelper:
    def __init__(self):

        self.conn = sqlite3.connect("./rps.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS scores (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, score INTEGER)")
        # set score of player and computer to 0 if the table is empty
        self.cursor.execute("SELECT * FROM scores")
        if len(self.cursor.fetchall()) == 0:
            self.cursor.execute("INSERT INTO scores (name, score) VALUES (?, ?)", ("player", 0))
            self.cursor.execute("INSERT INTO scores (name, score) VALUES (?, ?)", ("computer", 0))
        self.conn.commit()

    def save_score(self, name, score):
        self.cursor.execute("UPDATE scores SET score = score + ? WHERE name = ?", (score, name))
        self.conn.commit()

    def get_score(self, name):
        self.cursor.execute("SELECT score FROM scores WHERE name = ?", (name,))
        return self.cursor.fetchone()[0]

    def close(self):
        self.conn.close()

# creates a variable that will be used to run the game
def start_new_game():
    choice = input().lower() # gets the user's choice and converts it to lowercase
    options_dict = {
        "rock": rock_function,
        "paper": paper_function,
        "scissors": scissors_function
    }
    options_dict.get(choice, default_function)()
    start_new_game()

# Functions that run based on user input
def rock_function():
    dbhelper = DatabaseHelper()
    computer = computer_choice()
    # compare the user's choice to the computer's choice
    if computer == "rock":
        print("You chose rock and the computer chose", computer, ",", "It's a tie!")
    elif computer == "paper":
        print("You chose rock and the computer chose", computer, ",", "You lose!")
        dbhelper.save_score(name="computer",score=1)
        print("The computer's score is", dbhelper.get_score("computer"))
    else:
        print("You chose rock and the computer chose", computer, ",", "You win!")
        dbhelper.save_score(name="player",score=1)
        print("Your score is", dbhelper.get_score(name="player"))
    end_game()

def paper_function():
    dbhelper = DatabaseHelper()
    computer = computer_choice()
    # compare the user's choice to the computer's choice
    if computer == "paper":
        print("You chose paper and the computer chose", computer, "! It's a tie!")
    elif computer == "scissors":
        print("You chose paper and the computer chose", computer, "! You lose!")
        dbhelper.save_score(name="computer",score=1)
        print("The computer's score is", dbhelper.get_score("computer"))
    else:
        print("You chose paper and the computer chose", computer, "! You win!")
        dbhelper.save_score(name="player",score=1)
        print("Your score is", dbhelper.get_score(name="player"))
    end_game()

def scissors_function():
    dbhelper = DatabaseHelper()
    computer = computer_choice()
    # compare the user's choice to the computer's choice
    if computer == "scissors":
        print("You chose scissors and the computer chose", computer, "! It's a tie!")
    elif computer == "rock":
        print("You chose scissors and the computer chose", computer, "! You lose!")
        dbhelper.save_score(name="computer",score=1)
        print("The computer's score is", dbhelper.get_score("computer"))
    else:
        print("You chose scissors and the computer chose", computer, "! You win!")
        dbhelper.save_score(name="player",score=1)
        print("Your score is", dbhelper.get_score(name="player"))
    end_game()

def default_function():
    print("Invalid choice. Please try again.")

# Function that makes the computer choose between rock, paper and scissors at random
def computer_choice():
    computer = random.choice(options)
    return computer

# Functions that run at the end of the game
def end_game():
    print("")
    print("Would you like to play again? pick your choice below:")

# creates the main function of the game
def main():
    # welcome the user to the game
    print("Welcome to Rock, Paper, Scissors! please enter your choice below:")
    # calls the start_new_game function
    start_new_game()


if __name__ == '__main__':
    main()