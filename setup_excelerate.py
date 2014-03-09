"""
Usage: Python launch package application toolset

"""
from setuptools import setup
APP = ['GUI.py']
DATA_FILES = [('', ['Users']), ('', ['Tests']), ('', ['Graphs']), ('', ['HTML']), ('', ['Library'], ), ('', ['GUI'], )]
OPTIONS = {
}

setup(
	app = APP,
	data_files = DATA_FILES,
	setup_requires = ['py2app'],

)