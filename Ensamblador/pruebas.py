import re

with open("./values.txt", "r") as file:
    txt = file.read()
pattern = re.compile(r"[01]+")
match = re.findall(pattern, txt)
print(match)
