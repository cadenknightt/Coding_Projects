import random

def playgame():
     print("Welcome to Guess the Number!")
     print("I am thinking of a number from 1 and 500.")
     print("Start guessing and I will say higher or lower.\n")

     secret_num = random.randint(1, 500)
     attempts = 0

     while True:
          try:
               guess = int(input("Place your guess: "))
          except ValueError:
               print("Please enter valid number.")
               continue

          attempts += 1

          if guess < secret_num:
               print("Higher!\n")
          elif guess > secret_num:
               print("Lower!\n")
          else:
               print(f"Good job, you guessed the number in {attempts} attempts!")
               break

while True:
     playgame()
     playagain = input("\nWould you like to play again? (yes/y or no/n): ")
     if playagain != "yes" and playagain != "y":
          print("\nThanks for playing! See ya!")
          break

