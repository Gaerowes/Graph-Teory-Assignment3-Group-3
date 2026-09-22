import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    graph = [set() for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].add(b)
        graph[b].add(a)

    # Eulerian circuit requires every vertex to have even degree.
    for vertex in range(1, n + 1):
        if len(graph[vertex]) % 2 != 0:
            print("IMPOSSIBLE")
            return

    # Check that every vertex with an edge is connected to vertex 1.
    visited = [False] * (n + 1)
    stack = [1]
    visited[1] = True

    while stack:
        vertex = stack.pop()

        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)

    for vertex in range(1, n + 1):
        if graph[vertex] and not visited[vertex]:
            print("IMPOSSIBLE")
            return

    seen = [0] * (n + 1)
    visit_id = 0
    known_bridge = set()
    base = n + 1

    def edge_key(a, b):
        if a > b:
            a, b = b, a
        return a * base + b

    # Check if an edge is a bridge by searching for another path.
    def is_bridge(a, b):
        nonlocal visit_id
        key = edge_key(a, b)

        if key in known_bridge:
            return True

        # If one endpoint only has this edge, it must be a bridge.
        if len(graph[a]) == 1 or len(graph[b]) == 1:
            known_bridge.add(key)
            return True

        # Start from the endpoint with fewer remaining edges.
        if len(graph[b]) < len(graph[a]):
            start, target = b, a
        else:
            start, target = a, b

        visit_id += 1
        seen[start] = visit_id
        stack = [start]

        while stack:
            vertex = stack.pop()
            for neighbor in graph[vertex]:

                # Ignore the edge currently being tested.
                if vertex == start and neighbor == target:
                    continue

                if seen[neighbor] == visit_id:
                    continue

                # Another path exists, so this edge is not a bridge.
                if neighbor == target:
                    return False

                seen[neighbor] = visit_id
                stack.append(neighbor)

        known_bridge.add(key)
        return True

    route = [1]
    current = 1

    for _ in range(m):

        # If only one edge remains, Fleury must take it.
        if len(graph[current]) == 1:
            next_vertex = next(iter(graph[current]))

        else:
            next_vertex = None

            # Fleury: choose a non-bridge edge if possible.
            for neighbor in graph[current]:
                if not is_bridge(current, neighbor):
                    next_vertex = neighbor
                    break

            # A bridge is allowed only when there is no alternative.
            if next_vertex is None:
                next_vertex = next(iter(graph[current]))

        graph[current].remove(next_vertex)
        graph[next_vertex].remove(current)

        current = next_vertex
        route.append(current)

    if current != 1 or len(route) != m + 1:
        print("IMPOSSIBLE")
        return

    sys.stdout.write(" ".join(map(str, route)))
solve()