import heapq

def prim(graph, start):
    pq = []
    heapq.heappush(pq, (0, start))
    visited = set()
    mst = []
    total_weight = 0

    while pq:
        weight, u = heapq.heappop(pq)
        if u in visited:
            continue

        visited.add(u)
        total_weight += weight
        mst.append((u, weight))

        for v, w in graph[u]:
            if v not in visited:
                heapq.heappush(pq, (w, v))

    return mst, total_weight