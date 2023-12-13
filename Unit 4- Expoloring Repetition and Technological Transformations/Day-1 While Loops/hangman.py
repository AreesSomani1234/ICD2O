import random

def choose_words():
    word = ['hello', 'goodbye', 'Jaytee', 'sun', 'joshua', 'watch',]
    return random.choice(word)

def buildString(goodLetters, hiddenWord):
    # iterate through hiddenWord check if a letter is in goodLetters if itis then shoe the letter otherwise show the underscore
    print()

def hangman():
    hidden_word = choose_words()
    guesses_left = 6
    gameover = False

    goodLetters = ''
    badLetters = ''

    while guesses_left > 0 and not gameover:
        print(f"Number of Attempts: {guesses_left}")

        buildString(goodLetters, hidden_word)
        letter = input("Enter a letter: ").lower()

        if letter in hidden_word and letter not in goodLetters:
            goodLetters += letter
            print("Good")
        elif letter not in hidden_word and letter not in goodLetters:
            badLetters += letter
            guesses_left-=1
            print("nope")
        else:
            print("Already used that letter.")


        
       

    
hangman()


