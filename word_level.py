#word_level
import codecs
import re

def load_dictionary(filename, sep=';'):
	"""
	:parameter filename: A file that connects words to their respective level.
	:parameter sep: mark used to seperate the elements in a line. 
	:return: a dictionary that connects the words to a certain level.
	"""
	dictionary = [ ]
	for line in codecs.open(filename, 'r', 'utf8'):
		line = line.strip()
		components = line.split(sep)
		dictionary.append(components)
	dictionary = dict(dictionary)
	return (dictionary)

def load_input(filename):
	"""
	:parameter filename: A string representing a text.
	:return: A set of words representing the text.
	"""
	#text = open(filename, 'r','utf8')				#Voorlopige aanpassing aangezien de text getest wordt in py ipv file
	text = filename
	text = text.lower()
	word = [ ]
	words = set(text.split( ))
	return (words)

def lematization(words):
	lemmas = [ ]
	words = list(words)
	def plur (words):
		regex_es = r'(ses|zes|xes|oes|shes|ches)$'
		singulars = ['tooth', 'goose', 'man', 'foot', 'child', 'ox', 'mouse', 'man', 'woman', 'sheep', 'people']
		plurals = ['teeth', 'geese', 'men', 'feet', 'children', 'oxen', 'mice', 'men', 'women', 'sheep', 'people']
		zippy = dict(zip(plurals, singulars))
		for word in words:
			if word in plurals:
				lemmas.append(zippy[word])
			elif re.search(regex_es, word[-4:]):
				lemmas.append(word[:-2])
			elif re.search('ies$',word):
				lemmas.append(word[-3:]+'y')
			elif re.search('ves$',word[-3:]):
				lemmas.append(word[:-3] + 'f')
			elif re.search('s$',word[-1:]):		
				lemmas.append(word[:-1])
			else:
				None 
		return(lemmas)                   

	plur(words)
	return(lemmas)	

def lexicon(dictonary, words, lemmas):
	"""  
	:param dictionary: A dictionary of words connected to their respective levels.
    :param words: A set of words representing the text.
    :return: A lexicon of words in the text that can be found in the dictionary.
	"""
	lexicon = [ ]
	for word in words:
		if word in dictionary:			# 'go' doesn't appear
			lexicon.append(word)
	for lemma in lemmas:
		if lemma in dictionary:
			lexicon.append(lemma)
	return(lexicon)


""".................................................................................."""
dictionary = load_dictionary("data\\dictionaryABC2.csv", ';')
words = load_input("holidays")
lemmas = lematization(words)
lexicon = lexicon(dictionary,words, lemmas)
print(words)
print(len(words))
print(lemmas)
print(lexicon)
print(len(lexicon))


   