import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


parent = list(range(n + 1))
size = [1] * (n + 1)
active = [False] * (n + 1)


def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return False

    if size[a] < size[b]:
        a, b = b, a

    parent[b] = a
    size[a] += size[b]

    return True


components = 0
answer = 0

for u in range(n, 1, -1):
    active[u] = True
    components += 1

    for v in graph[u]:
        if active[v]:
            if union(u, v):
                components -= 1

    answer += components

print(answer)
