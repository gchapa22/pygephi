from doc_access import docu 
print 'Bienvenido!'
print 'Verificando librerias...'

error_lib = False

try:
	import gspread
except:
	print 'Porfavor instala gspread https://github.com/burnash/gspread'
	error_lib = True

try:
	import networkx
except:
	print 'Porfavor instala networkx http://networkx.github.io/'
	error_lib = True

if error_lib:
	exit()

print 'Para acceder por favor escribe tus datos.'

cols_sna_links = docu()

cols_sna_nodos = docu()

cols_sna_nodos
