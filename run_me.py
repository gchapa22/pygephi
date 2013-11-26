# -*- coding: utf-8 -*-
import sys
from doc_access import session, get_cols_from_doc 
from acentos import cambia_caracteres_utf, quita_letras

online = True

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

if online:
	# Mensaje de peticion de datos
	print 'Para acceder por favor escribe tus datos.'

	# Se manda llamar la funcion session()
	# la cual crea la sesion en Google Docs
	session()

	# Se obtiene las celdas del archivo con los nodos
	cols_sna_nodos = get_cols_from_doc('https://docs.google.com/spreadsheet/ccc?key=0Am6c--_scDIGdDZZbmJycXYtZ21WckVUYUFseW5wZXc&usp=drive_web#gid=0')

	# Se obtiene las celdas del archivo con los links
	cols_sna_links = get_cols_from_doc('https://docs.google.com/spreadsheet/ccc?key=0Am6c--_scDIGdC1VU01ZNGNCeUR2RHdqMGVxMkdINVE&usp=drive_web#gid=0')
else:
	cols_sna_nodos = ['','']
	cols_sna_nodos[1] = [u'Nombre completo del actor pol\xedtico', 'Manuel Bartlett', 'Jaime Torres Bodet', 'Manlio Fabio Beltrones', 'Carlos Salinas de Gortari', u'Manuel Camacho Sol\xeds', 'Patricia Pedrero Iduarte', 'Roberto del Cueto', 'Ernesto Zedillo Ponce de Leon', 'Romero Deschamps', u'Roberto Campa Cifri\xe1n', 'Manuel Camacho', 'Eduardo Bours', 'Vicente Fox', 'Madrazo', 'Emilio Chuayffet', 'Elba Esther Gordillo', u'Jorge Casta\xf1eda Gutman', 'Miguel Angel Yunes', 'Elba Esther Gordillo', u'Roberto Campa Cifri\xe1n', 'Roberto Madrazo', 'Miguel Angel Yunes', u'Tom\xe1s Ruiz ', 'Miguel Angel Yunes', u'Tom\xe1s Ruiz ', 'Joel Ayala ', 'Emilio Chuayffet', 'Roberto Madrazo', 'Ulises Ruiz', u'Jos\xe9 Murat', 'Roberto Madrazo', 'Ulises Ruiz', 'Roberto Madrazo', 'Presidente Fox', u'Di\xf3doro Carrasco', 'Gloria Trevi', u'Enrique Pe\xf1a Nieto', 'Presidente Fox', u' Jorge G. Casta\xf1eda', u'Antonio Manr\xedquez Guluarte', 'Beatriz Paredes', 'Luis Armando Reynoso Femat', u'\xd3scar Gonz\xe1lez', 'Francisco Rojas ', 'Madrazo', u' Miguel \xc1ngel Jim\xe9nez ', 'Carlos Madrazo', u'Rafael Ochoa Guzm\xe1n', 'Carlos Jonguitud Barrios', ' Emilio Chuayffet', 'Diego Armando Maradona', 'Eduardo Bours', 'Everardo Moreno', u'Natividad Gonz\xe1lez Par\xe1s', u'N\xe9stor Kirchner', 'Vicente Fox', u'V\xedctor Gonz\xe1lez Torres', 'Roberto Madrazo Pintado', 'Alfredo Rivera Flores', u'Gerardo Sosa Castel\xe1n', u'Miguel \xc1ngel Granados Chapa', 'Arturo Montiel', 'Enrique Jackson', u'Enrique Mart\xednez', u'Miguel \xc1ngel Yunes', u'Tom\xe1s Ruiz', u'Felipe Calder\xf3n', u'Andr\xe9s Manuel L\xf3pez Obrador', u'Jorge Casta\xf1eda Gutman', 'Carlos Armando Biebrich', 'Carlos Salinas de Gortari', u'Gabino Cu\xe9 Monteagudo', 'Mariano Palacios Alcocer', 'Roberto Madrazo Pintado', 'Ulises Ruiz Ortiz', 'Juan Molinar Horcasitas', u'Andr\xe9s Manuel L\xf3pez Obrador', u'Miguel \xc1ngel Yunes', 'Miguel Angel Yunes', u'Miguel \xc1ngel Yunes', u'Nicol\xe1s Sarkozy', u'Germ\xe1n Mart\xednez', u'Josefina V\xe1zquez Moya', u'Felipe Calder\xf3n', u'Fernando Gonz\xe1lez', 'Miguel Angel Yunes', u'Ferm\xedn Trujillo Fuentes', u'Benjam\xedn Gonz\xe1lez Roar', u'Aureliano Pe\xf1a Lomel\xed', 'Wanda Sigrid Arzt Colunga', u'Mar\xeda Elena P\xe9rez-Ja\xe9n Zerme\xf1o', u'Andr\xe9s Manuel L\xf3pez Obrador', u'Manuel Camacho Sol\xeds', 'Aguirre Rivero', 'Carlos Slim', 'Gil Zuarth', 'Ernesto Cordero', 'Alonso Lujambio', 'Fernando Larrazabal', 'Zeferino Salgado', u'Jes\xfas Villalobos', u'Felipe Calder\xf3n', u'Josefina V\xe1zquez Moya', u'Miguel \xc1ngel Yunes', u'Enrique Pe\xf1a Nieto', u'Ernesto G\xe1ndara', u'Luis Ch\xe1vez Orozco']

# Se crea el grafo con gexf
gexf = gx("Elba Esther Gordillo", "Analisis de la red social politica en Mexico")
graph = gexf.addGraph("undirected","static", "Red Social Politica en Mexico")
graph.addNodeAttribute('fecha', '', 'date')
graph.addNodeAttribute('evento', '', 'string')
graph.addEdgeAttribute("fecha","","date") 

e = 0
dict_nodes ={}
# Se crean los nodos con gexf
# print cols_sna_nodos[1]
for (counter,coded) in enumerate(cols_sna_nodos[1]):
	decoded = coded
	decoded = cambia_caracteres_utf(decoded)
	att = cambia_caracteres_utf(cols_sna_nodos[3][counter])
	#print decoded
	try:
		if not any(x.label == decoded for x in graph._nodes.values()) and decoded != 'Nombre completo del actor politico':
			graph.addNode(counter, decoded)
			graph._nodes[counter].addAttribute(0,cols_sna_nodos[2][counter])
			graph._nodes[counter].addAttribute(1,att)
			dict_nodes[decoded]=counter
			print "dict_nodes[%s]=%d" % (decoded, dict_nodes[decoded])
		else:
			for (n,node) in enumerate(graph._nodes.values()):
				if node.label==decoded:
					graph._nodes[n].addAttribute(0,cols_sna_nodos[2][counter])
					graph._nodes[n].addAttribute(1,cols_sna_nodos[3][counter])
					break
	except:
		print "Error %s" % sys.exc_info()[1]

edge = 0

output_file = open("red_politica_mex.gexf", "w")

# gexf.write(output_file)


for (counter, coded) in enumerate(cols_sna_links[1]):
	if counter > 2:
		index1=-1
		index2=-1
		decoded = cambia_caracteres_utf(coded)
		decoded2 = cambia_caracteres_utf(cols_sna_links[2][counter])
		# for (n,node) in enumerate(graph._nodes.values()):
		# 	if node.label == decoded:
		# 		index1 = n
		# 		index1_label = node.label
		# 	elif node.label == decoded2:
		# 		index2 = n
		# 		index2_label = node.label
		# 	if index1 > -1 and index2 > -1:
		# 		break
		if decoded in dict_nodes and decoded2 in dict_nodes:
			# print "index1 %d" % index1
			# print "index2 %d" % index2
			# print "valor %d" % int(cols_sna_links[3][counter])
			try:
				# e=graph.addEdge(edge, str(quita_letras(index1)), str(quita_letras(index2)), weight=str(quita_letras(cambia_caracteres_utf(cols_sna_links[3][counter]))), label=str(cambia_caracteres_utf(cols_sna_links[5][counter])))
				e=graph.addEdge(edge, dict_nodes[decoded], dict_nodes[decoded2], weight=str(quita_letras(cambia_caracteres_utf(cols_sna_links[3][counter]))), label=str(cambia_caracteres_utf(cols_sna_links[5][counter])))
				e.addAttribute(0,quita_letras(str(cols_sna_links[4][counter])))
				edge+=1
			except:
				print "Errorcito %s" % sys.exc_info()[1] 

gexf.write(output_file)

# ,start="",end="",r="",g="",b="",spells=[],startopen=False,endopen=False) 

	# try:
	# 	decoded = coded.decode('utf-8')
	# 	decoded = cambia_caracteres_utf(decoded)
	# 	print decoded
	# 	if decoded not in graph._nodes and decoded != u'Nombre completo del actor pol\xedtico':
	# 		graph.addNode(n, decoded)
	# 		# print cols_sna_nodos[3][counter]
	# 		# graph.nodes[n].addAttribute(0,cols_sna_nodos[3][counter])
	# 		# print "Se creo el nodo %s" % node.decode("utf-8")
	# 		# print n
	# 		# print decoded
	# 		n+=1
	# 	#print node
	# except:
	# 	# err = cambia_caracteres_utf(node.decode("utf-8"))
	# 	# print "Error %s" % sys.exc_info()[0] 
	# 	# print "en el nodo %s" % coded
	# 	e+=1


# for link in cols_sna_links:
# 	try:
# 		graph.addEdge()
# 		n+=1
# 	except:
# 		print "Error %s" % node

