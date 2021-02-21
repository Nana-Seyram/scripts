import string, secrets, csv, pyperclip
from hashlib import sha256
warning = u"\u26A0"
alphabets = string.ascii_letters + string.digits + string.punctuation

while True:
	password = "".join(secrets.choice(alphabets) for i in range(13))
	if(any(p.islower() for p in password)
		and any(p.isupper() for p in password)
		and sum(p.isdigit() for p in password) >= 3):
		break

pass_hash = sha256(password.encode('utf-8')).hexdigest()

app = input('what app would you need a password for? ')

with open('records.csv', 'a+', newline = '') as file_obj:
	fieldnames = ['app', 'password']
	thewriter = csv.DictWriter(file_obj, fieldnames = fieldnames)

	thewriter.writerow({'app': app, 'password': pass_hash})

pyperclip.copy(password)
print(f'password: {password}')
print(f'{warning}Your password has been copied to clipboard{warning}')