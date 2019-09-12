
import random
import create_dictionary
import time
import sys


def read_all_words():

    """This methos is used to return words list needed to process further."""

    words = []
    text = open("//Users/darshandoshi/Desktop/boggle-master/words.txt").read()
    lines = text.split("\n")
    for word in lines:
        word = word.strip()
        if word and word[0].islower():
            word = word.upper()
            if len(word) >= 3:
                words.append(word)

    return words


def generate_board(size):
    """This method generates bard with random letters."""
    board = []

    alphabet = range(ord("A"), ord("Z") + 1)

    for i in range(size * size):
        board.append(chr(random.choice(alphabet)))

    return board

def search(board, size, row, column, node, used, word, solutions):
    """THis method is used to search the board for the end word and starting with prefix "word" """

    # Off the end of the board.
    if row < 0 or row >= size or column < 0 or column >= size:
        return

    # Already visited in this word.
    index = row*size + column
    if used[index]:
        return

    # Extend the word.
    ch = board[index]
    word += ch

    # See if the new word is in the dictionary.
    child = node.get_child(ch, word)
    if child is not None:
        if child.is_terminal:
            solutions.add(word)

        used[index] = True
        for r in range(-1, 2):
            for c in range(-1, 2):
                if r != 0 or c != 0:
                    search(board, size, row + r, column + c, child, used, word, solutions)
        used[index] = False

def solve_board(board, size, dictionary):
    """This method solves the board and returns set of words found in dictionary created."""


    used = [False]*(size*size)

    solutions = set()


    for row in range(size):
        for column in range(size):
            search(board, size, row, column, dictionary, used, "", solutions)

    return solutions

def main(board_size):
    size = board_size
    start = time.time()
    words = read_all_words()
    end=time.time()
    print("Reading words-%.2f"%(end - start))

    # Create each of the dictionaries.
    dictionaries = []
    start = time.time()
    dictionaries.append(create_dictionary.PrefixDictionary.make_dictionary(words))
    end = time.time()
    print("Dictionary created-%.2f" %(end-start))

    # Generate a random board.
    board = generate_board(size)
    print(dictionaries)
    # Board is solved multiple times.
    solutions = []
    dictionary= dictionaries[0]
    start = time.time()
    for i in range(5):
        solution = solve_board(board, size, dictionary)
    end = time.time()
    print("Solved-%.2f"%(end - start))
    solutions.append(solution)

    print ("All words: " + ", ".join(sorted(solutions[0])))

if __name__ == "__main__":
    """Enter board size."""
    size = sys.argv
    main(int(size[1]))
