import re
def text_match(text):
        patterns = '^[a-z]+_[a-z]+$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("dirty_dirty"))
print(text_match("dirty_Dirty"))
print(text_match("Dirty_Dirty"))