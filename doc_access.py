import gspread as G
import getpass

print 'Bienvenido!'
print 'Para acceder por favor escribe tus datos.'

x = 1

while x == 1:
	usr = raw_input('gmail:')

	pwd = getpass.getpass('password:')

	try:
		gc = G.login(usr, pwd)
		x = 2
	except:
		print 'No se pudo acceder a tu cuenta.'
		wants = raw_input('Deseas intentar de nuevo (si/no)? ')
		if wants == 'si' or wants == 'Si' or wants == 'SI' or wants == 's':
			x == 1
		else:
			print 'Adios.'
			exit()

arch = raw_input('Nombre, llave o URL del archivo:')
try:
	print 'Accediendo al archivo %s...' % arch
	ss = gc.open(arch)
except:
	try:
		print 'Accediendo al archivo %s...' % arch
		ss = gc.open_by_key(arch).sheet1
	except:
		try:
			print 'Accediendo al archivo %s...' % arch
			ss = gc.open_by_url(arch).sheet1
		except:
			print 'No se pudo acceder a este archivo.'
			exit()

print ss.col_values(1)
