# -*- coding: utf-8 -*-
import sys
from doc_access import session, get_cols_from_doc 
from acentos import cambia_caracteres_utf

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
	print 'Porfavor instala gexf http://pythonhosted.org/pygexf/users.html/'
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

# Se obtiene las celdas del archivo con los nodos
cols_sna_nodos = get_cols_from_doc('https://docs.google.com/spreadsheet/ccc?key=0Am6c--_scDIGdDZZbmJycXYtZ21WckVUYUFseW5wZXc&usp=drive_web#gid=0')

# Se obtiene las celdas del archivo con los links
cols_sna_links = get_cols_from_doc('https://docs.google.com/spreadsheet/ccc?key=0Am6c--_scDIGdC1VU01ZNGNCeUR2RHdqMGVxMkdINVE&usp=drive_web#gid=0')

# Se crea el grafo con gexf
gexf = gx("Elba Esther Gordillo", "Analisis de la red social politica en Mexico")
graph = gexf.addGraph("directed","static", "Red Social Politica en Mexico")

n = 1
e = 0
# Se crean los nodos con gexf
for node in cols_sna_nodos[1]:
	try:
		node = node.encode("utf-8")
		if isinstance(node, unicode):
			decoded = node.decode("utf-8")
			decoded = cambia_caracteres_utf(decoded)
			print node, "es utf"
		else:
			decoded = node
		if decoded not in graph._nodes and decoded != 'Nombre completo del actor político':
			graph.addNode(n, decoded)
			# print "Se creo el nodo %s" % node.decode("utf-8")
			# print n
			n+=1
		#print node
	except:
		#err = cambia_caracteres_utf(node.decode("utf-8"))
		print "Error %s" % sys.exc_info()[0] 
		print "en el nodo %s" % node
		e+=1
print e
	
# for link in cols_sna_links:
# 	try:
# 		graph.addLink(n, node.decode("utf-8"))
# 		print node
# 	except:
# 		print "Error %s" % node
# 	n+=1

output_file = open("red_politica_mex.gexf", "w")

gexf.write(output_file)
