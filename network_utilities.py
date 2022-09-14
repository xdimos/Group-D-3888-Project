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

# A simple QoL function to cut down a network to a given nodelist (as opposed to the converse, which nx supplies)
def cutdown_network(graph, nodelist):
    graph_copy = graph.copy(); # just to allow modification
    nodes_to_remove = set(graph.nodes) - set(nodelist);
    graph_copy.remove_nodes_from(nodes_to_remove)
    return graph_copy
    
# My custom drawing function, with all my prefered defaults set. 
def my_draw(graph, # The networkx network to be plotted
            with_labels=False, # whether to include node labels. Can get very messy.
            kkl=False, # whether to use Kamada Kawai algorithm for layout. Looks nice, but is (much) slower
            color_by_weight=True, # Edge colors by confidence weight. 
                                  # ...Most of the nice things here assume this is True. Turn off at your peril... plus it looks pretty :P
            node_color="Blue", # Either a single string "Blue", "b", "r", or a list of the colors of individual node colors in order
            node_size=10, # Similar to above
            alpha=0.8, # The _node_ opacity. Similar to above (single value or list). Note that this will be modulated
            key_text=None, # Text at the bottom of the figure
            title_text=None, # Text above figure
            delay_show=False): # whether to not run plt.show() at end. Use this if you want to include more matplotlib details,
                               # or with to run nu.draw_path_from_nodes(...) - see below 
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
        # TODO 
        labels = None;
        if (with_labels):
            list_labels = list(graph.nodes);
            labels = {l : l for l in list_labels}
            nx.draw_networkx_labels(graph, my_layout, labels=labels, font_size=6)
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
    if (delay_show is False): plt.show();
    return my_layout;

#
# draws a path on an existing network plot, from a ordered node list. 
# !! If using this with nu.my_draw(...), make sure to set delay_show=True to avoid matplotlib plt.show()-ing the figure. !!
# 'pos' is a network layout (i.e. what is returned by nx.spring_layout(graph); and the like)
# 'node_list' is a list of the node names, in order of the path. 
# '**textkwargs' are keyword arguments passed with the plt.text call - e.g. font size.
#
def draw_path_from_nodes(pos, node_list, with_labels=False, color='r', **textkwargs):
    xs = [list(pos[node])[0] for node in node_list]
    ys = [list(pos[node])[1] for node in node_list]
    plt.plot(xs,ys, color=color)
    for i in range(len(xs)):
        plt.text(xs[i],ys[i], node_list[i], textkwargs)

#
# bit of an esoteric function. Takes a list of inputs, and creates a list consisting of given results, corresponding to whether each  
# value returns true the corresponding boolean lambda test. ... feel free to ignore this!
#
def value_lambda_result(values, tests, results, default=0): 
    # 'values' a list of inputs. 'tests' a boolean lambda function. 
    # The first test to be satisfied returns its 'results'
    # 'default' is returned otherwise.
    # ...'results' can also contain lambdas, in which case, the lambda is evaluated on the corresp' value
    output = [default for i in range(len(values))]
    for v in range(len(values)):
        for t in range(len(tests)):
            if (tests[t](values[v])): 
                if (callable(results[t])): output[v] = results[t](values[v])
                else: output[v] = results[t]
                break

    return output
    