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
				sen_lev(sentences)
				text_lev(level,sen_lev)
				simply_sen(filename)
"""
from word_level import *
import re
def nr_words(words): # Calculates the numbers of words in a file
	return len(words)

def av_length_words(words): #Calculates the average length of words in a file
	lengths = 0
	for word in words:
		lengths += len(word)
	return str(lengths/(nr_words(words)))

def max_length_words(words): #Looks for the longest word in a file
	counter = 0
	for word in words:
		if word.replace('?' or '!' or ',', '.').endswith('.'):
			word.replace(word, word[-1])
	for word in words:
		if len(word) > counter:
			max_len = word
			counter = len(word)
	return str(max_len)

def len_longest_word(words): #Calculates the length of the longest word in a file
	return str(len(max_length_words(words)))

def differentiation(words, filename): # Looks for differentiation in a text by dividing the length of the set of words over the length of the file
	return str(len(set(words))/len(filename.split()))
	
def load_input2(filename): # second way to load the input in order to separate the sentences instead of words.
	return filename.replace('?' or '!', '.').split('. ')

def sentence_count(sentences): #Calculated the number of sentences
	return len(sentences)

def av_sentence_length(sentences): # Calculates the average length of the sentences
	sen_length = 0
	for sentence in sentences:
		sentence = sentence.split(' ')
		sen_length += (len(sentence))
	return str(sen_length/sentence_count(sentences))

def max_sentence(sentences): # Calculates the length of the longest sentence.
	counter = 0
	for sentence in sentences:
		sentence = sentence.split(' ')
		if len(sentence) > counter:
			counter = (len(sentence))
	return str(counter)

def min_sentence(sentences): # Calculates the length of the shortest sentence
	counter = 1000
	for sentence in sentences:
		sentence = sentence.split(' ')
		if len(sentence) < counter:
			counter = (len(sentence))
	return str(counter)

def sen_lev(sentences):
	av_sen = float(av_sentence_length(sentences))
	if av_sen > 40:
		return 'C2'
	elif av_sen > 30:
		return 'C1'
	elif av_sen > 25:
		return 'B2'
	elif av_sen > 20:
		return 'B1'
	elif av_sen > 15:
		return 'A2'
	else: 
		return 'A1'

def text_level(level, sen_lev):
	"""Function to calculate the level of the text"""
	calcu = {'A1': 1, 'A2': 2, 'B1': 3, 'B2': 4, 'C1': 5, 'C2':6}
	W = int(calcu[level])*0.8 										#80% word level		
	S = int(calcu[sen_lev])*0.1 									#10% sentence level
	T = 1*0.1 														#10% temporal value the definition doesn't exist yet
	nr = (W + S + T)
	
	if nr > 5:
		return 'C2'
	elif nr > 4:
		return 'C1'
	elif nr > 3:
		return 'B2'
	elif nr > 2:
		return 'B1'
	elif nr > 1:
		return 'A2'
	else: 
		return 'A1'

def simply_sen(filename):
	"""this function splits sentences into shorter sentences when the length of the sentence is higher than a B1 level (>20)"""
	sentences= filename.replace('?' or '!', '.').split('.')
	simplies = [ ]
	for sentence in sentences:
		words=sentence.split(' ')
		if len(words) > 20:
			sen = sentence.replace(':' or ';' or '-', ',').split(',')  # the sentences are split on punctuation.
			if len(sen) > 1:
				counter = 0
				if counter <len(sen):
					words2=sen[counter].split(' ')
					words3= sen[counter+1].split(' ')
					counter +=1
					if len(words2) > 5 and len(words3) > 5:
						simply = '.'.join(sen)
						simplies.append(simply)
					else:
						simplies.append(sentence)
			else: 
				simplies.append(sentence)
	sentences2 = '.'.join(simplies)
	simplified = [ ]
	sentences2 = sentences2.split('.')
	regex= ['but','or','if', 'and']
	for sentence in sentences2:
		words=sentence.split(' ')
		if len(words) > 20:
			counter = 0
			for word in regex:
				if word in sentence:
					sen2 = sentence.replace(word, ('. '+word)).split('.') # the sentences are split on punctuation.
			words2=sen2[counter].split(' ')
			words3= sen2[counter+1].split(' ')
			if len(words2) > 5 and len(words3) > 5:
				simplify = '.'.join(sen2)
				simplified.append(simplify)
				counter +=1
			else:
				simplified.append(sentence)
		else: 
			simplified.append(sentence)	
	
	simplified = '.'.join(simplified)
	simplified = re.split('([.] *)', simplified)
	def upperfirst(text):
		return text[0].upper()+text[1:]
	simple = ''
	for i in simplified:
		if len(i) > 1:
			simple+= upperfirst(i)
	return simple
	
def search_unknown(filename, dictionary):
	""" Searches the words that are misspelled/not in the dictionary"""
	numbers = re.findall('[\d]+', filename)
	words = filename.lower().replace('.' or '?', ' ').replace('!' or '-',' ').split(' ')
	unknowns = list(words)
	rex= ['teeth','geese','men','feet','children', 'i','its', 'are','oxen','mice','men','women','sheep', 'me', 'mine', 'his', 'hers', 'there', 'theirs', 'yours', 'her','him', 'their', 'your', 'them', 'my', 'our', 'ours', 'them','people', 'am','these', 'those','could','might','would','should', 'rose','woke','bore','beat', 'been','became','began','bent','bound','bid','bound','bet','bit','bled','blew','broke','bred','brought','built','burned','bought','cast','caught','chose','clung','clothed','came','cost','crept','cut','dealt','dug','proved','dove','drew','dreamt','drank','drove','dwelt','ate','fell','fed','felt','fought','found','fitted','fled','flung','flew','forbade','forgot','forgave','forsook','froze','got','gave','went','ground','grew','hung','had','heard','hewed','hid','hit','held','hurt','inputted','kept','knelt','knit','knew','laid','led','leant','leapt','learnt','does','doing' ,'goes', 'left','lent','let','lay','lied','lit','lost','made','meant','met','mistook','misunderstood','mowed','paid','pled','prepaid','proofread','put','quitted','read','relayed','rid','rode','rang','rose','ran','sawed','said','saw','sought','sold','send','set','sewed','shook','shaved','sheared','shed','shone','shat','shot','showed','shrank','shut','sang','sank','sat','slew','slept','slid','slung','slunk','slit','smelt','snuck','sowed','spoke','sped','spelt','spent','spilt','spun','spit','spilt','spoilt','spread','sprang','stood','stole','stuck','stung','stank','strewed','strode','struck','strung','strove','swore','sweat','swept','swelled','swam','swung','took','taught','tore','told','thought','threw','thrust','trod','woke','wore','wove','wed','wept','wet','whetted','won','wound','withdrew','withheld','withstood','wrung','wrote', 'risen','woken','born','beaten','become','begun','bent','bound','bitten','bound','bet','bitten','bled','blown','broken','bred','brought','built','burnt','bought','cast','caught','chosen','clung','clad','come','cost','crept','cut','dealt','dug','proven','dived','drawn','dreamed','drunk','driven','dwelled','eaten','fallen','fed','felt','fought','found','fit','fled','flung','flown','forbidden','forgotten','forgiven','forsaken','frozen','gotten','given','gone','ground','grown','hung','had', 'has','heard','hewn','hidden','hit','held','hurt','inputted','kept','kneeled','knitted','known','laid','led', 'leaned','leaped','learned','left','lent','let','lain','lied','lighted','lost','made','meant','met','mistaken','misunderstood','mown','paid','pleaded','prepaid','proofread','put','quitted','read','relayed','rid','ridden','rung','risen','run','sawn','said','seen','sought','sold','sent','set','sewn','shaken','shaven','shorn','shed','shined','shitted','shot','shown','shrunk','shut','sung','sunk','sat','slayed','slept','slid','slung','slinked','slit','smelled','sneaked','sowed', 'spoken','speeded','spelled','spent','spilled','spun','spat','split','spoiled','spread','sprung','stood','stolen','stuck','stung','stunk','strewed','stridden','stricken','strung','strived','sworn','sweated','swept','swollen','swum','swung','taken','taught','torn','told','thought','thrown','thrust','trodden','woken','worn','weaved','wedded','wept','wetted','whetted','won','wound','withdrawn','withheld','withstood','wrung','written','were', 'was', "didn't", "wasn't", "couldn't", "wouldn't", "shouldn't", "i'm", "he's", "she's", "you're", "we're", "doesn't", "aren't", "they're", "i'll", "he'll", "we'll", "you'll", "she'll", "it'll", "they'll", "it's", "i'd", "you'd", "he'd", "she'd", "we'd", "they'd"]
	for word in words:
		if word == '' or word == r'\W':
			unknowns.remove(word)
		elif word[-1:] == '\?' or word[-1:] == ',' or word[-1:] == ':' or word[-1:] == ';' or word[-1:] == ')':
			unknowns.remove(word)
			unknowns.append(word[:-1])
	for word in words:
		if word in dictionary:
			unknowns.remove(word)
		elif word in rex:
			unknowns.remove(word)
		if word in numbers:
			unknowns.remove(word)

	for word in unknowns:
		if word[-5:] == 'tting' or word[-5:] =='nning' or word[-5:] == 'pping' or word[-5:] == 'mming' or word[-5:] == 'rring' or word[-5:] == 'lling' or word[-5:] == 'bbing' or word[-5:] == 'ation':
			if word[:-5] in dictionary:
				unknowns.remove(word)
			if word[:-4]+'e' in dictionary:
				unknowns.remove(word)
		if word[-1:] == 'a':
			if word[:-1]+'um' in dictionary:
				unknowns.remove(word)
		if word[-4:] == 'tted' or word[-4:] == 'rred' or word[-4:] == 'lled' or word[-4:] == 'bbed' or word[-4:] == 'gged' or word[-4:] == 'pped':
			if word[:-3] in dictionary:
				unknowns.remove(word) 
			if word[:-3] +'e' in dictionary:
				unknowns.remove(word)
		if word[-4:] == 'ment' or word[-4:] == 'ness' or word[-4:] == 'ship' or word[-4:] == 'less' or word[-4:] == 'able' or word[-4:] == 'ance': 
			if word[:-4] in dictionary:
				unknowns.remove(word)

	for word in unknowns:
		if word[-3:] == 'ing':
			if word[:-3]+'e' in dictionary:
				unknowns.remove(word)
		if word [-1:] == 's' or word[-1:] == 'y' or word[-1:] == 'd' or word[-1:] == 'r':
			if word[:-1] in dictionary:
				unknowns.remove(word)

	for word in unknowns:
		if word[-3:] == 'ing' or word[-3:] == 'dom' or word[-3:] == 'ize' or word[-3:] == 'ise' or word[-3:] == 'ism'or word[-3:] == 'ful' or word[-3:] == 'ish'or word[-3:] == 'ary'or word[-3:] == 'ate'or word[-3:] == 'ade' or word[-3:] == 'ity':
			if word[:-3] in dictionary:
				unknowns.remove(word)
		if word[-2:] == 'es' or word[-2:] == 'ly' or word[-2:] == 'en' or word[-2:] == 'or' or word[-2:] == 'en' or word[-2:] == 'al' or word[-2:] == 'ed' or word[-2:] == 'er' or word[-2:] == 'ty' :
			if word[:-2] in dictionary:
				unknowns.remove(word)

	for word in unknowns: 
		if word [:7] == 'counter':
			if word[7:] in dictionary:
				unknowns.remove(word)
		if word [:6] == 'contra':
			if word[6:] in dictionary:
				unknowns.remove(word)
		if word[:5] == 'extra' or word[:5] == 'hyper' or word[:5] == 'intra' or word[:5] == 'trans' or word[:5] == 'ultra' or word[:5] == 'onder' or word[:5] == 'super' :
			if word[5:] in dictionary:
				unknowns.remove(word)
		if word[:4] == 'ante' or word[:4] == 'anti' or word[:4] == 'hemi' or word[:4] == 'hypo' or word[:4] == 'peri' or word[:4] == 'semi' or word[:4] == 'over' or word[:4] == 'post' or word[:4] == 'auto' or word[:4] == 'mega':
			if word[4:] in dictionary:
				unknowns.remove(word)
		if word[:3] == 'dis' or word[:3] == 'non' or word[:3] == 'pre' or word[:3] == 'pro' or word[:3] == 'sub' or word[:3] == 'sup' or word[:3] == 'mis':
			if word[3:] in dictionary:
				unknowns.remove(word)
		if word[:2] == 'un' or word[:2] == 'in' or word[:2] == 'im' or word[:2] == 're' or word[:2] == 'an' or word[:2] == 'af' or word[:2] == 'al' or word[:2] == 'be' or word[:2] == 'co' or word[:2] == 'ex' or word[:2] == 'en' or word[:2] == 'up':
			if word[2:] in dictionary:
				unknowns.remove(word)
		if word[:1] == 'a' or word[:1] == 'e':
			if word[1:] in dictionary:
				unknowns.remove(word)

	for word in unknowns:
		if word == '':
			unknowns.remove(word)
	return unknowns