# Kevin Mathew
# Based on "Maze" by Christopher Manson
# "Maze" is book with series of 45 pictured rooms, each with ~4 doors which lead to another page/room
# The goal is to reach the final room (45) and return back to room 1. Doors are one-way.

# Room paths taken from http://www.intotheabyss.net/

from collections import deque

rooms = {
    1: [20, 21, 26, 41],
    2: [12, 22, 29],
    3: [9, 18, 33],
    4: [11, 15, 16, 24, 29, 43, 44],
    5: [20, 22, 30, 43],
    6: [40],
    7: [16, 33, 36],
    8: [6, 12, 29, 31],
    9: [3, 18],
    10: [14, 34, 41],
    11: [24, 40],
    12: [2, 8, 21, 39],
    13: [18, 25, 27],
    14: [10, 24, 43],
    15: [3, 30, 37],
    16: [7, 36],
    17: [6, 33, 45],
    18: [3, 13],
    19: [11, 31],
    20: [1, 5, 27],
    21: [24, 31, 44],
    22: [38, 43],
    23: [8, 19, 28, 45],
    24: [],
    25: [13, 34, 35],
    26: [1, 30, 36, 38],
    27: [9, 13],
    28: [23, 32, 43, 45],
    29: [2, 8, 17, 35, 40],
    30: [5, 15, 34, 42],
    31: [19, 21, 44],
    32: [6, 11, 16, 28],
    33: [3, 7, 35],
    34: [10, 25],
    35: [33],
    36: [7, 16],
    37: [10, 15, 20, 42],
    38: [22, 40, 43],
    39: [4, 11, 12],
    40: [6, 11, 38],
    41: [1, 10, 35, 38],
    42: [4, 22, 25, 30, 37],
    43: [22, 38],
    44: [18, 21],
    45: [17, 19, 23, 28, 36],
}



def bfs_path(rooms, start, goal):
    """Uses a BFS to find the first minimum-length path between start and goal."""
    queue = deque([(start, [start])])  # (current_room, path_so_far)
    visited = set()

    while queue:
        current, path = queue.popleft()
        if current == goal:
            return path
        visited.add(current)
        for neighbor in rooms.get(current, []):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
                visited.add(neighbor)  # prevent re-queuing
    return None


def DFS (rooms):
    current_room = 1
    pass

print(bfs_path(rooms, 1, 45))
print(bfs_path(rooms, 45, 1))