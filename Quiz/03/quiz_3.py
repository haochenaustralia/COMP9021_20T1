# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION


from random import seed, randrange
from collections import Counter


def give_values_to_letters(for_seed):
    seed(for_seed)
    return [randrange(1, 10) for _ in range(26)]


def read_dictionary():
    with open('dictionary.txt') as read_file:
        # lines = read_file.readlines()
        # for index in range(len(lines)):
        # while
        return set([line.strip() for line in read_file if not line.isspace()])


# word and letters are both meant to be strings of nothing but
# uppercase letters, values, a list returned by
# give_values_to_letters(). Returns:
# - -1 if word is not in dictionary.txt
# - 0 if word is in dictionary.txt but cannot be built from letters
# - the value of word according to values otherwise.
def can_be_built_from_with_value(word, letters, values):
    dictionary_result = read_dictionary()
    result = -1
    if word in dictionary_result:
        result = 0
        for char in word:
            if letters.count(char) < word.count(char):
                return 0
            else:
                result = result + values[ord(char) - ord('A')]
    return result


# letters is meant to be a string of nothing but uppercase letters.
# Returns the list of words in dictionary.txt that can be built
# from letters and whose value according to values is maximal.
# Longer words come before shorter words.
# For a given length, words are lexicographically ordered.

def can_be_built_from_with_value_extend(dictionary_result, word, letters, values):
    result = -1
    if word in dictionary_result:
        result = 0
        for char in word:
            if letters.count(char) < word.count(char):
                return 0
            else:
                result = result + values[ord(char) - ord('A')]
    return result


def most_valuable_solutions(letters, values):
    solutions = {}
    words = read_dictionary()
    for word in words:
        value = can_be_built_from_with_value_extend(words, word, letters, values)
        if value > 0:
            solutions[word] = value

    result = []
    if solutions:
        max_value =  max(solutions.values())
        for word,value in solutions.items():
            if value == max_value:
                result.append(word)

        result.sort(key = len, reverse= True)

        result = list(sorted(result, key = len,reverse=True))

        result = list(reversed(sorted(result, key = len)))

        result = list(sorted(result, key = len))[::-1]

    return result

# POSSIBLY DEFINE OTHER FUNCTIONS
