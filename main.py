import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
num = random.randint(1,101)
print(f"Pssst, the correct answer is {num}")
choose_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if choose_level == "easy":
    def easy_level():
        attempts = 10
        print("You have 10 attempts remaining to guess the number.")
        while True:
            guess = int(input("Make a guess: "))
            if guess == num:
               print(f"You got it! The answer was {num}.")
               break
            elif guess < num:
               print("Too low.\nGuess again: ")
            else:
               print("Too high.\nGuess again: ")
            attempts -= 1
            print(f"You have {attempts} attempts remaining to guess the number.")
            if attempts ==0:
                break
    easy_level()

else:
    def hard_level():
        if choose_level == "hard":
            attempts = 5
        print("You have 5 attempts remaining to guess the number.")
        while True:
            guess = int(input("Make a guess: "))
            if guess == num:
                print(f"You got it! The answer was {num}.")
                break
            elif guess < num:
                print("Too low.\nGuess again: ")
            else:
                print("Too high.\nGuess again: ")
            attempts -= 1
            print(f"You have {attempts} attempts remaining to guess the number.")
            if attempts ==0:
                break
    hard_level()






