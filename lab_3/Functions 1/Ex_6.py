def reversed_word_order(some_string : str):
    return ' '.join([(x) for x in some_string.split()][::-1])