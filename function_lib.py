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
from word_level import *
def nr_words(words): # Calculates the numbers of words in a file
	return(len(words))

def av_length_words(words): #Calculates the average length of words in a file
	lengths = 0
	for word in words:
		lengths += len(word)
	return(str(lengths/(nr_words(words))))

def max_length_words(words): #Looks for the longest word in a file
	counter = 0
	for word in words:
		if word.replace('?' or '!' or ',', '.').endswith('.'):
			words.replace(word, word[-1])
	for word in words:
		if len(word) > counter:
			max_len = word
			counter = len(word)
		else: 
			None 
	return(str(max_len))

def len_longest_word(words): #Calculates the length of the longest word in a file
	return(str(len(max_length_words(words))))

def differentiation(words, filename): # Looks for differentiation in a text by dividing the length of the set of words over the length of the file
	return(str(len(set(words))/len(filename.split())))
	
def load_input2(filename): # second way to load the input in order to separate the sentences instead of words.
	return(filename.replace('?' or '!', '.').split('. '))

def sentence_count(sentences): #Calculated the number of sentences
	return(len(sentences))

def av_sentence_length(sentences): # Calculates the average length of the sentences
	sen_length = 0
	for sentence in sentences:
		sentence = sentence.split(' ')
		sen_length += (len(sentence))
	return(str(sen_length/sentence_count(sentences)))

def max_sentence(sentences): # Calculates the length of the longest sentence.
	counter = 0
	for sentence in sentences:
		sentence = sentence.split(' ')
		if len(sentence) > counter:
			counter = (len(sentence))
		else: 
			None 
	return(str(counter))

def min_sentence(sentences): # Calculates the length of the shortest sentence
	counter = 1000
	for sentence in sentences:
		sentence = sentence.split(' ')
		if len(sentence) < counter:
			counter = (len(sentence))
		else: None
	return(str(counter))

def sen_lev(sentences):
	av_sen = float(av_sentence_length(sentences))
	if av_sen > 40:
		return('C2')
	elif av_sen > 30:
		return('C1')
	elif av_sen > 25:
		return('B2')
	elif av_sen > 20:
		return('B1')
	elif av_sen > 15:
		return('A2')
	else: 
		return ('A1')

def text_level(level, sen_lev):
	"""Function to calculate the level of the text"""
	calcu = {'A1': 1, 'A2': 2, 'B1': 3, 'B2': 4, 'C1': 5, 'C2':6}
	W = int(calcu[level])*0.8 										#80% word level		
	S = int(calcu[sen_lev])*0.1 									#10% sentence level
	T = 1*0.1 														#10% temporal value the definition doesn't exist yet
	nr = (W + S + T)
	
	if nr > 5:
		return('C2')
	elif nr > 4:
		return('C1')
	elif nr > 3:
		return('B2')
	elif nr > 2:
		return('B1')
	elif nr > 1:
		return('A2')
	else: 
		return('A1')
