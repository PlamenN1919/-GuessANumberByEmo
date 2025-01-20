import random

def play_game():
    print("Welcome to the 'Guess the Number' game!")

    difficulty = input("Choose difficulty (Easy, Medium, Hard): ").strip().lower()
    max_tries = {"easy": 10, "medium": 7, "hard": 5}.get(difficulty, 7)  # Default to Medium

    print(f"You have chosen {difficulty.capitalize()} mode. You have {max_tries} attempts per level!")
    
    level = 1
    min_num, max_num = 1, 100
    
    while True:
        print(f"\nLevel {level}: Guess the number between {min_num} and {max_num}!")
        number = random.randint(min_num, max_num)
        attempts = 0
        
        while attempts < max_tries:
            player_input = input(f"Attempt {attempts + 1}/{max_tries}: ")

            if not player_input.isdigit():
                print("Invalid input. Please enter a number.")
                continue

            player_number = int(player_input)
            attempts += 1

            if player_number == number:
                print(f"🎉 Correct! You've guessed the number in {attempts} attempts!")
                break
            elif player_number > number:
                print("Too High!")
            else:
                print("Too Low!")
        else:
            print(f"💔 You've run out of attempts! The number was {number}.")
            break

        level += 1
        max_num += 100  

        continue_game = input("Do you want to continue to the next level? (yes/no): ").strip().lower()
        if continue_game != "yes":
            print("Thanks for playing! See you next time!")
            break

    restart = input("Do you want to restart the game? (yes/no): ").strip().lower()
    if restart == "yes":
        play_game()
    else:
        print("Goodbye!")

play_game()
