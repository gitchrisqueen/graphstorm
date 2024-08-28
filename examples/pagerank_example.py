
from src.algorithms.pagerank import compute_pagerank
from src.utils.graph_loader import load_graph_from_file
import argparse

def start_example(distributed: bool = False):
    # Load the graph
    graph = load_graph_from_file('data/sample_graph_data/graph.edgelist')

    # Compute PageRank
    pagerank_scores = compute_pagerank(graph, alpha=0.85, distributed=distributed)

    # Print the results
    print(pagerank_scores)


if __name__ == '__main__':
    # Define the argument parser
    parser = argparse.ArgumentParser(description='Run PageRank example.')
    parser.add_argument('--distributed', action='store_true', help='Run PageRank in distributed mode')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Pass the parsed argument to the start_example function
    start_example(distributed=args.distributed)
