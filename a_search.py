# -*- coding: utf-8 -*-
"""A* Search.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jDDKQzBXNRjo7nYdLnDneXr0cCdRdeW0
"""

import random
from queue import PriorityQueue

# Function to conjure a random NxN matrix with values between 1 and 1000
def create_random_magic_matrix(N):#create_random_magic_matrix(N): This function generates a random square matrix of size N x N,
#where each element is a random number between 1 and 1000. The resulting matrix is like a magical world filled with enchanting values.
    return [[random.randint(1, 1000) for _ in range(N)] for _ in range(N)]

#enchant_matrix(matrix): This function takes a matrix (the magical world) as input and prints it row by row,
#making it appear as if the matrix is enchanted and displaying its mystical contents.
def enchant_matrix(matrix):
    for spell in matrix:
        print("\t".join(map(str, spell)))

# Function to calculate the mystical aura for a given state
def calculate_mystical_aura(state, enchantment, N):#calculate_mystical_aura(state, enchantment, N): This function calculates the mystical aura for a given state
#in the magical world. It considers the row and column of the state, along with the difference between the column and the last column (N-1), and the value at that state. It's as if the state possesses a unique magical aura.
    row, col = state
    return abs(row) + abs(col - (N - 1)) + abs(matrix[row][col] - enchantment)

# Function to embark on the Quest for the Holy Grail
def embark_on_holy_quest(matrix, enchantment):#embark_on_holy_quest(matrix, enchantment): This function is where the adventure begins. It takes the
#magical world (matrix) and an enchantment value to search for. The quest unfolds in this function, with heroes, quests, and mystical energies.
    N = len(matrix)
    starting_location = (0, N - 1)
    # legendary_destination: The final destination in the quest, where the enchantment is found. It's like finding the Holy Grail in a medieval legend.
    legendary_destination = None
#quest_log: A dictionary that keeps track of the quest's progress. It stores information about each step in the adventure, helping to retrace the path later.
    quest_log = {}  # To store the quest log
    magic_portal = PriorityQueue()
    #magic_portal: A priority queue that keeps track of the locations to explore next. Locations are prioritized based on the mystical energies they possess, guiding the quest in the most magical way.
    magic_portal.put((0, starting_location))
    #heroism_levels: A dictionary that stores the heroism levels of each location in the magical world. Heroism levels increase as the heroes (the questers) embark on their adventure.
    heroism_levels = {starting_location: 0}

    while not magic_portal.empty():
        _, current_location = magic_portal.get()

        if matrix[current_location[0]][current_location[1]] == enchantment:
            legendary_destination = current_location
            break

        # Possible movements (left, up, down)
        # adventure_path: A list that stores the locations visited during the quest, creating a magical adventure path from the starting location to the legendary destination.
        heroic_moves = [(0, -1), (-1, 0), (1, 0)]
        for heroic_move in heroic_moves:
            new_location = (current_location[0] + heroic_move[0], current_location[1] + heroic_move[1])

            if (
                0 <= new_location[0] < N
                and 0 <= new_location[1] < N
            ):
                new_heroism = heroism_levels[current_location] + (2 if heroic_move == (0, -1) else 1)

                if new_location not in heroism_levels or new_heroism < heroism_levels[new_location]:
                    heroism_levels[new_location] = new_heroism
                    #calculate_mystical_aura(state, enchantment, N): This function computes the mystical aura of a state in the magical world, combining various magical factors.
                    mystical_energy = new_heroism + calculate_mystical_aura(new_location, enchantment, N)
                    magic_portal.put((mystical_energy, new_location))
                    quest_log[new_location] = current_location

    # Map out the adventure path
    adventure_path = [legendary_destination]
    while legendary_destination != starting_location:
        legendary_destination = quest_log[legendary_destination]
        adventure_path.append(legendary_destination)
    adventure_path.reverse()

    return adventure_path

# Input
N = int(input("Enter the size of your imaginary world (5, 6, or 7): "))
#create_random_magic_matrix(N): This function conjures a random magical matrix filled with enchanting numbers. It sets the stage for the adventure.
matrix = create_random_magic_matrix(N)
#enchant_matrix(matrix): This function adds a touch of enchantment to the matrix, displaying it in a visually appealing way.
enchant_matrix(matrix)
enchantment = int(input("Choose a mystical number to search for: "))

if N not in [5, 6, 7]:
    print("Sorry, your imaginary world size must be 5, 6, or 7.")
else:#embark_on_holy_quest(matrix, enchantment): This is where the true adventure begins. It guides the questers through the magical world in search of the enchantment.
    epic_quest_path = embark_on_holy_quest(matrix, enchantment)

    # Output the adventure log
    print("The Magical Path taken to reach the mystical number", enchantment, "from the starting point:")
    for step in epic_quest_path:
        print(f"Teleport to Row: {step[0]}, Column: {step[1]}")