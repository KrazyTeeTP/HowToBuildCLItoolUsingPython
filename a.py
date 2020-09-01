import argparse

parser = argparse.ArgumentParser(
	prog='nameOfTheProgramHere',
	description='''
	#This is going to be our desc...
	''',
	epilog='copyright (c) 2020 KrazyTeeTP'
	)

parser.add_argument('-p', '--prt', default='[DEFAULT]', help='this is the help of this add_argument')
args = parser.parse_args()

if args.prt != '[DEFAULT]':
	print(args.prt + ': has been printed...')
else:
	print(args.prt + ': DEFAULT')