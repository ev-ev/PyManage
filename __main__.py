import os,sys,threading

def search(key,dir):
	for x in os.listdir(dir):
		if key in x:
			print '[!]Hit '+x
	
help='PYSPLOIT help\nCommands:\nattack - execute an attack module (attack [attack])\nsearch - search for attacks (search [type] [keyword])'
path='./attacks/'
try:
	print '[!]Welcome to pysploit'
	while True:
		command=raw_input('<<<')
		if command=='help':
			print(help)
		elif command[:6]=='attack':
			args=command[7:]
			try:
				print path+args
				dir=os.listdir(path+args)		
			except OSError:
				print '[!]No such attack'
				continue
			if args[:6]=='python':
				print '[*]Starting attack module...'
				os.system('python '+path+args)
				print '[1337]Attack module executed'
				continue
		elif command[:6]=='search':
			args=command[7:]
			keys=args.split(' ')
			try:
				search(keys[1],'attacks/'+keys[0])
				print('[*]Done')
			except:
				print('[*]Are you entered the correct arguments?')
		elif command=='':
			continue
		else:
			print(help)
			
except Exception as e:
	print str(e)
