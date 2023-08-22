# import pygame
# import pygame_widgets
# from pygame_widgets.button import Button, ButtonArray
#
# import sys
#
# # initializing the constructor
# pygame.init()
#
# smallfont = pygame.font.SysFont('Corbel', 35)
# color = (255, 255, 255)
#
# # light shade of the button
#
# # dark shade of the button
# color_dark = (100, 100, 100, 3)
#
# # screen resolution
# res = (720, 720)
# # opens up a window
# win = pygame.display.set_mode(res)
# wood_bg = pygame.image.load('assets/images/wood_bg_menu.jpg').convert()
# wood_bg = pygame.transform.scale(wood_bg, res)
# screen = pygame.Surface(res, pygame.SRCALPHA)
# screen.blit(wood_bg, (0, 0))
# def_color = (135, 132, 132, 2)
# light_color = (170, 170, 170, 2)
# texture_button = pygame.image.load('assets/images/wood_button.jpeg').convert()
# # rect_image = pygame.draw.rect(screen, 'gray', [400, 400, 100, 50], 0, 10)
# # button_surf = pygame.Surface((100, 50))
#
#
# # second_texture = pygame.image.load('./assets/second_texture.jpg').convert()
# # second_texture = pygame.transform.scale(second_texture, (100, 50))
#
#
# # button_quit = Button(
# #     screen,
# #     400,
# #     400,
# #     200,
# #     50,
# #     text='Quit',
# #     font=menu_font,
# #     textColour='White',
# #     radius=10,
# #     inactiveColour=(135, 132, 132, 2),
# #     hoverColour=(135, 132, 132, 2),
# #     pressedColour=(135, 132, 132, 2),
# #     hoverBorderColour='YELLOW',
# #     inactiveBorderColour=(135, 132, 132, 2),
# #     borderThickness=3,
# #     shadowColour='lightgray',
# #     shadowDistance=5,
# #     onClick=lambda: pygame.quit()
# # )
# # button_play = Button(
# #     screen,
# #     400,
# #     300,
# #     200,
# #     50,
# #     text='Options',
# #     font=menu_font,
# #     textColour='White',
# #     radius=10,
# #     inactiveColour=(135, 132, 132, 2),
# #     hoverColour=(135, 132, 132, 2),
# #     pressedColour=(135, 132, 132, 2),
# #     hoverBorderColour='YELLOW',
# #     inactiveBorderColour=(135, 132, 132, 2),
# #     borderThickness=3,
# #     shadowColour='lightgray',
# #     shadowDistance=5,
# #     onClick=lambda: print('Options')
# # )
# buttonArray = ButtonArray(
#     # Mandatory Parameters
#     screen,  # Surface to place button array on
#     res[0] // 2 - 100,  # X-coordinate
#     50,  # Y-coordinate
#     200,  # Width
#     150,  # Height
#     (1, 3),
#     colour=(0, 0, 0, 0),
#     # Shape: 2 buttons wide, 2 buttons tall
#     border=5,
#
#     fonts=(menu_font, menu_font, menu_font),
#     textColours=('White', 'White', 'White'),
#     textColour='White',
#     borderRadius=5,
#     radii=(10, 10, 10),
#     inactiveColours=(def_color, def_color, def_color),
#     hoverColours=(light_color, light_color, light_color),
#     pressedColours=(def_color, def_color, def_color),
#     # hoverBorderColours=('YELLOW', 'YELLOW', 'YELLOW'),
#     # inactiveBorderColours=('lightgray', 'lightgray', 'lightgray'),
#     shadowColours=('lightgray', 'lightgray', 'lightgray'),
#     shadowDistances=(5, 5, 5),
#     # radii=5,# Distance between buttons and edge of array
#     texts=('Play', 'Options', 'Quit'),  # Sets the texts of each button (counts left to right then top to bottom)
#     # When clicked, print number
#     onClicks=(lambda: print('Play!'), lambda: print('Options'), lambda: print('Quit')))
#
#
#
#
#
#
# # surface = pygame.Surface((500, 400), pygame.SRCALPHA)
# # pygame.draw.rect(win, (255,255,255,30), [300,200,200,100], 0)
#
#
# # screen.blit(surface, (0,0))
# # button = Button(
# #     # Mandatory Parameters
# #     screen,  # Surface to place button on
# #     100,  # X-coordinate of top left corner
# #     100,  # Y-coordinate of top left corner
# #     300,  # Width
# #     150,  # Height
# #
# #     # Optional Parameters
# #     text='Hello',  # Text to display1
# #     margin=20,  # Minimum distance between text/image and edge of button
# #     inactiveColour=(200, 50, 0),  # Colour of button when not being interacted with
# #     hoverColour=(150, 0, 0),  # Colour of button when being hovered over
# #     pressedColour=(0, 200, 20),  # Colour of button when being clicked
# #     radius=20,  # Radius of border corners (leave empty for not curved)
# #     onClick=lambda : quit() # Function to call when clicked on
# # )
#
#
# # white color
# def set_button(surface, txt, x, y, func):
#     btn = Button(
#         surface,
#         x,
#         y,
#         200,
#         50,
#         text=txt,
#         font=menu_font,
#         textColour='White',
#         radius=10,
#         inactiveColour=(135, 132, 132, 2),
#         hoverColour=(135, 132, 132, 2),
#         pressedColour=(135, 132, 132, 2),
#         hoverBorderColour='YELLOW',
#         inactiveBorderColour=(135, 132, 132, 2),
#         borderThickness=3,
#         shadowColour='lightgray',
#         shadowDistance=5,
#         onClick=lambda: func()
#     )
#     return btn
#
#
# def quit():
#     print('click!')
#
#
# # stores the width of the
# # screen into a variable
# width = screen.get_width()
#
# # stores the height of the
# # screen into a variable
# height = screen.get_height()
#
# # defining a font
#
#
# # rendering a text written in
# # this font
# fps = 60
#
# text = smallfont.render('quit', True, color)
# if __name__ == '__main__':
#     clock = pygame.time.Clock()
#     while True:
#         win.blit(screen, (0, 0))
#         set_button(screen, 'MyButton', 200, 600, quit)
#
#         pygame.display.flip()
#         mouse = pygame.mouse.get_pos()
#         for ev in pygame.event.get():
#
#             if ev.type == pygame.QUIT:
#                 pygame.quit()
#         # checks if a mouse is clicked
#         #     if ev.type == pygame.MOUSEBUTTONDOWN:
#         #
#         #         # if the mouse is clicked on the
#         #         # button the game is terminated
#         #         if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
#         #             pygame.quit()
#         #
#         # # fills the screen with a color
#         #
#         # # stores the (x,y) coordinates into
#         # # the variable as a tuple
#         #
#         # # if mouse is hovered on a button it
#         # # changes to lighter shade
#         # if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
#         #     pygame.draw.rect(screen, color_light, [width / 2, height / 2, 140, 40], border_radius=20)
#         #
#         # else:
#         #     pygame.draw.rect(screen, color_dark, [width / 2, height / 2, 140, 40], border_radius=1000)
#
#         # superimposing the text onto our button
#
#         # updates the frames of the game
import pygame

# Window size
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

### initialisation
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Gradient Rect")


def gradientRect(window, left_colour, right_colour, target_rect):
    """ Draw a horizontal-gradient filled rectangle covering <target_rect> """
    colour_rect = pygame.Surface((2, 2))  # tiny! 2x2 bitmap
    pygame.draw.line(colour_rect, left_colour, (0, 0), (0, 1))  # left colour line
    pygame.draw.line(colour_rect, right_colour, (1, 0), (1, 1))  # right colour line
    colour_rect = pygame.transform.smoothscale(colour_rect, (target_rect.width, target_rect.height))  # stretch!
    window.blit(colour_rect, target_rect)  # paint it


### Main Loop
clock = pygame.time.Clock()
finished = False
while not finished:

    # Handle user-input
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            done = True

    # Update the window
    window.fill((0, 0, 0))
    gradientRect(window, (0, 255, 0), (0, 100, 0), pygame.Rect(100, 100, 100, 50))
    gradientRect(window, (255, 255, 0), (0, 0, 255), pygame.Rect(100, 200, 128, 64))
    pygame.display.flip()
    # Clamp FPS
    clock.tick_busy_loop(60)

pygame.quit()
