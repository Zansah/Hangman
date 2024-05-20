from random_word import RandomWords

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def hangman():
    r = RandomWords()
    random_word = r.get_random_word().lower()  
    guessed_letters = []  
    max_guesses = 6
    guesses = 0

    print("Welcome to Hangman please try to guess the word")
   

    while guesses < max_guesses:
        print(f"\n {display_word(random_word, guessed_letters)}")
        guess = input("Enter a letter: ").lower() 
        if len(guess) != 1:
            print("Please enter only one letter.")
            continue
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        guessed_letters.append(guess)
        if guess not in random_word:
            guesses += 1
            print(f"Incorrect guess! {max_guesses - guesses} guesses remaining.")
        if random_word == guessed_letters:
            print(f"\nCongratulations you guessed the word: {random_word}")
            return
    print(f"\nYou ran out of guesses. The word was: {random_word}")


hangman()
