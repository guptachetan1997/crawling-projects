import pandas as pd

print('Enter batch name : ')
batch = input()

with open(batch+'.txt', 'rb') as file:
	lines = file.read().splitlines()
	length = len(lines) + 1
	df = pd.DataFrame()
	df['First Name'] = 4
	fnames = ['Target'+str(x) for x in range(1,length)]
	df['First Name'] = pd.Series(fnames)
	df['Last Name'] = 4
	lnames = [batch for x in range(1,length)]
	df['Last Name'] = pd.Series(lnames)
	nums = [line.decode('utf8') for line in lines]
	df['Home Phone'] = 4
	df['Home Phone'] = pd.Series(nums)
	df['Display Name'] = df['First Name'] + df['Last Name']
	print(df)
	df.to_csv(batch + '.csv', index=False)
