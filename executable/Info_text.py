"""
This file prints several bits of information about the text string.
"""
from  word_level import * 			#star imports all the functions in the library
from function_lib import *

filename = "The second reason for his delay was a personal one. He had dawdled over his cigar because he was at heart a dilettante, and thinking over a pleasure to come often gave him a subtler satisfaction than its realization. This was especially the case when the  pleasure was a delicate one, as his pleasures mostly were; and on this occasion the moment he looked forward to was so rare and exquisite in quality that - well, if he had timed his arrival in accord with the prima donna's stage manager he could not have entered the Academy at a more significant moment than just as she was singing and sprinkling the falling daisy petals with notes as clear as dew." # temporary
words = list(load_input(filename))
dictionary= load_dictionary("dictionaryABC.csv", ';')
lemmas = lematization(words)
lexicon = lexicon(dictionary,words,lemmas)
level = str(level(lexicon,dictionary))
sentences= load_input2(filename)

print("The level of the text: " + level)
print("The number of words: "+ str(nr_words(words)))
print(r' ')
print('The average length of the words: ' + (av_length_words(words)))
print('The longest word: ' + str(max_length_words(words)))
print('The length of the longest word: ' + len_longest_word(words))
print('The differentation of words within the text is: ' + differentiation(words, filename))
print("The number of sentences: "+ str(sentence_count(sentences)))
print("The average length of the sentences: " + av_sentence_length(sentences))
print("The longest sentence: " + max_sentence(sentences))
print("The shortest sentence: " + min_sentence(sentences))