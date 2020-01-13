# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 23:46:41 2020

@author: anikkuda
"""

def solveBoard(board):
    location = ()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                location = (i,j)

    if not location:
        return True
    
    row, col = location
    for i in range(1,10):
        if validPlacement(board, i, (row, col)):
            board[row][col] = i

            if solveBoard(board):
                return True

            board[row][col] = 0

    return False


def validPlacement(board, num, pos):
    
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True


def printSolvedBoard(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("---------------------------------")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | "),

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " "),



board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]


solveBoard(board)
printSolvedBoard(board)