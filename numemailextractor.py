# Program extracts phone number and email address from clipboard.
import pyperclip, re

# representing the phone number regex

PhoneNumRegex = re.compile(r'''((\d{3}|\(\d{3}\)) # area code
	((\s)+|-|\.) # separator
	((\()?\d{3}(\))?) # next three digits
	((\s)+|-|\.) # separator
	((\()?\d{4}(\))?) # next four digits
	(\s*(ext|x|ext.)\s*(\d{2,5}))?)
	''', re.VERBOSE)

# test_cases
#num1 = '(872)-(985)-(3026)'
#num2 = '872_985_3026 ext 555'
#num3 = '872.985.3026 x 4005'
#num4 = '(872) (985) (3026) 001'
#num5 = '(872).(985).(3026) 0'

#num = num1 + " " + num2 + " " + num3 + " " + num4 + " " + num5

#test1 = PhoneNumRegex.search(num1)
#test2 = PhoneNumRegex.search(num2)
#test3 = PhoneNumRegex.search(num3)
#test4 = PhoneNumRegex.search(num4)
#test5 = PhoneNumRegex.search(num5)

#test = PhoneNumRegex.findall(num)

#print(test1.group())
#print(test2.group())
#print(test3.group())
#print(test4.group())
#print(test5.group())

#print(test)

EmailRegex = re.compile(r'''((\w)+(\d)*
	\S([a-zA-Z]\.)?
	(\w)+\.(\w)+)''',re.I|re.VERBOSE)

#te1 = 'forsonkelvin84@gmail.com'

#te2 = 'kelvinforson2023@u.northwestern.edu'

#em1 = EmailRegex.search(te1)

#em2 = EmailRegex.search(te2)

#print(em1.group())

#print(em2.group())

# Find matches in clipboard text.

text = str(pyperclip.paste())

matches = []

for groups in PhoneNumRegex.findall(text):
	phoneNum = '-'.join([groups[1],groups[3],groups[5]])
	if groups[8] != '':
		phoneNum += ' X' + groups[8]
	matches.append(phoneNum)
for groups in EmailRegex.findall(text):
	matches.append(groups[0])
if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print('Copied to clipboard:')
	print('\n'.join(matches))
else:
	print('No phone numbers or email addresses found.')

