import data

""" Split up the data into usable dictionaries. """

raw_Data = data.data

""" Returns a bigram dictionary. """

def dictionary_assembly(raw_data):
    prepped_data = data_prep(raw_data)
    word_bank = {}

    for i in range(len(prepped_data)):
        word = prepped_data[i].lower().strip(",") # key
        next_word = get_next_word(prepped_data, i) # value

        # Bouncer condition
        if next_word is None:
            continue

        if if_proper_noun(next_word, i) is False:
            next_word = next_word.lower()

        if word not in word_bank:
            word_bank[word] = []

        word_bank[word].append(next_word)

    return word_bank

""" Get the next word. """

def get_next_word(words, index):
    if index + 1 >= len(words):
        return None

    return words [index + 1]

""" Checks if the word is a proper noun. """

def if_proper_noun(next_word, index):
    if next_word is None:
        return False

    # Check if the string index is even a letter. If not, check the next index.
    letter = next_word[0]
    if not letter.isalpha():
        letter = next_word[1]

    if index != 0 and letter.isupper():
        return True
    else:
        return False

""" Prep incoming data for the bigger function. """

def data_prep(raw_data):
    words_list = []

    for i in range(len(raw_data)):
        words = raw_data[i].split()

        for word in words:
            words_list.append(word)

    return words_list