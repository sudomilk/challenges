from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open('dictionary.txt', 'r') as f:
        return [i.rstrip('\n') for i in f.readlines()]

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    #words with hypens do not count in Scrabble
    if '-' in word: return 0
    return sum(LETTER_SCORES[l.upper()] for l in word)

def max_word_value(words=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    return max(words, key=calc_word_value)

if __name__ == "__main__":
    pass # run unittests to validate
