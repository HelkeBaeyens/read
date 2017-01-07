from tkinter import * #star imports all the functions in the library
from tkinter.filedialog import asksaveasfilename, askopenfile
import tkinter.messagebox
from tkinter.messagebox import askyesnocancel


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
		self.input.focus() #This way the user immediately finds himself in the right textbox.
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

		"""Third frame: the command buttons concerning the input"""
		self.button_frame = Frame(self)
		self.button_frame.pack(side=TOP, expand=0, fill=X)

		self.open_button = Button(self.button_frame, activebackground='blue',text="Open", command=self.open_doc)
		self.open_button.pack(padx=2, pady=2, side=LEFT)

		self.submit_button = Button(self.button_frame, activebackground='blue', text="Submit", command=self.analyse)
		self.submit_button.pack(padx=2, pady=2, side=LEFT)

		self.simplify_button = Button(self.button_frame, activebackground='blue', text="Make easier", command=self.simply)
		self.simplify_button.pack(padx=2, pady=2, side=LEFT)

		self.clear_button = Button(self.button_frame, activebackground='blue', text="Clear", command=self.clear)
		self.clear_button.pack(padx=2, pady=2, side=LEFT)

		"""Fourth frame: the instructions for the simplifyed text box"""
		self.simplify_frame = Frame(self)
		self.simplify_frame.pack(side=TOP, expand=0, fill=X)

		self.simplify = Label(self.simplify_frame, width='50', text="Simplification of the text:")
		self.simplify.pack(padx=2, pady=2, side=LEFT)

		"""Fifth frame: the output box for the simplified text and the gauge chart"""
		self.simple_frame = Frame(self)
		self.simple_frame.pack(side=TOP, expand=0, fill=X)

		self.simple = Text(self.simple_frame, width="50", height="10", wrap=WORD)
		scroll_simple = Scrollbar(self.simple_frame)
		scroll_simple['command'] = self.simple.yview
		self.simple['yscrollcommand'] = scroll_simple.set
		self.simple.pack(side=LEFT, expand=0, fill=None)
		self.simple.configure(state='disabled') # make sure no one can write in the box
		scroll_simple.pack(side=LEFT, expand=0, fill=Y)

		self.gauge = Canvas(self.simple_frame, bg='violet',height=150, width=250) #adds a gauge chart indicating the level of the text
		self.in_gauge()
		self.gauge.pack(side=RIGHT, expand=5, fill=Y)

		"""Sixth frame: the command bottons concerning the output"""
		self.button_frame2 = Frame(self)
		self.button_frame2.pack(side=TOP, expand=0, fill=X)

		self.save_button = Button(self.button_frame2, activebackground='blue', text="Save", command=self.save_doc)
		self.save_button.pack(padx=2, pady=2, side=LEFT)

		self.quit_button = Button(self.button_frame2, activebackground='blue', text="Quit", command=self.quit_prog)
		self.quit_button.pack(padx=2, pady=2, side=LEFT)

	def open_doc(self):
		"""Function to open a file saved on the computer """
		doc = askopenfile(initialdir="/", title="Open", filetypes=(("Text files", "*.txt"),("All files","*.*")))
		if doc != None:
			date = doc.read()
			self.input.insert(END, data)
			doc.close()
		else: 
			None

	def in_gauge(self):
		"""The gauge shart should start out empty."""

		coordarc= 10, 50, 240, 210
		self.gauge.create_text(93, 30, anchor=W, font="Pursia", text="Text Level" )
		self.gauge.create_arc(coordarc, start=0, extent=180, fill='gainsboro')
		self.gauge.create_text(30, 120, anchor=W, font="Pursia", text="A1")
		self.gauge.create_text(50, 90, anchor=W, font="Pursia", text='A2')
		self.gauge.create_text(90, 75, anchor=W, font="Pursia", text= 'B1')
		self.gauge.create_text(130, 75, anchor=W, font="Pursia", text= 'B2')
		self.gauge.create_text(170, 90, anchor=W, font="Pursua", text= 'C1')
		self.gauge.create_text(205, 120, anchor=W, font="Pursia", text='C2')

	def analyse(self): 
		"""Function recalling the functions from the library to put them in the second text box + error boxes when the textbox is empty, doesn't contain punctuation marks, or if the input is even English at all + graphs"""
		self.info.configure(state='normal') # open witing in box
		filename= self.input.get(1.0,"end-1c")
		
		if not filename:
			tkinter.messagebox.showinfo("Input Error", "There is no text to be analysed")
		elif not filename.endswith(r'.'):
			tkinter.messagebox.showinfo("Input Eror", "Lack of punctuation marks: \n Your sentences need to contain: . , ? , !")
		else:
			words = list(load_input(filename))
			test_list= ["i","we","you","they","he","she","it","a","an","the"]
			Test = False
			for word in words:
				if word in test_list:
					Test = True
					break
			if Test != True:
				tkinter.messagebox.showinfo("Error", "Easy Text doesn't recognize the input as English")
			else:
				dictionary= load_dictionary("data\\dictionaryABC.csv", ';')
				lemmas = lematization(words)
				lexiconX = lexicon(dictionary,words,lemmas)  #don't give the variable the same name as the function, it won't work twice
				levelX = str(level(lexiconX, dictionary))
				sentencesX= load_input2(filename)
				levelZ= sen_lev(sentencesX)
				levelY = (text_level(levelX, levelZ))
				message = "The level of the text: "+ levelY + "\n" + "The wordlevel is: " + levelX + "\n" + "The number of words: "+ str(nr_words(words)) + "\n" + r' ' + "\n" + 'The average length of the words: ' + av_length_words(words) + "\n" + 'The longest word: ' + str(max_length_words(words)) + "\n" + 'The length of the longest word: ' + len_longest_word(words) + "\n" + 'The differentation of words within the text is: ' + differentiation(words, filename) + "\n" + "The number of sentences: "+ str(sentence_count(sentencesX)) + "\n" + "The average length of the sentences: " + av_sentence_length(sentencesX) + "\n" + "The longest sentence: " + max_sentence(sentencesX) + "\n" + "The shortest sentence: " + min_sentence(sentencesX)
				self.info.delete(1.0, END) # empty the text box before adding new information
				self.info.insert(1.0, message) # fill the textbox with the answer
				self.info.configure(state='disabled') # close writing in box again

			"""according to the level of the text the gauge moves up"""	
			coordarc= 10,50,240,210
			if levelY == "A1":
				self.gauge.create_text(93, 30, anchor=W, font="Pursia", text="Text Level" )
				self.gauge.create_arc(coordarc, start=150, extent=30, fill='green')
				self.gauge.create_text(30,120, anchor=W, font="Pursia", text='A1')
			elif levelY == "A2":
				self.gauge.create_text(93, 30, anchor=W, font="Pursia", text="Text Level" )
				self.gauge.create_arc(coordarc, start=120, extent=60, fill='lime')
				self.gauge.create_text(50,90, anchor=W, font="Pursia", text='A2')
				self.gauge.create_arc(coordarc, start=150, extent=30, fill='green')
				self.gauge.create_text(30,120, anchor=W, font="Pursia", text='A1')
			elif levelY == "B1":
				self.gauge.create_text(93, 30, anchor=W, font="Pursia", text="Text Level" )
				self.gauge.create_arc(coordarc, start=90, extent=90, fill='yellow')
				self.gauge.create_text(90,75, anchor=W, font="Pursia", text='B1')
				self.gauge.create_arc(coordarc, start=120, extent=60, fill='lime')
				self.gauge.create_text(50,90, anchor=W, font="Pursia", text='A2')
				self.gauge.create_arc(coordarc, start=150, extent=30, fill='green')
				self.gauge.create_text(30,120, anchor=W, font="Pursia", text='A1')
			elif levelY == "B2":
				self.gauge.create_text(93, 30, anchor=W, font="Pursia", text="Text Level" )
				self.gauge.create_arc(coordarc, start=60, extent=120, fill='orange')
				self.gauge.create_text(130,75, anchor=W, font="Pursia", text='B2')
				self.gauge.create_arc(coordarc, start=90, extent=90, fill='yellow')
				self.gauge.create_text(90,75, anchor=W, font="Pursia", text='B1')
				self.gauge.create_arc(coordarc, start=120, extent=60, fill='lime')
				self.gauge.create_text(50,90, anchor=W, font="Pursia", text='A2')
				self.gauge.create_arc(coordarc, start=150, extent=30, fill='green')
				self.gauge.create_text(30,120, anchor=W, font="Pursia", text='A1')
			elif levelY == "C1":
				self.gauge.create_text(93, 30, anchor=W, font="Pursia", text="Text Level" )
				self.gauge.create_arc(coordarc, start=30, extent=150, fill='orange red')
				self.gauge.create_text(170,90, anchor=W, font="Pursia", text='C1')
				self.gauge.create_arc(coordarc, start=60, extent=120, fill='orange')
				self.gauge.create_text(130,75, anchor=W, font="Pursia", text='B2')
				self.gauge.create_arc(coordarc, start=90, extent=90, fill='yellow')
				self.gauge.create_text(90,75, anchor=W, font="Pursia", text='B1')
				self.gauge.create_arc(coordarc, start=120, extent=60, fill='lime')
				self.gauge.create_text(50,90, anchor=W, font="Pursia", text='A2')
				self.gauge.create_arc(coordarc, start=150, extent=30, fill='green')
				self.gauge.create_text(30,120, anchor=W, font="Pursia", text='A1')
			else: 
				self.gauge.create_text(93, 30, anchor=W, font="Pursia", text="Text Level" )
				self.gauge.create_arc(coordarc, start=0, extent=180, fill='crimson')
				self.gauge.create_text(205,120, anchor=W, font="Pursia", text='C2')
				self.gauge.create_arc(coordarc, start=30, extent=150, fill='red')
				self.gauge.create_text(170,90, anchor=W, font="Pursia", text='C1')
				self.gauge.create_arc(coordarc, start=60, extent=120, fill='dark orange')
				self.gauge.create_text(130,75, anchor=W, font="Pursia", text='B2')
				self.gauge.create_arc(coordarc, start=90, extent=90, fill='yellow')
				self.gauge.create_text(90,75, anchor=W, font="Pursia", text='B1')
				self.gauge.create_arc(coordarc, start=120, extent=60, fill='lime')
				self.gauge.create_text(50,90, anchor=W, font="Pursia", text='A2')
				self.gauge.create_arc(coordarc, start=150, extent=30, fill='green')
				self.gauge.create_text(30,120, anchor=W, font="Pursia", text='A1')

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
			words = list(load_input(filename))
			test_list= ["i","we","you","they","he","she","it","a","an","the"]
			Test = False
			for word in words:
				if word in test_list:
					Test = True
					break
			if Test != True:
				tkinter.messagebox.showinfo("Error", "Easy Text doesn't recognize the input as English")
			else:
				if content == 'Hallo':
					message = "short"
				else:
					message = "Hallo"
		self.simple.delete(1.0, END) # empty the text box before adding new information
		self.simple.insert(1.0, message) # fill the textbox with the answer
		self.simple.configure(state='disabled') # close writing in box again

	def clear(self):
		"""Function to simultaneously clear all the text windows"""
		self.info.configure(state='normal')
		self.simple.configure(state='normal')

		self.input.delete(0.0, 'end')
		self.info.delete(0.0, 'end')
		self.simple.delete(0.0,'end')

		self.info.configure(state='disabled')
		self.simple.configure(state='disabled')

	def save_doc(self):
		"""Function to save a textfile on the computer"""
		filename=asksaveasfilename(defaultextension="*.txt", filetypes=(("Text files","*.txt"), ("All files","*.*")))
		if filename:
			with open(filename,'w') as stream:
				stream.write(self.info.get("1.0","end-1c"))

	def quit_prog(self):
		"""Function connected to the quit button that verifies it the user has saved the information before closing the program."""
		confirm= askyesnocancel("Verify exit", "Do you want to save your document?")
		if confirm == True:
			self.save_doc()
		elif confirm == False:
			self._root().destroy()


	
#create the windoww + give title
root = Tk()
root.title('Easy Text')
root.geometry('900x300') #modify root window
root.iconbitmap('ET_Logo.ico') # changes the python icon into our own logo
app = Application(root)
root.mainloop()