import pygame
from pieces import *
from tools import *
from AI import *

class Board():
    def __init__(self, screen):
        self.screen = screen
        self.color = BLACK

    def draw_board(self, C):
        pygame.draw.rect(self.screen, C, (0, 0, SZ, PZ))
        pygame.draw.rect(self.screen, C, (0, 0, PZ, SZ))
        pygame.draw.rect(self.screen, C, (SZ-PZ, 0, PZ, SZ))
        pygame.draw.rect(self.screen, C, (0, SZ-PZ, SZ-PZ, PZ))
        for y in range(8):
            for x in range(8):
                if (x + y) % 2 == 0:
                    self.color = WHITE
                else:
                    self.color = GREEN
                pygame.draw.rect(self.screen, self.color,(PZ*(x+1), PZ*(y+1), PZ, PZ))


class Game():

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SZ, SZ))
        self.font = pygame.font.SysFont("comicsansms", 35)
        self.font2 = pygame.font.SysFont("comicsansms", 72)
        board = Board(self.screen)
        pieces = Pieces(self.screen)
        option = self.G_AI(board, pieces)
        self.End(board, pieces)
        pygame.quit()

    

    def G_AI(self, board, pieces):

        cplayer = ['w', 'b']
        C = [BLUE, BLUE]
        player= 0
        cl= -1
        st= [] 
        last_pos = ()
        AI = AI_Minimax(pieces.ar, pieces)
        running = True
        while running:
            pos_clicked = ()
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                if event.type == MOUSEBUTTONDOWN:
                    if player == 0 and pygame.mouse.get_pressed():
                        pos_clicked = rev_rect(pygame.mouse.get_pos())
                        cl += 1
                        if not pieces.Before(pos_clicked, player) and cl == 0:
                            cl -= 1
                            continue
            if player == 0:
                if pos_clicked != () and not check_valid(pos_clicked[0]-1, pos_clicked[1]-1):
                    cl -= 1
                    continue
                if pos_clicked != () and cl == 0:
                    pieces.selecting(pos_clicked)
                    st.append(pos_clicked)

                if pos_clicked != () and cl == 1:
                    if eq(st[0], pos_clicked):
                        cl -= 1
                        continue
                    if pieces.switch_piece(st[0], pos_clicked):
                        cl, st = -1, []
                        clean_selected(pieces.ar)
                        continue
                    if not pieces.move(pieces.ar, st[0], pos_clicked):
                        cl -= 1
                        continue
                    last_pos = (st[0], pos_clicked)
                    player, cl, st = 1 - player, -1, []
                    if pieces.is_checked(pieces.ar, cplayer[player]):
                        if pieces.is_checkmate(pieces.ar, cplayer[player]):
                         
                            running = False
            else: 
                pos = AI.minimax(pieces.ar,pieces,'b',-1000000000,1000000000,3,None,pieces.prev_move)
                
                pieces.selecting(pos[1])
                pieces.move(pieces.ar, pos[1], pos[2])
                last_pos = (pos[1], pos[2])
                player = 1 - player
                if pieces.is_checked(pieces.ar, cplayer[player]):
                        if pieces.is_checkmate(pieces.ar, cplayer[player]):
                  
                            running = False
            board.draw_board(C[player])

            pieces.draw_pieces_upgrade(last_pos)

            pygame.display.flip()
       

    def End(self, board, pieces):
        
        txt = "Good Game"
        txt = self.font.render(txt, True, RED)
        txt_center = (SZ/2 - txt.get_width() // 2,50//2 - txt.get_height() // 2)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False    

            board.draw_board(BLUE)
            pieces.draw_pieces()
            self.screen.blit(txt, txt_center)
            pygame.display.flip()



if __name__ == '__main__':
    t = Game()
