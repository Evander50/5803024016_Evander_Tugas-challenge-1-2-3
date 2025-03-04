from collections import defaultdict

graph = defaultdict(list)
edges = [('A', 'B'), ('A', 'D'), ('B', 'C'), ('B', 'E'), ('C', 'F'), ('D', 'E'), ('E', 'F')]
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
            if neighbor == start and len(path) > 2:  
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
        return "No paths found"
    
    shortest = min(all_paths, key=len)
    longest = max(all_paths, key=len)
    return shortest, longest

print("Task 1 - All Paths from A to C:")
paths = find_all_paths(graph, 'A', 'C')
print(paths)

print("\nTask 2 - All Cycles starting at C:")
cycles_c = find_all_cycles(graph, 'C')
print(cycles_c)

print("\nTask 3 - All Cycles starting at B:")
cycles_b = find_all_cycles(graph, 'B')
print(cycles_b)

print("\nTask 4 - Shortest and Longest Paths from A to C:")
shortest, longest = find_shortest_longest_paths(graph, 'A', 'C')
print("Shortest Path:", shortest)
print("Longest Path:", longest)