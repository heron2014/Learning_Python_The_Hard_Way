def break_words(stuff):
    """ This function will break up the words for us
    create a function called break_words , we pass 1 argument, We want to return
    return list - array of words separated by space (check if that explanation is correct)
    remember its no longer a string - its and array so if you want to run len() method - u do it :
    len(words)"""
    words = stuff.split(' ')
    return words


def sort_words(words):
    """ Sorts the words """
    return sorted(words)


def print_first_word(words):
    """Prints the first word after popping it off"""
    word = words.pop(0)
    print word


def print_last_word(words):
    """Prints the last word after popping it off"""
    word = words.pop(-1)
    print word


def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words"""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """Prints the first and last words of the sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the fist and last one"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
