class PrefixDictionary(object):

    """Creates and stores a map of words."""

    def __init__(self):
        self.words = {}

        self.is_terminal = False

    def get_child(self, ch, word):
        is_word = self.words.get(word, None)
        if is_word is None:
            return None

        child = PrefixDictionary()
        child.words = self.words
        child.is_terminal = is_word

        return child

    @classmethod
    def make_dictionary(cls, words):
        """ Creates dictionary with keys as prefix and value is boolean (false for prefix and true for word)"""

        dictionary = cls()

        # Read every word.
        for word in words:
            # Add all the prefixes.
            for i in range(len(word)):
                prefix = word[:i]
                if prefix not in dictionary.words:
                    dictionary.words[prefix] = False

            # Add the word.
            dictionary.words[word] = True

        return dictionary
