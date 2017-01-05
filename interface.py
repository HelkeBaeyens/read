from tkinter import * #star imports all the functions in the library
import tkinter.messagebox
from tkinter.messagebox import askokcancel

from word_level import * 			
from function_lib import *
import re

class Application(Frame):

	def __init__(self, master):
		Frame.__init__(self,master)
		self.pack()
		self.create_widgets()

	def create_widgets(self): # make frame, place frame, label|button|text, scrollbar
		"""First frame: instructions"""
		self.instr_frame = Frame(self)
		self.instr_frame.pack(side=TOP, expand=0, fill=X)

		self.instruction = Label (self.instr_frame, width='50', text='Enter your text here:')
		self.instruction.pack(padx=2, pady=2, side=LEFT) #put the lable to a certain side)
		
		self.level = Label(self.instr_frame, width='50', text='Information about the text:')
		self.level.pack(padx=2, pady=2, side=RIGHT)

		"""Second frame: text boxes for input and text information, added: a scrollbar that covers the Y and keeps record of which part of the text is shown """
		self.text_frame = Frame(self)
		self.text_frame.pack(side=TOP, expand=0, fill=X)

		self.input = Text(self.text_frame, width="50", height="5", wrap=WORD)
		scroll_input = Scrollbar(self.text_frame)
		scroll_input['command'] = self.input.yview
		self.input['yscrollcommand']= scroll_input.set
		self.input.pack(side=LEFT, expand=0, fill=None)
		scroll_input.pack(side=LEFT, expand=0, fill=Y)

		self.info = Text(self.text_frame, width="50", height="5", wrap=WORD)
		scroll_info = Scrollbar(self.text_frame)
		scroll_info['command'] = self.info.yview
		self.info['yscrollcommand'] = scroll_info.set
		self.info.pack(side=LEFT, expand=0, fill=None)
		self.info.configure(state='disabled') # make sure no one can write in the box
		scroll_info.pack(side=LEFT, expand=0, fill=Y)

		"""Third frame: the commant buttons concerning the input"""
		self.button_frame = Frame(self)
		self.button_frame.pack(side=TOP, expand=0, fill=X)

		self.submit_button = Button(self.button_frame, text="Submit", command=self.analyse)
		self.submit_button.pack(padx=2, pady=2, side=LEFT)

		self.simplify_button = Button(self.button_frame, text="Make easier", command=self.simply)
		self.simplify_button.pack(padx=2, pady=2, side=LEFT)
	
		"""Fourth frame: the instructions for the simplifyed text box"""
		self.simplify_frame = Frame(self)
		self.simplify_frame.pack(side=TOP, expand=0, fill=X)

		self.simplify = Label(self.simplify_frame, width='50', text="Simplification of the text:")
		self.simplify.pack(padx=2, pady=2, side=LEFT)

		"""Fifth frame: the output box for the simplified text"""
		self.simple_frame = Frame(self)
		self.simple_frame.pack(side=LEFT, expand=0, fill=X)

		self.simple = Text(self.simple_frame, width="50", height="5", wrap=WORD)
		scroll_simple = Scrollbar(self.simple_frame)
		scroll_simple['command'] = self.simple.yview
		self.simple['yscrollcommand'] = scroll_simple.set
		self.simple.pack(side=LEFT, expand=0, fill=None)
		self.simple.configure(state='disabled') # make sure no one can write in the box
		scroll_simple.pack(side=LEFT, expand=0, fill=Y)

	def analyse(self): 
		"""Function recalling the functions from the library to put them in the second text box + error boxes when the textbox is empty or doesn't contain punctuation marks"""
		self.info.configure(state='normal') # open witing in box
		filename= self.input.get(1.0,"end-1c")
		
		if not filename:
			tkinter.messagebox.showinfo("Input Error", "There is no text to be analysed")
		elif not filename.endswith(r'.'):
			tkinter.messagebox.showinfo("Input Eror", "Lack of punctuation marks: \n Your sentences need to contain: . , ? , !")
		else:
			words = list(load_input(filename))
			dictionary= load_dictionary("data\\dictionaryABC.csv", ';')
			lemmas = lematization(words)
			lexiconX = lexicon(dictionary,words,lemmas)  #don't give the variable the same name as the function, it won't work twice
			levelX = str(level(lexiconX,dictionary))
			sentences= load_input2(filename)
			message = "The level of the text: " + levelX + "\n" + "The number of words: "+ str(nr_words(words)) + "\n" + r' ' + "\n" + 'The average length of the words: ' + av_length_words(words) + "\n" + 'The longest word: ' + str(max_length_words(words)) + "\n" + 'The length of the longest word: ' + len_longest_word(words) + "\n" + 'The differentation of words within the text is: ' + differentiation(words, filename) + "\n" + "The number of sentences: "+ str(sentence_count(sentences)) + "\n" + "The average length of the sentences: " + av_sentence_length(sentences) + "\n" + "The longest sentence: " + max_sentence(sentences) + "\n" + "The shortest sentence: " + min_sentence(sentences)
			self.info.delete(1.0, END) # empty the text box before adding new information
			self.info.insert(1.0, message) # fill the textbox with the answer
			self.info.configure(state='disabled') # close writing in box again

	def simply(self):
		"""Temporal function to fill the textbox that is going to fill the simplified text + error boxes when the textbox is empty or doesn't contain punctuation marks"""
		self.simple.configure(state='normal') # open witing in box
		content= self.input.get(1.0,"end-1c")
		if not content:
			tkinter.messagebox.showinfo("Input Error", "There is no text to be analysed")
		elif not content.endswith(r'.'):
			tkinter.messagebox.showinfo("Input Eror", "Lack of punctuation marks: \n Your sentences need to contain: . , ? , !")
		else:
			if content == 'Hallo':
				message = "short"
			else:
				message = "Hallo"
		self.simple.delete(1.0, END) # empty the text box before adding new information
		self.simple.insert(1.0, message) # fill the textbox with the answer
		self.simple.configure(state='disabled') # close writing in box again
	
#create the windoww + give title
root = Tk()
root.title('Easy Text')
root.geometry('900x300') #modify root window
app = Application(root)
root.mainloop()