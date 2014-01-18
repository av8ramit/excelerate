import sys
sys.path.append('Library')

from Values import *
from Console import *

c = Console()
#print c.user
#print c.state
c.process_commands("load_user Neel")
c.process_commands("reset")
c.process_commands("grade 1760.csv")
c.process_commands("grade 1860.csv")
c.process_commands("grade 1870.csv")
c.process_commands("grade 1760.csv")
c.process_commands("grade 1860.csv")
c.process_commands("grade 1870.csv")
c.process_commands("grade 1860.csv")
c.process_commands("grade 1870.csv")
c.process_commands("grade 1930.csv")
c.process_commands("grade 1930.csv")
c.process_commands("grade 1930.csv")
c.process_commands("grade 1990.csv")
c.process_commands("grade 2110.csv")
c.process_commands("grade 2170.csv")
c.process_commands("grade 2280.csv")
c.process_commands("grade 2400.csv")
c.process_commands("grade 2280.csv")
c.process_commands("grade 2370.csv")
c.process_commands("grade 2400.csv")
c.process_commands("grade 2370.csv")
c.process_commands("grade 2370.csv")
c.process_commands("save")
c.process_commands("simple_report")
#c.process_commands("")
#c.process_commands("list_tests")

while True:
	line = raw_input(PROMPT)
	if line == "exit":
		break
	c.process_commands(line)