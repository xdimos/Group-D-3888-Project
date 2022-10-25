# Math/BCMB3888-D: Yeast models of Glioblastoma - Elden's branch

This is Elden's branch of the Math3888 Group D GitHub. In this README I will briefly summarise the contents of each Jupyter notebook.

```Lethality Fitting.ipynb``` contains code to calculate centrality measures on whole PPI networks. I generated the data used to train Freya's random forest lethality model.

```Machine categorising.ipynb``` contains code parsing the <a href="https://string-db.org/">string-db</a> short descriptions, facilitating the identification of key features in the Degree-Eigenvector centrality space.

```Protein Local Processing.ipynb``` is the main body of code for identifying targets, and is built up from of the old ```Yeast_network_visualisation.ipynb``` code in the first weeks. Its main job is community finding, and plotting node centrality distributions around key targets to look for interesting outliers.

I whilst I want to apologise for the terrible state of my code... I really can't: this repository is a working jumble of my ideas!

<details>
  <summary>Random miscellanea</summary>
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

#### <a href="https://www.nature.com/articles/35075138">Lethality and centrality in protein networks [H. Jeong, 2001]</a>
<a href="https://edstem.org/au/courses/9294/resources?download=14255">(EdStem download)</a><br>
<em>Summary</em>: in yeast, more connected proteins are more lethal when knocked out. Hence our desire to avoid knocking out essential nodes. <br><br>The degree distribution is roughly scale free Examine for our network:
<p align="center">
  <img style="display: block; margin-left: auto; margin-right: auto; width: 50%;" alt="Log-log degree distribution for yeast." src="https://user-images.githubusercontent.com/34012884/186669141-8929599c-6a06-4d4d-9bef-7bf6832a6b65.png">
</p>
Looking for things to knock out we are therefore looking for relatively low degree nodes.

#### Week 5 project proposal - Maths
##### Scheme
 - Recieve key proteins from BCMB students. In particular we are concerned with <em>sources</em> (of metabolites etc.) and <em>targets</em> (e.g. growth protein)
 - Locate community [Louvain, etc.]
 - Analyse centrality (cross check with different measures) [subgraph more lethal, different to degree centrality, cite paper] (pathway?) analysis on community
 - Look for weakly connected alternate pathways (avoiding central nodes), targeting to modulate expression of target.
   - specialise pathway to cancer(?)
 - approach to essential nodes: include for structure, avoid in selecting pathways/nodes.
 - Pick target nodes with a cost function optimising for minimal degree <=> lethality [cite], and cut number. Essential nodes have a high cost.


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
</details>
