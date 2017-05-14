def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    inList = False
    
    if word in wordList:
        inList = True
        
    for i in word:
        if not (i in hand and word.count(i) <= hand[i]):
            return False
        
    return inList
