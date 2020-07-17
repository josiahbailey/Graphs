from room import Room
from player import Player
from world import World

from util import Stack, Queue

import random
from ast import literal_eval

room_graph = {
    0: [(3, 5), {'n': 1, 's': 5, 'e': 3, 'w': 7}],
    1: [(3, 6), {'s': 0, 'n': 2, 'e': 12, 'w': 15}],
    2: [(3, 7), {'s': 1}],
    3: [(4, 5), {'w': 0, 'e': 4}],
    4: [(5, 5), {'w': 3}],
    5: [(3, 4), {'n': 0, 's': 6}],
    6: [(3, 3), {'n': 5, 'w': 11}],
    7: [(2, 5), {'w': 8, 'e': 0}],
    8: [(1, 5), {'e': 7}],
    9: [(1, 4), {'n': 8, 's': 10}],
    10: [(1, 3), {'n': 9, 'e': 11}],
    11: [(2, 3), {'w': 10, 'e': 6}],
    12: [(4, 6), {'w': 1, 'e': 13}],
    13: [(5, 6), {'w': 12, 'n': 14}],
    14: [(5, 7), {'s': 13}],
    15: [(2, 6), {'e': 1, 'w': 16}],
    16: [(1, 6), {'n': 17, 'e': 15}],
    17: [(1, 7), {'s': 16}]
}

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
# room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

traversal_order = []
s = Stack()
s.push(0)
visited = set()

while s.size() > 0:
    curr = s.pop()
    traversal_order.append(curr)

    if curr not in visited:
        visited.add(curr)
        neighbors = world.rooms[curr].get_exit_ids()
        neighbors.sort()

        for value in neighbors:
            if value not in visited:
                s.push(value)

"""
check if current room can move to next room
p = Player(world.rooms[room_id])

if not p.can_travel(next_room_id):
    neighbors = world.rooms[room_id].get_exit_ids()

    for n in neighbors:
        next_neighbors = world.rooms[n].get_exit_ids()
        for xn in next_neighbors:
            if xn == next_room_id
                traversal_order.insert(i + 1, n)

check all of current room's neighbors for the next room
insert it after current room in array
"""
j = 0
while j < (len(traversal_order) - 1):
    room_id = traversal_order[j]
    next_room_id = traversal_order[j + 1]
    directions = world.rooms[room_id].get_exit_dir()
    direct = ''
    if next_room_id in directions:
        direct = directions[next_room_id]
    else:
        direct = 'y'

    p = Player(world.rooms[room_id])

    if not p.can_travel(direct):
        neighbors = world.rooms[room_id].get_exit_ids()

        for n in neighbors:
            next_neighbors = world.rooms[n].get_exit_ids()
            for xn in next_neighbors:
                if xn == next_room_id:
                    traversal_order.insert(j + 1, n)
    j += 1


traversal_path = []
for i in range(0, len(traversal_order) - 1):
    room_id = traversal_order[i]
    next_room_id = traversal_order[i + 1]
    directions = world.rooms[room_id].get_exit_dir()

    # print(room_id, directions, next_room_id)
    if next_room_id in directions:
        traversal_path.append(directions[next_room_id])

# print(traversal_path)
print(traversal_order)


# traversal_path = []
# s = Stack()
# s.push([0, ''])
# visited = set()

# while s.size() > 0:
#     room = s.pop()
#     curr = room[0]
#     direction = room[1]
#     if player.travel(direction):
#         traversal_path.append(direction)
#     # print(curr, direction)
#     if curr not in visited:
#         visited.add(curr)
#         neighbors = world.rooms[curr].get_exit_ids()

#         for key, value in neighbors.items():
#             s.push([value, key])
#     # else:

# traversal_path.pop(0)
# print(traversal_path)

# grab current room neighbors
# find direction of next room with room.get_exit_dir
# i = 0
# traversal_path = []
# for room_id in traversal_order:
#     directions = world.rooms[room_id].get_exit_dir()
#     next_room_id = traversal_order[i + 1]
#     # print(directions, room_id)
#     if next_room_id in directions:
#         traversal_path.append(next_room_id)
#     if (i + 1) < len(traversal_order):
#         i += 1

# TRAVERSAL TEST

visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    # print(move, player.current_room.id)
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
