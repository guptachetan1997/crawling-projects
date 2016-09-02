import subprocess
import os

def change_metadata():
	for thing in os.listdir():
		if os.path.isfile(thing) and thing[thing.rfind('.'):] != '.py':
			file_name = thing
			ft = thing.rfind('Fe')
			dash = thing.rfind('-')
			if ft == -1:
				ft = 10000000
			index = min(dash, ft)
			artist = thing[:index]
			song_name = thing[dash+1:thing.rfind('.')]
			print(artist, song_name)
			subprocess.call(["eyeD3", "-a", artist, "-t", song_name, thing])
			

if __name__ == '__main__':
	change_metadata()
