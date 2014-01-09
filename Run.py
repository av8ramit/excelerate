import sys
sys.path.append('Library')

from Values import *
from Console import *

c = Console()
#print c.user
#print c.state
c.process_commands("load_user Nicole")
c.process_commands("simple_report")
c.process_commands("advanced_report")

while False:
	line = raw_input(PROMPT)
	if line == "exit":
		break
	c.process_commands(line)