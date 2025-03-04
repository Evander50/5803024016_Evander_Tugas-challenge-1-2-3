from collections import defaultdict
graph = defaultdict(list)
edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D')]
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)  
def find_trail(graph, start, end):
    def dfs(node, end, visited_edges, path):
        if node == end:
            return path
        for neighbor in graph[node]:
            edge = tuple(sorted([node, neighbor]))
            if edge not in visited_edges:
                visited_edges.add(edge)
                result = dfs(neighbor, end, visited_edges, path + [neighbor])
                if result:
                    return result
                visited_edges.remove(edge)
        return None

    path = dfs(start, end, set(), [start])
    return path if path else "No trail found"

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
    return cycles if cycles else "No cycles found starting at A"

print("Task 1 - Trail from A to D:")
trail = find_trail(graph, 'A', 'D')
print(trail)

print("\nTask 2 - All Paths from A to D:")
paths = find_all_paths(graph, 'A', 'D')
print(paths)

print("\nTask 3 - All Cycles starting at A:")
cycles = find_all_cycles(graph, 'A')
print(cycles)