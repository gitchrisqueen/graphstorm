# Design Decisions

## Overview

This document outlines the key design decisions made during the development of the **GraphStorm** project. It provides the rationale behind the architectural choices, technologies selected, and implementation strategies. These decisions are intended to optimize the performance, scalability, and maintainability of the project.

## 1. Choice of Distributed Framework: Dask and Ray

### Decision:
- **Dask** and **Ray** were selected as the primary distributed computing frameworks for **GraphStorm**.

### Rationale:
- **Dask** provides a flexible and scalable framework that integrates well with Python’s existing data science ecosystem. Its ability to parallelize and distribute tasks across a cluster makes it ideal for graph analytics.
- **Ray** offers a simple and powerful API for distributed computing and is particularly well-suited for workloads that involve a mix of CPU-bound and I/O-bound tasks. It also has strong support for reinforcement learning and machine learning workloads, providing potential avenues for future extensions.

## 2. Graph Processing Library: NetworkX

### Decision:
- **NetworkX** was chosen as the core graph processing library.

### Rationale:
- **NetworkX** is a well-established library for network analysis and provides a comprehensive set of tools for creating, manipulating, and studying the structure and dynamics of complex networks.
- Its integration with **Dask** allows for easy scalability from single-node to distributed environments, making it a perfect fit for **GraphStorm**.

## 3. Algorithm Selection: PageRank and Community Detection

### Decision:
- **PageRank** and **Community Detection** were selected as the initial algorithms to implement.

### Rationale:
- **PageRank** is a foundational algorithm used in various applications, from search engines to social network analysis. Its implementation demonstrates the project’s ability to handle large-scale graph computations.
- **Community Detection** is crucial for identifying clusters within networks, which is a common task in graph analytics. This algorithm showcases the project’s capability to provide insights into the structure of complex networks.

## 4. Data Partitioning Strategy

### Decision:
- A **graph partitioning** strategy was implemented to divide the graph data across multiple nodes in a cluster.

### Rationale:
- Efficient partitioning is key to optimizing the performance of distributed graph algorithms. By dividing the graph into smaller, balanced subgraphs, we can reduce communication overhead and improve computational efficiency.
- The choice of partitioning algorithms (e.g., METIS or random partitioning) depends on the specific use case and graph structure.

## 5. Performance Monitoring and Optimization

### Decision:
- Performance monitoring tools such as **psutil** and **tqdm** were incorporated to track system resources and progress during execution.

### Rationale:
- Monitoring performance is essential to identify bottlenecks and optimize the code. By tracking CPU, memory, and I/O usage, we can make informed decisions on where to focus optimization efforts.
- **tqdm** provides a simple yet effective way to visualize progress in long-running computations, improving the user experience.

## 6. Visualization of Results

### Decision:
- **Matplotlib** was chosen as the primary tool for visualizing graph structures and algorithm results.

### Rationale:
- Visualizing the results of graph algorithms is important for understanding the underlying patterns and insights derived from the data. **Matplotlib** is widely used in the Python ecosystem and integrates seamlessly with **NetworkX**, making it a natural choice.
