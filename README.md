# GraphStorm: Distributed Graph Analytics on HPC Clusters

![GraphStorm Logo](./GraphStorm.webp) 

## Overview

**GraphStorm** is a high-performance distributed graph analytics framework designed to run on HPC clusters. This project demonstrates the power of distributed computing by implementing and optimizing several graph algorithms, such as PageRank and community detection, across multiple nodes in a cluster. It showcases how graph processing can be scaled efficiently from a single machine to a full-blown HPC cluster using free and open-source resources.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Running on a Single Machine](#running-on-a-single-machine)
  - [Running on a Distributed Cluster](#running-on-a-distributed-cluster)
- [Algorithms Implemented](#algorithms-implemented)
- [Benchmarking](#benchmarking)
- [File Structure](#file-structure)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Distributed Processing**: Utilize tools like Dask and Ray to distribute graph algorithms across multiple nodes.
- **Scalable**: Efficiently process large-scale graph datasets on HPC clusters.
- **Real-World Applications**: Implement graph algorithms used in social network analysis, recommendation systems, fraud detection, and more.
- **Optimized Partitioning**: Advanced graph partitioning and load balancing techniques to maximize performance.
- **Free & Open-Source**: Built entirely using free resources and open-source software.

## Installation

### Prerequisites

- Python 3.8+
- [Dask](https://dask.org/)
- [Ray](https://ray.io/)
- [NetworkX](https://networkx.github.io/)

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/gitchrisqueen/graphstorm.git
   cd graphstorm
   ```

2. Create a virtual environment and install dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. Download sample graph data:

   Sample data can be found in the `graphstorm/data/sample_graph_data` directory. You can add more datasets as needed.

## Usage

### Running on a Single Machine

To run graph algorithms on a single machine:

1. Navigate to the `graphstorm/examples/` directory.
2. Execute one of the example scripts:

   ```bash
   python pagerank_example.py
   ```

This will run the PageRank algorithm on a sample graph and output the results.

### Running on a Distributed Cluster

To run the project on a distributed cluster:

1. Ensure that Dask or Ray is installed on all cluster nodes.
2. Modify the `graphstorm/src/distributed_processing/` scripts to match your cluster's configuration (IP addresses, ports, etc.).
3. Start the Dask or Ray cluster:

   ```bash
   python dask_cluster_setup.py  # For Dask
   python ray_cluster_setup.py   # For Ray
   ```

4. Run the desired algorithm:

   ```bash
   python pagerank_example.py
   ```

The script will automatically distribute the workload across the available nodes.

## Algorithms Implemented

- **PageRank**: Calculates the importance of nodes within a graph.
- **Community Detection**: Identifies clusters of nodes that are more densely connected to each other than to other nodes.
- **Graph Partitioning**: Divides the graph into partitions for efficient distributed processing.

## Benchmarking

Performance results and benchmarks comparing single-node versus distributed processing can be found in the `graphstorm/benchmarks/` directory. This section includes:

- **Performance Results**: Detailed performance metrics for each algorithm.
- **Scalability Tests**: Analysis of how well the algorithms scale across multiple nodes.
- **Local vs. Distributed**: Comparisons between local execution and distributed execution.

## File Structure

```plaintext
graphstorm/
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
├── data/
│   ├── sample_graph_data/
│   └── README.md
├── src/
│   ├── graph_partitioning/
│   │   ├── partitioner.py
│   │   └── load_balancer.py
│   ├── algorithms/
│   │   ├── pagerank.py
│   │   └── community_detection.py
│   ├── distributed_processing/
│   │   ├── dask_cluster_setup.py
│   │   └── ray_cluster_setup.py
│   └── utils/
│       ├── graph_loader.py
│       └── graph_saver.py
├── benchmarks/
│   ├── performance_results.md
│   ├── local_vs_distributed.md
│   └── scalability_tests.md
├── docs/
│   ├── design_decisions.md
│   ├── optimization_strategies.md
│   ├── cluster_setup_guide.md
│   └── api_documentation.md
└── examples/
    ├── pagerank_example.py
    ├── community_detection_example.py
    └── graph_partitioning_example.py
```

## Documentation

For detailed design decisions, optimization strategies, and performance results, please refer to the `graphstorm/docs/` directory. This directory includes:

- **Design Decisions**: Rationale behind architectural choices.
- **Optimization Strategies**: Techniques used to improve performance.
- **Cluster Setup Guide**: Instructions on configuring your cluster.
- **API Documentation**: Comprehensive API reference for all modules.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the `graphstorm/LICENSE` file for details.

## Contact

For any inquiries, please contact [Christopher Queen](mailto:christopher.queen@gmail.com).
