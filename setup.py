import sys, os
from cx_Freeze import setup, Executable

def find_data_file(filename):
    if getattr(sys, 'frozen', False):
        # The application is frozen
        datadir = os.path.dirname(sys.executable)
    else:
        # The application is not frozen
        # Change this bit to match where you store your data files:
        datadir = os.path.dirname(__file__)

    return os.path.join(datadir, filename)

lib = find_data_file("Library")

build_exe_options = {"packages":['Libary', 'Graphs'], 
					"includes":["tkinter", "csv", "subprocess", "datetime", "shutil", "random", lib, 'Graphs'],
					"include_files": ['GUI','HTML','Users','Tests', 'Library','E.icns', 'Graphs'],
					}

base = None
if sys.platform == "win32":
	base = "Win32GUI"

setup( name = "Excelerate",
	version = "2.0",
	description = "Excelerate Test Preparation",
	options = {"build.exe": build_exe_options},
	executables = [Executable("GUI.py", base=base)])