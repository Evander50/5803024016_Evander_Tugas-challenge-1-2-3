from collections import defaultdict

graph = defaultdict(list)
edges = [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'E'), ('C', 'F'), ('D', 'F'), 
         ('D', 'H'), ('E', 'G'), ('F', 'I'), ('G', 'H'), ('I', 'J'), ('J', 'K'), ('H', 'K')]
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)  

def find_all_paths(graph, start, end):
    def dfs(node, end, visited, path, all_paths):
        if node == end:
            all_paths.append(path[:])
            return
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                path.append(neighbor)
                dfs(neighbor, end, visited, path, all_paths)
                path.pop()
                visited.remove(neighbor)

    all_paths = []
    dfs(start, end, {start}, [start], all_paths)
    return all_paths if all_paths else "No paths found"

def find_all_cycles(graph, start):
    def dfs(node, start, visited, path, cycles):
        for neighbor in graph[node]:
            if neighbor == start and len(path) > 2:  # Found a cycle
                cycles.append(path + [start])
            elif neighbor not in visited:
                visited.add(neighbor)
                path.append(neighbor)
                dfs(neighbor, start, visited, path, cycles)
                path.pop()
                visited.remove(neighbor)

    cycles = []
    dfs(start, start, {start}, [start], cycles)
    return cycles if cycles else "No cycles found starting at " + start


def find_shortest_longest_paths(graph, start, end):
    all_paths = find_all_paths(graph, start, end)
    if all_paths == "No paths found":
        return "No paths found", "No paths found"
    
    shortest = min(all_paths, key=len)
    longest = max(all_paths, key=len)
    return shortest, longest


print("Task 1 - All Paths from A to K:")
paths_a_k = find_all_paths(graph, 'A', 'K')
print(paths_a_k)

print("\nTask 2 - All Paths from G to J:")
paths_g_j = find_all_paths(graph, 'G', 'J')
print(paths_g_j)

print("\nTask 3 - All Paths from E to F:")
paths_e_f = find_all_paths(graph, 'E', 'F')
print(paths_e_f)

print("\nTask 4 - All Cycles starting at A:")
cycles_a = find_all_cycles(graph, 'A')
print(cycles_a)

print("\nTask 5 - All Cycles starting at K:")
cycles_k = find_all_cycles(graph, 'K')
print(cycles_k)

print("\nTask 6 - Shortest and Longest Paths from A to K:")
shortest_a_k, longest_a_k = find_shortest_longest_paths(graph, 'A', 'K')
print("Shortest Path:", shortest_a_k)
print("Longest Path:", longest_a_k)

print("\nTask 7 - Shortest and Longest Paths from G to J:")
shortest_g_j, longest_g_j = find_shortest_longest_paths(graph, 'G', 'J')
print("Shortest Path:", shortest_g_j)
print("Longest Path:", longest_g_j)

print("\nTask 8 - Shortest and Longest Paths from E to F:")
shortest_e_f, longest_e_f = find_shortest_longest_paths(graph, 'E', 'F')
print("Shortest Path:", shortest_e_f)
print("Longest Path:", longest_e_f)