#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 20:07:36 2020

@author: arash
"""

import tictactoe as ttt

board = [
        [None, "X", "O"],
        ["O", "X", "X"],
        ["X", None, "O"]
    ]

print(ttt.minimax(board))