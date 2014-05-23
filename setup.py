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
e = find_data_file("E.gif")

packages = [lib, 'Graphs']
includes = ["tkinter", "csv", "subprocess", "datetime", "shutil", "random", "Graphs", "Library"]
includefiles = ['./GUI','HTML','Users','Tests', lib,'E.icns', 'Graphs','*.py', '*.gif']
zip_includes = [e,'./GUI']
icon = ["E.icns"]

build_exe_options = {"packages": packages, 
		    "includes": includes,
		    "include_files": includefiles,
                     "zip_includes": zip_includes,
                     "icon": icon,
					}

base = None
exe = None
if sys.platform == "win32":
	exe = Executable(
		script="GUI.py",
		initScript = None,
		base = "Win32GUI",
		targetDir = r"build",
		targetName = "GUI.exe",
		compress = True,
		copyDependentFiles = True,
		appendScriptToExe = False,
		appendScriptToLibrary = False,
		icon = None
	)
	base = "Win32GUI"

setup( name = "Excelerate",
	version = "2.0",
	description = "Excelerate Test Preparation",
	options = {"build.exe": build_exe_options},
	#executables = [Executable("GUI.py", base=base)]
	executables = [exe]
	)
