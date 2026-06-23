from abc import ABC, abstractmethod
import random


class Player(ABC):
    def __init__(self):
        # Available moves (will be defined by child classes)
        self.moves = []

        # Starting position
        self.position = (0, 0)

        # Store movement history
        self.path = [self.position]

    def make_move(self):
        # Select a random move
        move = random.choice(self.moves)

        # Current position
        x, y = self.position

        # Selected movement
        move_x, move_y = move

        # Update position
        self.position = (x + move_x, y + move_y)

        # Save new position in path
        self.path.append(self.position)

        return self.position

    @abstractmethod
    def level_up(self):
        pass


class Pawn(Player):
    def __init__(self):
        # Call Player constructor
        super().__init__()

        # Normal movements:
        # up, down, left, right
        self.moves = [
            (0, 1),    # Up
            (0, -1),   # Down
            (-1, 0),   # Left
            (1, 0)     # Right
        ]

    def level_up(self):
        # Add diagonal movements
        self.moves.extend([
            (1, 1),     # Up-right
            (1, -1),    # Down-right
            (-1, 1),    # Up-left
            (-1, -1)    # Down-left
        ])


# Program Execution
pawn = Pawn()

print("Initial position:")
print(pawn.position)

print("\nAvailable moves:")
print(pawn.moves)


print("\nMaking moves:")

for i in range(5): # you can make more moves as well e.g 6,10 etc
    new_position = pawn.make_move()
    print(f"Move {i+1}: {new_position}")


print("\nPath taken:")
print(pawn.path)


print("\nLeveling up pawn...")
pawn.level_up()


print("\nNew available moves:")
print(pawn.moves)


print("\nMaking diagonal moves:")

for i in range(5):
    new_position = pawn.make_move()
    print(f"Move {i+1}: {new_position}")


print("\nFinal path:")
print(pawn.path)

