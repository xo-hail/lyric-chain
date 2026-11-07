import data
import ngrams
import text_generation
import random

raw_data = data.data[7]
bigrams = ngrams.dictionary_assembly(raw_data)
print(bigrams)
print(text_generation.generate_text(bigrams, 30))

# random.randint(1, 6)