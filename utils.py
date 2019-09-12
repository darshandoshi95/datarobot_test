def binary_search(words, word, low=0, high=None):
    """This method checks if index is where is word is found or it should be and then returns a typle(index, found)"""

    if high is None:
        high = len(words) - 1

    while low <= high:
        mid = low + (high - low)/2

        print(mid)
        mid_word = words[round(mid)]

        if word < mid_word:
            high = mid - 1
        elif word > mid_word:
            low = mid + 1
        else:
            return (round(mid), True)

    return (round(low), False)

def make_next_word(word):

    if not word:
        return "{"

    prefix = word[:-1]
    last_ch = word[-1]
    if last_ch == "z":
        return make_next_word(prefix)
    else:
        return prefix + chr(ord(last_ch) + 1)

# Quick tests.
assert make_next_word("a") == "b"
assert make_next_word("hello") == "hellp"
assert make_next_word("pooz") == "pop"
assert make_next_word("z") == "{"
assert make_next_word("zzz") == "{"
