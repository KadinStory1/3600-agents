from collections.abc import Callable

from typing import List, Set, Tuple

import numpy as np
from game import *
from game.enums import MoveType

"""
Melvin is the dumbest agent of all. He randomly selects a move from the list of valid moves.
"""


class PlayerAgent:
    """
    /you may add functions, however, __init__ and play are the entry points for
    your program and should not be changed.
    """

    def __init__(self, board: board.Board, time_left: Callable):
        self.time_left = time_left
        self.turn_counter = 0 
        self.corners: List[Tuple[int, int]] = [
            (0, 0), 
            (0, 7), 
            (7, 0), 
            (7, 7),
            
        ]
        self.start_position: Tuple[int, int] = board.chicken_player.get_location()
        self.history = []
        
        self.egg_score = 100
        self.plain_score = 10
        self.turd_score = -1
        

    def play(
        self,
        board: board.Board,
        sensor_data: List[Tuple[bool, bool]],
        time_left: Callable,
    ):
        location = board.chicken_player.get_location()
        print(f"I'm at {location}.")
        print(f"Trapdoor A: heard? {sensor_data[0][0]}, felt? {sensor_data[0][1]}")
        print(f"Trapdoor B: heard? {sensor_data[1][0]}, felt? {sensor_data[1][1]}")
        print(f"Starting to think with {time_left()} seconds left.")
        # Not really thinking; Yolanda is not a deep thinker
        self.turn_counter += 1
        moves = board.get_valid_moves()
        
        best_move = None 
        bestScore = float("-inf")
        for move in moves: 
            score = self.score_move(board, move, sensor_data)
            if score > bestScore: 
                bestScore = score
                best_move = move
        print(f"I have {time_left()} seconds left. Playing {best_move}.")
        return best_move

    def score_move(self, board: board.Board, move, sensor_data: List[Tuple[bool, bool]] ) -> float:
        try: 
            direction, move_type = move
        except:
            move_type = move.move_type
        if move_type == MoveType.EGG: 
            base = self.egg_score
        elif move_type == MoveType.PLAIN: 
            base = self.plain_score
        elif move_type == MoveType.TURD: 
            base = self.turd_score
        else: 
            base = 0
        return base