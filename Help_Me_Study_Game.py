import pygame
import constant as const
import intro as intro
import helper as help
import leaderboard as ldr
from sys import exit


def main():
    """
    main method to start the program and run the whole game

    Parameters:
    ----
    No Parameters

    Return:
    ----
    None

    """
    pygame.init()
    clock = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((const.GAME_WIDTH, const.GAME_HEIGHT))
    pygame.display.set_caption(const.GAME_CAPTION)
    username = const.default_username
    user_input = intro.intro(SCREEN)
    if user_input != "":
        username = user_input
    curr_time = pygame.time.get_ticks()
    pygame.event.clear()
    play(SCREEN, curr_time, username, clock)


def play(SCREEN, time, username, clock):
    """
    Executes game loop to play the game and game over loop

    Parameters:
    ----
    SCREEN <pygame.Surface>:
        Display surface for the game
    time <int>:
        Starting time of the game in milliseconds since pygame.init() is called
    username <str>:
        username that the user input, otherwise it's the default username
    clock <pgame.Clock>:
        A pygame Clock object to help track time within the game

    Return:
    ----
    None

    """

    GAME_BACKGROUND_MUSIC = pygame.mixer.Sound(
                            const.GAME_BACKGROUND_MUSIC_FILEPATH)
    SCORE_FONT = pygame.font.Font(const.SCORE_FONT_FILEPATH,
                                  const.SCORE_FONT_SIZE)
    main_char = pygame.Rect(const.INITIAL_MAIN_CHARACTER_X,
                            const.INITIAL_MAIN_CHARACTER_Y,
                            const.MAIN_CHARACTER_RECT_WIDTH,
                            const.MAIN_CHARACTER_RECT_HEIGHT)
    # creates a replica of the main_char but on the other side
    # this replica is not shown and is used to clear get rid of
    # falling obstacles
    invisible_main_char = pygame.Rect(const.INITIAL_INVISIBLE_X,
                                      const.INITIAL_MAIN_CHARACTER_Y,
                                      const.MAIN_CHARACTER_RECT_WIDTH,
                                      const.MAIN_CHARACTER_RECT_HEIGHT)
    main_char_image = intro.load_image(const.MAIN_CHARACTER_FILEPATH,
                                       const.MAIN_CHARACTER_IMAGE_WIDTH,
                                       const.MAIN_CHARACTER_IMAGE_HEIGHT)
    GAME_BACKGROUND_MUSIC.play(loops=-1)
    score = 0
    game_is_active = True
    obstacle_lst = []
    book_lst = []
    start_time = time
    time_end = const.MAX_TIME_LIMIT + start_time

    while game_is_active:
        clock.tick(const.FPS)
        for event in pygame.event.get():
            score, time_end = check_game_event(event, SCREEN, obstacle_lst,
                                               book_lst, main_char,
                                               invisible_main_char,
                                               score, SCORE_FONT, time_end)
        help.draw_game_window(SCREEN, obstacle_lst, book_lst, score,
                              SCORE_FONT, time_end)
        help.draw_main_char(SCREEN, main_char, main_char_image)
        pygame.display.update()
        if pygame.time.get_ticks() - time_end >= 0:
            game_is_active = False

    help.game_over(username, score)

    while not game_is_active:
        clock.tick(const.FPS)
        score_message = f'{username} got {score} points'
        help.draw_game_over(SCREEN, const.GAME_OVER_TEXT, score_message,
                            SCORE_FONT, const.GAME_RESTART_TEXT)
        for event in pygame.event.get():
            check_game_over_event(event, SCREEN, username, clock)
        pygame.display.update()


def check_game_event(event, SCREEN, obstacle_lst, book_lst, main_char,
                     invisible_main_char, score, SCORE_FONT, time_end):
    """
    Checks events in the game over state
    Updates the x coordinate of main character

    Parameters:
    ----
    event <pygame.Event>:
        Given pygame Event object
    SCREEN <pygame.Surface)
    obstacle_lst <list[pygame.Rect]>:
        list of obstacles currently in the game
    book_lst <list[pygame.Rect]>:
        list of assets currently in the game
    main_char <pygame.Rect>:
        pygame.Rect object denoting position of main character
    inivisible_main_char <pygame.Rect>:
        pygame.Rect object denoting position of invisible main character
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

    TAKE_OBSTACLE = pygame.USEREVENT + 1
    TAKE_PROGRESS = pygame.USEREVENT + 2
    if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            help.execute_left(obstacle_lst, book_lst, main_char,
                              invisible_main_char, TAKE_PROGRESS,
                              TAKE_OBSTACLE)
        if event.key == pygame.K_RIGHT:
            help.execute_right(obstacle_lst, book_lst, main_char,
                               invisible_main_char, TAKE_PROGRESS,
                               TAKE_OBSTACLE)
    if event.type == TAKE_PROGRESS:
        score, time_end = execute_take_progress(score, time_end)
    if event.type == TAKE_OBSTACLE:
        stun_start = pygame.time.get_ticks()
        execute_stun(SCREEN, stun_start, main_char, time_end, obstacle_lst,
                     book_lst, score, SCORE_FONT)
    return score, time_end


def execute_take_progress(score, time_end):
    """
    Plays music, and increases score and time_end

    Parameters:
    ----
    score <int>:
        user's current score
    time_end <int>:
        milliseconds since pygame.init() to denote the time which the game end

    Return:
    ----
    score <int>:
        score after increment
    time_end <int>:
        new increased time end
        timer + time_increment if bonus time results in exceeding the set limit

    """
    COLLECT_BOOKS_MUSIC = pygame.mixer.Sound(const.COLLECT_BOOK_FILEPATH)
    COLLECT_BOOKS_MUSIC.play()
    time_end = execute_time_increment(score, time_end)
    score = score + const.SCORE_INCREMENT
    return score, time_end


def execute_time_increment(score, time_end):
    """
    Increase time limit

    Parameters:
    ----
    score <int>:
        user's current score
    time_end <int>:
        milliseconds since pygame.init() to denote the time which the game end

    Return:
    ----
    time_end <int>:
        new increased time end
        timer + time_increment if bonus time results in exceeding the set limit

    """
    time_increment = help.calculate_bonus_time(score)
    time_end = min(pygame.time.get_ticks() + const.MAX_TIME_LIMIT,
                   time_end + time_increment)
    return time_end


def check_game_over_event(event, SCREEN, username, clock):
    """
    Checks events in the game over state

    Parameters:
    ----
    event <pygame.Event>:
        Given pygame Event object
    SCREEN <pygame.Surface>:
        Display surface for the game
    username <str>:
        username that the user input, otherwise it's the default username
    clock <pgame.Clock>:
        A pygame Clock object to help track time within the game

    Return:
    ----
    None

    """

    if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            start_time = pygame.time.get_ticks()
            pygame.mixer.stop()
            play(SCREEN, start_time, username, clock)
        if event.key == pygame.K_l:
            ldr.open_leaderboard(SCREEN)


def execute_stun(SCREEN, stun_start, main_char, time_end, obstacle_lst,
                 book_lst, score, SCORE_FONT):
    """
    Disable any movement of the main character for a fixed duration

    Parameters:
    ----
    SCREEN <pygame.Surface>:
        Display surface for the game
    stun_start <int>:
        Starting time of the stun, in miliseconds from pygame.init()
    main_char <pygame.Rect>:
        pygame.Rect object to denote main character position
    time_end <int>:
        milliseconds since pygame.init() to denote the time which the game end
    obstacle_lst <list[pygame.Rect]>:
        list of obstacles currently in the game
    book_lst <list[pygame.Rect]>:
        list of assets currently in the game
    score <int>:
        score that user has gotten so far
    SCORE_FONT <pygame.Font>:
        Font for the score text

    Return:
    ----
    None

    """

    COLLECT_OBSTACLE_MUSIC = pygame.mixer.Sound(
                    const.COLLECT_OBSTACLE_FILEPATH)
    COLLECT_OBSTACLE_MUSIC.play()
    STUN_IMAGE1 = intro.load_image(const.STUN_IMAGE_FILEPATH1,
                                   const.STUN_IMAGE_WIDTH,
                                   const.STUN_IMAGE_HEIGHT)
    STUN_IMAGE2 = intro.load_image(const.STUN_IMAGE_FILEPATH2,
                                   const.STUN_IMAGE_WIDTH,
                                   const.STUN_IMAGE_HEIGHT)
    stun_lst = [STUN_IMAGE1, STUN_IMAGE2]
    stun_index = 0
    curr_stun_img = stun_lst[stun_index]
    stun_end = stun_start + const.STUN_DURATION
    curr_time = pygame.time.get_ticks()
    while curr_time < stun_end:
        stun_index += const.STUN_ANIMATION_SPEED
        curr_stun_img = stun_lst[int(stun_index) % 2]
        help.draw_game_window(SCREEN, obstacle_lst, book_lst, score,
                              SCORE_FONT, time_end)
        help.draw_main_char(SCREEN, main_char, curr_stun_img)
        pygame.display.update()
        curr_time = pygame.time.get_ticks()
    pygame.event.clear()


if __name__ == "__main__":
    main()
