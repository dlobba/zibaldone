import sys, logging
import re
import networkx as nx
import matplotlib.pyplot as plt

# TODO:
# add argparse support

# just a simple node class with some specific behavior, not something huge \
# to take into account to move it into another file
class Node:

    def __init__ (self, node, adj = None):
        self.node = node
        self.adj = adj

    # this should be the str representation? How to deal \
    # with the str vs repr problem?
    def __repr__ (self):
        return "node: {0}, adjacency-list: {1}".format(self.node, self.adj)

logging.basicConfig(level=logging.DEBUG)
nodes = []
try:
    with  open (sys.argv[1], 'r') as file:
        for line in file:
            token = re.split ('[\s,]+', line)
            logging.debug ("Token found:{0}".format(token))
            if len (token[0]) > 0:
                nodes.append (Node(token[0], token[2:-1])) # I had to use \
                # the -1 cause split puts the remainder of the match as \
                # the last element of the sequence. How could I avoid this \
                # behaviour?

                
except (IndexError, FileNotFoundError) as e:
    logging.error ("{0}. Did you try to just put a (valid)" \
               "file as first argument?".format(e))

logging.debug ("Nodes found:\n{0}".format (nodes))
if len (nodes) > 0:
    g = nx.DiGraph ()
    edges = []
    for node in nodes:
        # this also takes care if an adjacency list of a node is empty
        edges.extend (tuple ((node.node, adjacent) for adjacent in node.adj))
    logging.debug (edges)
    g.add_edges_from (edges)
    nx.drawing.nx_pydot.write_dot (g, 'graph.dot')
    nx.draw (g, with_labels = True, arrows = True)
    plt.show ()
