filename = "I am going crazy. Because I just keep programming." # temporary
from  word_level import * 			#star imports all the functions in the library
from function_lib import *
words = list(load_input(filename))
dictionary= load_dictionary("data\\dictionaryABC.csv", ';')
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