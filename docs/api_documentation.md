# API Documentation

## Overview

This document provides a comprehensive guide to the APIs available in the **GraphStorm** project. It details the functions, classes, and modules implemented within the project, including descriptions of their purpose, parameters, and return values. This documentation is intended to help developers and contributors understand how to interact with the codebase effectively.

## Table of Contents

1. [Graph Partitioning Module](#graph-partitioning-module)
   - `partitioner.py`
   - `load_balancer.py`
2. [Algorithms Module](#algorithms-module)
   - `pagerank.py`
   - `community_detection.py`
3. [Distributed Processing Module](#distributed-processing-module)
   - `dask_cluster_setup.py`
   - `ray_cluster_setup.py`
4. [Utilities Module](#utilities-module)
   - `graph_loader.py`
   - `graph_saver.py`

---

## Graph Partitioning Module

### `partitioner.py`

#### **Function: `partition_graph`**

**Description:**
Partitions a given graph into a specified number of subgraphs for distributed processing.

**Parameters:**
- `graph (networkx.Graph)`: The input graph to be partitioned.
- `num_partitions (int)`: The number of subgraphs to create.
- `method (str)`: The partitioning method to use, e.g., 'metis', 'random'. Default is 'metis'.

**Returns:**
- `List[networkx.Graph]`: A list of subgraphs.

**Usage:**
```python
from src.graph_partitioning.partitioner import partition_graph

subgraphs = partition_graph(graph, num_partitions=4, method='metis')
```

---

### `load_balancer.py`

#### **Function: `balance_load`**

**Description:**
Balances the load across multiple nodes in a cluster by adjusting the distribution of graph partitions.

**Parameters:**
- `partitions (List[networkx.Graph])`: The list of graph partitions.
- `nodes (int)`: The number of nodes available in the cluster.

**Returns:**
- `Dict[int, List[networkx.Graph]]`: A dictionary mapping node IDs to lists of graph partitions.

**Usage:**
```python
from src.graph_partitioning.load_balancer import balance_load

balanced_partitions = balance_load(subgraphs, nodes=4)
```

---

## Algorithms Module

### `pagerank.py`

#### **Function: `compute_pagerank`**

**Description:**
Calculates the PageRank of nodes in a graph, optionally using distributed processing.

**Parameters:**
- `graph (networkx.Graph)`: The graph on which to compute PageRank.
- `alpha (float)`: The damping factor (typically 0.85).
- `distributed (bool)`: Whether to run the computation in a distributed manner. Default is `False`.

**Returns:**
- `Dict`: A dictionary where keys are node IDs and values are their PageRank scores.

**Usage:**
```python
from src.algorithms.pagerank import compute_pagerank

pagerank_scores = compute_pagerank(graph, alpha=0.85, distributed=True)
```

---

### `community_detection.py`

#### **Function: `detect_communities`**

**Description:**
Identifies communities within a graph using modularity optimization or other community detection algorithms.

**Parameters:**
- `graph (networkx.Graph)`: The graph on which to detect communities.
- `algorithm (str)`: The algorithm to use, e.g., 'louvain', 'girvan-newman'. Default is 'louvain'.
- `distributed (bool)`: Whether to run the detection in a distributed manner. Default is `False`.

**Returns:**
- `Dict`: A dictionary mapping community IDs to lists of node IDs.

**Usage:**
```python
from src.algorithms.community_detection import detect_communities

communities = detect_communities(graph, algorithm='louvain', distributed=True)
```

---

## Distributed Processing Module

### `dask_cluster_setup.py`

#### **Function: `setup_dask_cluster`**

**Description:**
Sets up a Dask cluster for distributed processing.

**Parameters:**
- `n_workers (int)`: The number of worker nodes to start.
- `threads_per_worker (int)`: The number of threads per worker.
- `memory_limit (str)`: The memory limit for each worker, e.g., '2GB'.

**Returns:**
- `distributed.Client`: A Dask client connected to the cluster.

**Usage:**
```python
from src.distributed_processing.dask_cluster_setup import setup_dask_cluster

client = setup_dask_cluster(n_workers=4, threads_per_worker=2, memory_limit='2GB')
```

---

### `ray_cluster_setup.py`

#### **Function: `setup_ray_cluster`**

**Description:**
Sets up a Ray cluster for distributed processing.

**Parameters:**
- `n_nodes (int)`: The number of nodes to include in the cluster.

**Returns:**
- `ray.init()`: A Ray cluster object.

**Usage:**
```python
from src.distributed_processing.ray_cluster_setup import setup_ray_cluster

ray_cluster = setup_ray_cluster(n_nodes=4)
```

---

## Utilities Module

### `graph_loader.py`

#### **Function: `load_graph_from_file`**

**Description:**
Loads a graph from a specified file format.

**Parameters:**
- `file_path (str)`: The path to the graph file.
- `file_format (str)`: The format of the file, e.g., 'edgelist', 'adjlist'. Default is 'edgelist'.

**Returns:**
- `networkx.Graph`: The loaded graph object.

**Usage:**
```python
from src.utils.graph_loader import load_graph_from_file

graph = load_graph_from_file('data/sample_graph_data/graph.edgelist', file_format='edgelist')
```

---

### `graph_saver.py`

#### **Function: `save_graph_to_file`**

**Description:**
Saves a graph to a specified file format.

**Parameters:**
- `graph (networkx.Graph)`: The graph to be saved.
- `file_path (str)`: The path to save the graph file.
- `file_format (str)`: The format to save the file in, e.g., 'edgelist', 'adjlist'. Default is 'edgelist'.

**Returns:**
- `None`

**Usage:**
```python
from src.utils.graph_saver import save_graph_to_file

save_graph_to_file(graph, 'data/output/graph.edgelist', file_format='edgelist')
```
