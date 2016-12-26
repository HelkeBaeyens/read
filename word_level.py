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
	
	def verbs(words):
		modals = ['can', 'may' ,'will' ,'shall'] 
		past_modals = ['could', 'might', 'would', 'should']
		irr_stems = ['rise','wake','bear','beat','become','begin','bend','bind','bid','bind','bet','bite','bleed','blow','break','breed','bring','build','burn','buy','cast','catch','choose','cling','clothe','come','cost','creep','cut','deal','dig','prove','dive','draw','dream','drink','drive','dwell','eat','fall','feed','feel','fight','find','fit','flee','fling','fly','forbid','forget','forgive','forsake','freeze','get','give','go','grind','grow','hang','have','hear','hew','hide','hit','hold','hurt','input','keep','kneel','knit','know', 'lay','lead','lean','leap','learn','leave','lend','let','lie','lie','light','lose','make','mean','meet','mistake','misunderstand','mow','pay','plead','prepay','proofread','put','quit','read','relay','rid','ride','ring','rise','run','saw','say','see','seek','sell','send','set','sew','shake','shave','shear','shed','shine','shit','shoot','show','shrink','shut','sing','sink','sit','slay','sleep','slide','sling','slink','slit','smell','sneak','sow','speak','speed','spell','spend','spill','spin','spit','split','spoil','spread','spring','stand','steal','stick','sting','stink','strew','stride','strike','string','strive','swear','sweat','sweep','swell','swim','swing','take','teach','tear','tell','think','throw','thrust','tread', 'wake','wear','weave','wed','weep','wet','whet','win','wind','withdraw','withhold','withstand','wring','write']
		irr_SPs = ['rose','woke','bore','beat','became','began','bent','bound','bid','bound','bet','bit','bled','blew','broke','bred','brought','built','burned','bought','cast','caught','chose','clung','clothed','came','cost','crept','cut','dealt','dug','proved','dove','drew','dreamt','drank','drove','dwelt','ate','fell','fed','felt','fought','found','fitted','fled','flung','flew','forbade','forgot','forgave','forsook','froze','got','gave','went','ground','grew','hung','had','heard','hewed','hid','hit','held','hurt','inputted','kept','knelt','knit','knew','laid','led','leant','leapt','learnt','left','lent','let','lay','lied','lit','lost','made','meant','met','mistook','misunderstood','mowed','paid','pled','prepaid','proofread','put','quitted','read','relayed','rid','rode','rang','rose','ran','sawed','said','saw','sought','sold','send','set','sewed','shook','shaved','sheared','shed','shone','shat','shot','showed','shrank','shut','sang','sank','sat','slew','slept','slid','slung','slunk','slit','smelt','snuck','sowed','spoke','sped','spelt','spent','spilt','spun','spit','spilt','spoilt','spread','sprang','stood','stole','stuck','stung','stank','strewed','strode','struck','strung','strove','swore','sweat','swept','swelled','swam','swung','took','taught','tore','told','thought','threw','thrust','trod','woke','wore','wove','wed','wept','wet','whetted','won','wound','withdrew','withheld','withstood','wrung','wrote']
		irr_PPs = ['risen','woken','born','beaten','become','begun','bent','bound','bitten','bound','bet','bitten','bled','blown','broken','bred','brought','built','burnt','bought','cast','caught','chosen','clung','clad','come','cost','crept','cut','dealt','dug','proven','dived','drawn','dreamed','drunk','driven','dwelled','eaten','fallen','fed','felt','fought','found','fit','fled','flung','flown','forbidden','forgotten','forgiven','forsaken','frozen','gotten','given','gone','ground','grown','hung','had','heard','hewn','hidden','hit','held','hurt','inputted','kept','kneeled','knitted','known','laid','led', 'leaned','leaped','learned','left','lent','let','lain','lied','lighted','lost','made','meant','met','mistaken','misunderstood','mown','paid','pleaded','prepaid','proofread','put','quitted','read','relayed','rid','ridden','rung','risen','run','sawn','said','seen','sought','sold','sent','set','sewn','shaken','shaven','shorn','shed','shined','shitted','shot','shown','shrunk','shut','sung','sunk','sat','slayed','slept','slid','slung','slinked','slit','smelled','sneaked','sowed', 'spoken','speeded','spelled','spent','spilled','spun','spat','split','spoiled','spread','sprung','stood','stolen','stuck','stung','stunk','strewed','stridden','stricken','strung','strived','sworn','sweated','swept','swollen','swum','swung','taken','taught','torn','told','thought','thrown','thrust','trodden','woken','worn','weaved','wedded','wept','wetted','whetted','won','wound','withdrawn','withheld','withstood','wrung','written']
		zippy_SPs = dict(zip(irr_SPs, irr_stems))
		zippy_PPs = dict(zip(irr_PPs, irr_stems))
		for word in words:
			if word in irr_SPs:
				lemmas.append(zippy_SPs[word])
			if word in irr_PPs:
				lemmas.append(zippy_PPs[word])
			elif re.search('ing$', word[-3:]):	#gerund
				lemmas.append(word[:-3])
			elif re.search('ed$', word[-2:]):	#perfect
				lemmas.append(word[-1])
			elif word in past_modals:
				for modal, past_modal in zip(modals, past_modals):
					lemmas.append(modal)
			elif re.search (r'^(am|is|are|was|were|been|being)$', word):
				lemmas.append('be')

			else: None
		return (lemmas) 
	plur(words)
	verbs(words)
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
dictionary = load_dictionary("data\\dictionaryABC.csv", ';')
words = load_input("written")
lemmas = lematization(words)
lexicon = lexicon(dictionary,words, lemmas)
print(words)
print(len(words))
print(lemmas)
print(lexicon)
print(len(lexicon))


   