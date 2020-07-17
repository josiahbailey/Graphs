from room import Room
from player import Player
from world import World

from util import Stack, Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()
player = Player(world.starting_room)

traversal_path = []
traversal_order = []


def bfs(index, room_id, next_room_id):
    q = Queue()
    visited = set()
    path_to_room = []
    q.en([room_id])

    while q.size() > 0:
        curr_path = q.de()
        curr = curr_path[-1]
        if room_id != next_room_id and (curr == next_room_id or next_room_id in curr_path):
            del curr_path[0]
            path_to_room = reversed(curr_path)
            break
        if curr not in visited:
            visited.add(curr)
            neighbors = world.rooms[curr].get_exits_ids()
            for neighbor in neighbors:
                path_copy = curr_path[:]
                path_copy.append(neighbor)
                q.en(path_copy)
    for path in path_to_room:
        traversal_order.insert(index + 1, path)


def create_order():
    s = Stack()
    s.push(0)
    visited = set()

    while s.size() > 0:
        curr = s.pop()
        traversal_order.append(curr)

        if curr not in visited:
            visited.add(curr)
            neighbors = world.rooms[curr].get_exits_ids()
            neighbors.sort()

            for value in neighbors:
                if value not in visited:
                    s.push(value)


def fill_in_holes():
    j = 0
    while j < (len(traversal_order) - 1):
        room_id = traversal_order[j]
        room = world.rooms[room_id]
        next_room_id = traversal_order[j + 1]
        neighbors = room.get_exits_dir()
        travel_direction = 'x'

        if next_room_id in neighbors:
            travel_direction = neighbors[next_room_id]

        can_travel = room.get_room_in_direction(travel_direction)
        if can_travel is None:
            bfs(j, room_id, next_room_id)
        j += 1

    if j > 500:
        for i in range(j % 11 + 2):
            traversal_order.pop()

    remove_dupes()


def remove_dupes():
    j = 0
    while j < (len(traversal_order) - 1):
        room_id = traversal_order[j]
        next_room_id = traversal_order[j + 1]

        if room_id == next_room_id:
            del traversal_order[j + 1]
        j += 1


def forge_path():
    for i in range(0, len(traversal_order) - 1):
        room_id = traversal_order[i]
        next_room_id = traversal_order[i + 1]
        directions = world.rooms[room_id].get_exits_dir()

        if next_room_id in directions:
            traversal_path.append(directions[next_room_id])


create_order()
fill_in_holes()
forge_path()
print(traversal_order)
# print(traversal_path)

# TRAVERSAL TEST

visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")

# print(world.rooms[300].get_exits())
