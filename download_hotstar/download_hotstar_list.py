import os
import sys

def download(url):
	print (url)
	os.system("youtube-dl " + url)

def main():
	file_name =  str(sys.argv[1])
	try:
		with open(file_name) as file:
			for line in file:
				url = line[:len(line)-1]
				download(url)
	except IOError:
		print ("File does not exist.")
	

if __name__ == '__main__':
	main()
