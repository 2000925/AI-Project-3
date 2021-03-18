import pygame
import os.path

from pygame.locals import (
    MOUSEBUTTONDOWN,
    KEYDOWN,
    K_ESCAPE,
    K_SPACE,
    K_UP,
    RLEACCEL,
    QUIT,
)
SW = 800
SH = 780
SZ = 820
PZ = 82
WL = 2
CR = 7


BLACK = (0, 0, 0)

WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
BLUE = (135, 206, 250)
RED = (255, 0, 0)
RED_B = (255, 102, 102)
RED_P = (255, 51, 51)
GRIS_BRIGHT = (192, 192, 192)
GRIS = (128, 128, 128)

B = {
        'king': pygame.image.load(os.path.join("img", "black_king.png")),
        'queen': pygame.image.load(os.path.join("img", "black_queen.png")),
        'rook': pygame.image.load(os.path.join("img", "black_rook.png")),
        'bishop': pygame.image.load(os.path.join("img", "black_bishop.png")),
        'knight': pygame.image.load(os.path.join("img", "black_knight.png")),
        'pawn': pygame.image.load(os.path.join("img", "black_pawn.png")),
    }

W = {
        'king': pygame.image.load(os.path.join("img", "white_king.png")),
        'queen': pygame.image.load(os.path.join("img", "white_queen.png")),
        'rook': pygame.image.load(os.path.join("img", "white_rook.png")),
        'bishop': pygame.image.load(os.path.join("img", "white_bishop.png")),
        'knight': pygame.image.load(os.path.join("img", "white_knight.png")),
        'pawn': pygame.image.load(os.path.join("img", "white_pawn.png")),
    }

Score_init_WK = [
    [-3,-4,-4,-5,-5,-4,-4,-3],
    [-3,-4,-4,-5,-5,-4,-4,-3],
    [-3,-4,-4,-5,-5,-4,-4,-3],
    [-3,-4,-4,-5,-5,-4,-4,-3],
    [-2,-3,-3,-4,-4,-3,-3,-2],
    [-1,-2,-2,-2,-2,-2,-2,-1],
    [ 2, 2, 0, 0, 0, 0, 2, 2],
    [ 2, 3, 1, 0, 0, 1, 3, 2]
]
Score_init_WQ = [
    [  -2,  -1,  -1,-0.5,-0.5,  -1,  -1,  -2],
    [  -1,   0,   0,   0,   0,   0,   0,  -1],
    [  -1,   0, 0.5, 0.5, 0.5, 0.5,   0,  -1],
    [-0.5,   0, 0.5, 0.5, 0.5, 0.5,   0,-0.5],
    [   0,   0, 0.5, 0.5, 0.5, 0.5,   0,-0.5],
    [  -1, 0.5, 0.5, 0.5, 0.5, 0.5,   0,  -1],
    [  -1,   0, 0.5,   0,   0,   0,   0,  -1],
    [  -2,  -1,  -1,-0.5,-0.5,  -1,  -1,  -2]
]
Score_init_WR = [
    [   0,   0,   0,   0,   0,   0,   0,   0],
    [ 0.5,   1,   1,   1,   1,   1,   1, 0.5],
    [-0.5,   0,   0,   0,   0,   0,   0,-0.5],
    [-0.5,   0,   0,   0,   0,   0,   0,-0.5],
    [-0.5,   0,   0,   0,   0,   0,   0,-0.5],
    [-0.5,   0,   0,   0,   0,   0,   0,-0.5],
    [-0.5,   0,   0,   0,   0,   0,   0,-0.5],
    [   0,   0,   0, 0.5, 0.5,   0,   0,   0]
]
Score_init_WN = [
    [  -5,  -4,  -3,  -3,  -3,  -3,  -4,  -5],
    [  -4,  -2,   0,   0,   0,   0,  -2,  -4],
    [  -3,   0,   1, 1.5, 1.5,   1,   0,  -3],
    [  -3, 0.5, 1.5,   2,   2, 1.5, 0.5,  -3],
    [  -3,   0, 1.5,   2,   2, 1.5,   0,  -3],
    [  -3, 0.5,   1, 1.5, 1.5,   1, 0.5,  -3],
    [  -4,  -2,   0, 0.5, 0.5,   0,  -2,  -4],
    [  -5,  -4,  -3,  -3,  -3,  -3,  -4,  -5]
]
Score_init_WP = [
    [   0,   0,   0,   0,   0,   0,   0,   0],
    [   5,   5,   5,   5,   5,   5,   5,   5],
    [   1,   1,   2,   3,   3,   2,   1,   1],
    [ 0.5, 0.5,   1, 2.5, 2.5,   1, 0.5, 0.5],
    [   0,   0,   0,   2,   2,   0,   0,   0],
    [ 0.5,-0.5,  -1,   0,   0,  -1,-0.5, 0.5],
    [ 0.5,   1,   1,  -2,  -2,   1,   1, 0.5],
    [   0,   0,   0,   0,   0,   0,   0,   0]
]
Score_init_WB = [
    [  -2,  -1,  -1,  -1,  -1,  -1,  -1,  -2],
    [  -1,   0,   0,   0,   0,   0,   0,  -1],
    [  -1,   0, 0.5,   1,   1, 0.5,   0,  -1],
    [  -1, 0.5, 0.5,   1,   1, 0.5, 0.5,  -1],
    [  -1,   0,   1,   1,   1,   1,   0,  -1],
    [  -1,   1,   1,   1,   1,   1,   1,  -1],
    [  -1, 0.5,   0,   0,   0,   0, 0.5,  -1],
    [  -2,  -1,  -1,  -1,  -1,  -1,  -1,  -2]
]
Score_init_BK1 = [
    [ 2, 3, 1, 0, 0, 1, 3, 2],
    [ 2, 2, 0, 0, 0, 0, 2, 2],
    [-1,-2,-2,-2,-2,-2,-2,-1],
    [-2,-3,-3,-4,-4,-3,-3,-2],
    [-3,-4,-4,-5,-5,-4,-4,-3],
    [-3,-4,-4,-5,-5,-4,-4,-3],
    [-3,-4,-4,-5,-5,-4,-4,-3],
    [-3,-4,-4,-5,-5,-4,-4,-3]
]
Score_init_BQ1 = [
    [  -2,  -1,  -1,-0.5,-0.5,  -1,  -1,  -2],
    [  -1,   0, 0.5,   0,   0,   0,   0,  -1],
    [  -1, 0.5, 0.5, 0.5, 0.5, 0.5,   0,  -1],
    [   0,   0, 0.5, 0.5, 0.5, 0.5,   0,-0.5],
    [-0.5,   0, 0.5, 0.5, 0.5, 0.5,   0,-0.5],
    [  -1,   0, 0.5, 0.5, 0.5, 0.5,   0,  -1],
    [  -1,   0,   0,   0,   0,   0,   0,  -1],
    [  -2,  -1,  -1,-0.5,-0.5,  -1,  -1,  -2]
]
Score_init_BR1 = [
    [ 0, 0, 0, 0.5, 0.5, 0, 0, 0],
    [ -0.5, 0, 0, 0, 0, 0, 0, -0.5],
    [ -0.5, 0, 0, 0, 0, 0, 0, -0.5],
    [ -0.5, 0, 0, 0, 0, 0, 0, -0.5],
    [ -0.5, 0, 0, 0, 0, 0, 0, -0.5],
    [ -0.5, 0, 0, 0, 0, 0, 0, -0.5],
    [ 0.5, 1, 1, 1, 1, 1, 1, 0.5],
    [ 0, 0, 0, 0, 0, 0, 0, 0],
]
Score_init_BN1 = [
    [ -5, -4, -3, -3, -3, -3, -4, -5],
    [ -4, -2, 0, 0.5, 0.5, 0, -2, -4],
    [ -3, 0.5, 1, 1.5, 1.5, 1, 0.5, -3],
    [ -3, 0, 1.5, 2, 2, 1.5, 0,-3],
    [ -3, 0.5, 1.5, 2, 2, 1.5, 0.5, -3],
    [ -3, 0, 1, 1.5, 1.5, 1, 0, -3],
    [ -4, -2, 0, 0, 0, 0, -2, -4],
    [ -5, -4, -3, -3, -3, -3, -4, -5]
]
Score_init_BP1 = [
    [ 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0.5, 1, 1, -2, -2, 1, 1, 0.5],
    [ 0.5, -0.5, -1, 0, 0,-1, -0.5, 0.5],
    [ 0, 0, 0, 2, 2, 0, 0, 0],
    [ 0.5, 0.5, 1, 2.5, 2.5, 1, 0.5, 0.5],
    [ 1, 1, 2, 3, 3, 2, 1, 1],
    [ 5, 5, 5, 5, 5, 5, 5, 5],
    [ 0, 0, 0, 0, 0, 0, 0, 0]
]
Score_init_BB1 = [
    [ -2, -1, -1, -1, -1, -1, -1, -2],
    [ -1, 0.5, 0, 0, 0, 0, 0.5, -1],
    [ -1, 1, 1, 1, 1, 1, 1, -1],
    [ -1, 0, 1, 1, 1, 1, 0, -1],
    [ -1, 0.5, 0.5, 1, 1, 0.5, 0.5, -1],
    [ -1, 0, 0.5, 1, 1, 0.5, 0, -1],
    [ -1, 0, 0, 0, 0, 0, 0, -1],
    [ -2, -1, -1, -1, -1, -1, -1, -2],
]

Score_init_BK = [i[::-1] for i in Score_init_BK1]
Score_init_BQ = [i[::-1] for i in Score_init_BQ1]
Score_init_BR = [i[::-1] for i in Score_init_BR1]
Score_init_BB = [i[::-1] for i in Score_init_BB1]
Score_init_BN = [i[::-1] for i in Score_init_BN1]
Score_init_BP = [i[::-1] for i in Score_init_BP1]

Score_init = {
    'wk': Score_init_WK,
    'wq': Score_init_WQ,
    'wr': Score_init_WR,
    'wb': Score_init_WB,
    'wn': Score_init_WN,
    'wp': Score_init_WP,

    'bk': Score_init_BK,
    'bq': Score_init_BQ,
    'br': Score_init_BR,
    'bb': Score_init_BB,
    'bn': Score_init_BN,
    'bp': Score_init_BP,
}



def cal_rect(bool, rect0, rect1):
    if bool:
        return (rect1 * PZ, rect0 * PZ, )
    else:
        return (rect1 * PZ + PZ//2, rect0 * PZ + PZ//2, )

def rev_rect(pos):
    return (pos[1] // PZ, pos[0] // PZ)

def eq(a, b):
    if a[0] == b[0] and a[1] == b[1]:
        return True
    return False

def check_valid(n, m):
    if (n >= 0 and n <= 7) and (m >= 0 and m <= 7):
        return True
    return False


def clean_selected(ar):
    for i in range(8):
        for j in range(8):
            if ar[i][j] == '..' or ar[i][j] == '...':
                ar[i][j] = '  '
            if ar[i][j][:2] == '.w' or ar[i][j][:2] == '.b':
                ar[i][j] = ar[i][j][1:]

def king_position(ar, type):
    king = type + 'k'
    for i in range(8):
        for j in range(8):
            if ar[i][j] == king:
                return (i,j)

def check_position(pos, min1, max1, min2, max2):
    if pos[0] >= min1 and pos[0] <= max1 and pos[1] >= min2 and pos[1] <= max2:
        return True
    return False
