import networkx as nx
from dask import delayed
from dask.distributed import Client

def compute_pagerank(graph: nx.Graph, alpha: float = 0.85, distributed: bool = False) -> dict:
    """
    Calculates the PageRank of nodes in a graph, optionally using distributed processing.

    Parameters:
        graph (networkx.Graph): The graph on which to compute PageRank.
        alpha (float): The damping factor (typically 0.85).
        distributed (bool): Whether to run the computation in a distributed manner. Default is False.

    Returns:
        dict: A dictionary where keys are node IDs and values are their PageRank scores.
    """
    if distributed:
        # Convert the graph into a Dask-delayed object
        graph_delayed = delayed(nx.pagerank)(graph, alpha=alpha)

        # Execute the computation across the Dask cluster
        client = Client()
        pagerank_scores = client.compute(graph_delayed).result()
    else:
        # Use NetworkX's built-in PageRank function for local execution
        pagerank_scores = nx.pagerank(graph, alpha=alpha)

    return pagerank_scores