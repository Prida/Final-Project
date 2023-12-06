def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display.strip()

def hangman(word):
    strikes = 0
    guessed_letters = []

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while '_' in display_word(word, guessed_letters):
        guess = input("Guess a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You've already guessed that letter. Try again.")
            elif guess in word:
                print("Good guess!")
                guessed_letters.append(guess)
            else:
                print("Incorrect guess!")
                strikes += 1
                print(f"Strikes: {strikes}")
                guessed_letters.append(guess)
        else:
            print("Invalid input. Please enter a single letter.")

        print(display_word(word, guessed_letters))

        if strikes == 6:
            print("Sorry, you're out of strikes. The word was:", word)
            break

    if '_' not in display_word(word, guessed_letters):
        print("Congratulations! You've guessed the word:", word)

word = "hangman"
hangman(word)
