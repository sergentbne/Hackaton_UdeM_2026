import random
import numpy as np
from collections import defaultdict


class HamiltonianPathMonteCarlo:
    def __init__(self, graph):
        """
        graph: adjacency list representation
        e.g., {0: [1, 2], 1: [0, 3], ...}
        """
        self.graph = graph
        self.n = len(graph)

    def random_path(self, start=None):
        """Generate a random permutation path"""
        vertices = list(self.graph.keys())
        if start is not None and start in vertices:
            vertices.remove(start)
            path = [start] + random.sample(vertices, len(vertices))
        else:
            path = random.sample(vertices, len(vertices))
        return path

    def is_valid_path(self, path):
        """Check if the path is a valid Hamiltonian path"""
        # Check all vertices are visited exactly once
        if len(set(path)) != self.n or len(path) != self.n:
            return False

        # Check consecutive vertices are connected
        for i in range(len(path) - 1):
            if path[i + 1] not in self.graph[path[i]]:
                return False
        return True

    def find_path_monte_carlo(self, max_iterations=100000, start=None):
        """
        Monte Carlo search for Hamiltonian path
        Returns (path, iterations_tried)
        """
        for iteration in range(max_iterations):
            # Generate random path
            path = self.random_path(start)

            # Check if it's a valid Hamiltonian path
            if self.is_valid_path(path):
                return path, iteration + 1

        return None, max_iterations

    def find_path_with_restarts(self, trials=1000, path_length=10000, start=None):
        """
        Enhanced version with multiple trials
        """
        best_path = None
        best_iterations = float("inf")

        for trial in range(trials):
            path, iterations = self.find_path_monte_carlo(path_length, start)

            if path is not None:
                # Found a solution
                print(f"Trial {trial + 1}: Found path after {iterations} iterations")
                return path
            else:
                print(f"Trial {trial + 1}: No path found in {iterations} iterations")

        return None


# Example usage
def example_1():
    """Complete graph - always has Hamiltonian paths"""
    graph = {0: [1, 2, 3], 1: [0, 2, 3], 2: [0, 1, 3], 3: [0, 1, 2]}

    solver = HamiltonianPathMonteCarlo(graph)
    path, iterations = solver.find_path_monte_carlo(max_iterations=10000)

    if path:
        print(f"Found Hamiltonian path in {iterations} iterations: {path}")
    else:
        print("No Hamiltonian path found")


def example_2():
    """Path graph - only one Hamiltonian path"""
    graph = {0: [1], 1: [0, 2], 2: [1, 3], 3: [2]}

    solver = HamiltonianPathMonteCarlo(graph)
    # Try with restarts for better chance
    path = solver.find_path_with_restarts(trials=10, path_length=10000)

    if path:
        print(f"Found Hamiltonian path: {path}")
    else:
        print("No Hamiltonian path found")


def example_3():
    """Graph with Hamiltonian path but not obvious"""
    graph = {0: [1, 2], 1: [0, 3], 2: [0, 3, 4], 3: [1, 2, 5], 4: [2, 5], 5: [3, 4]}

    solver = HamiltonianPathMonteCarlo(graph)
    path = solver.find_path_with_restarts(trials=20, path_length=5000)

    if path:
        print(f"Found Hamiltonian path: {path}")
        print("Verification:", solver.is_valid_path(path))
    else:
        print("No Hamiltonian path found")


if __name__ == "__main__":
    print("Example 1: Complete graph K4")
    example_1()
    print("\nExample 2: Path graph")
    example_2()
    print("\nExample 3: Custom graph")
    example_3()
