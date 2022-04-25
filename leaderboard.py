import pygame
import constant as const
from sys import exit
from intro import load_image


def open_leaderboard(SCREEN):
    """
    Executes the leaderboard loop

    Parameters:
    ----
    SCREEN <pygame.Surface>:
        Display surface for the game

    Return:
    ----
    None

    """
    exit_leaderboard = False
    top_users = get_leaderboard_data()
    while not exit_leaderboard:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit_leaderboard = True
        draw_leaderboard(SCREEN, top_users)


def draw_leaderboard(SCREEN, top_users):
    """
    Displays the top users onto the screen

    Parameters:
    ----
    SCREEN <pygame.Surface>:
        Display surface for the game
    top_users <list[tuple[str,str,str]]>:
        List of (rank,username,score) tuples, of the top users

    Return:
    ----
    None

    """
    LEADERBOARD_NAME_FONT = pygame.font.Font(const.SUBOLEYA_FONT_FILEPATH,
                                             const.LEADERBOARD_NAME_FONT_SIZE)
    POKEMON_FONT = pygame.font.Font(const.POKEMON_FONT_FILEPATH,
                                    const.LEADERBOARD_TITLE_FONT_SIZE)
    GAME_RETURN_FONT = pygame.font.Font(const.POKEMON_FONT_FILEPATH,
                                        const.GAME_RETURN_FONT_SIZE)
    LEADERBOARD_BACKGROUND = load_image(const.LEADERBOARD_BACKGROUND_FILEPATH,
                                        const.GAME_WIDTH, const.GAME_HEIGHT)
    SCREEN.blit(LEADERBOARD_BACKGROUND, (const.BACKGROUND_IMAGE_X,
                                         const.BACKGROUND_IMAGE_Y))
    title_text = POKEMON_FONT.render(const.LEADERBOARD_TITLE, True,
                                     const.BLACK)
    SCREEN.blit(title_text, (const.GAME_WIDTH//2 - title_text.get_width()//2,
                             const.LEADERBOARD_TITLE_Y))
    return_text = GAME_RETURN_FONT.render(const.EXIT_LEADERBOARD_TEXT, True,
                                          const.BLACK)
    SCREEN.blit(return_text, (const.GAME_WIDTH//2 - return_text.get_width()//2,
                              const.GAME_HEIGHT - return_text.get_height()))
    if top_users is not None:
        for i in range(len(top_users)):
            index, username, score = top_users[i]
            index_text = POKEMON_FONT.render(index, True, const.BLACK)
            username_text = LEADERBOARD_NAME_FONT.render(username, True,
                                                         const.BLACK)
            score_text = POKEMON_FONT.render(score, True, const.BLACK)
            SCREEN.blit(index_text, (const.LEADERBOARD_INDEX_X,
                                     (i+const.TEXT_HEIGHT) *
                                     index_text.get_height()))
            SCREEN.blit(username_text, (const.LEADERBOARD_NAME_X,
                                        (i+const.TEXT_HEIGHT) *
                                        index_text.get_height()))
            SCREEN.blit(score_text, (const.LEADERBOARD_SCORE_X,
                                     (i+const.TEXT_HEIGHT) *
                                     index_text.get_height()))
    pygame.display.update()


def update_leaderboard(username, score):
    """
    Updates the data in the leaderboard text file

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
    try:
        with open(const.LEADERBOARD_FILEPATH) as file:
            data = file.readlines()
            data = list(map(lambda x: x.split(","), data))
            data = list(map(lambda x: (x[0], int(x[1])), data))
            if len(data) < const.LEADERBOARD_SIZE:
                data.append((username, score))
                data.sort(key=lambda x: x[1], reverse=True)
            else:
                index_insert = None
                for i in range(-1, len(data)-1):
                    if score > data[i+1][1]:
                        index_insert = i+1
                        break
                if index_insert is not None:
                    data.insert(index_insert, (username, str(score)))
                    data = data[:-1]
            with open(const.LEADERBOARD_FILEPATH, "w") as file:
                for name, score in data:
                    file.write(name + "," + str(score) + "\n")
    except FileNotFoundError:
        with open(const.LEADERBOARD_FILEPATH, "w") as file:
            file.write(username + "," + str(score) + "\n")
    except TypeError as e:
        repr(e)
    except ValueError as e:
        repr(e)
    except PermissionError as e:
        repr(e)
    except OSError as e:
        repr(e)


def get_leaderboard_data():
    """
    Reads in Data from leaderboard text file

    Parameters:
    ----
    No Parameters

    Return:
    ----
    final <list[tuple[str,str,str]]>:
        List of (rank,username,score) tuples, of the top users
        None if error is faced

    """
    try:
        with open(const.LEADERBOARD_FILEPATH, "r") as file:
            data = file.readlines()
            data = list(map(lambda x: x.split(","), data))
            final = []
            for index, row in enumerate(data):
                name, score = row
                entry = (str(index+1), name, score[:-1])
                final.append(entry)
        return final
    except FileNotFoundError as e:
        repr(e)
    except TypeError as e:
        repr(e)
    except ValueError as e:
        repr(e)
    except PermissionError as e:
        repr(e)
    except OSError as e:
        repr(e)
