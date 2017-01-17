"""
This file looks up the level of words in a file and decides on the level of the text according to this level.
"""
import codecs
import re

def load_dictionary(filename, sep=';'):
	"""
	:param filename: A file that connects words to their respective level.
	:param sep: mark used to seperate the elements in a line. 
	:return: a dictionary that connects the words to a certain level.
	"""
	dictionary = [ ]
	for line in codecs.open(filename,'r','utf8'):
		line = line.strip()
		components = line.split(sep)
		dictionary.append(components)
	dictionary = dict(dictionary)
	return(dictionary)

def load_input(filename):
	"""
	:param filename: A string representing a text.
	:return: A set of words representing the text.
	"""
	text = filename.lower()
	words = set(text.split( ))
	return(words)

def lematization(words):
	"""
	:param words: A set of words representing the text.
	:return: a list of lemmas by reducing the words to stem-forms (the overgeneration resulting in non-exising words are automatically filtered out in the next step)
	"""
	words = list(words)
	lemmas = [ ]
	puncty = [ ]

	def punctuation(words): #split punctuations from words.
		regex = r':|,|\'|\.|\?|\!'
		for word in words:
			if re.search(regex,word[-1]):
				puncty.append(word[:-1])
				lemmas.append(word[:-1])
			else: None
		return(puncty,lemmas)

	def pronoun(words): #reverts pronouns back to their base form
		for word in words:
			if re.search(r'^(my|me|mine)$',word):
				lemmas.append('I')
			elif re.search(r'^(her|hers)$',word):
				lemmas.append('she')
			elif re.search(r'^(his|him)$',word):
				lemmas.append('he')
			elif re.search(r'^(our|ours)$',word):
				lemmas.append('we')
			elif re.search(r'^(your|yours)$',word):
				lemmas.append('you')
			elif re.search(r'^(their|theirs|them)$',word):
				lemmas.append('they')
		return(lemmas)

	def plur(words): #reverts words from their plural form to their singular form
		regex_es = r'(ses|zes|xes|oes|shes|ches)$'
		singulars = ['tooth','goose','man','foot','child','ox','mouse','man','woman','sheep','people']
		plurals = ['teeth','geese','men','feet','children','oxen','mice','men','women','sheep','people']
		zippy = dict(zip(plurals,singulars)) # a zipfile connecting each plural to its singular
		for word in words:
			if word in plurals:
				lemmas.append(zippy[word])
			elif re.search(regex_es,word[-4:]):
				lemmas.append(word[:-2])
			elif re.search('ies$',word):
				lemmas.append(word[-3:]+'y')
			elif re.search('ves$',word[-3:]):
				lemmas.append(word[:-3]+'f')
			elif re.search('s$',word[-1:]):		
				lemmas.append(word[:-1])
			else:
				None 
		return(lemmas)                   
	
	def verbs(words): # reverts verbs to their stem
		modals = ['can','may','will','shall'] 
		past_modals = ['could','might','would','should']
		irr_stems = ['rise','wake','bear','beat','become','begin','bend','bind','bid','bind','bet','bite','bleed','blow','break','breed','bring','build','burn','buy','cast','catch','choose','cling','clothe','come','cost','creep','cut','deal','dig','prove','dive','draw','dream','drink','drive','dwell','eat','fall','feed','feel','fight','find','fit','flee','fling','fly','forbid','forget','forgive','forsake','freeze','get','give','go','grind','grow','hang','have','hear','hew','hide','hit','hold','hurt','input','keep','kneel','knit','know', 'lay','lead','lean','leap','learn','leave','lend','let','lie','lie','light','lose','make','mean','meet','mistake','misunderstand','mow','pay','plead','prepay','proofread','put','quit','read','relay','rid','ride','ring','rise','run','saw','say','see','seek','sell','send','set','sew','shake','shave','shear','shed','shine','shit','shoot','show','shrink','shut','sing','sink','sit','slay','sleep','slide','sling','slink','slit','smell','sneak','sow','speak','speed','spell','spend','spill','spin','spit','split','spoil','spread','spring','stand','steal','stick','sting','stink','strew','stride','strike','string','strive','swear','sweat','sweep','swell','swim','swing','take','teach','tear','tell','think','throw','thrust','tread', 'wake','wear','weave','wed','weep','wet','whet','win','wind','withdraw','withhold','withstand','wring','write']
		irr_SPs = ['rose','woke','bore','beat','became','began','bent','bound','bid','bound','bet','bit','bled','blew','broke','bred','brought','built','burned','bought','cast','caught','chose','clung','clothed','came','cost','crept','cut','dealt','dug','proved','dove','drew','dreamt','drank','drove','dwelt','ate','fell','fed','felt','fought','found','fitted','fled','flung','flew','forbade','forgot','forgave','forsook','froze','got','gave','went','ground','grew','hung','had','heard','hewed','hid','hit','held','hurt','inputted','kept','knelt','knit','knew','laid','led','leant','leapt','learnt','left','lent','let','lay','lied','lit','lost','made','meant','met','mistook','misunderstood','mowed','paid','pled','prepaid','proofread','put','quitted','read','relayed','rid','rode','rang','rose','ran','sawed','said','saw','sought','sold','send','set','sewed','shook','shaved','sheared','shed','shone','shat','shot','showed','shrank','shut','sang','sank','sat','slew','slept','slid','slung','slunk','slit','smelt','snuck','sowed','spoke','sped','spelt','spent','spilt','spun','spit','spilt','spoilt','spread','sprang','stood','stole','stuck','stung','stank','strewed','strode','struck','strung','strove','swore','sweat','swept','swelled','swam','swung','took','taught','tore','told','thought','threw','thrust','trod','woke','wore','wove','wed','wept','wet','whetted','won','wound','withdrew','withheld','withstood','wrung','wrote']
		irr_PPs = ['risen','woken','born','beaten','become','begun','bent','bound','bitten','bound','bet','bitten','bled','blown','broken','bred','brought','built','burnt','bought','cast','caught','chosen','clung','clad','come','cost','crept','cut','dealt','dug','proven','dived','drawn','dreamed','drunk','driven','dwelled','eaten','fallen','fed','felt','fought','found','fit','fled','flung','flown','forbidden','forgotten','forgiven','forsaken','frozen','gotten','given','gone','ground','grown','hung','had','heard','hewn','hidden','hit','held','hurt','inputted','kept','kneeled','knitted','known','laid','led', 'leaned','leaped','learned','left','lent','let','lain','lied','lighted','lost','made','meant','met','mistaken','misunderstood','mown','paid','pleaded','prepaid','proofread','put','quitted','read','relayed','rid','ridden','rung','risen','run','sawn','said','seen','sought','sold','sent','set','sewn','shaken','shaven','shorn','shed','shined','shitted','shot','shown','shrunk','shut','sung','sunk','sat','slayed','slept','slid','slung','slinked','slit','smelled','sneaked','sowed', 'spoken','speeded','spelled','spent','spilled','spun','spat','split','spoiled','spread','sprung','stood','stolen','stuck','stung','stunk','strewed','stridden','stricken','strung','strived','sworn','sweated','swept','swollen','swum','swung','taken','taught','torn','told','thought','thrown','thrust','trodden','woken','worn','weaved','wedded','wept','wetted','whetted','won','wound','withdrawn','withheld','withstood','wrung','written']
		zippy_SPs = dict(zip(irr_SPs,irr_stems))
		zippy_PPs = dict(zip(irr_PPs,irr_stems))
		zippy_modals = dict(zip(past_modals,modals))
		for word in words:
			if word in irr_SPs:
				lemmas.append(zippy_SPs[word])
			if word in irr_PPs:
				lemmas.append(zippy_PPs[word])
			elif re.search('tting',word[-5:]): #doubling with gerunds
				lemmas.append(word[:-4])
			elif re.search('ing$',word[-3:]):	#gerund
				lemmas.append(word[:-3])
				lemmas.append(word[:-3]+'e')
			elif re.search('ed$',word[-2:]):	#perfect
				lemmas.append(word[:-2])
				lemmas.append(word[:-1])
			elif word in past_modals:
				lemmas.append(zippy_modals[word])
			elif re.search(r'^(am|is|are|was|were|been|being)$',word):
				lemmas.append('be')
			elif re.search(r'^(has|had)$',word):
				lemmas.append('have')
			else: None
		return(lemmas) 

	def prefix(words): # splits prefixes from the words
		regex_pre1 = r'^(a|e)'
		regex_pre2 = r'^(un|in|im|re|an|af|al|be|co|ex|en|up)'
		regex_pre3 = r'^(dis|non|pre|pro|sub|sup|mis)'
		regex_pre4 = r'^(ante|anti|hemi|hypo|peri|semi|over|post|auto|mega)'
		regex_pre5 = r'^(extra|hyper|infra|trans|ultra|under|super)'
		regex_pre6 = r'^(contra)'
		regex_pre7 = r'^(counter)'
		for word in words:
			if re.search(regex_pre7,word):
				lemmas.append(word[7:])
			elif re.search(regex_pre6,word):
				lemmas.append(word[6:])
			elif re.search(regex_pre5,word):
				lemmas.append(word[5:])
			elif re.search(regex_pre4,word):
				lemmas.append(word[4:])
			elif re.search(regex_pre3,word):
				lemmas.append(word[3:])
			elif re.search(regex_pre2,word):
				lemmas.append(word[2:])
			elif re.search(regex_pre1,word):
				lemmas.append(word[1:])
			else:
				None 
		return(lemmas)
	
	def suffix(words):	#splits suffixes from the words
		regex_suff1 = r'(y|ly)$'
		regex_suff2 = r'(ly|er|or|en|al)$'			
		regex_suff2b = r'(al)$'						
		regex_suff3 = r'(dom|ism|ize|ise|ful|ish|ary|ate|ade)$'
		regex_suff3b = r'(ity|ive|ary)$'
		regex_suff4 = r'(ment|ness|ship|less|able|ance)$'
		regex_suff4b = r'(able)$'
		regex_suff4c = r'(sion)$'
		regex_suff5 = r'(ation)$'	
		for word in words:
			if re.search(regex_suff5,word[-5:]):
				lemmas.append(word[:-5])
			elif re.search(regex_suff4,word[-4:]):
				lemmas.append(word[:-4])
			elif re.search(regex_suff4b,word[-4:]):
				lemmas.append(word[:-4]+'e')
			elif re.search(regex_suff4c,word[-4:]):
				lemmas.append(word[:-4]+'de')
			elif re.search(regex_suff3,word[-3:]):
				lemmas.append(word[:-3])
			elif re.search(regex_suff3b,word[-3:]):
				lemmas.append(word[:-3]+'e')
			elif re.search(regex_suff2,word[-2:]):
				lemmas.append(word[:-2])
			elif re.search(regex_suff2b,word[-2:]):
				lemmas.append(word[:-2]+'e')
			else:
				None
		return(lemmas)
	"""
	function(words): iterates over all the words in the text
	function(puncty): iterates over all the words after they the punctuation is split off
	function(lemmas): to prevent circumflexes and verbs starting with a prefix by iterating over the previous lemmas
	"""
	punctuation(words)
	pronoun(words)
	pronoun(puncty)
	plur(words)
	plur(puncty)
	verbs(words)
	verbs(puncty)
	prefix(words)
	prefix(lemmas)
	suffix(words)
	suffix(lemmas)
	return(lemmas)	

def lexicon(dictonary,words,lemmas):
	"""  
	:param dictionary: A dictionary of words connected to their respective levels.
    :param words: A set of words representing the text.
    :return: A lexicon of words in the text that can be found in the dictionary.
	"""
	lexicon = [ ]
	for word in words:
		if word in dictionary:	
			lexicon.append(word)
	for lemma in lemmas:
		if lemma in dictionary:
			lexicon.append(lemma)
	return(set(lexicon))

def level(lexicon,dictionary):
	"""
	:param lexicon: A lexicon of words in the text that can be found in the dictionary.
	:param dictionary: A dictionary of words connected to their respective levels.
	:return: The word level of the text.
	"""
	word_levels = [ ]
	
	def level_words(lexicon,dictionary): # Looks up the words of the lexicon in the dictionary and retrieves them with their according level
		for word in lexicon:
			level = dictionary[word]
			word_levels.append(level)
		return(word_levels)
	
	def level_text(word_levels): # Calculates the word level of a text according to the theory that to properly comprehend a text the reader has to understand at least 90% of the vocabulary in that text.
		length = (len(word_levels)/10)
		counter_A1 = word_levels.count('A1')
		counter_A2 = word_levels.count('A2')
		counter_B1 = word_levels.count('B1')
		counter_B2 = word_levels.count('B2')
		counter_C1 = word_levels.count('C1')
		counter_C2 = word_levels.count('C2')

		if counter_C2 >= length:
			return('C2')
		elif (counter_C2+counter_C1) >= length:
			return('C1')
		elif (counter_B2+counter_C1+counter_C2) >= length:
			return('B2')
		elif (counter_B1+counter_B2+counter_C1+counter_C2) >= length:
			return('B1')
		elif (counter_A2+counter_B1+counter_B2+counter_C1+counter_C2) >= length:
			return('A2')
		else:
			return('A1')
	level_words(lexicon,dictionary)
	return(level_text(word_levels))

def nr_wordlev(lexicon,dictionary):
	"""Looks up the level of a word and counts how many time each level appears in the text"""	
	word_levels=[ ]
	for word in lexicon:
		level = dictionary[word]
		word_levels.append(level)
	counter_A1 = word_levels.count('A1')
	counter_A2 = word_levels.count('A2')
	counter_B1 = word_levels.count('B1')
	counter_B2 = word_levels.count('B2')
	counter_C1 = word_levels.count('C1')
	counter_C2 = word_levels.count('C2')

	counters = {'levels':['A1', 'A2', 'B1', 'B2', 'C1', 'C2'], 'counters': [counter_A1, counter_A2, counter_B1, counter_B2, counter_C1, counter_C2]}
	return (counters)
""".................................................................................."""
dictionary = load_dictionary("data\\dictionaryABC.csv",';')
#words = load_input(filename)
#lemmas = lematization(words)
#lexicon = lexicon(dictionary,words, lemmas)
#print(words)
#print(len(words))
#print(lemmas)
#print(lexicon)
#print(len(lexicon))
#print(level(lexicon,dictionary))
#print(nr_wordlev(lexicon,dictionary))