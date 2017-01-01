import math
def nr_words(words):
	nr = (len(words))
	return (nr)

def av_length_words(words):
	lengths = 0
	for word in words:
		lengths +=len(word)
	length = (lengths / (nr_words(words)))
	return(str(length))

def max_length_words(words):
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

def len_longest_word(words):
	return (str(len(max_length_words(words))))

def differentiation(words, filename):
	text = filename.split()
	diff = len(set(words))/len(text)
	return (str(diff))
	
def load_input2 (filename):
	sentences = [ ]
	text = filename
	sentences = text.split('. ')
	return (sentences)

def sentence_count(sentences):
	return(len(sentences))

def av_sentence_length(sentences):
	sen_length = 0
	for sentence in sentences:
		sentence = sentence.split(' ')
		sen_length += (len(sentence))
	av_length = (sen_length/sentence_count(sentences))
	return(str(av_length))

def max_sentence(sentences):
	counter = 0
	for sentence in sentences:
		sentence = sentence.split(' ')
		if len(sentence) > counter:
			counter = (len(sentence))
		else: 
			None 
	return (str(counter))

def min_sentence(sentences):
	counter = 1000
	for sentence in sentences:
		sentence = sentence.split(' ')
		if len(sentence) < counter:
			counter = (len(sentence))
		else: None
	return (str(counter))