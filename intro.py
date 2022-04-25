import pygame
import constant as const
from sys import exit


def load_image(filepath, width, height):
    """
    Loads and rescale an image

    Parameters:
    ----
    filepath <str>:
        File path of the image to be loaded
    width <int>:
        desired width of rescaled image
    height <int>:
        desired height of rescaled image

    Return:
    ----
    img <pygame.Surface>:
        Rescaled image

    """

    img = pygame.image.load(filepath)
    img = pygame.transform.scale(img, (width, height))
    return img


def intro(SCREEN):
    """
    Executes the intro loop

    Parameters:
    ----
    SCREEN <pygame.Surface>:
        Display surface for the game

    Return:
    ----
    user_input <str>:
        String that the user has typed
        "" if user did not type anything

    """

    user_input = ""
    done_typing = False
    INPUT_FONT = pygame.font.Font(const.INPUT_FONT_STYLE, const.INPUT_FONT)
    INPUT_RECT = pygame.Rect(const.INPUT_X, const.INPUT_Y,
                             const.INPUT_WIDTH, const.INPUT_HEIGHT)
    LOGIN_BACKGROUND = load_image(const.LOGIN_BACKGROUND_FILEPATH,
                                  const.GAME_WIDTH, const.GAME_HEIGHT)
    TITLE_FONT = pygame.font.Font(const.POKEMON_FONT_FILEPATH,
                                  const.TITLE_FONT_SIZE)
    while not done_typing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                elif event.key == pygame.K_RETURN:
                    done_typing = True
                elif len(user_input) == const.MAX_LENGTH_USERNAME:
                    pass
                else:
                    user_input += event.unicode
        draw_login_window(SCREEN, LOGIN_BACKGROUND, user_input, INPUT_FONT,
                          INPUT_RECT, TITLE_FONT)
        pygame.display.update()
    draw_instructions(SCREEN)
    return user_input


def draw_instructions(SCREEN):
    """
    Displays the instructions onto the screen and executes instruction loop

    Parameters:
    ----
    SCREEN <pygame.Surface>:
        Display surface for the game

    Return:
    ----
    None

    """
    start_game = False
    INSTRUCTION_TITLE_FONT = pygame.font.Font(
        const.INSTRUCTION_TITLE_FONT_FILEPATH,
        const.INSTRUCTION_TITLE_FONT_SIZE)
    INSTRUCTION_TEXT_FONT = pygame.font.Font(
        const.INSTRUCTION_TEXT_FONT_FILEPATH,
        const.INSTRUCTION_TEXT_SIZE)
    GAME_START_FONT = pygame.font.Font(const.START_GAME_FONT_FILEPATH,
                                       const.START_GAME_SIZE)

    INSTRUCTION_TITLE = INSTRUCTION_TITLE_FONT.render(const.INSTRUCTION_TITLE,
                                                      True, const.BLACK)
    INSTRUCTION_TEXT_1 = INSTRUCTION_TEXT_FONT.render(const.INSTRUCTION_TEXT_1,
                                                      True, const.BLACK)
    INSTRUCTION_TEXT_2 = INSTRUCTION_TEXT_FONT.render(const.INSTRUCTION_TEXT_2,
                                                      True, const.BLACK)
    INSTRUCTION_TEXT_3 = INSTRUCTION_TEXT_FONT.render(const.INSTRUCTION_TEXT_3,
                                                      True, const.BLACK)
    GAME_START = GAME_START_FONT.render(const.START_GAME, True, const.BLACK)
    INTRO_BACKGROUND = load_image(const.INTRO_BACKGROUND_IMAGE_FILEPATH,
                                  const.GAME_WIDTH, const.GAME_HEIGHT)
    while not start_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start_game = True
        SCREEN.blit(INTRO_BACKGROUND, (const.BACKGROUND_IMAGE_X,
                                       const.BACKGROUND_IMAGE_Y))
        SCREEN.blit(INSTRUCTION_TITLE, (const.GAME_WIDTH//2 -
                                        INSTRUCTION_TITLE.get_width()//2,
                                        const.INSTRUCTION_TITLE_Y))
        SCREEN.blit(INSTRUCTION_TEXT_1, (const.INSTRUCTION_TEXT_X,
                                         const.INSTRUCTION_TEXT_Y))
        SCREEN.blit(INSTRUCTION_TEXT_2, (const.INSTRUCTION_TEXT_X,
                                         const.INSTRUCTION_TEXT_Y +
                                         INSTRUCTION_TEXT_1.get_height()))
        SCREEN.blit(INSTRUCTION_TEXT_3, (const.INSTRUCTION_TEXT_X,
                                         const.INSTRUCTION_TEXT_Y +
                                         INSTRUCTION_TEXT_1.get_height() +
                                         INSTRUCTION_TEXT_2.get_height()))
        SCREEN.blit(GAME_START, (const.INSTRUCTION_TEXT_X, const.GAME_START_Y))
        pygame.display.update()


def draw_login_window(SCREEN, login_background, user_input, input_font,
                      input_rect, title_font):
    """
    Displays the login window to the screen

    Parameters:
    ----
    SCREEN <pygame.Surface>:
        Display surface for the game
    login_background <pygame.Surface>:
        Image that is used as the background
    user_input <str>:
        String showing what the user is typing
    input_font <pygame.Font>:
        Font for the user's input
    input_rect <pygame.Rect>:
        Rectangle that denotes the box for users to type in
    title_font <pygame.Font>:
        Font for the title

    Return:
    ----
    None

    """
    SCREEN.blit(login_background,
                (const.BACKGROUND_IMAGE_X, const.BACKGROUND_IMAGE_Y))
    pygame.draw.rect(SCREEN, const.LIGHTSKYBLUE, input_rect,
                     const.INPUT_BOX_WIDTH)
    text_surface = input_font.render(user_input, True, const.BLACK)
    prompt_surface = input_font.render(const.INPUT_PROMPT, True,
                                       const.BLACK)
    title_top_surface = title_font.render(const.GAME_TITLE_TOP, True,
                                          const.WHITE)
    title_bot_surface = title_font.render(const.Game_TITLE_BOTTOM, True,
                                          const.BLACK)
    SCREEN.blit(text_surface, input_rect)
    SCREEN.blit(prompt_surface, (const.INPUT_PROMPT_X, const.INPUT_PROMPT_Y))
    SCREEN.blit(title_top_surface,
                (const.GAME_TITLE_TOP_X, const.GAME_TITLE_TOP_Y))
    SCREEN.blit(title_bot_surface,
                (const.GAME_TITLE_BOTTOM_X, const.GAME_TITLE_BOTTOM_Y))
