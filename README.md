# Guess the Best Things 
A simple Python program that asks the user to guess the "best" animal, film, and food. The program uses loops, conditions, hints and counters to test my knowledge on beginner basics.

# Features:
- Reusable function for guessing with:
  - Custom question
  - Correct answer
  - Hint after 2 wrong attempts
  - Limited number of tries
- Summary to check if all answers were correct.

1. The program defines the function `guess_the_best()` so that it:
   - Asks the user a question.
   - Checks if the answer is correct.
   - Gives a hint after 2 wrong attempts.
   - Stops after 3 attempts/when the user guesses correctly.
    
2. The main program calls this function `guess_the_best()` for:
   - Best animal (Lion)
   - Best film (Lion King)
   - Best food (Chicken)
  
3. At the end, it prints a summary message based on the answers.
   The correct answers will have "Good Choices!", otherwise, "Not so good taste, ey?"
