import re
text = "VDoteObnovaVishla"
print(re.findall('[A-Z][^A-Z]*', text))