#!/usr/bin/env python

import random
import time

import unicornhat as unicorn

try:
    xrange
except NameError:
    xrange = range

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(90)
unicorn.brightness(0.5)
width,height=unicorn.get_shape()

size = width*height
blue = [[154, 154, 174], [0, 0, 255], [0, 0, 200], [0, 0, 160], [0, 0, 140], [0, 0, 90], [0, 0, 60], [0, 0, 0,]]

class GameOfLife:
    """Adapted from https://github.com/pimoroni/unicorn-hat/blob/master/examples/game_of_life.py
    to include a shift parameter.
    """
    def __init__(self, r_shift=0, g_shift=0, b_shift=0):
        self.board = [int(7 * random.getrandbits(1)) for _ in xrange(size)]
        self.color = blue
        for color in self.color:
            unit = 32 # 256 / 8
            color[0] = (color[0] + r_shift*unit) % 256
            color[1] = (color[1] + g_shift*unit) % 256
            color[2] = (color[2] + b_shift*unit) % 256

    def value(self, x, y):
        index = ((x % width) * height) + (y % height)
        return self.board[index]

    def neighbors(self, x, y):
        sum = 0
        for i in xrange(3):
            for j in xrange(3):
                if i == 1 and j == 1:
                    continue
                if self.value(x + i -1, y + j -1) == 0:
                    sum = sum + 1
        return sum

    def next_generation(self):
        new_board = [False] * size
        for i in xrange(width):
            for j in xrange(height):
                neigh = self.neighbors(i, j)
                lvl = self.value(i, j)
                if lvl == 0:
                    if neigh < 2:
                        new_board[i * height + j] = min(7, lvl + 1)
                    elif 2 <= neigh <= 3:
                        new_board[i * height + j] = 0
                    else:
                        new_board[i * height + j] = min(7, lvl + 1)
                else:
                    if neigh == 3:
                        new_board[i * height + j] = 0
                    else:
                        new_board[i * height + j] = min(7, lvl + 1)
        self.board = new_board

    def all_dead(self):
        for i in xrange(size):
            if self.board[i] != 7:
                return False
        return True

    def show_board(self):
        for i in xrange(width):
            for j in xrange(height):
               rgb = self.color[self.value(i, j)]
               unicorn.set_pixel(i, j, rgb[0], rgb[1], rgb[2])
        unicorn.show()
