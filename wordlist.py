
""" This methods are used for manipu;ating and searching the string of words"""

def previous_word_index(words, pos):

    if pos == 0:
        return -1
    else:
        # This handles all cases above.
        return words.rfind("\n", 0, max(pos - 1, 0)) + 1

# Test cases.
TEST_WORDS = "one\ntwo\nthree\n"
assert previous_word_index(TEST_WORDS, 0) == -1
assert previous_word_index(TEST_WORDS, 2) == 0
assert previous_word_index(TEST_WORDS, 3) == 0
assert previous_word_index(TEST_WORDS, 4) == 0
assert previous_word_index(TEST_WORDS, 5) == 4
assert previous_word_index(TEST_WORDS, 6) == 4
assert previous_word_index(TEST_WORDS, 13) == 8
assert previous_word_index(TEST_WORDS, 14) == 8
del TEST_WORDS

def current_word_index(words, pos):
    return words.rfind("\n", 0, pos) + 1

# Test cases.
TEST_WORDS = "one\ntwo\nthree\n"
assert current_word_index(TEST_WORDS, 0) == 0
assert current_word_index(TEST_WORDS, 2) == 0
assert current_word_index(TEST_WORDS, 3) == 0
assert current_word_index(TEST_WORDS, 4) == 4
assert current_word_index(TEST_WORDS, 5) == 4
assert current_word_index(TEST_WORDS, 6) == 4
assert current_word_index(TEST_WORDS, 13) == 8
del TEST_WORDS

def next_word_index(words, pos):

    return words.find("\n", pos) + 1

# Test cases.
TEST_WORDS = "one\ntwo\nthree\n"
assert next_word_index(TEST_WORDS, 0) == 4
assert next_word_index(TEST_WORDS, 2) == 4
assert next_word_index(TEST_WORDS, 3) == 4
assert next_word_index(TEST_WORDS, 4) == 8
assert next_word_index(TEST_WORDS, 5) == 8
assert next_word_index(TEST_WORDS, 6) == 8
assert next_word_index(TEST_WORDS, 13) == len(TEST_WORDS)
assert next_word_index(TEST_WORDS, len(TEST_WORDS) - 1) == len(TEST_WORDS)
del TEST_WORDS

def word_at_index(words, pos):

    return words[pos:words.find("\n", pos)]

# Test cases.
TEST_WORDS = "one\ntwo\nthree\n"
assert word_at_index(TEST_WORDS, 0) == "one"
assert word_at_index(TEST_WORDS, 4) == "two"
assert word_at_index(TEST_WORDS, 8) == "three"
del TEST_WORDS

def binary_text_search(words, word, low, high):

    while low <= high:
        mid = low + (high - low)/2
        mid = current_word_index(words, mid)
        mid_word = word_at_index(words, mid)

        if word < mid_word:
            high = previous_word_index(words, mid)
        elif word > mid_word:
            low = next_word_index(words, mid)
        else:
            return (mid, True)

    return (low, False)
