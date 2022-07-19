import random
import hangman_words
import hangman_art
#NOTE: - wordlist is from hangman_words.py and ascii arts is from hangman_art.py

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

print(hangman_art.logo)

#NOTE:Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #NOTE: If user repeated the letter
    if guess in display:
        print(f"You have already guessed: {guess}, guess another letter.")

    #NOTE:Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #NOTE:Check if user is wrong.
    if guess not in chosen_word:
        print(f"You have guessed: {guess}, it is wrong. You lose a life!")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String. (?????????????)
    print(f"{' '.join(display)}")

    #NOTE:Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])