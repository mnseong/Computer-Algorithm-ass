class MinHeap:
    def __init__(self, heap=None):
        self.heap = [] if heap is None else heap
        self._heapify()

    def push(self, item):
        self.heap.append(item)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        last = len(self.heap) - 1
        self._swap(0, last)
        item = self.heap.pop()
        self._sift_down(0)
        return item

    def peek(self):
        return self.heap[0]

    def __len__(self):
        return len(self.heap)

    def _heapify(self):
        n = len(self.heap)
        for i in reversed(range(n // 2)):
            self._sift_down(i)

    def _sift_up(self, pos):
        parent_pos = (pos - 1) // 2
        if pos > 0 and self.heap[pos] < self.heap[parent_pos]:
            self._swap(pos, parent_pos)
            self._sift_up(parent_pos)

    def _sift_down(self, pos):
        child_pos = 2 * pos + 1
        if child_pos >= len(self.heap):
            return
        if child_pos + 1 < len(self.heap) and self.heap[child_pos + 1] < self.heap[child_pos]:
            child_pos += 1
        if self.heap[child_pos] < self.heap[pos]:
            self._swap(child_pos, pos)
            self._sift_down(child_pos)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


def prim(graph, start):
    visited = [False] * (len(graph))
    distance = [float('inf')] * (len(graph))
    distance[start] = 0
    pq = MinHeap()
    pq.push((0, start))
    while pq:
        dist, node = pq.pop()
        visited[node] = True
        for v, w in graph[node]:
            if not visited[v] and w < distance[v]:
                distance[v] = w
                pq.push((w, v))
    return distance


n, s1, s2 = map(int, input().split())
s1 -= 1
s2 -= 1
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append((v, w))
    graph[v].append((u, w))

mst = prim(graph, s1)

contaminated = [False] * n
priority_queue = MinHeap()
priority_queue.push((0, s1))
priority_queue.push((0, s2))

while priority_queue:
    time, vertex = priority_queue.pop()
    if contaminated[vertex]:
        continue
    contaminated[vertex] = True
    if vertex not in [s1, s2]:
        print(vertex + 1)
    for v, w in graph[vertex]:
        if not contaminated[v]:
            priority_queue.push((time + w, v))
