import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())