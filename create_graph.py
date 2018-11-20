import networkx as nx
from random import *
import matplotlib.pyplot as plt

def createGraph(D):
	rowdy = []

	G = nx.Graph()
	for i in range(1, 6):
		G.add_node(str(i))

	# add the first few edges
	G.add_edge("3", "2")
	G.add_edge("1", "2")
	G.add_edge("3", "1")
	G.add_edge("3", "4")
	G.add_edge("4", "5")
	G.add_edge("6", "5")

	start = 6

	# Create clusters of i vertices
	for i in range(4,D):
		# add the vertices
		for j in range(start, start + i):
			G.add_node(str(j))

		# add edge from start to all other vertices in this subgraph
		for j in range(start, start + i):
			G.add_edge(str(start), str(j))

		# also add this one edge
		G.add_edge(str(start + 1), str(start + 2))

		# creates a rowdy for each pair with start except start + 1, and start + 2
		for j in range(start + 3, start+i):
			rowdy.append([str(start), str(j)])
			# add more rowdy groups
			rowdy.append([str(j - 1), str(j)])
			rowdy.append([str(j - 1), str(j), str(j-2)])


		if i != 4:
			# add the edge between subgraphs
			G.add_edge(str(start), str(start - i + 1))
			# a rowdy group between subgraphs
			rowdy.append([str(start), str(start - i + 1), str(start - i + 2)])
		start += i

	return G, rowdy
