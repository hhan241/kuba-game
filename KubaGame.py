# Author: Hongliu Han
# Date: 6/7/2021
# Description: This program is a board game called Kuba. Game ends when a player wins. Rules to move a marble: You need
# an empty space(or the edge of the board) on the side you are pushing away from; A player cannot undo a move the
# opponent just made (if it leads to the exact same board position). A players wins by pushing off and capturing seven
# neutral red stones or by pushing off all of the opposing stones. A player who has no legal moves available has lost
# the game.

import copy


class KubaGame:
    """Represents a board game called Kuba between two players. It has the function that checks if the move is valid.
    If valid, it updates the board, the turn, the winner, the number of marbles in each color. It also has the
    functions that return the current turn, the winner, the red marbles captured by the player, the marble that is
    present at the location and the counts of marbles in each color as tuple. This class does not communicate with
    other classes."""

    def __init__(self, tuple_1, tuple_2):
        """The function takes as its parameters two tuples and doesn't return any value. It Initializes all data
        members."""
        self._tuple_1 = tuple_1
        self._tuple_2 = tuple_2
        self._current_turn = None  # Initializes the current turn with None
        self._winner = None  # Initializes the winner with None
        self._tuple_1_player_captured_marbles = 0  # Initializes the red marbles captured by the first player with 0
        self._tuple_2_player_captured_marbles = 0  # Initializes the red marbles captured by the second player with 0
        self._tuple_1_player_marbles = 8  # Initializes the first player's marbles with 8
        self._tuple_2_player_marbles = 8  # Initializes the second player's marbles with 8
        self._white_marbles = 8  # Initializes the white marbles with 8
        self._black_marbles = 8  # Initializes the black marbles with 8
        self._red_marbles = 13  # Initializes the red marbles with 13
        self._board = [["W", "W", "", "", "", "B", "B"], ["W", "W", "", "R", "", "B", "B"],
                       ["", "", "R", "R", "R", "", ""], ["", "R", "R", "R", "R", "R", ""],
                       ["", "", "R", "R", "R", "", ""], ["B", "B", "", "R", "", "W", "W"],
                       ["B", "B", "", "", "", "W", "W"]]
        self._deepcopy_board_list = []    # Initializes the deepcopy board list to an empty list

    def get_current_turn(self):
        """The function doesn't take any parameters and returns current turn."""
        return self._current_turn

    def undo_opponent(self):
        """Checks if it undoes a move the opponent just made. If yes, return False."""
        for i in range(len(self._deepcopy_board_list)):
            if i > 1:
                if self._deepcopy_board_list[i - 2] == self._deepcopy_board_list[i]:
                    self._board = self._deepcopy_board_list[i - 1]
                    return False

    def make_move(self, playername, coordinates, direction):
        """The function takes three parameters playername, coordinates, and direction. It checks if the move is valid,
        returns True for valid move and False for invalid move. If the move is valid, it makes the move and updates
        the turn, the winner, the board and the number of marbles for each color."""

        # If the game has been won, return False
        if self._winner is not None:
            return False

        # If the coordinates are out of range, return False.
        if coordinates[0] > 6 or coordinates[1] > 6:
            return False

        # If there is no marble in that coordinates, return False.
        if self._board[coordinates[0]][coordinates[1]] == "":
            return False

        # If it is not the player's turn or it is not the player's marble, return False.
        if playername == self._tuple_1[0]:
            if self._current_turn is not None and self._current_turn != playername:
                return False
            if self._board[coordinates[0]][coordinates[1]] != self._tuple_1[1]:
                return False

        if playername == self._tuple_2[0]:
            if self._current_turn is not None and self._current_turn != playername:
                return False
            if self._board[coordinates[0]][coordinates[1]] != self._tuple_2[1]:
                return False

        if direction == "B":
            # There's an empty space(or edge of board) on the side player is pushing away from, the marble can be moved.
            if coordinates[0] == 0 or self._board[coordinates[0] - 1][coordinates[1]] == "":
                # Updates the turn
                if playername == self._tuple_1[0]:
                    self._current_turn = self._tuple_2[0]
                if playername == self._tuple_2[0]:
                    self._current_turn = self._tuple_1[0]

                # If there are empty spaces in the same direction that the marble is pushed.
                # If the first empty location is right after the marble that is pushed, update the board.
                if coordinates[0] < 6 and self._board[coordinates[0] + 1][coordinates[1]] == "":
                    for i in range(1, -1, -1):
                        if i > 0:
                            self._board[coordinates[0]+i][coordinates[1]] = \
                                self._board[coordinates[0]+i-1][coordinates[1]]
                    self._board[coordinates[0]][coordinates[1]] = ""

                # If the first empty location is the second space after the marble that is pushed, update the board.
                elif coordinates[0] < 5 and self._board[coordinates[0] + 2][coordinates[1]] == "":
                    for i in range(2, -1, -1):
                        if i > 0:
                            self._board[coordinates[0]+i][coordinates[1]] = \
                                self._board[coordinates[0]+i-1][coordinates[1]]
                    self._board[coordinates[0]][coordinates[1]] = ""

                # If the first empty location is the third space after the marble that is pushed, update the board.
                elif coordinates[0] < 4 and self._board[coordinates[0] + 3][coordinates[1]] == "":
                    for i in range(3, -1, -1):
                        if i > 0:
                            self._board[coordinates[0]+i][coordinates[1]] = \
                                self._board[coordinates[0]+i-1][coordinates[1]]
                    self._board[coordinates[0]][coordinates[1]] = ""

                # If the first empty location is the fourth space after the marble that is pushed, update the board.
                elif coordinates[0] < 3 and self._board[coordinates[0] + 4][coordinates[1]] == "":
                    for i in range(4, -1, -1):
                        if i > 0:
                            self._board[coordinates[0]+i][coordinates[1]] = \
                                self._board[coordinates[0]+i-1][coordinates[1]]
                    self._board[coordinates[0]][coordinates[1]] = ""

                # If the first empty location is the fifth space after the marble that is pushed, update the board.
                elif coordinates[0] < 2 and self._board[coordinates[0] + 5][coordinates[1]] == "":
                    for i in range(5, -1, -1):
                        if i > 0:
                            self._board[coordinates[0]+i][coordinates[1]] = \
                                self._board[coordinates[0]+i-1][coordinates[1]]
                    self._board[coordinates[0]][coordinates[1]] = ""

                # If the first empty location is the sixth space after the marble that is pushed, update the board.
                elif coordinates[0] < 1 and self._board[coordinates[0] + 6][coordinates[1]] == "":
                    for i in range(6, -1, -1):
                        if i > 0:
                            self._board[coordinates[0]+i][coordinates[1]] = \
                                self._board[coordinates[0]+i-1][coordinates[1]]
                    self._board[coordinates[0]][coordinates[1]] = ""

                # If there are no empty spaces in the same direction that the marble is pushed.
                else:
                    # If the last marble is red, update the red marbles captured by each player and red marble left.
                    if self._board[6][coordinates[1]] == "R":
                        if playername == self._tuple_1[0]:
                            self._tuple_1_player_captured_marbles += 1
                            if self._tuple_1_player_captured_marbles == 7:
                                self._winner = playername                    # Updates the winner.
                        if playername == self._tuple_2[0]:
                            self._tuple_2_player_captured_marbles += 1
                            if self._tuple_2_player_captured_marbles == 7:
                                self._winner = playername                    # Updates the winner.
                        self._red_marbles -= 1

                    # If the last marble is white, update the number of white marble left on the board accordingly.
                    if self._board[6][coordinates[1]] == "W":
                        if playername == self._tuple_1[0]:
                            return False
                        else:
                            self._white_marbles -= 1

                    # If the last marble is black, update the number of black marble left on the board accordingly.
                    if self._board[6][coordinates[1]] == "B":
                        if playername == self._tuple_2[0]:
                            return False
                        else:
                            self._black_marbles -= 1

                    # Updates the board
                    if coordinates[0] == 5:  # if the space chosen by the user are on the sixth row
                        for i in range(1, -1, -1):
                            self._board[coordinates[0] + i][coordinates[1]] = \
                                self._board[coordinates[0] + i - 1][coordinates[1]]

                    if coordinates[0] == 4:  # if the space chosen by the user are on the fifth row
                        for i in range(2, -1, -1):
                            self._board[coordinates[0] + i][coordinates[1]] = \
                                self._board[coordinates[0] + i - 1][coordinates[1]]

                    if coordinates[0] == 3:  # if the space chosen by the user are on the fourth row
                        for i in range(3, -1, -1):
                            self._board[coordinates[0] + i][coordinates[1]] = \
                                self._board[coordinates[0] + i - 1][coordinates[1]]

                    if coordinates[0] == 2:  # if the space chosen by the user are on the third row
                        for i in range(4, -1, -1):
                            self._board[coordinates[0] + i][coordinates[1]] = \
                                self._board[coordinates[0] + i - 1][coordinates[1]]

                    if coordinates[0] == 1:  # if the space chosen by the user are on the second row
                        for i in range(5, -1, -1):
                            self._board[coordinates[0] + i][coordinates[1]] = \
                                self._board[coordinates[0] + i - 1][coordinates[1]]

                    if coordinates[0] == 0:  # if the space chosen by the user are on the first row
                        for i in range(6, -1, -1):
                            if i > 0:
                                self._board[coordinates[0] + i][coordinates[1]] = \
                                    self._board[coordinates[0] + i - 1][coordinates[1]]
                    self._board[coordinates[0]][coordinates[1]] = ""

                # Checks if it undoes a move the opponent just made. If yes, update the turn and deepcopy board list.
                self._deepcopy_board_list.append(copy.deepcopy(self._board))
                if self.undo_opponent() is False:
                    self._current_turn = playername
                    self._deepcopy_board_list.remove(copy.deepcopy(self._board))
                    return False

                return True
            else:
                return False

        if direction == "F":
            # There's an empty space(or edge of board) on the side player is pushing away from, the marble can be moved.
            if coordinates[0] == 6 or self._board[coordinates[0] + 1][coordinates[1]] == "":
                # Updates the turn
                if playername == self._tuple_1[0]:
                    self._current_turn = self._tuple_2[0]
                if playername == self._tuple_2[0]:
                    self._current_turn = self._tuple_1[0]

                # If there are empty spaces in the same direction that the marble is pushed.
                # If the first empty location is right after the marble that is pushed, update the board.
                if coordinates[0] > 0 and self._board[coordinates[0] - 1][coordinates[1]] == "":
                    for i in range(1, -1, -1):
                        if i > 0:
                            self._board[coordinates[0]-i][coordinates[1]] = \
                                self._board[coordinates[0]-i+1][coordinates[1]]
                    self._board[coordinates[0]][coordinates[1]] = ""

                # If the first empty location is the second space after the marble that is pushed, update the board.
                elif coordinates[0] > 1 and self._board[coordinates[0] - 2][coordinates[1]] == "":
                    for i in range(2, -1, -1):
                        if i > 0:
                            self._board[coordinates[0]-i][coordinates[1]] = \
                                self._board[coordinates[0]-i+1][coordinates[1]]
                    self._board[coordinates[0]][coordinates[1]] = ""

                # If the first empty location is the third space after the marble that is pushed, update the board.
                elif coordinates[0] > 2 and self._board[coordinates[0] - 3][coordinates[1]] == "":
                    for i in range(3, -1, -1):
                        if i > 0:
                            self._board[coordinates[0]-i][coordinates[1]] = \
                                self._board[coordinates[0]-i+1][coordinates[1]]
                    self._board[coordinates[0]][coordinates[1]] = ""

                # If the first empty location is the fourth space after the marble that is pushed, update the board.
                elif coordinates[0] > 3 and self._board[coordinates[0] - 4][coordinates[1]] == "":
                    for i in range(4, -1, -1):
                        if i > 0:
                            self._board[coordinates[0]-i][coordinates[1]] = \
                                self._board[coordinates[0]-i+1][coordinates[1]]
                    self._board[coordinates[0]][coordinates[1]] = ""

                # If the first empty location is the fifth space after the marble that is pushed, update the board.
                elif coordinates[0] > 4 and self._board[coordinates[0] - 5][coordinates[1]] == "":
                    for i in range(5, -1, -1):
                        if i > 0:
                            self._board[coordinates[0]-i][coordinates[1]] = \
                                self._board[coordinates[0]-i+1][coordinates[1]]
                    self._board[coordinates[0]][coordinates[1]] = ""

                # If the first empty location is the sixth space after the marble that is pushed, update the board.
                elif coordinates[0] > 5 and self._board[coordinates[0] - 6][coordinates[1]] == "":
                    for i in range(6, -1, -1):
                        if i > 0:
                            self._board[coordinates[0]-i][coordinates[1]] = \
                                self._board[coordinates[0]-i+1][coordinates[1]]
                    self._board[coordinates[0]][coordinates[1]] = ""

                # If there are no empty spaces in the same direction that the marble is pushed.
                else:
                    # If the last marble is red, update the red marbles captured by each player and red marble left.
                    if self._board[0][coordinates[1]] == "R":
                        if playername == self._tuple_1[0]:
                            self._tuple_1_player_captured_marbles += 1
                            if self._tuple_1_player_captured_marbles == 7:
                                self._winner = playername                # Updates the winner
                        if playername == self._tuple_2[0]:
                            self._tuple_2_player_captured_marbles += 1
                            if self._tuple_2_player_captured_marbles == 7:
                                self._winner = playername                # Updates the winner
                        self._red_marbles -= 1

                    # If the last marble is white, update the number of white marble left on the board accordingly.
                    if self._board[0][coordinates[1]] == "W":
                        if playername == self._tuple_1[0]:
                            return False
                        else:
                            self._white_marbles -= 1

                    # If the last marble is black, update the number of black marble left on the board accordingly.
                    if self._board[0][coordinates[1]] == "B":
                        if playername == self._tuple_2[0]:
                            return False
                        else:
                            self._black_marbles -= 1

                    # Updates the board
                    if coordinates[0] == 1:  # if the space chosen by the user are on the second row
                        for i in range(1, -1, -1):
                            self._board[coordinates[0] - i][coordinates[1]] = \
                                self._board[coordinates[0] - i + 1][coordinates[1]]

                    if coordinates[0] == 2:  # if the coordinates chosen by the user are on the third row
                        for i in range(2, -1, -1):
                            self._board[coordinates[0] - i][coordinates[1]] = \
                                self._board[coordinates[0] - i + 1][coordinates[1]]

                    if coordinates[0] == 3:  # if the coordinates chosen by the user are on the fourth row
                        for i in range(3, -1, -1):
                            self._board[coordinates[0] - i][coordinates[1]] = \
                                self._board[coordinates[0] - i + 1][coordinates[1]]

                    if coordinates[0] == 4:  # if the coordinates chosen by the user are on the fifth row
                        for i in range(4, -1, -1):
                            self._board[coordinates[0] - i][coordinates[1]] = \
                                self._board[coordinates[0] - i + 1][coordinates[1]]

                    if coordinates[0] == 5:  # if the coordinates chosen by the user are on the sixth row
                        for i in range(5, -1, -1):
                            self._board[coordinates[0] - i][coordinates[1]] = \
                                self._board[coordinates[0] - i + 1][coordinates[1]]

                    if coordinates[0] == 6:  # if the coordinates chosen by the user are on the seventh row
                        for i in range(6, -1, -1):
                            if i > 0:
                                self._board[coordinates[0] - i][coordinates[1]] = \
                                    self._board[coordinates[0] - i + 1][coordinates[1]]
                    self._board[coordinates[0]][coordinates[1]] = ""

                # Checks if it undoes a move the opponent just made. If yes, update the turn and deepcopy board list.
                self._deepcopy_board_list.append(copy.deepcopy(self._board))
                if self.undo_opponent() is False:
                    self._current_turn = playername
                    self._deepcopy_board_list.remove(copy.deepcopy(self._board))
                    return False

                return True

            else:
                return False

        if direction == "R":
            # There's an empty space(or edge of board) on the side player is pushing away from, the marble can be moved.
            if coordinates[1] == 0 or self._board[coordinates[0]][coordinates[1] - 1] == "":
                # Updates the turn
                if playername == self._tuple_1[0]:
                    self._current_turn = self._tuple_2[0]
                if playername == self._tuple_2[0]:
                    self._current_turn = self._tuple_1[0]

                # If there are empty spaces in the same direction that the marble is pushed.
                # If the first empty location is right after the marble that is pushed, update the board.
                if coordinates[1] < 6 and self._board[coordinates[0]][coordinates[1] + 1] == "":
                    for i in range(1, -1, -1):
                        if i > 0:
                            self._board[coordinates[0]][coordinates[1] + i] = \
                                self._board[coordinates[0]][coordinates[1] + i - 1]
                    self._board[coordinates[0]][coordinates[1]] = ""

                # If the first empty location is the second space after the marble that is pushed, update the board.
                elif coordinates[1] < 5 and self._board[coordinates[0]][coordinates[1] + 2] == "":
                    for i in range(2, -1, -1):
                        if i > 0:
                            self._board[coordinates[0]][coordinates[1] + i] = \
                                self._board[coordinates[0]][coordinates[1] + i - 1]
                    self._board[coordinates[0]][coordinates[1]] = ""

                # If the first empty location is the third space after the marble that is pushed, update the board.
                elif coordinates[1] < 4 and self._board[coordinates[0]][coordinates[1] + 3] == "":
                    for i in range(3, -1, -1):
                        if i > 0:
                            self._board[coordinates[0]][coordinates[1] + i] = \
                                self._board[coordinates[0]][coordinates[1] + i - 1]
                    self._board[coordinates[0]][coordinates[1]] = ""

                # If the first empty location is the fourth space after the marble that is pushed, update the board.
                elif coordinates[1] < 3 and self._board[coordinates[0]][coordinates[1] + 4] == "":
                    for i in range(4, -1, -1):
                        if i > 0:
                            self._board[coordinates[0]][coordinates[1] + i] = \
                                self._board[coordinates[0]][coordinates[1] + i - 1]
                    self._board[coordinates[0]][coordinates[1]] = ""

                # If the first empty location is the fifth space after the marble that is pushed, update the board.
                elif coordinates[1] < 2 and self._board[coordinates[0]][coordinates[1] + 5] == "":
                    for i in range(5, -1, -1):
                        if i > 0:
                            self._board[coordinates[0]][coordinates[1] + i] = \
                                self._board[coordinates[0]][coordinates[1] + i - 1]
                    self._board[coordinates[0]][coordinates[1]] = ""

                # If the first empty location is the sixth space after the marble that is pushed, update the board.
                elif coordinates[1] < 1 and self._board[coordinates[0]][coordinates[1] + 6] == "":
                    for i in range(6, -1, -1):
                        if i > 0:
                            self._board[coordinates[0]][coordinates[1] + i] = \
                                self._board[coordinates[0]][coordinates[1] + i - 1]
                    self._board[coordinates[0]][coordinates[1]] = ""

                # If there are no empty spaces in the same direction that the marble is pushed.
                else:
                    # If the last marble is red, update the red marbles captured by each player and red marble left.
                    if self._board[coordinates[0]][6] == "R":
                        if playername == self._tuple_1[0]:
                            self._tuple_1_player_captured_marbles += 1
                            if self._tuple_1_player_captured_marbles == 7:
                                self._winner = playername               # Updates the winner
                        if playername == self._tuple_2[0]:
                            self._tuple_2_player_captured_marbles += 1
                            if self._tuple_2_player_captured_marbles == 7:
                                self._winner = playername               # Updates the winner
                        self._red_marbles -= 1

                    # If the last marble is white, update the number of white marble left on the board accordingly.
                    if self._board[coordinates[0]][6] == "W":
                        if playername == self._tuple_1[0]:
                            return False
                        else:
                            self._white_marbles -= 1

                    # If the last marble is black, update the number of black marble left on the board accordingly.
                    if self._board[coordinates[0]][6] == "B":
                        if playername == self._tuple_2[0]:
                            return False
                        else:
                            self._black_marbles -= 1

                    # Updates the board
                    if coordinates[1] == 5:  # if the coordinates chosen by the user are on the sixth column
                        for i in range(1, -1, -1):
                            self._board[coordinates[0]][coordinates[1] + i] = \
                                self._board[coordinates[0]][coordinates[1] + i - 1]

                    if coordinates[1] == 4:  # if the coordinates chosen by the user are on the fifth column
                        for i in range(2, -1, -1):
                            self._board[coordinates[0]][coordinates[1] + i] = \
                                self._board[coordinates[0]][coordinates[1] + i - 1]

                    if coordinates[1] == 3:  # if the coordinates chosen by the user are on the fourth column
                        for i in range(3, -1, -1):
                            self._board[coordinates[0]][coordinates[1] + i] = \
                                self._board[coordinates[0]][coordinates[1] + i - 1]

                    if coordinates[1] == 2:  # if the coordinates chosen by the user are on the third column
                        for i in range(4, -1, -1):
                            self._board[coordinates[0]][coordinates[1] + i] = \
                                self._board[coordinates[0]][coordinates[1] + i - 1]

                    if coordinates[1] == 1:  # if the coordinates chosen by the user are on the second column
                        for i in range(5, -1, -1):
                            self._board[coordinates[0]][coordinates[1] + i] = \
                                self._board[coordinates[0]][coordinates[1] + i - 1]

                    if coordinates[1] == 0:  # if the coordinates chosen by the user are on the first column
                        for i in range(6, -1, -1):
                            if i > 0:
                                self._board[coordinates[0]][coordinates[1] + i] = \
                                    self._board[coordinates[0]][coordinates[1] + i - 1]
                    self._board[coordinates[0]][coordinates[1]] = ""

                # Checks if it undoes a move the opponent just made. If yes, update the turn and deepcopy board list.
                self._deepcopy_board_list.append(copy.deepcopy(self._board))
                if self.undo_opponent() is False:
                    self._current_turn = playername
                    self._deepcopy_board_list.remove(copy.deepcopy(self._board))
                    return False

                return True
            else:
                return False

        if direction == "L":
            # There's an empty space(or edge of board) on the side player is pushing away from, the marble can be moved.
            if coordinates[1] == 6 or self._board[coordinates[0]][coordinates[1] + 1] == "":
                # Updates the turn
                if playername == self._tuple_1[0]:
                    self._current_turn = self._tuple_2[0]
                if playername == self._tuple_2[0]:
                    self._current_turn = self._tuple_1[0]

                # If there are empty spaces in the same direction that the marble is pushed.
                # If the first empty location is right after the marble that is pushed, update the board.
                if coordinates[1] > 0 and self._board[coordinates[0]][coordinates[1] - 1] == "":
                    for i in range(1, -1, -1):
                        if i > 0:
                            self._board[coordinates[0]][coordinates[1] - i] = \
                                self._board[coordinates[0]][coordinates[1] - i + 1]
                    self._board[coordinates[0]][coordinates[1]] = ""

                # If the first empty location is the second space after the marble that is pushed, update the board.
                elif coordinates[1] > 1 and self._board[coordinates[0]][coordinates[1] - 2] == "":
                    for i in range(2, -1, -1):
                        if i > 0:
                            self._board[coordinates[0]][coordinates[1] - i] = \
                                self._board[coordinates[0]][coordinates[1] - i + 1]
                    self._board[coordinates[0]][coordinates[1]] = ""

                # If the first empty location is the third space after the marble that is pushed, update the board.
                elif coordinates[1] > 2 and self._board[coordinates[0]][coordinates[1] - 3] == "":
                    for i in range(3, -1, -1):
                        if i > 0:
                            self._board[coordinates[0]][coordinates[1] - i] = \
                                self._board[coordinates[0]][coordinates[1] - i + 1]
                    self._board[coordinates[0]][coordinates[1]] = ""

                # If the first empty location is the fourth space after the marble that is pushed, update the board.
                elif coordinates[1] > 3 and self._board[coordinates[0]][coordinates[1] - 4] == "":
                    for i in range(4, -1, -1):
                        if i > 0:
                            self._board[coordinates[0]][coordinates[1] - i] = \
                                self._board[coordinates[0]][coordinates[1] - i + 1]
                    self._board[coordinates[0]][coordinates[1]] = ""

                # If the first empty location is the fifth space after the marble that is pushed, update the board.
                elif coordinates[1] > 4 and self._board[coordinates[0]][coordinates[1] - 5] == "":
                    for i in range(5, -1, -1):
                        if i > 0:
                            self._board[coordinates[0]][coordinates[1] - i] = \
                                self._board[coordinates[0]][coordinates[1] - i + 1]
                    self._board[coordinates[0]][coordinates[1]] = ""

                # If the first empty location is the sixth space after the marble that is pushed, update the board.
                elif coordinates[1] > 5 and self._board[coordinates[0]][coordinates[1] - 6] == "":
                    for i in range(6, -1, -1):
                        if i > 0:
                            self._board[coordinates[0]][coordinates[1] - i] = \
                                self._board[coordinates[0]][coordinates[1] - i + 1]
                    self._board[coordinates[0]][coordinates[1]] = ""

                # If there are no empty spaces in the same direction that the marble is pushed.
                else:
                    # If the last marble is red, update the red marbles captured by each player and red marble left.
                    if self._board[coordinates[0]][0] == "R":
                        if playername == self._tuple_1[0]:
                            self._tuple_1_player_captured_marbles += 1
                            if self._tuple_1_player_captured_marbles == 7:
                                self._winner = playername                    # Updates the winner
                        if playername == self._tuple_2[0]:
                            self._tuple_2_player_captured_marbles += 1
                            if self._tuple_2_player_captured_marbles == 7:
                                self._winner = playername                    # Updates the winner
                        self._red_marbles -= 1

                    # If the last marble is white, update the number of white marble left on the board accordingly.
                    if self._board[coordinates[0]][0] == "W":
                        if playername == self._tuple_1[0]:
                            return False
                        else:
                            self._white_marbles -= 1

                    # If the last marble is black, update the number of black marble left on the board accordingly.
                    if self._board[coordinates[0]][0] == "B":
                        if playername == self._tuple_2[0]:
                            return False
                        else:
                            self._black_marbles -= 1

                    # Updates the board
                    if coordinates[1] == 1:  # if the coordinates chosen by the user are on the second column
                        for i in range(1, -1, -1):
                            self._board[coordinates[0]][coordinates[1] - i] = \
                                self._board[coordinates[0]][coordinates[1] - i + 1]

                    if coordinates[1] == 2:  # if the coordinates chosen by the user are on the third column
                        for i in range(2, -1, -1):
                            self._board[coordinates[0]][coordinates[1] - i] = \
                                self._board[coordinates[0]][coordinates[1] - i + 1]

                    if coordinates[1] == 3:  # if the coordinates chosen by the user are on the fourth column
                        for i in range(3, -1, -1):
                            self._board[coordinates[0]][coordinates[1] - i] = \
                                self._board[coordinates[0]][coordinates[1] - i + 1]

                    if coordinates[1] == 4:  # if the coordinates chosen by the user are on the fifth column
                        for i in range(4, -1, -1):
                            self._board[coordinates[0]][coordinates[1] - i] = \
                                self._board[coordinates[0]][coordinates[1] - i + 1]

                    if coordinates[1] == 5:  # if the coordinates chosen by the user are on the sixth column
                        for i in range(5, -1, -1):
                            self._board[coordinates[0]][coordinates[1] - i] = \
                                self._board[coordinates[0]][coordinates[1] - i + 1]

                    if coordinates[1] == 6:  # if the coordinates chosen by the user are on the seventh column
                        for i in range(6, -1, -1):
                            if i > 0:
                                self._board[coordinates[0]][coordinates[1] - i] = \
                                    self._board[coordinates[0]][coordinates[1] - i + 1]
                    self._board[coordinates[0]][coordinates[1]] = ""

                # Checks if it undoes a move the opponent just made. If yes, update the turn and deepcopy board list.
                self._deepcopy_board_list.append(copy.deepcopy(self._board))
                if self.undo_opponent() is False:
                    self._current_turn = playername
                    self._deepcopy_board_list.remove(copy.deepcopy(self._board))
                    return False

                return True
            else:
                return False

        else:
            return False

    def get_winner(self):
        """The function doesn't take any parameters. It returns the winner. If no winners, returns None."""
        return self._winner

    def get_captured(self, player_name):
        """The function takes player's name as parameter and returns the number of Red marbles captured by the
        player."""
        # Checks the name of the player and returns the number of marbles accordingly.
        if player_name == self._tuple_1[0]:
            return self._tuple_1_player_captured_marbles
        else:
            return self._tuple_2_player_captured_marbles

    def get_marble(self, coordinates):
        """The function takes the coordinates of a cell as a tuple. It returns the marble that is present at the
        location. If no marble is present at the coordinate location, it returns 'X'."""
        if self._board[coordinates[0]][coordinates[1]] != "":
            return self._board[coordinates[0]][coordinates[1]]
        else:
            return "X"  # If no marble is present, return 'X'.

    def get_marble_count(self):
        """The function doesn't take any parameters. It returns the number of White marbles, Black marbles and Red
        marbles as tuple in the order (W,B,R)."""
        tuple_marble_count = (self._white_marbles, self._black_marbles, self._red_marbles)
        return tuple_marble_count
