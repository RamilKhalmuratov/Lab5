import re
def text_match(text):
        patterns = '[A-Z]+[a-z]+$'
        if re.search(patterns, text):
                return 'Found a match!'
        else:
                return('Not matched!')
print(text_match("aHAhaAa"))
print(text_match("AhAhAhAh"))
print(text_match("ahahahah"))