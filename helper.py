import pygame
import random
import constant as const
from intro import load_image
from leaderboard import update_leaderboard


def draw_main_char(SCREEN, main_char, image):
    """
    Displays the given image of the main character onto the screen

    Parameters:
    ----
    SCREEN <pygame.Surface>:
        Display surface for the game
    main_char <pygame.Rect>:
        pygame.Rect object denoting position of main character
    image <pygame.Surface>:
        Image of the main character to be displayed

    Return:
    ----
    None

    """
    SCREEN.blit(image, (main_char.x, main_char.y))


def calculate_bonus_time(score):
    """
    Calculates the amount of bonus time user should get

    Parameters:
    ----
    score <int>:
        score that user has gotten so far

    Return:
    ----
    <int> :
        Bonus time corresponding to the current tier at which the user is at

    """
    if score <= const.TIER_1_SCORE:
        return const.TIER_1_TIME
    elif score <= const.TIER_2_SCORE:
        return const.TIER_2_TIME
    elif score <= const.TIER_3_SCORE:
        return const.TIER_3_TIME
    elif score <= const.TIER_4_SCORE:
        return const.TIER_4_TIME
    elif score <= const.TIER_5_SCORE:
        return const.TIER_5_TIME
    elif score > const.TIER_5_SCORE:
        return 0


def draw_timer(SCREEN, time_end):
    """
    Draws the timer onto the screen

    Parameters:
    ----
    SCREEN <pygame.Surface>:
        Display surface for the game
    time_end <int>:
        milliseconds since pygame.init() to denote the time which the game end
    Return:
    ----
    None

    """

    loading_bar_boarder_image = load_image(const.LOADING_BAR_BOARDER_FILEPATH,
                                           const.LOADING_BAR_WIDTH +
                                           const.LOADING_BAR_PADDING,
                                           const.LOADING_BAR_HEIGHT +
                                           const.LOADING_BAR_PADDING).convert()
    loading_bar_image = load_image(const.LOADING_BAR_FILEPATH,
                                   const.LOADING_BAR_WIDTH,
                                   const.LOADING_BAR_HEIGHT)
    scale_factor = int((time_end - pygame.time.get_ticks()) /
                       const.MAX_TIME_LIMIT * const.LOADING_BAR_WIDTH)
    if scale_factor < 0:
        scale_factor = 0
    scaled_loading_bar_image = \
        pygame.transform.scale(loading_bar_image,
                               (scale_factor,
                                const.LOADING_BAR_HEIGHT))
    SCREEN.blit(loading_bar_boarder_image, (const.LOADING_BAR_X,
                                            const.LOADING_BAR_Y))

    SCREEN.blit(scaled_loading_bar_image, (const.LOADING_BAR_X +
                                           const.LOADING_BAR_PADDING//2,
                                           const.LOADING_BAR_Y +
                                           const.LOADING_BAR_PADDING//2))


def draw_game_window(SCREEN, obstacle_lst, book_lst, score,
                     SCORE_FONT, time_end):
    """
    Displays game window display onto the screen

    Parameters:
    ----
    SCREEN <pygame.Surface>:
        Display surface for the game
    obstacle_lst <list[pygame.Rect]>:
        list of obstacles currently in the game
    book_lst <list[pygame.Rect]>:
        list of assets currently in the game
    score <int>:
        score that user has gotten so far
    SCORE_FONT <pygame.Font>:
        Font for the score text
    time_end <int>:
        milliseconds since pygame.init() to denote the time which the game end
    Return:
    ----
    None

    """

    book_image = load_image(const.BOOK_FILEPATH,
                            const.BOOK_IMAGE_WIDTH,
                            const.BOOK_IMAGE_HEIGHT)

    obstacle_image = load_image(const.OBSTACLE_FILEPATH,
                                const.OBSTACLE_IMAGE_WIDTH,
                                const.OBSTACLE_IMAGE_HEIGHT)

    pillar = pygame.Rect(const.GAME_WIDTH//2 - const.CENTRE_PILLAR_WIDTH,
                         const.CENTRE_PILLAR_Y, const.CENTRE_PILLAR_WIDTH,
                         const.GAME_HEIGHT)

    game_background_image = load_image(const.GAME_BACKGROUND_IMAGE_FILEPATH,
                                       const.GAME_WIDTH, const.GAME_HEIGHT)

    SCREEN.blit(game_background_image,
                (const.BACKGROUND_IMAGE_X, const.BACKGROUND_IMAGE_Y))
    game_score = SCORE_FONT.render(const.SCORE_TEXT + str(score), True,
                                   const.BLACK)
    SCREEN.blit(game_score, (const.GAME_WIDTH - game_score.get_width(),
                             const.SCORE_PADDING))
    pygame.draw.rect(SCREEN, const.BLACK, pillar)
    for obstacle in obstacle_lst:
        SCREEN.blit(obstacle_image, (obstacle.x, obstacle.y))
    for book in book_lst:
        SCREEN.blit(book_image, (book.x, book.y))
    draw_timer(SCREEN, time_end)


def draw_game_over(SCREEN, text, score, SCORE_FONT, restart_msg):
    """
    Displays the game over display onto the screen

    Parameters:
    ----
    SCREEN <pygame.Surface>:
        Display surface for the game
    text <str>:
        Text message to be displayed
    score <str>:
        score message to be displayed
    SCORE_FONT <pygame.Font>:
        Font for the score text
    restart_msg <str>:
        Restart message to be displayed

    Return:
    ----
    None

    """

    GAME_RESTART_FONT = pygame.font.Font(const.POKEMON_FONT_FILEPATH,
                                         const.GAME_RESTART_FONT_SIZE)
    GAME_OVER_IMAGE = load_image(const.GAME_OVER_BACKGROUND_FILEPATH,
                                 const.GAME_WIDTH, const.GAME_HEIGHT)
    GAME_OVER_FONT = pygame.font.Font(const.POKEMON_FONT_FILEPATH,
                                      const.GAME_OVER_FONT_SIZE)
    SCREEN.blit(GAME_OVER_IMAGE,
                (const.BACKGROUND_IMAGE_X, const.BACKGROUND_IMAGE_Y))
    game_over_text = GAME_OVER_FONT.render(text, True, const.BLACK)
    score_text = SCORE_FONT.render(score, True, const.BLACK)
    restart_text = GAME_RESTART_FONT.render(restart_msg, True, const.BLACK)
    leaderboard_text = GAME_RESTART_FONT.render(const.LEADERBOARD_TEXT,
                                                True, const.BLACK)
    SCREEN.blit(game_over_text,
                (const.GAME_WIDTH//2 - game_over_text.get_width()//2,
                 const.GAME_HEIGHT//2 - game_over_text.get_height()))
    SCREEN.blit(score_text, (const.GAME_WIDTH//2 - score_text.get_width()//2,
                             const.GAME_HEIGHT//2))
    SCREEN.blit(restart_text,
                (const.GAME_WIDTH//2 - restart_text.get_width()//2,
                 const.GAME_HEIGHT//2 + score_text.get_height()))
    SCREEN.blit(leaderboard_text,
                (const.GAME_WIDTH//2 - leaderboard_text.get_width()//2,
                 const.GAME_HEIGHT//2 + score_text.get_height() +
                 restart_text.get_height()))
    pygame.display.update()


def execute_move(obstacle_lst, book_lst, main_char, invisible_main_char,
                 direction, TAKE_PROGRESS, TAKE_OBSTACLE):
    """
    Checks if main character can be moved in the given direction

    Parameters:
    ----
    obstacle_lst <list[pygame.Rect]>:
        list of obstacles currently in the game
    book_lst <list[pygame.Rect]>:
        list of assets currently in the game
    main_char <pygame.Rect>:
        pygame.Rect object denoting position of main character
    inivisible_main_char <pygame.Rect>:
        pygame.Rect object denoting position of invisible main character
    TAKE_PROGRESS <pygame.Event>:
        Pygame Event denoting that user has "collected" an asset
    TAKE_OBSTACLE <pygame.Event>:
        Pygame Event denoting that user has "collected" an obstacle

    Return:
    ----
    None

    """

    left_bound = const.INITIAL_MAIN_CHARACTER_X
    right_bound = const.INITIAL_MAIN_CHARACTER_X + const.CENTRE_PILLAR_WIDTH +\
        const.MAIN_CHARACTER_RECT_WIDTH
    amt = (const.CENTRE_PILLAR_WIDTH + const.MAIN_CHARACTER_RECT_WIDTH) *\
        direction
    if left_bound <= main_char.x + amt <= right_bound:
        swap_position(main_char, invisible_main_char, amt)
    update_drops(obstacle_lst, book_lst, main_char, invisible_main_char,
                 TAKE_PROGRESS, TAKE_OBSTACLE)
    random_spawn(obstacle_lst, book_lst)


def execute_right(obstacle_lst, book_lst, main_char, invisible_main_char,
                  TAKE_PROGRESS, TAKE_OBSTACLE):
    """
    Mimics main character moving right
    Attempt to increase the x coordinate of main character

    Parameters:
    ----
    obstacle_lst <list[pygame.Rect]>:
        list of obstacles currently in the game
    book_lst <list[pygame.Rect]>:
        list of assets currently in the game
    main_char <pygame.Rect>:
        pygame.Rect object denoting position of main character
    inivisible_main_char <pygame.Rect>:
        pygame.Rect object denoting position of invisible main character
    TAKE_PROGRESS <pygame.Event>:
        Pygame Event denoting that user has "collected" an asset
    TAKE_OBSTACLE <pygame.Event>:
        Pygame Event denoting that user has "collected" an obstacle

    Return:
    ----
    None

    """

    execute_move(obstacle_lst, book_lst, main_char, invisible_main_char, 1,
                 TAKE_PROGRESS, TAKE_OBSTACLE)


def execute_left(obstacle_lst, book_lst, main_char, invisible_main_char,
                 TAKE_PROGRESS, TAKE_OBSTACLE):
    """
    Mimics main character moving left
    Attempt to decrease the x coordinate of main character

    Parameters:
    ----
    obstacle_lst <list[pygame.Rect]>:
        list of obstacles currently in the game
    book_lst <list[pygame.Rect]>:
        list of assets currently in the game
    main_char <pygame.Rect>:
        pygame.Rect object denoting position of main character
    inivisible_main_char <pygame.Rect>:
        pygame.Rect object denoting position of invisible main character
    TAKE_PROGRESS <pygame.Event>:
        Pygame Event denoting that user has "collected" an asset
    TAKE_OBSTACLE <pygame.Event>:
        Pygame Event denoting that user has "collected" an obstacle

    Return:
    ----
    None

    """

    execute_move(obstacle_lst, book_lst, main_char, invisible_main_char, -1,
                 TAKE_PROGRESS, TAKE_OBSTACLE)


def update_drops(obstacle_lst, book_lst, main_char, invisible_main_char,
                 TAKE_PROGRESS, TAKE_OBSTACLE):
    """
    Updates y coordinate of all obstacles and assets in obstacles/assets list
    Removes objects that goes below the height of the main character
    Removes "collected" items from their respective lists

    Parameters:
    ----
    obstacle_lst <list[pygame.Rect]>:
        list of obstacles currently in the game
    book_lst <list[pygame.Rect]>:
        list of assets currently in the game
    main_char <pygame.Rect>:
        pygame.Rect object denoting position of main character
    inivisible_main_char <pygame.Rect>:
        pygame.Rect object denoting position of invisible main character
    TAKE_PROGRESS <pygame.Event>:
        Pygame Event denoting that user has "collected" an asset
    TAKE_OBSTACLE <pygame.Event>:
        Pygame Event denoting that user has "collected" an obstacle

    Return:
    ----
    None

    """

    for book in book_lst.copy():
        book.y += const.DROP_UPDATE_DISTANCE + const.DROP_PADDING
        if main_char.colliderect(book):
            pygame.event.post(pygame.event.Event(TAKE_PROGRESS))
            book_lst.remove(book)
        if invisible_main_char.colliderect(book):
            book_lst.remove(book)

    for obstacle in obstacle_lst.copy():
        obstacle.y += const.DROP_UPDATE_DISTANCE + const.DROP_PADDING
        if main_char.colliderect(obstacle):
            pygame.event.post(pygame.event.Event(TAKE_OBSTACLE))
            obstacle_lst.remove(obstacle)
        if invisible_main_char.colliderect(obstacle):
            obstacle_lst.remove(obstacle)


def swap_position(main_char, inivisible_main_char, amt):
    """
    Updates x coordinate of main_char and invisible_main_char

    Parameters:
    ----
    main_char <pygame.Rect>:
        pygame.Rect object denoting position of main character
    inivisible_main_char <pygame.Rect>:
        pygame.Rect object denoting position of invisible main character
    amt <int>:
        value to shift the main character horizontally by

    Return:
    ----
    None

    """
    MOVEMENT_MUSIC = pygame.mixer.Sound(const.MOVEMENT_MUSIC_FILE_PATH)
    main_char.x += amt
    inivisible_main_char.x -= amt
    MOVEMENT_MUSIC.play()


def random_spawn(obstacle_lst, book_lst):
    """
    Randomly adds a new pygame.Rect object into the obstacle/asset list

    Parameters:
    ----
    obstacle_lst <list[pygame.Rect]>:
        list of obstacles currently in the game
    book_lst <list[pygame.Rect]>:
        list of assets currently in the game

    Return:
    ----
    None

    """

    side = random.randint(0, 1)
    if side == const.LEFT_RNG_VALUE:
        side = const.LEFT_SIDE
    elif side == const.RIGHT_RNG_VALUE:
        side = const.RIGHT_SIDE

    drop_item = random.randint(0, 1)
    if drop_item == const.OBSTACLE_RNG_VALUE:
        spawn(obstacle_lst, side)
    if drop_item == const.BOOK_RNG_VALUE:
        spawn(book_lst, side)


def spawn(drop_obj_lst, initial_x):
    """
    Adds a new pygame.Rect object into the given list

    Parameters:
    ----
    drop_obj_lst <list[pygame.Rect]>:
        list of obstacles or assets currently in the game
    initial_x <int>:
        x coordinate of the new object to be added

    Return:
    ----
    None

    """

    new_obj = pygame.Rect(initial_x, const.INITIAL_DROP_Y,
                          const.DROP_RECT_WIDTH, const.DROP_RECT_HEIGHT)
    drop_obj_lst.append(new_obj)


def game_over(username, score):
    """
    Stops background music and plays game over music

    Parameters:
    ----
    username <str>:
        username that the user input, otherwise it's the default username
    score <int>:
        score that user achieved from the game instance

    Return:
    ----
    None

    """

    pygame.mixer.stop()
    update_leaderboard(username, score)
    GAME_OVER_MUSIC = pygame.mixer.Sound(const.GAME_OVER_MUSIC_FILEPATH)
    GAME_OVER_MUSIC.play()
