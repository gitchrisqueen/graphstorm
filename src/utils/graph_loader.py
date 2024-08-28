
import networkx as nx

def load_graph_from_file(file_path: str, file_format: str = 'edgelist') -> nx.Graph:
    """
    Loads a graph from a specified file format.

    Parameters:
        file_path (str): The path to the graph file.
        file_format (str): The format of the file, e.g., 'edgelist', 'adjlist'. Default is 'edgelist'.

    Returns:
        networkx.Graph: The loaded graph object.
    """
    if file_format == 'edgelist':
        graph = nx.read_edgelist(file_path, nodetype=int, data=(('weight', float),))
    elif file_format == 'adjlist':
        graph = nx.read_adjlist(file_path, nodetype=int)
    else:
        raise ValueError(f"Unsupported file format: {file_format}")

    return graph