

from src.graph_partitioning.partitioner import partition_graph
from src.utils.graph_loader import load_graph_from_file

def start_example():

    # Load the graph
    graph = load_graph_from_file('data/sample_graph_data/graph.edgelist')

    # Partition the graph
    subgraphs = partition_graph(graph, num_partitions=4, method='metis')

    # Print the number of subgraphs
    print(f"Number of partitions created: {len(subgraphs)}")


if __name__ == '__main__':
    start_example()
