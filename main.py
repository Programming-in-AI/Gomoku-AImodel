import pygame
import utils
import Menu

if __name__ == '__main__':

    # TODO 0 : let computer play game, black is human, white is computer by rule 3 in ppt maybe [yet]
    # TODO 1 : whoever start, black first. [done]
    # TODO 2 : black should start from center. [yet]
    # TODO 3 : white randomly chooses the spot which is empty. [yet]
    # TODO 4 : balck's third stone must be out of center area 5x5. [yet]
    # TODO 5 : must play by taking turn. [done]
    # TODO 6 : visualize the board [done]
    # TODO 7 : win twice, get the win [done]
    # TODO 8 : let it available to input opponent's coordinate and react in 5 sec. [yet]

    # initialize
    pygame.init()
    surface = pygame.display.set_mode((utils.window_width, utils.window_height))
    pygame.display.set_caption("Omok game")

    # make instance
    omok = utils.Omok(surface)
    menu = Menu.Menu(surface)

    while True:
        omok.run_game(omok, menu)
        if menu.game_over(omok):  # if anyside win twice quit the window
            pygame.quit()
            break

