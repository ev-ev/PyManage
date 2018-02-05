import os,sys,threading

def search(key,dir):
	for x in os.listdir(dir):
		if key in x:
			print '[!]Hit '+x
python2=raw_input('[*]Command to invoke/link to python (python for linux users):')
help='PYMANAGE help\nCommands:\nuse - execute a module (use [module])\nsearch - search for modules (search [type] [keyword])'
path='./modules/'
try:
	print '[!]Welcome to pymanage'
	while True:
		command=raw_input('<<<')
		if command=='help':
			print(help)
		elif command[:3]=='use':
			args=command[4:]
			try:
				dir=os.listdir(path+args)		
			except OSError:
				print '[!]No such module'
				continue
			if args[:6]=='python':
				print '[*]Starting module...'
				try:
					os.system(python2+' '+path+args)
				except KeyboardInterrupt:
					print '[*]Module stopping...'
				except Exception as e:
					print '[!]'+str(e)
				print '[1337]Module executed'
				continue
		elif command[:6]=='search':
			args=command[7:]
			keys=args.split(' ')
			try:
				search(keys[1],'modules/'+keys[0])
				print('[*]Done')
			except:
				print('[*]Are you entered the correct arguments?')
		elif command=='':
			continue
		else:
			print(help)
			
except Exception as e:
	print str(e)
