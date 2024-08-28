# Sample Data Sets

### **1. SNAP (Stanford Large Network Dataset Collection)**
SNAP provides a variety of real-world graph datasets, including social networks, web graphs, and collaboration networks.

- **Website**: [SNAP Datasets](http://snap.stanford.edu/data/)
- **Example Dataset**: [Facebook Social Network](http://snap.stanford.edu/data/egonets-Facebook.html)

**Steps:**
1. Visit the SNAP datasets page and choose a dataset, such as the Facebook Social Network.
2. Download the dataset in the edge list format (`facebook_combined.txt.gz`).
3. Extract the file and rename it to `graph.edgelist`.
4. Place the file in the `data/sample_graph_data/` directory.

**Example Command (Linux/MacOS):**
```bash
wget http://snap.stanford.edu/data/facebook_combined.txt.gz
gunzip facebook_combined.txt.gz
mv facebook_combined.txt data/sample_graph_data/graph.edgelist
```

### **2. Open Graph Benchmark (OGB)**
OGB provides large-scale graph datasets suitable for benchmarking graph neural networks and other graph algorithms.

- **Website**: [OGB Datasets](https://ogb.stanford.edu/docs/dataset_overview/)
- **Example Dataset**: [ogbn-arxiv](https://ogb.stanford.edu/docs/nodeprop/)

**Steps:**
1. Install the OGB package using pip:
   ```bash
   pip install ogb
   ```
2. Use the OGB library to download and convert a dataset to edge list format.

**Example Python Script:**
```python
from ogb.nodeproppred import NodePropPredDataset
import networkx as nx

# Load the dataset
dataset = NodePropPredDataset(name="ogbn-arxiv")
graph, _ = dataset[0]

# Convert to NetworkX graph
G = nx.Graph()
G.add_edges_from(graph['edge_index'].T)

# Save as edge list
nx.write_edgelist(G, 'data/sample_graph_data/graph.edgelist')
```

### **3. NetworkX Built-In Datasets**
NetworkX includes some simple built-in datasets that can be used for testing purposes.

**Example Code:**
```python
import networkx as nx

# Load a sample graph
G = nx.karate_club_graph()

# Save as edge list
nx.write_edgelist(G, 'data/sample_graph_data/graph.edgelist')
```

### **4. Custom Synthetic Data**
If you want to generate a synthetic graph for testing:

**Example Code:**
```python
import networkx as nx

# Generate a random graph
G = nx.erdos_renyi_graph(n=100, p=0.05)

# Save as edge list
nx.write_edgelist(G, 'data/sample_graph_data/graph.edgelist')
```

### **Summary:**
- Use SNAP or OGB datasets for real-world data.
- Use NetworkX’s built-in graphs or generate synthetic graphs for quick tests.
- Ensure that the file is saved in the `data/sample_graph_data/` directory with the name `graph.edgelist`.

