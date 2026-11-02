import data

""" Split up the data into usable dictionaries. """

raw_Data = data.data

""" Returns a bigram dictionary. """

def dictionary_assembly(raw_data):
    prepped_data = data_prep(raw_data)
    word_bank = {}

    for i in range(len(prepped_data)):
        word = prepped_data[i].lower().strip(",")

        if word not in word_bank:
                word_bank[word] = []

    # Preserve capitalization per word for the values.
        word_bank[word].append(get_next_word(prepped_data, i))

    return word_bank

""" In progress. Have yet to understand this block of code. """

def get_next_word(words, index):
    if index + 1 >= len(words):
         return ""

    return words [index + 1]


""" Prep incoming data for the bigger function. """

def data_prep(raw_data):
    words_list = []

    for i in range(len(raw_data)):
        words = raw_data[i].split()

        for word in words:
            words_list.append(word)

    return words_list

