import random
import ngrams
import data

# *Create a function that handles generated text assembly so that everything is an actual sentence!

""" Generate text according to the dictionaries created by the last module. """

def generate_text(word_bank, max_words):
    start_word = pick_random_word(word_bank)
    generated_text = [start_word]

    # Start a loop that runs up to the set maximum
    while len(generated_text) <= max_words:
       if start_word not in word_bank:
            break
       
        # Clean the word to append to smooth it out
       word_to_append = random.choice(word_bank[start_word])
       word_to_append = word_to_append.strip(",").lower()

       generated_text.append(word_to_append)
       start_word = word_to_append

       generated_Sentence = assembly(generated_text)

    return generated_Sentence


""" Clean up lists before arranging them. """

# Sentence minimum. Working on it.. 

def assembly(generated_text):
    generated_sentence = " ".join(generated_text)
    generated_sentence = generated_sentence.capitalize()

    # For sentence punctuation. WIP

    return generated_sentence


""" Pick a random word from the bigram keys. """

def pick_random_word(bigrams):
    words_list = []

    # Iterate over the keys in the dictionary and move it into a list for easier randomization
    for word in bigrams.keys():
        words_list.append(word)

    random_word = random.choice(words_list)

    return random_word
