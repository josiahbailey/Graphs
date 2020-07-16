"""
1. create an object to house ancestry
2. iterate over ancestors and put the child as the key and the parent as the value
3. iterate over the parents of the starting_node finding the parents of parents until the parents does not exist within the object (this means its the oldest ancestor)
4. iterate over 
"""
from util import Graph, Stack


def earliest_ancestor(ancestors, starting_node):
    # ancestry = {}
    # oldest = set()
    # debth = 0

    # for item in ancestors:
    #     parent = item[0]
    #     child = item[1]
    #     if child not in ancestry:
    #         ancestry[child] = {parent}
    #     else:
    #         ancestry[child].add(parent)

    # if starting_node not in ancestry:
    #     return - 1

    # for item in ancestry[starting_node]:
    #     if item not in ancestry:
    #         oldest.add(item)
    #         parents = None
    #     else:
    #         parents = ancestry[item]
    #     curr_debth = 1
    #     if parents:
    #         while parents != None:
    #             if curr_debth > debth:
    #                 debth = curr_debth
    #                 oldest = set()

    #             curr_debth += 1

    #             for parent in parents:
    #                 if parent not in ancestry and debth == curr_debth:
    #                     if parent in oldest:
    #                         parents = None
    #                     oldest.add(parent)
    #                 elif parent in ancestry:
    #                     # curr_debth += 1
    #                     parents = ancestry[parent]
    #                 else:
    #                     parents = None

    # return oldest

    graph = Graph()
    for parent, child in ancestors:
        graph.add_vertex(parent)
        graph.add_vertex(child)
        graph.add_edge(child, parent)

    s = Stack()
    s.push([starting_node])

    longest = [starting_node]
    visited = set()
    oldest = -1

    while s.size() > 0:
        path = s.pop()
        curr = path[-1]

        if (len(path) > len(longest)) or (len(path) == len(longest) and curr < oldest):
            longest = path
            oldest = longest[-1]

        if curr not in visited:
            visited.add(curr)

            parents = graph.get_neighbors(curr)

            for parent in parents:
                new_path = path + [parent]
                s.push(new_path)

    return oldest


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 1))
