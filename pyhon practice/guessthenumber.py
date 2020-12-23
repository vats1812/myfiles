print("Hey Welcome all")
print("So here is a guess the number game. \n ")
print("So I have choosed a number, now you have to guess whats my number")
print("Rules for the game are:-\n  1.Your number should be between 1 to 50.\n  2.You have 7 chances to guess.\n  3.I will give you hint by telling if my number is less than of greather than your guessed number\n")
n = 38
guesses = 1
while (guesses <= 7):
    number = (int(input("Guess your number:")))

    if number < n:
        print("Enter a greater number\n")
    elif number > n:
        print("Enter a smaller number\n")
    else :
        print("\nCongratulations!! You have guessed the right number\n")
        print("You took",guesses,"Guess to win.")
        break
    print(7-guesses,"Guesses left !!")
    guesses=guesses+1

    if guesses>7: 
        print("\nGame over !!!!!")

