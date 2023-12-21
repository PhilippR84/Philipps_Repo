"""

chatgpt: 

import random

def choose_word():
    words = ["python", "java", "ruby", "javascript", "html", "css", "php"]
    return random.choice(words)

def hangman():
    word_to_guess = choose_word()
    guessed_letters = set()
    attempts = 6

    while attempts > 0:
        display_word = ""
        for letter in word_to_guess:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"

        print(display_word)

        if display_word == word_to_guess:
            print("Congratulations! You guessed the word.")
            break

        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess not in word_to_guess:
            attempts -= 1
            print(f"Incorrect! You have {attempts} attempts left.")

        if attempts == 0:
            print(f"Sorry, you ran out of attempts. The word was {word_to_guess}.")

# Uncomment the line below to play the game
# hangman()
"""

# Zufälliges Wort auswählen
# Ausgabe mit "_" wie viele Zeichen das Wort hat
# Eingabe welchen Buchstabe man wählt
# Ausgabe ob der Buchstabe im Wort vorhanden ist 
# Wenn Ja: Buchstabe angben
# Wenn nein: counter hochzählen

"""
with open('\notebooks\Python_lernen\Hangman_words.txt', 'r') as file:
    # Lies alle Zeilen und speichere sie in einer Liste
    list = file.readlines()
    print(list)
"""

datei = open('C:/Users/Phili/OneDrive/DHBW/VSCode/Philipps_Repo/notebooks/Python_lernen/Hangman_words.txt','r')
print(datei)


