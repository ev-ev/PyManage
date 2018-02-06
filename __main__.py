import os,sys,threading

def search(key,dir):
	for x in os.listdir(dir):
		if key in x:
			print '[!]Hit '+x
try:
	file=open('settings.spagett','r')
	data=file.read()
	file.close()
	data=data.split('\n')
	python2=data[0]
	python3=data[1]
except Exception as e:
	python2=raw_input('[*]Command to invoke/link to python 2 (python for linux users):')
	python3=raw_input('[*]Command to invoke/link to python 3 (python3 for linux users):')
	file=open('settings.spagett','w')
	file.write(python2+'\n'+python3)
	file.close()
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
			if args[:7]=='python2':
				print '[*]Starting module...'
				try:
					os.system(python2+' '+path+args)
				except KeyboardInterrupt:
					print '[*]Module stopping...'
				except Exception as e:
					print '[!]'+str(e)
				print '[1337]Module executed'
				continue
			elif args[:7]=='python3':
				print '[*]Starting module...'
				try:
					os.system(python3+' '+path+args)
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
