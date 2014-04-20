"""
Usage: Python launch package application toolset

"""
from setuptools import setup
APP = ['GUI.py']
DATA_FILES = [('', ['Users']), ('', ['Tests']), ('', ['Graphs']), ('', ['HTML']), ('', ['Library'], ), ('', ['GUI'], ), ('', ['Documents'], )]
OPTIONS = {'iconfile':'Documents/E.icns',
}

setup(
	app = APP,
	data_files = DATA_FILES,
	options = {'py2app': OPTIONS},
	setup_requires = ['py2app'],

)