import os
import time

def download_video_youtube(url):
	try:
		print ("Downloading " + url)
		if url.find("youtube") is not -1:
			os.system("youtube-dl " + url)
		else:
			os.system("wget -c \"" + url + "\"")
		return 1
	except KeyboardInterrupt:
		return 0

def main():
	i=0
	try:
		with open("list.txt", 'r') as readfile:
			for link in readfile:
				url = link
				if download_video_youtube(url) == 0:
					raise KeyboardInterrupt
				else:
					i+=1
	except KeyboardInterrupt:
		print ("Thing")
		lines = open('list.txt').readlines()
		open('newfile.txt', 'w').writelines(lines[i:])
		os.remove('list.txt')
		os.rename('newfile.txt', 'list.txt')

	lines = open('list.txt').readlines()
	open('newfile.txt', 'w').writelines(lines[i:])
	os.remove('list.txt')
	os.rename('newfile.txt', 'list.txt')

if __name__ == '__main__':
	main()
