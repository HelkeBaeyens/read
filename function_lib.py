"""
This file is a library of all the short functions necessary for the interface.
in__file__ = 	nr_words(words)
				av_length_words(words)
				max_length_words(words)
				len_longest_word(words)
				differentiation(words, filename)
				sentence_count(sentences)
				av_sentence_length(sentences)
				max_sentence(sentences)
				min_sentence(sentences)
"""
import math
def nr_words(words): # Calculates the numbers of words in a file
	nr = (len(words))
	return (nr)

def av_length_words(words): #Calculates the average length of words in a file
	lengths = 0
	for word in words:
		lengths +=len(word)
	length = (lengths / (nr_words(words)))
	return(str(length))

def max_length_words(words): #Looks for the longest word in a file
	counter = 0
	lemmas = []
	for word in words:
		if word.endswith('.'):
			lemmas.append(word[:-1])
	for lemma in lemmas:
		if len(lemma) > counter:
			max_len = lemma
			counter = len(lemma)
		else: 
			None 
	return (str(max_len))

def len_longest_word(words): #Calculates the length of the longest word in a file
	return (str(len(max_length_words(words))))

def differentiation(words, filename): # Looks for differentiation in a text by dividing the length of the set of words over the length of the file
	text = filename.split()
	diff = len(set(words))/len(text)
	return (str(diff))
	
def load_input2 (filename): # second way to load the input in order to separate the sentences instead of words.
	sentences = [ ]
	text = filename
	sentences = text.split('. ')
	return (sentences)

def sentence_count(sentences): #Calculated the number of sentences
	return(len(sentences))

def av_sentence_length(sentences): # Calculates the average length of the sentences
	sen_length = 0
	for sentence in sentences:
		sentence = sentence.split(' ')
		sen_length += (len(sentence))
	av_length = (sen_length/sentence_count(sentences))
	return(str(av_length))

def max_sentence(sentences): # Calculates the length of the longest sentence.
	counter = 0
	for sentence in sentences:
		sentence = sentence.split(' ')
		if len(sentence) > counter:
			counter = (len(sentence))
		else: 
			None 
	return (str(counter))

def min_sentence(sentences): # Calculates the length of the shortest sentence
	counter = 1000
	for sentence in sentences:
		sentence = sentence.split(' ')
		if len(sentence) < counter:
			counter = (len(sentence))
		else: None
	return (str(counter))