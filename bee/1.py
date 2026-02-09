import numpy as np
from tqdm import tqdm
from glob import glob
import itertools
import matplotlib.pyplot as plt
import math
from yaspin import yaspin

def calculate_distance(city1, city2):
    return np.linalg.norm(np.array(city1) - np.array(city2))
 
def total_distance(route, distances):
    total = 0
    for i in range(len(route) - 1):
        total += distances[route[i], route[i+1]]
    total += distances[route[-1], route[0]]  # Complete the loop
    return total
 
def brute_force_tsp(coords, city_names):
    n = len(coords)
    distances = np.zeros((n, n))
    for i in tqdm(range(n), desc="finding all possible distances", leave=False):
        for j in range(i, n):
            distances[i, j] = distances[j, i] = calculate_distance(coords[i], coords[j])
 
    min_distance = float('inf')
    min_route = None
 
    for route in tqdm(itertools.permutations(range(n)), desc="finding route...", leave=False, total=math.factorial(n)):
        distance = total_distance(route, distances)
        if distance < min_distance:
            min_distance = distance
            min_route = route
 
    return list(min_route), min_distance
path_distance = lambda r,c: np.sum([np.linalg.norm(c[r[p]]-c[r[p-1]]) for p in range(len(r))])
# Reverse the order of all elements from element i to element k in array r.
two_opt_swap = lambda r,i,k: np.concatenate((r[0:i],r[k:-len(r)+i-1:-1],r[k+1:len(r)]))

@yaspin(text="two_opt")
def two_opt(cities,improvement_threshold): # 2-opt Algorithm adapted from https://en.wikipedia.org/wiki/2-opt
    route = np.arange(cities.shape[0]) # Make an array of row numbers corresponding to cities.
    improvement_factor = 1 # Initialize the improvement factor.
    best_distance = path_distance(route,cities) # Calculate the distance of the initial path.
    while improvement_factor > improvement_threshold: # If the route is still improving, keep going!
        distance_to_beat = best_distance # Record the distance at the beginning of the loop.
        for swap_first in range(1,len(route)-2): # From each city except the first and last,
            for swap_last in range(swap_first+1,len(route)): # to each of the cities following,
                new_route = two_opt_swap(route,swap_first,swap_last) # try reversing the order of these cities
                new_distance = path_distance(new_route,cities) # and check the total distance with this modification.
                if new_distance < best_distance: # If the path distance is an improvement,
                    route = new_route # make this the accepted best route
                    best_distance = new_distance # and update the distance corresponding to this route.
        improvement_factor = 1 - best_distance/distance_to_beat # Calculate how much the route has improved.
    return route, best_distance # When the route is no longer improving substantially, stop searching and return the route.

def sol_dispatch(routes, names):
    sol = None
    if math.factorial(len(routes)) > 10**7:
        sol = []
        value_of_func = two_opt(np.array(routes), 0.001)
        # n = len(routes)
        # distances = np.zeros((n, n))
        # for i in tqdm(range(n), desc="finding all possible distances", leave=False):
        #     for j in range(i, n):
        #         distances[i, j] = distances[j, i] = calculate_distance(routes[i], routes[j])
        r = two_opt(np.array(routes), 0.001)

        return r[0], r[1]
    else:
        
        sol = brute_force_tsp(edges, names)

        return sol
# Generate random city coordinates and city names
# np.random.seed(0)
# city_names = ['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Ahmedabad', 'Chennai', 'Kolkata', 'Surat', 'Pune', 'Jaipur']
# num_cities = len(city_names)
# coords_list = [(np.random.randint(1, 100), np.random.randint(1, 100)) for _ in range(num_cities)]
 
# Solve TSP using brute force
# best_route, best_distance = brute_force_tsp(coords_list, city_names)
#
# print('Best Route:', best_route)
# print('Best Distance:', best_distance)
#
# # Plot the cities and the route
# plt.figure(figsize=(8, 6))
# plt.scatter(*zip(*coords_list), color='blue')
# for i, city in enumerate(coords_list):
#     plt.text(city[0], city[1], city_names[i], fontsize=12)
# for i in range(len(best_route) - 1):
#     city1 = coords_list[city_names.index(best_route[i])]
#     city2 = coords_list[city_names.index(best_route[i+1])]
#     plt.plot([city1[0], city2[0]], [city1[1], city2[1]], color='red', linewidth=1)
# plt.plot([coords_list[city_names.index(best_route[-1])][0], coords_list[city_names.index(best_route[0])][0]],
#          [coords_list[city_names.index(best_route[-1])][1], coords_list[city_names.index(best_route[0])][1]], color='red', linewidth=1)  # Complete the loop
# plt.title('Brute Force TSP - Best Route')
# plt.xlabel('X Coordinate')
# plt.ylabel('Y Coordinate')
# plt.grid(True)
# plt.show()
for file in sorted(glob("input_*")):
    with open(file, "r") as f:
        edges = []
        names = []
        for i in f.readlines():
            names.append(i)
            i = i.split(",")
            if len(i) < 2: continue
            i = [x.replace("\n", "") for x in i]
            # print(i)
            i = [int(x) for x in i if x != ""]
            edges.append(i)
        route, distance = sol_dispatch(edges, names)
        print(f"{file}: chemin = {repr(route)}\ndistance = {distance}")
