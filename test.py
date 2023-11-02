import re

s = input("Enter a string: ")

pattern = r"[a-zA-Z]+"

match = re.search(pattern, s)

if match:
  print(match.group())

# Prints "abc"