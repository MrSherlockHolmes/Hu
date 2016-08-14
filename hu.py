# imports

import re

# code

input = raw_input("Scenario?")
input = re.sub(r"cat\S*", "", input).split(" ")

# cat\S*

print(input)
