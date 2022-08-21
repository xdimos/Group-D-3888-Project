#===============================================================================================================================#
# This .py contains some of the standard utility functions that would be frustrating to intersperse in the Jupyter notebooks.   #
# Rather, they are included here, and should be imported in with "import network_utilities as nu"                               #
#===============================================================================================================================#

import networkx as nx

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

# let's define a little function to trim the leading "4932." off protein names
# This _should_ work with any hierarchy of strings in lists.
def trim(protein_name):
    if (type(protein_name) is str):   
        # returns everything _after_ the first period.
        return '.'.join(protein_name.split(".")[1:])
    elif (type(protein_name) is list):
        trimmed_list = []
        for name in protein_name:
            trimmed_list.append(trim(name))
        return trimmed_list

# A simple QoL function to cut down a network to a given nodelist
def cutdown_network(graph, nodelist):
    graph_copy = graph.copy(); # just to allow modification
    nodes_to_remove = set(graph.nodes) - nodelist;
    graph_copy.remove_nodes_from(nodes_to_remove)
    return graph_copy
    
# My custom drawing function, with all my prefered defaults set. Useful general functions like this should probably be broken
# out into their own documents-to-be-included.
def my_draw(graph, with_labels=False, kkl=False, color_by_weight=True, node_color="Blue", node_size=10, alpha=0.8,
            key_text=None, title_text=None):
    # "make a new figure"
    network_fig = plt.figure(figsize=(12,12))
    # Pick the layout option. At the moment I just have KK or spring. KK is much more time-intensive.
    if (kkl):
        my_layout = nx.kamada_kawai_layout(graph, weight=None);
    else:
        my_layout = nx.spring_layout(graph, k=0.5);
    # We will almost always want to color by weight... if only 'cause it is prettier!
    if (color_by_weight):
        edges = graph.edges()
        weights = [graph[u][v]['weight'] for u,v in edges]
        # Pick the colormap here if you like!
        cmap=plt.cm.plasma;
    
        nx.draw_networkx_nodes(graph, pos=my_layout, node_size=node_size, alpha=alpha, node_color=node_color)
        nx.draw_networkx_edges(graph, pos=my_layout, edge_color=weights, edge_cmap=cmap, width=0.2)

        # Adding a colorbar as per https://stackoverflow.com/questions/26739248/how-to-add-a-simple-colorbar-to-a-network-graph-plot-in-python
        sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin = min(weights), vmax=max(weights)))
        sm._A = [];
        cb = plt.colorbar(sm, aspect=50, fraction=0.05);
        cb.set_label("Confidence score", fontsize=15);
    else:
        # If not coloring by weight... (I really haven't worked to make this that nice though!)
        nx.draw(graph, pos=my_layout, node_size=node_size, alpha=alpha, node_color=node_color, font_size='10',with_labels=False)
    # Title, and text in bottom left
    if (key_text is not None):
        network_fig.text(0.15,0.15, key_text, fontsize=15, fontweight='light')
    if (title_text is not None):
        plt.title(title_text);
    # "show the figure"
    plt.show();