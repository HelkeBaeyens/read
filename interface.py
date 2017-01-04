from tkinter import *


class Application(Frame):

	def __init__(self, master):
		Frame.__init__(self,master)
		self.pack()
		self.create_widgets()


	def create_widgets(self):
		self.instr_frame = Frame(self)
		self.instr_frame.pack(side="top", expand = 0, fill = X)

		self.instruction = Label (self.instr_frame,width = '50', text='Enter your text here:')
		self.instruction.pack(padx = 2, pady=2, side=LEFT) #put the lable to a certain side)
		
		self.level = Label(self.instr_frame, width = '50', text='Information about the text:')
		self.level.pack(padx=2, pady=2, side=RIGHT)


		self.text_frame = Frame(self)
		self.text_frame.pack(side='top', expand = 0, fill = X)

		self.input = Text(self.text_frame, width="50", height="5", wrap=WORD)
		scroll_input = Scrollbar(self.text_frame)
		scroll_input['command'] = self.input.yview
		self.input['yscrollcommand']= scroll_input.set
		self.input.pack(side=LEFT, expand =1, fill=None)
		scroll_input.pack(side=LEFT, expand=1, fill=Y)

		self.info = Text(self.text_frame, width = "50", height ="5", wrap = WORD)
		scroll_info = Scrollbar(self.text_frame)
		scroll_info['command'] = self.input.yview
		self.info['yscrollcommand'] = scroll_info.set
		self.info.pack(side='left',expand=0,fill=None)
		self.info.configure(state ='disabled') # make sure noone can write in second box
		scroll_info.pack(side=LEFT, expand=1, fill=Y)


		self.button_frame = Frame(self)
		self.button_frame.pack(side='top', expand = 0, fill = X)

		self.submit_button = Button(self.button_frame, text = "Submit", command = self.reveal)
		self.submit_button.pack(padx=2, pady=2, side=LEFT)

		self.simplify_button = Button(self.button_frame, text= "Make easier", command= self.reveal)
		self.simplify_button.pack(padx=2, pady=2, side=LEFT)

		
		self.simplify_frame = Frame(self)
		self.simplify_frame.pack(side='top', expand=0, fill=X)

		self.simplify = Label(self.simplify_frame, width = '50', text='Simplification of the text:')
		self.simplify.pack(padx=2, pady=2, side=LEFT)


		self.simple_frame = Frame(self)
		self.simple_frame.pack(side='left', expand= 0, fill = X)

		self.simple = Text(self.simple_frame, width = "50", height ="5", wrap = WORD)
		scroll_simple = Scrollbar(self.simple_frame)
		scroll_simple['command'] = self.simple.yview
		self.simple['yscrollcommand'] = scroll_simple.set
		self.simple.pack(side='left',expand=0,fill=None)
		self.simple.configure(state ='disabled') # make sure noone can write in second box
		scroll_simple.pack(side=LEFT, expand=1, fill=Y)
 # make sure noone can write in second box
#	def retrieve_input():
#		input = self.test.get("1.0",'end-1C')

	def reveal(self): # Tekst verbonden aan knop 'test ' --> wat getoond word
		self.info.configure(state ='normal') # open witing in box
		content = self.input.get(1.0,"end-1c")

		if content == "Hallo":
			message = "YES"
		else:
			message = "Shit"
		self.info.delete(0.0, END) # programma leeg maken voor er weer toegevoegd word
		self.info.insert(0.0, message) #enter your answer
		self.info.configure(state ='disabled') # close writing in box
 
"""make buttons"""
#button1 = Button(app, text = "Word level") 
#button1.grid()



#create the windoww + give title
#modify root window
#give the application a name
#kick off the event loop

"""Without nothing shows """
root = Tk()
root.title('Test')
root.geometry('900x200')
app = Application(root)
root.mainloop()