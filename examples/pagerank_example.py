
from src.algorithms.pagerank import compute_pagerank
from src.utils.graph_loader import load_graph_from_file

# Load the graph
graph = load_graph_from_file('data/sample_graph_data/graph.edgelist')

# Compute PageRank
pagerank_scores = compute_pagerank(graph, alpha=0.85, distributed=True)

# Print the results
print(pagerank_scores)
