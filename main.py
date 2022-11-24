import os
import pygame
import tkinter
from tkinter import messagebox


colors = {
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "gray": (120, 120, 120),
    "yellow": (255, 255, 0),
    "red": (255, 0, 255),
    "blue": (0, 255, 255),
}

root = tkinter.Tk()
root.withdraw()


class Game:
    SCREEN_SIZE = 500
    IMAGE_SIZE = SCREEN_SIZE / 3 - 50
    X_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('images', 'x.png')), (IMAGE_SIZE, IMAGE_SIZE))
    O_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('images', 'o.png')), (IMAGE_SIZE, IMAGE_SIZE))

    def __init__(self):
        pygame.display.set_caption("Tic Tac Toe")

        self.screen = pygame.display.set_mode((self.SCREEN_SIZE, self.SCREEN_SIZE + 80))
        self.buttons = ()
        self.player_time = "X"
        self.positions = [
            "", "", "",
            "", "", "",
            "", "", ""
        ]

    def _draw_buttons(self):
        rect_size = ((self.SCREEN_SIZE / 3) - 10, (self.SCREEN_SIZE / 3) - 10)

        # First Line
        button_01 = pygame.draw.rect(
            self.screen,
            colors['yellow'],
            pygame.Rect((0, 0), rect_size)
        )
        button_02 = pygame.draw.rect(
            self.screen,
            colors['red'],
            pygame.Rect(((self.SCREEN_SIZE / 3) + 5, 0), rect_size)
        )
        button_03 = pygame.draw.rect(
            self.screen,
            colors['blue'],
            pygame.Rect(((self.SCREEN_SIZE / 3) * 2 + 10, 0), rect_size)
        )

        # Second Line
        button_04 = pygame.draw.rect(
            self.screen,
            colors['blue'],
            pygame.Rect((0, (self.SCREEN_SIZE / 3) + 5), rect_size)
        )
        button_05 = pygame.draw.rect(
            self.screen,
            colors['yellow'],
            pygame.Rect(((self.SCREEN_SIZE / 3) + 5, (self.SCREEN_SIZE / 3) + 5), rect_size)
        )
        button_06 = pygame.draw.rect(
            self.screen,
            colors['red'],
            pygame.Rect(((self.SCREEN_SIZE / 3) * 2 + 10, (self.SCREEN_SIZE / 3) + 5), rect_size)
        )

        # Third Line
        button_07 = pygame.draw.rect(
            self.screen,
            colors['yellow'],
            pygame.Rect((0, (self.SCREEN_SIZE / 3) * 2 + 10), rect_size)
        )
        button_08 = pygame.draw.rect(
            self.screen,
            colors['red'],
            pygame.Rect(((self.SCREEN_SIZE / 3) + 5, (self.SCREEN_SIZE / 3) * 2 + 10), rect_size)
        )
        button_09 = pygame.draw.rect(
            self.screen,
            colors['blue'],
            pygame.Rect(((self.SCREEN_SIZE / 3) * 2 + 10, (self.SCREEN_SIZE / 3) * 2 + 10), rect_size)
        )

        pygame.draw.rect(
            self.screen,
            colors['black'],
            pygame.Rect((0, 0), (self.SCREEN_SIZE, self.SCREEN_SIZE)),
            10
        )

        self.buttons = (
            button_01,
            button_02,
            button_03,
            button_04,
            button_05,
            button_06,
            button_07,
            button_08,
            button_09
        )

    @property
    def __images_coordinates(self):
        return (
            (25, 25),
            ((self.SCREEN_SIZE / 3) + 25, 25),
            ((self.SCREEN_SIZE / 3) * 2 + 25, 25),
            (25, (self.SCREEN_SIZE / 3) + 25),
            ((self.SCREEN_SIZE / 3) + 25, (self.SCREEN_SIZE / 3) + 25),
            ((self.SCREEN_SIZE / 3) * 2 + 25, (self.SCREEN_SIZE / 3) + 25),
            (25, (self.SCREEN_SIZE / 3) * 2 + 25),
            ((self.SCREEN_SIZE / 3) + 25, (self.SCREEN_SIZE / 3) * 2 + 25),
            ((self.SCREEN_SIZE / 3) * 2 + 25, (self.SCREEN_SIZE / 3) * 2 + 25)
        )

    def _show_score(self):
        pygame.font.init()
        font = pygame.font.SysFont('arial', 20)

        score_player_one = font.render('Player One: 0', 1, colors['white'])
        score_player_two = font.render('Player Two: 0', 1, colors['white'])
        player_time = font.render(f'Player Time: {self.player_time}', 1, colors['white'])

        self.screen.blit(score_player_one, (10, self.SCREEN_SIZE))
        self.screen.blit(score_player_two, (self.SCREEN_SIZE - score_player_two.get_width() - 10, self.SCREEN_SIZE))
        self.screen.blit(player_time, (10, self.SCREEN_SIZE + 40))

    def _draw_positions(self):
        for index, position in enumerate(self.positions):
            if position == "X":
                self.screen.blit(self.X_IMAGE, self.__images_coordinates[index])
            elif position == "O":
                self.screen.blit(self.O_IMAGE, self.__images_coordinates[index])

    def main(self):
        frames_per_second = pygame.time.Clock()
        executing = True

        while executing:
            frames_per_second.tick(5)

            self._draw_buttons()
            self._show_score()
            self._draw_positions()

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for index, button in enumerate(self.buttons):
                        if button.collidepoint(pygame.mouse.get_pos()):
                            if self.positions[index] != "":
                                messagebox.showinfo("Ops!", "This positions already is in use")
                            else:
                                self.positions[index] = self.player_time
                                self.player_time = "X" if self.player_time == "O" else "O"


game = Game()

game.main()
