
from src.algorithms.community_detection import detect_communities
from src.utils.graph_loader import load_graph_from_file


def start_example():
    # Load the graph
    graph = load_graph_from_file('data/sample_graph_data/graph.edgelist')

    # Detect communities
    communities = detect_communities(graph, algorithm='louvain', distributed=True)

    # Print the results
    print(communities)


if __name__ == '__main__':
    start_example()
