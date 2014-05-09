import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages":['Library', 'Graphs'], 
					"includes":["tkinter", "csv", "subprocess", "datetime", "shutil", "random",'Library','Graphs'],
					"include_files": ['GUI','HTML','Users','Tests','Library','E.icns', 'Graphs'],
					}

base = None
if sys.platform == "win32":
	base = "Win32GUI"

setup( name = "Excelerate",
	version = "2.0",
	description = "Excelerate Test Preparation",
	options = {"build.exe": build_exe_options},
	executables = [Executable("GUI.py", base=base)])