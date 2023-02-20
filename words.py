def print_upper_words(words, must_start_with = ['e']):
    """prints words that starts with the given parameter
    params:
        words: collection of string words
        must_start_with: collection of characters to check if words start with. ["e"] by default.
    """
    for word in words:
        if(word[0] in must_start_with):
            print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes","eee"])