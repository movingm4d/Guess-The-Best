# Guess the best things.


# SUBPROGRAM
#def will define guess_the_best with four parameters
#def will make it flexible and reusable for film & food
def guess_the_best(question, correct_answer, hint, max_attempts=3):
    
    attempts = 0 #counter starts at 0
    guess = "" #stays empty so loop can be run

    #loop will run until correct guesses or max attempts
    
    while guess.lower() != correct_answer.lower() and attempts < max_attempts:
        #loop continues until correct answer/3 attempts
        
        guess = input(question).strip() #asks question + removes spaces
        
        if guess.lower() == correct_answer.lower():
            print("That's right!")
            return guess
        #if statement is correct, return will exit the function
        
        else:
            print("Try again.")
            attempts += 1
            if attempts == 2:
                print(f"Hint: {hint}")
        #if wrong, attempts increase
        #hint is shown at 2 attempts

    # after the loop ends
    if guess.lower() != correct_answer.lower():
        print(f"Out of tries! The correct answer was {correct_answer}.")
    return guess
    #print the correct answer if user never gets it right
    #returns last guess even if wrong to allow consistency in program

#MAIN PROGRAM
# see how guess_the_best is defined by the 4 parameters mentioned in subprogram
# ordered in question, correct_answer, hint

animal = guess_the_best("What's the best animal?", "Lion", "L___")
film = guess_the_best("What's the best film?", "Lion King", "Starts with Lion, ends with King")
food = guess_the_best("What's the best food?", "Chicken", "C______")

# END POINT
# will check if answers are correct to grant a special message
# otherwise, will recieve another message 
if animal.lower() == "lion" and film.lower() == "lion king" and food.lower() == "chicken":
    print("Good choices!")
else:
    print("Not so good choices, ey?")

    
