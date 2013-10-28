# -*- coding: utf-8 -*-
from doc_access import session, get_cols_from_doc 

# Mensaje de Bienvenida
print 'Bienvenido!'
print 'Verificando librerias...'

# Variable que guarda si hay un error con las librerias
error_lib = False

# Se intenta exportar la libreria gspread
# si marca error se imprime un mensaje y 
# el valor de error_lib cambia a verdadero
try:
	import gspread as g
except:
	print 'Porfavor instala gspread https://github.com/burnash/gspread'
	error_lib = True

# Se intenta exportar la libreria gexf
# si marca error se imprime un mensaje y 
# el valor de error_lib cambia a verdadero
try:
	from gexf import Gexf as gx
except:
	print 'Porfavor instala gefx http://pythonhosted.org/pygexf/users.html/'
	error_lib = True

# Si error_lib es verdadero entonces 
# el script termina
if error_lib:
	exit()

# Mensaje de peticion de datos
print 'Para acceder por favor escribe tus datos.'

# Se manda llamar la funcion session()
# la cual crea la sesion en Google Docs
session()

cols_sna_nodos = get_cols_from_doc('https://docs.google.com/spreadsheet/ccc?key=0Am6c--_scDIGdDZZbmJycXYtZ21WckVUYUFseW5wZXc&usp=drive_web#gid=0')

cols_sna_links = get_cols_from_doc('https://docs.google.com/spreadsheet/ccc?key=0Am6c--_scDIGdC1VU01ZNGNCeUR2RHdqMGVxMkdINVE&usp=drive_web#gid=0')

print cols_sna_nodos[1][1]

# Se crea el grafo con gexf
gexf = gx("Elba Esther Gordillo", "Analisis de la red social politica en Mexico")
graph = gexf.addGraph("directed","static", "Red Social Politica en Mexico")

n = 1
# Se crean los nodos con gexf
for node in cols_sna_nodos[1]:
	try:
		graph.addNode(n, node)
		print node
	except:
		print "Error %s" % node
	n+=1

output_file = open("red_politica_mex.gexf", "w")

gexf.write(output_file)
