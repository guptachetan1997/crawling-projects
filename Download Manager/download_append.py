import sys

def main():
	try:
		url =  str(sys.argv[1]) + '\n'
		with open('list.txt', 'a') as file:
			file.write(url) 
	except:
		print("Print some error occured")
if __name__ == '__main__':
	main()
