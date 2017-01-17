from tkinter import * #star imports all the functions in the library
from tkinter.filedialog import asksaveasfilename, askopenfile
import tkinter.messagebox
from tkinter.messagebox import askyesnocancel

from word_level import * 	
from function_lib import *
import re
import math

class Application(Frame):

	def __init__(self, master):
		Frame.__init__(self,master)
		self.pack()
		self.create_widgets()

	def create_widgets(self): # make frame, place frame, label|button|text, scrollbar, functions, ...
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

		"""Seventh frame: the graphs belonging to the information about the text"""
		self.graph_frame = Frame(self, width = 800, height= 260)
		self.graph_frame.pack(side=TOP, expand=1, fill=X)
		
		self.bar_chart = Canvas(self.graph_frame, bg='beige', height=260, width=400, scrollregion=(0,0,400,260)) #adds a bar chart indicating the lenght of the sentences
		#scroll_chart = Scrollbar(self.bar_chart, orient=HORIZONTAL)
		#scroll_chart.pack(side=BOTTOM,expand=0,fill=X)
		#scroll_chart.config(command=self.bar_chart.xview)
		#self.bar_chart.config(xscrollcommand=scroll_chart.set)
		self.bar_chart.pack(side=LEFT, expand=1, fill=BOTH)
		self.in_bar_chart()

		self.histo = Canvas(self.graph_frame, bg='beige', height=260, width=400) #adds a bar chart indicating the number of words within a certain level
		self.histo.pack(side=RIGHT, expand=0, fill=None)
		self.in_histo() 
		
	def open_doc(self):
		"""Function to open a file saved on the computer """
		doc = askopenfile(initialdir="/", title="Open", filetypes=(("Text files", "*.txt"),("All files","*.*")))
		if doc != None:
			data = doc.read()
			self.input.insert(END, data)
			doc.close()
		else: 
			None

	def in_gauge(self):
		"""The gauge shart should start out empty."""

		coordarc= 10, 50, 240, 210
		self.gauge.create_text(90, 30, anchor=W, font=("times", 16, "italic"), text="Text Level" )
		self.gauge.create_arc(coordarc, start=0, extent=180, fill='gainsboro')
		self.gauge.create_text(30, 120, anchor=W, font="Pursia", text="A1")
		self.gauge.create_text(50, 90, anchor=W, font="Pursia", text='A2')
		self.gauge.create_text(90, 75, anchor=W, font="Pursia", text= 'B1')
		self.gauge.create_text(130, 75, anchor=W, font="Pursia", text= 'B2')
		self.gauge.create_text(170, 90, anchor=W, font="Pursua", text= 'C1')
		self.gauge.create_text(205, 120, anchor=W, font="Pursia", text='C2')

	def in_bar_chart(self):
		self.bar_chart.create_line(30,230,380,230)
		self.bar_chart.create_line(30,230,30,20)
		self.bar_chart.create_text(150, 25, anchor=W, font=("times",16,"italic"), text="Sentence Length" )
		self.bar_chart.create_text(150,260, font=("times",12,"bold"), anchor=SW, text="Sentences")
		self.bar_chart.pack(side=LEFT, expand=0, fill=Y)

	def in_histo(self):
		self.histo.create_line(30,230,380,230)
		self.histo.create_line(30,230,30,20)
		self.histo.create_text(150, 25, anchor=W, font=("times",16,"italic"), text="Word Level" )
		self.histo.create_text(150,260, font=("times",12,"bold"), anchor=SW, text="Levels")
		self.histo.pack(side=RIGHT, expand=0, fill=Y)

	def analyse(self): 
		"""Function recalling the functions from the library to put them in the second text box + error boxes when the textbox is empty, doesn't contain punctuation marks, or if the input is even English at all + graphs"""
		self.info.configure(state='normal') # open witing in box
		filename= self.input.get(1.0,"end-1c")
		self.in_gauge()
		self.in_bar_chart()
		self.in_histo()
		
		if not filename:
			tkinter.messagebox.showinfo("Input Error", "There is no text to be analysed")
		elif not filename.replace('?' or '!','.').endswith(r'.'):
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
					self.gauge.create_text(90, 30, anchor=W, font=("times",16,"italic"), text="Text Level" )
					self.gauge.create_arc(coordarc, start=150, extent=30, fill='green')
					self.gauge.create_text(30,120, anchor=W, font="Pursia", text='A1')
				elif levelY == "A2":
					self.gauge.create_text(90, 30, anchor=W, font=("times",16,"italic"), text="Text Level" )
					self.gauge.create_arc(coordarc, start=120, extent=60, fill='lime')
					self.gauge.create_text(50,90, anchor=W, font="Pursia", text='A2')
					self.gauge.create_arc(coordarc, start=150, extent=30, fill='green')
					self.gauge.create_text(30,120, anchor=W, font="Pursia", text='A1')
				elif levelY == "B1":
					self.gauge.create_text(90, 30, anchor=W, font=("times",16,"italic"), text="Text Level" )
					self.gauge.create_arc(coordarc, start=90, extent=90, fill='yellow')
					self.gauge.create_text(90,75, anchor=W, font="Pursia", text='B1')
					self.gauge.create_arc(coordarc, start=120, extent=60, fill='lime')
					self.gauge.create_text(50,90, anchor=W, font="Pursia", text='A2')
					self.gauge.create_arc(coordarc, start=150, extent=30, fill='green')
					self.gauge.create_text(30,120, anchor=W, font="Pursia", text='A1')
				elif levelY == "B2":
					self.gauge.create_text(90, 30, anchor=W, font=("times",16,"italic"), text="Text Level" )
					self.gauge.create_arc(coordarc, start=60, extent=120, fill='orange')
					self.gauge.create_text(130,75, anchor=W, font="Pursia", text='B2')
					self.gauge.create_arc(coordarc, start=90, extent=90, fill='yellow')
					self.gauge.create_text(90,75, anchor=W, font="Pursia", text='B1')
					self.gauge.create_arc(coordarc, start=120, extent=60, fill='lime')
					self.gauge.create_text(50,90, anchor=W, font="Pursia", text='A2')
					self.gauge.create_arc(coordarc, start=150, extent=30, fill='green')
					self.gauge.create_text(30,120, anchor=W, font="Pursia", text='A1')
				elif levelY == "C1":
					self.gauge.create_text(90, 30, anchor=W, font=("times",16,"italic"), text="Text Level" )
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
					self.gauge.create_text(90, 30, anchor=W, font="Pursia", text="Text Level" )
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

				"""A graph indicating the length of the sentences """
				senList = [ ]
				for sentence in sentencesX:
					words = sentence.split(" ")
					senList.append(len(words))	
				self.bar_chart.delete(ALL)
				self.in_bar_chart()
				len_list = len(senList)
				senList = sorted(senList)
				 # Values important for the graph such as changeable hight of the y axis
				highest = max(senList)
				round_up = int(math.ceil(highest/10.0))*10
				graph_hight = 190
				c_height = 260
				lm= 30
				rm=20
				tm= 40
				if len_list > 350:
					graph_width = len_list
					c_width=graph_width+lm+rm
					self.bar_chart.pack_forget()
					self.bar_chart = Canvas(self.graph_frame, width=c_width, height=c_height, bg='beige', scrollregion=(0,0,c_width, c_height))
					scroll_chart = Scrollbar(self.bar_chart, orient=HORIZONTAL)
					scroll_chart.pack(side=BOTTOM,expand=0,fill=X)
					scroll_chart.config(command=self.bar_chart.xview)
					self.bar_chart.config(xscrollcommand=scroll_chart.set)
					self.bar_chart.create_line(30,230,graph_width,230)
					self.bar_chart.create_line(30,230,30,20)
					self.bar_chart.create_text(150, 25, anchor=W, font=("times",16,"italic"), text="Sentence Length" )
					self.bar_chart.create_text(150,260, font=("times",12,"bold"), anchor=SW, text="Sentences")
					self.bar_chart.pack(side=LEFT, expand=1, fill=BOTH)

		
		#self.bar_chart.pack(side=LEFT, expand=0, fill=Y)
				else:
					graph_width = 350
					c_width = graph_width+50
				
				bar = graph_width/len_list


				for x,y in enumerate(senList):		#Here the length of the bars is indicated
	 				x0 = x*(graph_width/len_list)+lm
	 				x1 = x0 + bar
	 				y0 = (graph_hight-((graph_hight*y)/highest))+tm		
	 				y1 = graph_hight+tm

	 				self.bar_chart.create_rectangle(x0,y0,x1,y1, fill='red')
	 				if len_list <=50:
	 					self.bar_chart.create_text(x0+bar/3 , y0, anchor=SW, text=str(y))

						#indication of the values printed on the x-axis
				if len_list <=20:
					j=1
					for sen in senList:
	 					if j<= len_list:
	 						self.bar_chart.create_line(bar*(j-1)+ (bar/2)+lm,235, bar*(j-1)+(bar/2)+lm,230)
	 						self.bar_chart.create_text(bar*(j-1)+bar/2+lm,250, anchor=SW, text=str(j))
	 						j+=1

				elif len_list <= 50:
					j=5
					for sen in senList:
	 					if j<= len_list:
	 						self.bar_chart.create_line(bar*(j-1)+ (bar/2)+lm,235, bar*(j-1)+(bar/2)+lm,230)
	 						self.bar_chart.create_text(bar*(j-1)+bar/2+lm,250, anchor=SW, text=str(j))
	 						j+=5
	 					
				elif len_list <=100:
					j=10
					for sen in senList:
						if j <= len_list:
	 						self.bar_chart.create_line(bar*(j-1)+ (bar/2)+lm,235, bar*(j-1)+(bar/2)+lm,230)
	 						self.bar_chart.create_text(bar*(j-1)+bar/2+lm,250, anchor=SW, text=str(j))
	 						j+=10

				else:
					j=50
					for sen in senList:
	 					self.bar_chart.create_line(bar*(j-1)+ (bar/2)+lm,235, bar*(j-1)+(bar/2)+lm,230)
	 					self.bar_chart.create_text(bar*(j-1)+bar/2+lm,250, anchor=SW, text=str(j))
	 					j+=50

				j=0				#indication of the values printed on the y-axis
				fact=0
				if highest <=10:
					while j <= 10:
	 					self.bar_chart.create_line(20,tm+(j*graph_hight/round_up),lm,tm+(j*graph_hight/round_up))
	 					self.bar_chart.create_text(15,tm+(j*graph_hight/round_up), anchor= SW, text= str(round_up-fact))
	 					j +=1
	 					fact +=1
				elif highest <=100:
					while j < round_up/10:
						self.bar_chart.create_line(20,tm+(j*graph_hight*10/round_up),lm,tm+(j*graph_hight*10/round_up))
						self.bar_chart.create_text(10,tm+(j*graph_hight*10/round_up), anchor= SW, text= str(round_up-fact))
						j +=1
						fact +=10
				else: 
					while j < round_up/50:
						self.bar_chart.create_line(20,tm+(j*graph_hight*50/round_up),lm,tm+(j*graph_hight*50/round_up))
						self.bar_chart.create_text(10,tm+(j*graph_hight*50/round_up), anchor = SW, text=str(round_up-fact))
						j+=1
						fact+=50


				"""A histogram indicating the number of words of a certain level"""
				data =(nr_wordlev(lexiconX, dictionary))	
				ct=data['counters']
				lv=data['levels']
				self.histo.delete(ALL)
				self.in_histo()
				count = len(ct)
				highest = max(ct)
				round_up = int(math.ceil(highest/10.0))*10
				graph_height= 190
				graph_width= 360	
				#c_height= 260
				#c_width= graph_width+50
				bar= 60	

				lm= 30
				tm= 40
				bl= 3

				for x,y in enumerate(ct):		#Here the length of the bars is indicated
	 				x0 = x*(graph_width/count)+lm+bl
	 				x1 = x0 + bar
	 				y0 = (graph_hight-(graph_hight*y/round_up))+tm		
	 				y1 = graph_hight+tm
	 				
	 				self.histo.create_rectangle(x0,y0,x1,y1, fill='green')
	 				self.histo.create_text(x0+20 , y0, anchor=SW, text=str(y))

				for a,b in enumerate(lv):			#Values prinnted on the x-axis
	 				self.histo.create_line(bar*a+(bar/2)+lm+bl,graph_height+tm+5,bar*a+(bar/2)+lm+bl,graph_height+tm)
	 				self.histo.create_text(bar*a+(bar/2)+lm+bl,graph_height+tm+20, anchor=SW, text=str(b))
				j=0
				fact=0
				if highest <=10:
					while j <=10:            # Values printed on the y-axis
	 					self.histo.create_line(20,tm+(j*graph_height/round_up),lm,tm+(j*graph_height/round_up))
	 					self.histo.create_text(10,tm+(j*graph_height/round_up), anchor= SW, text= str(round_up-fact))
	 					j +=1
	 					fact +=1
				elif highest <=100:
					while j <(round_up/10):            # Values printed on the y-axis
						self.histo.create_line(20,tm+(j*graph_height*10/round_up),lm,tm+(j*graph_height*10/round_up))
						self.histo.create_text(10,tm+(j*graph_height*10/round_up), anchor= SW, text= str(round_up-fact))
						j +=1
						fact +=10
				else:
					while j <(round_up/25):            # Values printed on the y-axis
						self.histo.create_line(20,tm+(j*graph_height*25/round_up),lm,tm+(j*graph_height*25/round_up))
						self.histo.create_text(10,tm+(j*graph_height*25/round_up), anchor= SW, text= str(round_up-fact))
						j +=1
						fact +=25				
				"""Giving a colour to the words that are not recognized"""
				unknowns = (search_unknown(filename, dictionary))
				print (unknowns)
				if unknowns: 
					tkinter.messagebox.showinfo("Information", "Easy Text doesn't recognize the following words, please check their spelling!")
				pos = '1.0'
				for word in unknowns:
	 				while True: 
	 					idx = self.input.search(word,pos,END)
	 					if not idx:
	 						break
	 					pos = '{}+{}c'.format(idx,len(word))
	 					self.input.tag_add(word, idx, pos)
	 					self.input.tag_config(word, background = 'orange')	
				
	def simply(self):
		"""Temporal function to fill the textbox that is going to fill the simplified text + error boxes when the textbox is empty or doesn't contain punctuation marks"""
		self.simple.configure(state='normal') # open witing in box
		content= self.input.get(1.0,'end-1c')
		if not content:
			tkinter.messagebox.showinfo("Input Error", "There is no text to be analysed")
		elif not content.replace('?'or'!', '.').endswith('.'):
			tkinter.messagebox.showinfo("Input Eror", "Lack of punctuation marks: \n Your sentences need to contain: . , ? , !")
		else:
			words = list(load_input(content))
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
				sentencesX= load_input2(content)
				levelZ= sen_lev(sentencesX)
				levelY = (text_level(levelX, levelZ))
				if levelY == 'B1':
					tkinter.messagebox.showinfo("Error", "The level of the text is lower than the B1 level!")
				elif levelY == 'A2':
					tkinter.messagebox.showinfo("Error", "The level of the text is lower than the B1 level!")
				elif levelY == 'A1':
					tkinter.messagebox.showinfo("Error", "The level of the text is lower than the B1 level!")					
				else:
					message = simply_sen(content)

		self.simple.delete(1.0, END) # empty the text box before adding new information
		self.simple.insert(1.0, message) # fill the textbox with the answer
		self.simple.configure(state='disabled') # close writing in box again

	def clear(self):
		"""Function to simultaneously clear all the text windows and graphs"""
		self.info.configure(state='normal')
		self.simple.configure(state='normal')

		self.input.delete(0.0, 'end')
		self.info.delete(0.0, 'end')
		self.simple.delete(0.0,'end')

		self.gauge.delete(ALL)
		self.in_gauge()
		self.bar_chart.delete(ALL)
		self.in_bar_chart()
		self.histo.delete(ALL)
		self.in_histo()

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
root.geometry('900x650') #modify root window
root.iconbitmap('ET_Logo.ico') # changes the python icon into our own logo
app = Application(root)
root.mainloop()