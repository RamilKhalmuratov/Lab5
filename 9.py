import re
def capital_words_spaces(str1):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)

print(capital_words_spaces("VDoteObnovaVishla"))
print(capital_words_spaces("VDoteObnova"))
print(capital_words_spaces("VDote"))
print(capital_words_spaces("V"))