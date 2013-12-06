import networkx as nx
from gexf import Gexf as gx

gexf = None
graph = None
G = None
dict_nodes ={}

def new_file(who, title):
	global gexf
	gexf = gx(who, title)


def new_graph(title, is_directed, is_static):
	global G
	global graph
	G = nx.Graph()

	if is_directed:
		dire = 'directed'
	else:
		dire = 'undirected'
	if is_static:
		static = 'static'
	else:
		static = 'dinamic'

	graph = gexf.addGraph(dire, static, title)

def add_att_node(title,something, types):
	global graph
	graph.addNodeAttribute(title, something, types)

def add_att_edge(title,something, types):
	global graph
	graph.addEdgeAttribute(title, something, types) 

def node_exists(label):
	global graph
	return any(x.label == label for x in graph._nodes.values()) 

def add_node(id_num, label):
	global graph
	global G
	global dict_nodes
	G.add_node(label)
	graph.addNode(id_num, label)
	dict_nodes[label]=id_num

def set_node_att(node_num,id_num,data):
	global graph
	graph._nodes[node_num].addAttribute(id_num,data)

def set_edge_att(edge_num,att_id,data):
	global graph
	graph._edges[edge_num].addAttribute(att_id,data)

def add_edge(edge_num, node_1, node_2, w, label):
	global graph
	global G
	G.add_edge(node_1,node_2)
	graph.addEdge(edge_num, node_1, node_2, weight=w, label=label)

def save_file(output_file):
	global gexf
	gexf.write(output_file)

def get_node_id(label):
	global dict_nodes
	return dict_nodes[label]
