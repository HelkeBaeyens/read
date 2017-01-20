import cx_Freeze
import sys
import os

import os

os.environ['TCL_LIBRARY'] = "C:\\Users\\kimbe\\Anaconda3\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\kimbe\\Anaconda3\\tcl\\tk8.6"

base= None
if sys.platform == 'win32':
	base='Win32GUI'

executables= [cx_Freeze.Executable('interface.py', base=base, icon = 'ET_Logo.ico')]

cx_Freeze.setup(
	name="Easy_Text",
	options = {"build_exe":{"packages":["tkinter"], "include_files":["ET_Logo.ico", (r"C:\\Users\\kimbe\\Anaconda3\\tcl\\tcl8.6", "tcl"), (r"C:\\Users\\kimbe\\Anaconda3\\tcl\\tk8.6", "tk")]}},
	version="1.1",
	description = "Easy Text: a program to compute the level of texts and simplify them when necessary",
	author = 'Helke Baeyens and Kimberly Moors',
	executables = executables
	)