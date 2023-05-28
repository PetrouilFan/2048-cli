import random
import os
import numpy as np

def fill_with_spaces(num,desierd_len=4):
    num = str(num)
    if len(num) == desierd_len:
        return str(num)
    # write half of the spaces before the number
    to_write = " "*((desierd_len-len(num))//2) + num
    # and the others in the end
    to_write += " "*(desierd_len-len(to_write))
    return to_write
    
class Game:
    def __init__(self,auto_restart=False):
        self.auto_restart = auto_restart
        self.new_game()

    def new_tiles(self):
        '''
        Randomly places a 2 or 4 on the board's empty cells.
        '''
        if self.board_full:
            return
        number = np.random.choice([2,4],p=[0.9,0.1])
        empty_cells = np.where(self.game_board == 0)
        empty_index = random.randint(0,len(empty_cells[0])-1)
        self.game_board[empty_cells[0][empty_index]][empty_cells[1][empty_index]] = number
    
    @property
    def board_full(self):
        return len(np.where(self.game_board == 0)[0]) == 0
    
    def show_board(self):
        os.system("cls" if os.name == "nt" else "clear")
        print(f"Score:  {self.score}\n")
        print(" ____ ____ ____ ____")
        for column in range(4):
            print("|",end="")
            for row in range(4):
                num = self.game_board[column][row]
                # If it is 0 dont write anything
                if num == 0:
                    to_write = fill_with_spaces("")
                else:
                    to_write = fill_with_spaces(num)
                print(to_write,end="|")
            print()
        print(" ---- ---- ---- ----")
        
    def moves(self, event):
        if event == 's' or event == 0:
            for j in range(0, 4):
                shift = 0
                for i in range(3, -1, -1):
                    if self.game_board[i][j] == 0:
                        shift += 1
                    else:
                        if i - 1 >= 0 and self.game_board[i - 1][j] == self.game_board[i][j]:
                            self.game_board[i][j] *= 2
                            self.score += self.game_board[i][j]
                            self.game_board[i - 1][j] = 0
                        elif i - 2 >= 0 and self.game_board[i - 1][j] == 0 and self.game_board[i - 2][j] == self.game_board[i][j]:
                            self.game_board[i][j] *= 2
                            self.score += self.game_board[i][j]
                            self.game_board[i - 2][j] = 0
                        elif i == 3 and self.game_board[2][j] + self.game_board[1][j] == 0 and self.game_board[0][j] == self.game_board[3][
                            j]:
                            self.game_board[3][j] *= 2
                            self.score += self.game_board[3][j]
                            self.game_board[0][j] = 0
                        if shift > 0:
                            self.game_board[i + shift][j] = self.game_board[i][j]
                            self.game_board[i][j] = 0
        elif event == 'd' or event == 1:
            for i in range(0, 4):
                shift = 0
                for j in range(3, -1, -1):
                    if self.game_board[i][j] == 0:
                        shift += 1
                    else:
                        if j - 1 >= 0 and self.game_board[i][j - 1] == self.game_board[i][j]:
                            self.game_board[i][j] *= 2
                            self.score += self.game_board[i][j]
                            self.game_board[i][j - 1] = 0
                        elif j - 2 >= 0 and self.game_board[i][j - 1] == 0 and self.game_board[i][j - 2] == self.game_board[i][j]:
                            self.game_board[i][j] *= 2
                            self.score += self.game_board[i][j]
                            self.game_board[i][j - 2] = 0
                        elif j == 3 and self.game_board[i][2] + self.game_board[i][1] == 0 and self.game_board[0][j] == self.game_board[3][
                            j]:
                            self.game_board[i][3] *= 2
                            self.score += self.game_board[i][3]
                            self.game_board[i][0] = 0
                        if shift > 0:
                            self.game_board[i][j + shift] = self.game_board[i][j]
                            self.game_board[i][j] = 0
        elif event == 'a' or event == 2:
            for i in range(0, 4):
                shift = 0
                for j in range(0, 4):
                    if self.game_board[i][j] == 0:
                        shift += 1
                    else:
                        if j + 1 < 4 and self.game_board[i][j + 1] == self.game_board[i][j]:
                            self.game_board[i][j] *= 2
                            self.score += self.game_board[i][j]
                            self.game_board[i][j + 1] = 0
                        elif j + 2 < 4 and self.game_board[i][j + 1] == 0 and self.game_board[i][j + 2] == self.game_board[i][j]:
                            self.game_board[i][j] *= 2
                            self.score += self.game_board[i][j]
                            self.game_board[i][j + 2] = 0
                        elif j == 0 and self.game_board[i][1] + self.game_board[i][2] == 0 and self.game_board[i][3] == self.game_board[i][
                            0]:
                            self.game_board[i][0] *= 2
                            self.score += self.game_board[i][0]
                            self.game_board[i][3] = 0
                        if shift > 0:
                            self.game_board[i][j - shift] = self.game_board[i][j]
                            self.game_board[i][j] = 0
        elif event == 'w' or event == 3:
            for j in range(0, 4):
                shift = 0
                for i in range(0, 4):
                    if self.game_board[i][j] == 0:
                        shift += 1
                    else:
                        if i + 1 < 4 and self.game_board[i + 1][j] == self.game_board[i][j]:
                            self.game_board[i][j] *= 2
                            self.score += self.game_board[i][j]
                            self.game_board[i + 1][j] = 0
                        elif i + 2 < 4 and self.game_board[i + 1][j] == 0 and self.game_board[i + 2][j] == self.game_board[i][j]:
                            self.game_board[i][j] *= 2
                            self.score += self.game_board[i][j]
                            self.game_board[i + 2][j] = 0
                        elif i == 0 and self.game_board[1][j] + self.game_board[2][j] == 0 and self.game_board[3][j] == self.game_board[0][
                            j]:
                            self.game_board[0][j] *= 2
                            self.score += self.game_board[0][j]
                            self.game_board[3][j] = 0
                        if shift > 0:
                            self.game_board[i - shift][j] = self.game_board[i][j]
                            self.game_board[i][j] = 0
        self.new_tiles()
        if self.auto_restart:
            self.game_over()

    def new_game(self):
        self.score = 0
        self.game_board = np.zeros((4,4),np.int16)
        self.new_tiles()
        self.new_tiles()

    def game_over(self):
        if not self.board_full:
            return False
        
        # Check if there are same numbers in the same row or column next to each other
        for i in range(0, 4):
            for j in range(0, 3):
                if (self.game_board[i][j] == self.game_board[i][j + 1]):
                    return False
        for j in range(0, 4):
            for i in range(0, 3):
                if self.game_board[i][j] == self.game_board[i + 1][j]:
                    return False
                
        if self.auto_restart:
            self.new_game()

        return True

    @property
    def state(self):
        return (self.game_board.copy(), self.score)

    def load_state(self, state):
        self.game_board, self.score = state

if __name__ == "__main__":
    game = Game()
    game.new_game()
    while not game.game_over():
        game.show_board()
        move = input("wasd: ")
        game.moves(move)
    print(game.score)