import re

a = "The agent phone number is 281-674-5418"
# pattern = 'phone number'
# match=re.search(pattern,a)
# print(match)
#
# # It gives the index location of span
# print(match.span())
#
# #Start position of string
# print(match.start())
#
# #Group together
# print(match.group())
#
# for match in re.finditer('phone',a):
#     print(match.group())

# match = re.search(r'\d{3}-\d{3}-\d{4}', a)
# print(match.group())

pattern=re.compile(r'(\d{3})-(\d{3})-(\d{4})')
match=re.search(pattern,a)
print(match.group(1))
