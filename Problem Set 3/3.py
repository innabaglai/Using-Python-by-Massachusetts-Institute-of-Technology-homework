def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    result = ""
    for e in string.ascii_lowercase:
        if e not in lettersGuessed:
            result += e
    return result