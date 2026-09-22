import sys

input = sys.stdin.readline


def iterative_euler(graph, edges, degree, start):
    used = [False] * len(edges)

    stack = [start]
    path = []

    while stack:
        current = stack[-1]

        while graph[current] and used[graph[current][-1]]:
            graph[current].pop()

        if not graph[current]:
            path.append(stack.pop())
        else:
            edge_id = graph[current].pop()

            if used[edge_id]:
                continue

            used[edge_id] = True

            u, v = edges[edge_id]

            if u == current:
                next_vertex = v
            else:
                next_vertex = u

            stack.append(next_vertex)

    return path[::-1]


def solve():
    n, m = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    edges = []
    degree = [0] * (n + 1)

    for edge_id in range(m):
        u, v = map(int, input().split())

        edges.append((u, v))

        graph[u].append(edge_id)
        graph[v].append(edge_id)

        degree[u] += 1
        degree[v] += 1

    # Semua degree harus genap
    for vertex in range(1, n + 1):
        if degree[vertex] % 2 != 0:
            print("IMPOSSIBLE")
            return

    path = iterative_euler(
        graph,
        edges,
        degree,
        1
    )

    # Harus menggunakan semua edge
    if len(path) != m + 1:
        print("IMPOSSIBLE")
        return

    # Harus kembali ke node 1
    if path[0] != 1 or path[-1] != 1:
        print("IMPOSSIBLE")
        return

    print(*path)


if __name__ == "__main__":
    solve()