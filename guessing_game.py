

secret_word = "giraffe"
guess = ""
guess_count = 1
out_of_guesses = False
limit = 3

while guess != secret_word and not out_of_guesses:
    guess = input("Enter guess: ")

    if guess_count == limit:
        out_of_guesses = True
    else:
        guess_count += 1

if out_of_guesses:
    print("You are out of guesses, You lost!!!!")
else:
    print("Hey you win, your guess was: " + guess)

