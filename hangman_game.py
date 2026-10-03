import random


word_list = ["honorificabilitudinitatibus", "coding", "wealth", "pnuemonia", "javascript", "Chatbot", "pnuemonoultramicroscopicsilicovolcanoconiosis"]


secret_word = random.choice(word_list)


guessed_letters = []


incorrect_guesses = 0
max_incorrect = 6

print("Welcome to Hangman!")


while incorrect_guesses < max_incorrect:
    
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord: " + display_word.strip())
    print(f"Incorrect guesses remaining: {max_incorrect - incorrect_guesses}")
    print(f"Guessed letters: {', '.join(guessed_letters)}")

    
    if "_" not in display_word:
        print("\nCongratulations! You guessed the word correctly!")
        break

    
    guess = input("Guess a letter: ").lower()

    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
    elif guess in guessed_letters:
        print("You already guessed that letter!")
    else:
        
        guessed_letters.append(guess)

        
        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")


if incorrect_guesses == max_incorrect:
    print(f"\nGame Over! The word was '{secret_word}'.")