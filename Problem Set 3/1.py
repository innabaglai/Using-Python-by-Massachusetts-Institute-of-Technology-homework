def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    result = False
    for i in range(len(secretWord)):
      if secretWord[i] in lettersGuessed:
        result = True
      else:
        result = False
        break
    return result
    
    
