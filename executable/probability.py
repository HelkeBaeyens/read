# Calculates the probability that a given word is deleted / substituted
import nltk
from collections import defaultdict

def probability_word_substitution (filename_raw,filename_adjusted):
	f = open(filename_raw, 'rt', encoding='utf-8')
	raw_text = f.read().lower()
	f.close()
	raw_words = nltk.tokenize.word_tokenize(raw_text)
	print (raw_words)

	f = open(filename_adjusted, 'rt', encoding='utf-8')
	adjusted_text = f.read().lower()
	f.close()
	adjusted_words = nltk.tokenize.word_tokenize(adjusted_text)
	print (adjusted_words)

	dict_raw_text = defaultdict(int)
	dict_adjusted_text = defaultdict(int)

	for word in raw_words:
		dict_raw_text[word] += 1
	for word in adjusted_words:		
		dict_adjusted_text[word] += 1
	dict_prob = {}
	print (dict_raw_text)
	print (dict_adjusted_text)

	for key in dict_raw_text.keys():
		dict_prob[key] = ((dict_raw_text[key]) - dict_adjusted_text[key]) / (dict_raw_text[key]) 
	return dict_prob
	print(dict_prob)

