import random
from util import Stack
# import numpy as np


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Create users
        for i in range(1, num_users + 1):
            self.add_user(i)

        # Create lists of random users for friendships
        high = avg_friendships + 1
        low = avg_friendships / 2
        random_users = [random.randint(1, num_users)
                        for i in range(1, (high * num_users * 2) + 1)]
        random_friends = [random.randint(low, high)
                          for i in range(1, num_users + 1)]

        z = 0  # variable to track random users key

        # Map random friends to users
        for i in range(0, len(random_friends)):
            user_id = i + 1
            num_friends = random_friends[i]

            for x in range(1, num_friends):
                friend_id = random_users[z]
                check = True
                while check == True:
                    if friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id] or friend_id == user_id:
                        z += 1
                        friend_id = random_users[z]
                    else:
                        check = False
                self.add_friendship(user_id, friend_id)
                z += 1

        # print(random_users)
        # print(random_friends)
        # print(self.users)
        # print(self.friendships)

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        s = Stack()
        s.push(user_id)
        visited = set()

        while s.size() > 0:
            curr = s.pop()
            if curr not in visited:
                print(curr)
                visited.add(curr)
                neighbors = self.get_neighbors(curr)

                for neighbor in neighbors:
                    s.push(neighbor)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    # print(sg.friendships)
    # connections = sg.get_all_social_paths(1)
    # print(connections)
