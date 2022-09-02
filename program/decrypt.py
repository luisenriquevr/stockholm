from cryptography.fernet import Fernet
import os
from sys import argv
from platform import system
from pathlib import Path

def key_charge():
	return open('key.key', 'rb').read()

def decrypt(items, key, silent):
	f = Fernet(key)
	for item in items:
		if item.endswith('.ft') == True and item.count('.') == 2:
			with open(item, 'rb') as file:
				encrypted_data = file.read()
				file.close()
			decrypted_data = f.decrypt(encrypted_data)
			
			with open(item, 'wb') as file:
				file.write(decrypted_data)
				file.close()
			os.rename(item, item[0:-3])
			if silent == False:
				print(Path(item).stem + ' decrypted')

if __name__ == '__main__':
	silent = False
	if system() == "Linux":
		if len(argv) == 3 and (argv[1] == "-reverse" or argv[1] == "-r"):
			reverse = True
		else:
			reverse = False
		if len(argv) > 2 and reverse == False:
			print('Too arguments')
		else:
			if len(argv) == 2 and (argv[1] == "-silent" or argv[1] == "-s") and reverse == False:
				silent = True
			if len(argv) == 2 and (argv[1] == "-help" or argv[1] == "-h") and reverse == False:
				print('OPTIONAL FLAGS:\n -v or -version to see actual version\n -s or -silent to silent mode')
			elif len(argv) == 2 and (argv[1] == "-version" or argv[1] == "-v") and reverse == False:
				print('Version: 1.0.0')
			elif len(argv) == 2 and silent == False:
				print('Too many arguments')
			else:
				if os.getcwd().endswith('home'):
					path_to_encrypt = os.getcwd() + '/files'
					if os.path.exists(path_to_encrypt + '/' + 'msg.txt'):
						os.remove(path_to_encrypt + '/' + 'msg.txt')
					items = os.listdir(path_to_encrypt)
					full_path = [path_to_encrypt + '/' + item for item in items]

					key = key_charge()

					if os.path.exists('key.key') == True:
						os.remove('key.key')

					decrypt(full_path, key, silent)
				else:
					print("You are not in the home folder")
	else:
		print("Your system is not Linux")
