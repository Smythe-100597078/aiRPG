from collections import deque


class searches():

    def bfs(self,g, start):
        queue, enqueued = deque([(None, start)]), set([start])
        while queue:
            parent, n = queue.popleft()
            yield parent, n
            new = set(g[n]) - enqueued
            enqueued |= new
            queue.extend([(n, child) for child in new])

    def dfs(self,g, start):
        stack, enqueued = [(None, start)], set([start])
        while stack:
            parent, n = stack.pop()
            yield parent, n
            new = set(g[n]) - enqueued
            enqueued |= new
            stack.extend([(n, child) for child in new])

    def shortest_path(self,g, start, end):
        parents = {}
        for parent, child in self.bfs(g, start):
            parents[child] = parent
            if child == end:
                revpath = [end]
                while True:
                    parent = parents[child]
                    revpath.append(parent)
                    if parent == start:
                        break
                    child = parent
                return list(reversed(revpath))
        return None # or raise appropriate exception

