# Math/BCMB3888-D: Yeast models of Glioblastoma 

Think of this as the "front page" for our project. As it grows we should fill out this page as a reference and a record of progress.

I apologise for the terrible state of my code...

## Aim

## Glossary and other info

The homologs of WRAP53 in yeast are RSA4 "YCR072C" and TAF5 "YBR198C".

#### Proteins from Week 3 (Sunday):
TP63 - tumour protein 63<br>
associated with aggressive form of pancreatic cancer<br>
pancreatic ductal adenocarcinoma<br>
PDAC<br>
BUD16<br>
BUD17<br>
UBX3 <- might be very important<br>
Identifier (YDL091C)

#### Week 5 project proposal - Maths
##### Scheme
 - Recieve key proteins from BCMB students. In particular we are concerned with <em>sources</em> (of metabolites etc.) and <em>targets</em> (e.g. growth protein)
 - Locate community [Louvain, etc.]
 - Analyse centrality (cross check with different measures) [subgraph more lethal, different to degree centrality, cite paper] (pathway?) analysis on community
 - Look for weakly connected alternate pathways (avoiding central nodes), targeting to modulate expression of target.
   - specialise pathway to cancer(?)
 - approach to essential nodes: include for structure, avoid in selecting pathways/nodes.
 - Pick target nodes with a cost function optimising for minimal degree <=> lethality [cite], and cut number. Essential nodes have a high cost. Subgraph centrality is best prediction method we have so far.


Dual passes with and without essential proteins--how does this effect the structure of the community finding:<br><br>
E.g. <em><b>Essential removed before community finding:</b></em>
<p align="center">
  <img style="display: block; margin-left: auto; margin-right: auto; width: 70%;" alt="Neighbourhood of YCR072C, the WRAP53 homolog in yeast." src="https://user-images.githubusercontent.com/34012884/186800221-395bcf8c-c6b7-43f2-afdd-f049adda39bd.png">
</p>
vs. <em><b>Essential removed after community finding:</b></em>
<p align="center">
  <img style="display: block; margin-left: auto; margin-right: auto; width: 70%;" alt="Neighbourhood of YCR072C, the WRAP53 homolog in yeast." src="https://user-images.githubusercontent.com/34012884/186800500-9631017c-3dda-4693-a53b-7534b45a949c.png">
</p>

## Pretty Pictures
Until we have anything else to put here, enjoy some pretty pictures :P

<p align="center">
  <img style="display: block; margin-left: auto; margin-right: auto; width: 75%;" alt="Neighbourhood of YCR072C, the WRAP53 homolog in yeast." src="https://user-images.githubusercontent.com/34012884/185737294-9e32ced4-31d7-4875-8ceb-0b99f2681cd3.png">
</p>

## Freyas notes - subgraph centrality paper
- subgraph centrality measures the number of connected graphs the node takes part in, giving more weight to smaller nodes.
- It is more discriminative than other measures, and produces a different ranking of nodes. However, still yields highest rank for nodes with largest degree, disagrees on majority of other nodes.
- The node with highest subgraph centrality would be one in a complete network (everything connected to everything)
- After testing with the yeast dataset, ranking with subgraph centrality better predicts essential nodes compared to dc
- biomed theory for this: duplication-divergence model of evolution, triangles are formed among duplicating genes and any neighbour of the parent gene, squares with duplicating genes and any pair of neighbours.
- Part about scaling properties is largely about the small-world model which I don't understand :( will read and report back!
- Apparently shows a power-law distribution even when dc does not display scale free distribution?

## Yin En's Notes - Community Finding paper
### <a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1357925">Communities in Networks - [Porter et al., 2009]</a>
- The rationale behind community finding is based on the mesoscopic (i.e. intermediate structures, between macro/micro worlds) and arose from sociology, in an attempt to map the relationship between "micro" groups and "macro" patterns.
  - Specifically, this took off in 2002 once Michelle Girvan and Mark Newman researched graph-partitionining problems. It kicked off attempts to solve these problems through community finding among physicists and applied mathematicians.
- Communities are context-specific and the process of identifying them is inherently interdisciplinary, but is problematised by the way each discipline will often formulate communities in a domain-specific manner.
  - Many community-finding algorithms exist, all to identify and detect "strong" edges that bind certain nodes together into a community. The following is a list of those included in this article:
    - **Traditional Clustering Techniques** - A broader category that includes partitional clustering (e.g. k-means clustering), neural network clustering (self-organising maps) and multidimension scaling (singular value decomposition and principal component analysis)
      - These techniques involve a matrix identifying similarities, which then return a coordinate matrix minimising an appropriate loss function (p. 1087)
      - Linkage Clustering (an example of an agglomerative method) begins with *N* individual nodes in a undirected/weighted network that is represented by an adjacency matrix *A<sub>ij</sub>* and forms communities through connecting each maximal *A<sub>ij</sub>* pair.
        - The formation of clusters is important for community finding, and thus differs from technique to technique within this method.
      - Divisive techniques, on the other hand, break down a graph to find communities.
    - **Kernighan-Lin Algorithm** - An algorithm derived in 1970 by Brian Kernighan and Shen Lin to minimise the number of connections between different electrical boards within partitioned electrical circuits (p. 1087)
      - By partitioning a graph into two groups of predefined size, the algorithm swaps an equal number of vertices between the groups, determined by a quality function (˜Q) that relates intra-group connections to inter-group connections. This then expands until there are multiple groups, which naturally form communities.
      - The algorithm heavily depends on the initial partition chosen, which is why this algorithm is often paired with other methods to create higher-quality partitions.
    - **Centrality-Based Community Detection** - Based on the notion of *betweenness centrality* from sociology, which rose to attention due to Michelle Girvan and Mark Newman (pp. 1087-8)
      - By considering geodesic betweenness (shortest paths) and random walk betweenness (random paths) in a pair of nodes, edges are ranked based on their betweenness. Once the edge with the highest betweenness is removed, all remaining edges are recalculated, with the process iterating divisely until a set of isolated nodes is obtained.
      - Such a method has been applied to other network components that aren't nodes, but is both slow and returns poor results for densely-populated/large networks.
    - **Local Methods** - a set of global clustering algorithms that include *k*-clique percolations (p. 1088)
      - *k*-Clique Percolation involves complete subgraphs of *k* nodes with all possible links (i.e. $k \left( k - 1 \right)/2$) forming a union of 'adjacent' cliques in a *k*-clique community. Generally, 3 <= *k* <= 6, as larger values become unwieldy and *k* = 2 focuses on links, while *k* = 1 focuses on nodes.
      - Nodes can belong to no community (if they are isolated) or multiple communities (if they interact with multiple communities).
      - While these methods overlook other modules that aren't as well-connected, they are one of the best methods to consider community overlap (which is particularly suitable for sociology).
    - **Modularity Optimisation** - Assortative methods that involve one of the most popular quality functions, wherein a network partition is measured to see how well it compartmentalises communities (pp. 1088-9)
      - The original definition of modularity states that an unweighted/undirected network can be partitioned into $Q = \sum_{i} \left( e_ii - b_1^2 \right)$ where $e_ij$ are the edges with $i$ and $j$ as their endpoints and $b_i = \sum _j e_ij$ are the edges in group $i$.
        - High values of Q suggest that more edges exist within the group than if they were arranged by chance.
      - These methods partition graphs into groups where nodes are either more likely (assortative) or less likely (disassortative) to be connected to nodes of the same type.
      - Maximising modularity is closely related to graph visualisation, particularly in energy models of pairwise attraction.
      - While modularity functions are the best to optimise for community finding, it only contains information on network structure and cannot exhaustively enumerate all possible network partitions.
    - **Spectral Partitioning** - A method that was developed for parallel computational algorithms (pp. 1089-90)
      - Traditional spectral partitioning relates network properties to the graph's Laplacean matrix. The network is split into two groups and can then continue to be split into more two-group partitions.
        - In the two-group instance (where there is only a single split), an index vector $s$ has components that take the value $+1$ if they are in the first group and $-1$ if they are in the second group. The total edge weight is expressed as $R = 1/4 S^T Ls$.
        - The 'best' partition of the network relies on choosing $s$ such that $R$ is minimised, but discounting the trivial case of partitioning all nodes into a single group. Usually, the group sizes are fixed to avoid the latter issue, which becomes a problem in and of itself when the number/size of communities isn't known in advance. This is why modularity is often used with this method.
    - **Potts Method** - involves nodes that are magnetised and seek to align certain ways. I have omitted further notes on this because a) I can't see the relevance of this to proteins, and b) I didn't really understand it anyway (pp. 1090-1)
- Different community-finding techniques are applied to different practical problems, as some will be better-suited than others to detect communities. As biological systems is the only one relevant to our project, I've only included notes on that one.
  - Motifs (i.e. basic building blocks in complex networks) are repeated across different types of networks, often as an evolutionary response. The most prominent example is the 3-chain, or triangles (which would tie into the paper Freya read on subgraph centrality).
  - Most prominently, Guimerà and Amaral (2005) calculated the properties of nodes within communities found in twelve different organisms through their within-module degree ($i$, which represented its connectedness within its community) and their participation ratio ($P_i$, which represented the link distribution across all communities).
    - By comparing the z-scores ($z_i$) and $P_i$ of nodes, they found that *non-hub connector nodes* (with low $z_i$, moderately high $P_i$, and indicated preferential connectivity to a subset of the network's communities) didn't appear as frequently as *provincial hubs* (with high $z_i$ and low $P_i$).
- Many community-finding algorithms exist, but research so far (at the time this paper was published) focused on formulating fast and generally accurate community-finding algorithms. Few algorithms exist to handle directed or signed networks (an example of signed networks appears in Potts Method), as well as algorithms that can work with interval ranges rather than precise values and other networks that are time-dependent or parameter-dependent.

## <a href="https://www.nature.com/articles/35075138">Lethality and centrality in protein networks [H. Jeong, 2001]</a>
<a href="https://edstem.org/au/courses/9294/resources?download=14255">(EdStem download)</a><br>
<em>Summary</em>: in yeast, more connected proteins are more lethal when knocked out. Hence our desire to avoid knocking out essential nodes. <br><br>The degree distribution is roughly scale free Examine for our network:
<p align="center">
  <img style="display: block; margin-left: auto; margin-right: auto; width: 50%;" alt="Log-log degree distribution for yeast." src="https://user-images.githubusercontent.com/34012884/186669141-8929599c-6a06-4d4d-9bef-7bf6832a6b65.png">
</p>
Looking for things to knock out we are therefore looking for relatively low degree nodes.
