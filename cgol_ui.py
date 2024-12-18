#!/usr/bin/env python3
import pygame
import cgol
import plaintext
import guide
import random

BCKRND_COLOR = (100, 100, 100)
(WIDTH, HEIGHT) = (1200, 1200)
G_DIMENSION = 100
NEXT_STEP = pygame.USEREVENT
MIN_CELLW = int(WIDTH/G_DIMENSION)
ZOOM_FACTOR = 2
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
qicon = pygame.image.load("./qicon.png").convert()
qicon_scaled = pygame.transform.scale(qicon, (60, 60))


class App:
    def __init__(self, sim, txtx, txty):
        self.sim = sim
        self.button = QuestionIcon(qicon_scaled, txtx, txty)
        self.text_shown = False

    def draw(self, screen, iconx, icony):
        self.sim.draw(screen)
        self.button.draw_icon(iconx, icony)
        if self.text_shown is True:
            self.button.drawtxt()

    def event_handle(self, event):
        s = self.sim.event_handle(event)
        b = self.button.event_handle(event)
        if b is True:
            self.text_shown = not self.text_shown
        return s or b


class Simulator:
    def __init__(self, g, ispaused):
        self.g = g
        self.ispaused = ispaused
        self.view = cgol.View(G_DIMENSION, 0, 0)
        self.lcolor = (20, 20, 20)
        self.live_color = (210, 210, 210)
        self.dead_color = (100, 100, 100)
        self.cell_w = int(WIDTH/G_DIMENSION)

    def draw(self, screen):
        screen.fill(BCKRND_COLOR)

        for x in range(self.view.view_size):
            conv_x = self.cell_w * x
            pygame.draw.line(
                screen, self.lcolor, (conv_x, 0),
                (conv_x, HEIGHT), 1
            )

        for y in range(self.view.view_size):
            conv_y = self.cell_w * y
            pygame.draw.line(
                screen, self.lcolor, (0, conv_y),
                (HEIGHT, conv_y), 1
            )

        for x in range(self.view.view_size):
            for y in range(self.view.view_size):
                conv_x = self.cell_w * x
                conv_y = self.cell_w * y
                if self.g.get(x + self.view.x, y + self.view.y) == 1:
                    pygame.draw.rect(
                        screen, self.live_color,
                        pygame.Rect(conv_x, conv_y, self.cell_w, self.cell_w)
                    )

    def event_handle(self, event):
        mouse_left = 1
        mouse_right = 3
        testptxt = """
        !Name: Gosper glider gun
        !
        ........................O...........
        ......................O.O...........
        ............OO......OO............OO
        ...........O...O....OO............OO
        OO........O.....O...OO..............
        OO........O...O.OO....O.O...........
        ..........O.....O.......O...........
        ...........O...O....................
        ............OO......................
        """
        transptxt = plaintext.read_plaintext(testptxt)

        if event.type == NEXT_STEP:
            if self.ispaused is False:
                self.g = cgol.conwayslife(self.g, G_DIMENSION)
                return True

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                self.ispaused = not self.ispaused

            elif event.key == pygame.K_e:
                self.g = cgol.conwayslife(self.g, G_DIMENSION)
                return True

            elif event.key == pygame.K_f:
                self.g.clear()
                return True

            elif event.key == pygame.K_r:
                self.g.random(G_DIMENSION, 50)
                return True

            elif event.key == pygame.K_z:
                if self.cell_w > MIN_CELLW:
                    self.view.zoom(G_DIMENSION, ZOOM_FACTOR)
                    self.cell_w /= ZOOM_FACTOR
                    return True
                else:
                    pass

            elif event.key == pygame.K_c:
                self.view.zoom(G_DIMENSION, 1/ZOOM_FACTOR)
                self.cell_w *= ZOOM_FACTOR
                return True

            elif event.key == pygame.K_s:
                self.view.pan(G_DIMENSION, 0, 1)
                return True

            elif event.key == pygame.K_w:
                self.view.pan(G_DIMENSION, 0, -1)
                return True

            elif event.key == pygame.K_a:
                self.view.pan(G_DIMENSION, -1, 0)
                return True

            elif event.key == pygame.K_d:
                self.view.pan(G_DIMENSION, 1, 0)
                return True

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == mouse_left:
            convpos = self.g.ccoords(pygame.mouse.get_pos(), self.cell_w)
            if self.g.get(convpos[0], convpos[1]) == 0:
                self.g.set(convpos[0], convpos[1], 1)
            else:
                self.g.set(convpos[0], convpos[1], 0)
            return True

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == mouse_right:
            mpos = self.g.ccoords(pygame.mouse.get_pos(), self.cell_w)
            self.g.insert(mpos[0], mpos[1], transptxt)
            return True


class Icon:
    def draw(self, image, x, y):
        rect = image.get_rect()
        rect.topleft = (x, y)
        screen.blit(image, (rect.x, rect.y))


class QuestionIcon:
    def __init__(self, image, x, y):
        self.image = image
        self.rect = None
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def drawtxt(self):
        guide.draw_rect(
            200, 200,
            screen
        )
        guide.draw_text(
            600, 300,
            'Welcome to my game!',
            40,
            screen
        )
        guide.draw_text(
            600, 350,
            'This is a small guide on how to use this software.',
            30,
            screen
        )
        guide.draw_text(
            600, 400,
            'Left click -toggle cell alive/dead',
            30,
            screen
        )
        guide.draw_text(
            600, 450,
            'Right click -copy pattern (currently gosper glider gun)',
            30,
            screen
        )
        guide.draw_text(
            600, 500,
            'Space bar -pause progam',
            30,
            screen
        )
        guide.draw_text(
            600, 550,
            'E -move single step in the program',
            30,
            screen
        )
        guide.draw_text(
            600, 600,
            'F -clear grid entirely',
            30,
            screen
        )
        guide.draw_text(
            600, 650,
            'R -randomise entire grid',
            30,
            screen
        )
        guide.draw_text(
            600, 700,
            'WASD -pan the screen up, left, down, right, respectively',
            30,
            screen
        )
        guide.draw_text(
            600, 750,
            'CZ -zoom in and out respectively',
            30,
            screen
        )
        guide.draw_text(
            600, 800,
            'DISCLAIMER: This program is fairly early in',
            30,
            screen
        )
        guide.draw_text(
            600, 830,
            'development! I have big plans for it, so keep an',
            30,
            screen
        )
        guide.draw_text(
            600, 860,
            'eye open.',
            30,
            screen
        )
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def draw_icon(self, x, y):
        icon = Icon()
        icon.draw(self.image, x, y)

    def event_handle(self, event):
        if self.rect is None:
            return
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                if self.rect.collidepoint(pos):
                    return True


def main():
    running = True
    pygame.init()
    pygame.display.set_caption('Conway')
    screen.fill(BCKRND_COLOR)
    # pygame.display.flip()
    app = App(Simulator(cgol.Grid(), True), 0, 0)
    pygame.time.set_timer(NEXT_STEP, 100)
    app.draw(screen, 0, 0)
    pygame.display.flip()

    while running:
        # For look through event queue

        for event in pygame.event.get():
            if app.event_handle(event):
                app.draw(screen, 0, 0)
                pygame.display.update()

            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    main()
