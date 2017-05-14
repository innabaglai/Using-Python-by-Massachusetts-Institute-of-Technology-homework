def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE... 
    guessesLeft = 8
    lettersGuessed =[]

    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.' )
    print('-----------')

    while guessesLeft > 0:
        if isWordGuessed(secretWord, lettersGuessed):
            return print('Congratulations, you won!')
        print('You have ' + str(guessesLeft) + ' guesses left.')
        print('Available Letters: ' + getAvailableLetters(lettersGuessed))
        user_input = input('Please guess a letter: ')
        user_input = str(user_input)
        user_input = user_input.lower()

        if user_input not in lettersGuessed:
            lettersGuessed.append(user_input)

            if user_input in secretWord:
                print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
                print('-----------')
            else:
                print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
                print('-----------')
                guessesLeft -= 1
        else:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
            print('-----------')

    return print("Sorry, you ran out of guesses. The word was " + str(secretWord))