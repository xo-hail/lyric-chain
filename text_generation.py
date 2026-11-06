import random

# *Create a function that handles generated text assembly so that everything is an actual sentence!

""" Generate text according to the dictionaries created by the last module. """

def generate_text(word_bank, max_words):
    start_word = pick_random_word(word_bank)
    generated_text = [start_word]
    set_aside_word = ""

    # Start a loop that runs up to the set maximum
    while len(generated_text) <= max_words:
       if start_word not in word_bank:
            break

       word_to_append = random.choice(word_bank[start_word])
       # Break the loop if the word to append (key) doesn't have a value
       if word_to_append is None:
           generated_text.append(start_word)
           break

       # If a word contains a punctuation mark, set it aside for the next loop.
       # If there is a next word, put it before the current word.
       word_to_append = word_to_append

       if not word_to_append.isalpha():
           (set_aside_word := set_aside(word_to_append))
           start_word = word_to_append
           continue
       
       set_check = if_set_aside(set_aside_word)
       if set_check:
           generated_text.append(set_aside_word)
           
       generated_text.append(word_to_append)
       start_word = word_to_append

    generated_Sentence = assembly(generated_text)

    return generated_Sentence


""" Clean up lists before arranging them. """

# Sentence minimum. Working on it.. 

def assembly(generated_text):
    generated_sentence = " ".join(generated_text)
    generated_sentence = generated_sentence.capitalize()

    # For sentence ending
    final_sentence = generated_sentence + "."

    return final_sentence


""" Pick a random word from the bigram keys. """

def pick_random_word(bigrams):
    words_list = []

    # Iterate over the keys in the dictionary and move it into a list for easier randomization
    for word in bigrams.keys():
        words_list.append(word)

    random_word = random.choice(words_list)

    return random_word

def set_aside(word_to_append):
    set_aside_word = word_to_append
    return set_aside_word

def if_set_aside(set_aside_word):
    if not set_aside_word:
        return False
    return True
