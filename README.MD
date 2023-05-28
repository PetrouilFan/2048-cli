## 2048-cli

This is a 2048 version of the game designed to run on cli and it can also be used to train AIs.

### Usage for cli game
```python
from game_2048 import Game
# initialize game
game = Game()
game.new_game()

# while the game is not over (board has at least one move)
while not game.game_over():
    # show the latest state of the board
    game.show_board()
    # ask for move
    move = input("wasd: ")
    # update the board with the new move
    game.moves(move)

# after the game ends, print the score
print(game.score)
```

### Info for machine learning
```python
from game_2048 import Game
# initialize game
game = Game() # you can also add auto_restart=True in order to automatically restart when the game is over
game.new_game()

# move can be either "w, a, s, d" or 0,1,2,3 (int) for Up, Left, Down, Right
game.moves(0)

# you can also get the current state of the game with:
state = game.state
board, score = state
'''
that returns a tuple containing the current board and the current score:
(numpy array with shape=(4,4), score)
'''

# you can also load a state with:
game.load_state(state)
# state must be a tuple or list containing a game board and a score
```

#### To Do
- Remove if from move function
 