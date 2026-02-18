import numpy as np
from pyparsing import List

# TODO [1]: implement the guessing_game function
def guessing_game(max: int, *, attempts: int) -> tuple[bool, tuple[int, ...], int]: # hint: return type is tuple[bool, list[int], int]:
    chosen_int: int = int(np.random.randint(1,max + 1))
    guesses: List[int] = []

    print(f"\nPlease choose a number between 1 and {max}.")
    print(f"You have {attempts} attempts to guess it.\n")

    remaining_attempts: int = attempts

    while remaining_attempts > 0:
        try:
            user_input: str = input("Enter your guess: ")
            guess: int = int(user_input)
        except ValueError as e:
            raise ValueError("Invalid input. Please enter a valid one.") from e
        
        guesses.append(guess)

        if guess == chosen_int:
            print("CORRECT!")
            return True, tuple(guesses), chosen_int
        
        remaining_attempts -= 1

        if remaining_attempts > 0:
            if guess < chosen_int:
                print("Too low! number of remaining attempts: ", remaining_attempts)
            else:
                print("Too high! number of remaining attempts: ", remaining_attempts)
        else:
            print("GAME OVER!")
    
    print(f"The correct number was: {chosen_int}")
    return False, tuple(guesses), chosen_int



# TODO [2]: implement the play_game function
def play_game()-> None:
    max_value:int = 20
    attempts:int = 5
    
    while True:
        won, guesses, chosen_int = guessing_game(max_value, attempts=attempts)

        if not won:
            assert chosen_int not in guesses, "ERROR: in game function, your guess was incorrect but there is an error"
            
            play_again: str = input("Do you want to play again? (yes/no): ").strip().lower()
            if play_again.lower() != "yes":
                print("Thanks for playing! Goodbye!")
                break
        else:
            assert chosen_int in guesses, "ERROR: in game function, your guess was correct but there is an error"
            print("Congratulations! You guessed the number correctly!")
            break

