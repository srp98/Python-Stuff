zip_code = ['25115', '14515', '1231x']


# Function to check if US zip code is correct, which is 5 digits
def is_valid_zip(z):
    for i in range(len(z)):
        print(z[i], end=' ')
        print('Correct' if len(z[i]) == 5 and z[i].isdigit() else 'Wrong')


print(is_valid_zip(zip_code))


# Word Search in articles
def word_search(document, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword.
    Returns list of the index values into the original list for all documents
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(document, 'casino')
    >>> [0]
    """
    indices = []
    for i, doc in enumerate(document):
        tokens = doc.split()
        print('Tokens: ', tokens)
        normalized = [token.rstrip('.,').lower() for token in tokens]
        print('Normalized Words: ', normalized)
        if keyword.lower() in normalized:
            indices.append(i)
    return indices


doc_list = ['The Learn Python Challenge is a Casino', 'They bought a car from a casino, and a horse', 'Casinoville?']
key = 'casino'
keys = ['casino', 'a']
print(word_search(doc_list, key))


def multi_word_search(document, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """
    return {k: word_search(document, k) for k in keywords}


print(multi_word_search(doc_list, keys))


# Printing a diamond of given length Function
def diamond(height):
    s = ''
    # The characters currently being used to build the left and right half of
    # the diamond, respectively. (We need to escape the backslash with another
    # backslash so Python knows we mean a literal "\" character.)
    l, r = '/', '\\'
    # The "radius" of the diamond (used in lots of calculations)
    rad = height // 2
    for row in range(height):
        # The first time we pass the halfway mark, swap the left and right characters
        if row == rad:
            l, r = r, l
        if row < rad:
            # For the first row, use one left character and one right. For
            # the second row, use two of each, and so on...
            nchars = row + 1
        else:
            # Until we go past the midpoint. Then we start counting back down to 1.
            nchars = height - row
        left = (l * nchars).rjust(rad)
        right = (r * nchars).ljust(rad)
        s += left + right + '\n'
    # Trim the last newline - we want every line to end with a newline character
    # *except* the last
    return s[:-1]


print(diamond(8))

# Conditional Roulette
"""
Analyze a list containing a history of roulette spins. 

Return a dictionary where the keys are numbers on the roulette wheel, and the values are dictionaries mapping numbers 
on the wheel to probabilities, such that `d[n1][n2]` is an estimate of the probability that the next spin will land on 
n2, given that the previous spin landed on n1."""


def conditional_roulette(hist):
    def f(x):
        X = [hist[n + 1] for n, k in enumerate(hist) if k == x and n + 1 != len(hist)]
        return {n: X.count(n)/len(X) for n in X}
    return {x: f(x) for x in [set(hist)]}


history = [1, 3, 1, 5, 1]
print(conditional_roulette(history))
