"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        arr = []

        for item in self.vertices[vertex_id]:
            arr.append(item)

        return arr

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.en(starting_vertex)
        visited = set()

        while q.size() > 0:
            curr = q.de()
            if curr not in visited:
                visited.add(curr)

            neighbors = self.get_neighbors(curr)

            for neighbor in neighbors:
                if neighbor not in visited:
                    q.en(neighbor)

        for x in visited:
            print(x)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)
        visited = set()

        while s.size() > 0:
            curr = s.pop()
            if curr not in visited:
                print(curr)
                visited.add(curr)
                neighbors = self.get_neighbors(curr)

                for neighbor in neighbors:
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        print(starting_vertex)
        visited.add(starting_vertex)
        neighbors = self.get_neighbors(starting_vertex)
        for neighbor in neighbors:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.

        for v of graph.vertexes:
            v.color = white

        startVert.color = gray
            queue.enqueue(startVert)

        while !queue.isEmpty():
            u = queue[0]  // Peek at head of the queue, but do not dequeue!

            for v of u.neighbors:
                if v.color == white:
                    v.color = gray
                    queue.enqueue(v)

            queue.dequeue()
            u.color = black
        """
        # output = []
        # q = Queue()
        # visited = {}
        # curr = starting_vertex

        # while curr != None:
        #     output.append(curr)
        #     if curr == destination_vertex:
        #         break
        #     visited[curr] = curr
        #     neighbors = self.get_neighbors(curr)
        #     for item in neighbors:
        #         if item not in visited:
        #             q.en(item)
        #     curr = q.de()

        # return output
        q = Queue()
        visited = set()
        path = [starting_vertex]
        q.en(path)

        while q.size() > 0:
            curr_path = q.de()
            curr = curr_path[-1]
            if curr == destination_vertex:
                return curr_path
            if curr not in visited:
                visited.add(curr)
                neighbors = self.get_neighbors(curr)
                for neighbor in neighbors:
                    path_copy = curr_path[:]
                    path_copy.append(neighbor)

                    q.en(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # s = Stack()
        # visited = {starting_vertex: starting_vertex}
        # curr = starting_vertex
        # s.push(curr)

        # while curr != None:
        #     prev = curr
        #     visited[curr] = curr
        #     neighbors = self.get_neighbors(curr)
        #     for item in neighbors:
        #         if item not in visited:
        #             s.push(item)
        #             curr = item
        #             break

        #     if curr == destination_vertex:
        #         break

        #     if curr == prev:
        #         curr = s.pop()

        # return [*s.stack]
        s = Stack()
        visited = set()
        path = [starting_vertex]
        s.push(path)

        while s.size() > 0:
            curr_path = s.pop()
            curr = curr_path[-1]
            if curr == destination_vertex:
                return curr_path
            if curr not in visited:
                visited.add(curr)
                neighbors = self.get_neighbors(curr)
                for neighbor in neighbors:
                    path_copy = curr_path[:]
                    path_copy.append(neighbor)

                    s.push(path_copy)

    def dfs_recursive(self, vertex, destination_vertex, path=[], visited=set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        visited.add(vertex)
        if len(path) < 1:
            path.append(vertex)
        if vertex == destination_vertex:
            return path

        neighbors = self.get_neighbors(vertex)
        for neighbor in neighbors:
            if neighbor not in visited:
                result = self.dfs_recursive(
                    neighbor, destination_vertex, path + [neighbor], visited)
                if result is not None:
                    return result


graph = Graph()

graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
graph.add_vertex(5)
graph.add_vertex(6)
graph.add_vertex(7)

graph.add_edge(5, 3)
graph.add_edge(6, 3)
graph.add_edge(7, 1)
graph.add_edge(4, 7)
graph.add_edge(1, 2)
graph.add_edge(7, 6)
graph.add_edge(2, 4)
graph.add_edge(3, 5)
graph.add_edge(2, 3)
graph.add_edge(4, 6)

# print(graph.dft_recursive(1))
# print(graph.bfs(1, 6))

# graph = Graph()
# graph.add_vertex('hi')
# graph.add_vertex('bye')
# graph.add_vertex('hello')
# graph.add_edge('hi', 'bye')
# graph.add_edge('hi', 'hello')
# print(graph.get_neighbors('hi'))


# if __name__ == '__main__':
#     graph = Graph()  # Instantiate your graph
#     # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
#     graph.add_vertex(1)
#     graph.add_vertex(2)
#     graph.add_vertex(3)
#     graph.add_vertex(4)
#     graph.add_vertex(5)
#     graph.add_vertex(6)
#     graph.add_vertex(7)
#     graph.add_edge(5, 3)
#     graph.add_edge(6, 3)
#     graph.add_edge(7, 1)
#     graph.add_edge(4, 7)
#     graph.add_edge(1, 2)
#     graph.add_edge(7, 6)
#     graph.add_edge(2, 4)
#     graph.add_edge(3, 5)
#     graph.add_edge(2, 3)
#     graph.add_edge(4, 6)

#     '''
#     Should print:
#         {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
#     '''
#     print(graph.vertices)

#     '''
#     Valid BFT paths:
#         1, 2, 3, 4, 5, 6, 7
#         1, 2, 3, 4, 5, 7, 6
#         1, 2, 3, 4, 6, 7, 5
#         1, 2, 3, 4, 6, 5, 7
#         1, 2, 3, 4, 7, 6, 5
#         1, 2, 3, 4, 7, 5, 6
#         1, 2, 4, 3, 5, 6, 7
#         1, 2, 4, 3, 5, 7, 6
#         1, 2, 4, 3, 6, 7, 5
#         1, 2, 4, 3, 6, 5, 7
#         1, 2, 4, 3, 7, 6, 5
#         1, 2, 4, 3, 7, 5, 6
#     '''
#     graph.bft(1)

#     '''
#     Valid DFT paths:
#         1, 2, 3, 5, 4, 6, 7
#         1, 2, 3, 5, 4, 7, 6
#         1, 2, 4, 7, 6, 3, 5
#         1, 2, 4, 6, 3, 5, 7
#     '''
#     graph.dft(1)
#     graph.dft_recursive(1)

#     '''
#     Valid BFS path:
#         [1, 2, 4, 6]
#     '''
#     print(graph.bfs(1, 6))

#     '''
#     Valid DFS paths:
#         [1, 2, 4, 6]
#         [1, 2, 4, 7, 6]
#     '''
#     print(graph.dfs(1, 6))
#     print(graph.dfs_recursive(1, 6))
