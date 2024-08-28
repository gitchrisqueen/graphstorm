import os
import time
from datetime import datetime
import psutil
from tqdm import tqdm
from src.algorithms.pagerank import compute_pagerank
from src.utils.graph_loader import load_graph_from_file


def benchmark_pagerank(graph, alpha=0.85, distributed=False):
    start_time = time.time()
    process = psutil.Process(os.getpid())
    start_mem = process.memory_info().rss / (1024 * 1024)  # Memory in MB

    # Compute PageRank
    pagerank_scores = compute_pagerank(graph, alpha=alpha, distributed=distributed)

    end_time = time.time()
    end_mem = process.memory_info().rss / (1024 * 1024)  # Memory in MB

    execution_time = end_time - start_time
    memory_used = end_mem - start_mem

    return execution_time, memory_used


def run_benchmarks():
    # Load the graph
    graph = load_graph_from_file('data/sample_graph_data/graph.edgelist')

    results = []

    # Benchmark local execution
    print("Benchmarking Local PageRank Execution...")
    exec_time, mem_used = benchmark_pagerank(graph, distributed=False)
    results.append(("Local", exec_time, mem_used))

    # Benchmark distributed execution
    print("Benchmarking Distributed PageRank Execution...")
    exec_time, mem_used = benchmark_pagerank(graph, distributed=True)
    results.append(("Distributed", exec_time, mem_used))

    # Save the results to a file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_filename = f"benchmarks/benchmark_report_{timestamp}.txt"

    with open(report_filename, 'w') as report_file:
        report_file.write("Benchmark Report - PageRank Execution\n")
        report_file.write(f"Generated on: {datetime.now()}\n\n")
        report_file.write(f"{'Type':<15} {'Execution Time (s)':<25} {'Memory Used (MB)':<25}\n")
        report_file.write("-" * 65 + "\n")

        for result in results:
            report_file.write(f"{result[0]:<15} {result[1]:<25.4f} {result[2]:<25.2f}\n")

    print(f"Benchmark report saved to {report_filename}")


if __name__ == "__main__":
    run_benchmarks()
