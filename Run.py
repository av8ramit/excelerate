import sys
sys.path.append('Library')

from Values import *
from Console import *

c = Console()
#print c.user
#print c.state
#c.process_commands("print_report")

while True:
	line = raw_input(PROMPT)
	if line == "exit":
		break
	c.process_commands(line)