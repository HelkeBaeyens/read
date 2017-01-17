import nltk
import re
import os
text =  """in regression analysis is a lagged 5 year average of
years t- 1 to t- 5. The lagged average was used
for two reasons. First, the direction of causality
from past consumption to current agricultural
production is more clearly unidirectional. Second,
a 5 year average better reflects historical nutrient
availability.
Estimates for both calorie supply and requirements are from the FAO. Calorie supplies are
calorie equivalents of a country's food supplies.
Food supplies comprise domestic production, net
imports, and changes in stocks. Daily calorie requirements are estimates of calories needed to
sustain a person at normal levels of activity and
health. Requirements for each country differ taking account of age and sex distributions, average
body weights, and environmental temperatures.
The calorie availability variable may also be
thought of as a measure of food security, albeit a
relatively crude one. The variable says nothing
about the distribution of food availability within a
country. However, it seems reasonable to expect
that as aggregate food availability declines chronic
food insecurity increases. Chronic food insecurity
represents a country's longer term difficulties in
meeting basic nutritional requirements. Food insecurity may adversely effect agricultural productivity for another reason besides its more direct
effect on labor productivity. In areas of chronic
insecurity agricultural producers are likely to
adopt risk-reducing rather than yield-increasing
production strategies (Roumasset, 1976).
2.2.5. Agricultural export growth (Z 5 )
The role of export growth in stimulating overall economic development (Fosu, 1990; GyimahBrempong, 1991; Edwards, 1993) and sectoral
total factor productivity growth (Tybout, 1992;
Edwards, 1993) has received much attention in
the literature.
Export development has been hypothesized to
stimulate productivity growth in a number of ways.
First, countries benefit from basic comparative
advantages and more rapid learning-by-doing
from specialization. Second, expansion into international markets allows the export sector to benefit from scale economies. Third, the pressures of
international competition are thought to force

countries to adopt modern technologies and efficient methods of production more quickly. Fourth,
exports form an important source of foreign exchange necessary for importation of modern inputs and capital formation. Finally, export levies
are an important source of government revenues"""

text2 = "The second reason for his delay was a personal one. He had dawdled over his cigar because he was at heart a dilettante, and thinking over a pleasure to come often gave him a subtler satisfaction than its realization. This was especially the case when the  pleasure was a delicate one,Cecilia was present while the plans were being examined, and observed Sir James's illusion. 'He thinks that Dodo cares about him, and she only cares about her plans. Yet I am not certain that she would refuse him if she thought he would let her manage everything and carry out all her notions. as his pleasures mostly were; and on this occasion the moment he looked forward to was so rare and exquisite in quality that - well, if he had timed his arrival in accord with the prima donna's stage manager he could not have entered the Academy at a more significant moment than just as she was singing and sprinkling the falling daisy petals with notes as clear as dew.\n Why is 'The Great Gatsby' such a quintessential twentieth-century novel? After mixed reviews and  slow start in sales, Fitzgerald's 1925 novel has moved to the centre of literary history, to the extent that to many readers this is the modern American novel. Gatsby is widely loved, and has achieved the unusual status of appealing to both that mythical creature the 'Common Reader' and an academic audience. \n Sky lifted her face and he bent down for a kiss. Wow. I should not be here. They were making out like they had only just found each other, not the behaviour of a couple who had been dating for nearly two years. I turned to leave them some privacy but my flip-flop squeaked on the floorboard. Annabeth laughed. For a moment, she looked almost happy, and Piper thought she'd be a cool friend to hang out with in better times. Forget it, Piper reminded herself. You're not going to make any friends here. Not once they find out. By the end of that day the lives of all three will have been changed for ever. Robbie and Cecilia will have crossed a boundary they had not even imagined at its start, and will become victims of the younger girl's imagination24/12/2016 Briony will have witnessed mysteries, and commited a crime for which whe will spend the rest of her life trying to atone. When she was a child Jennifer liked sports and she played hockey and basketball for an all-boys team. She also worked as a model. At the age of 14 she knew she wanted to be an actress, so she went  to New York City to look for work. She appeared in advertisements for MTV and the fashion company H&M and got work as an actress on TV. Her family moved to LA so that Jennifer could work on TV and in films. Tom is like any other teenager. He goes to school, does his homework, meets his friends an enjoys doing sport. But between 5.30 and 6.30 from Monday to Friday, Tom does something different. He cooks dinner for all the family: mum, dad, younger brother and older sister. In the past, Tom didn't help out at home and his mum wasn't very happy with him. Today, things are different an she is very happy."


text = text.lower()
sentences = text.split('.')
words = set(text.split( ))
print (len(words))

text2 = text2.lower()
sentences = text2.split('.')
word = [ ]
for sentence in sentences:
	word = set(text2.split( ))

dicty = (words-word)
print(dicty)
print(len(dicty))