def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result = ""
    for i in range(len(secretWord)):
      if secretWord[i] in lettersGuessed:
        result += secretWord[i]
      else:
        result += "_"
    return result
