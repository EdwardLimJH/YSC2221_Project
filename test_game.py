from Help_Me_Study_Game import (
    check_game_event
)
from unittest.mock import patch
import pygame
import pygame.locals as pyloc
pygame.init()


@patch("helper.execute_left")
@patch("helper.execute_right")
@patch("Help_Me_Study_Game.execute_take_progress", return_value=(10, 10))
@patch("Help_Me_Study_Game.execute_stun")
def test_check_game_event(mock_execute_stun,
                          mock_execute_take_progress,
                          mock_execute_right, mock_execute_left):
    # create events, test if my object's x position moved right / left
    left_key_event = pygame.event.Event(pyloc.KEYDOWN, key=pyloc.K_LEFT)
    right_key_event = pygame.event.Event(pyloc.KEYDOWN, key=pyloc.K_RIGHT)
    obstacle_obj = pygame.Rect(0, 0, 10, 10)
    TAKE_OBSTACLE = pygame.USEREVENT + 1
    TAKE_PROGRESS = pygame.USEREVENT + 2
    take_obstacle_event = pygame.event.Event(TAKE_OBSTACLE)
    take_progress_event = pygame.event.Event(TAKE_PROGRESS)
    # create other relevant objects to call check_game_event function
    screen = pygame.display.set_mode((100, 100))
    score = 0
    time_end = 0
    obstacle_lst = [obstacle_obj]
    book_lst = []
    main_char = pygame.Rect(0, 0, 10, 10)
    invisible_main_char = pygame.Rect(0, 0, 10, 10)
    SCORE_FONT = pygame.font.Font(None, 10)
    check_game_event(left_key_event, screen, obstacle_lst, book_lst, main_char,
                     invisible_main_char, score, SCORE_FONT, time_end)

    assert mock_execute_left.call_count == 1
    assert mock_execute_right.call_count == 0
    assert mock_execute_stun.call_count == 0
    assert mock_execute_take_progress.call_count == 0

    check_game_event(right_key_event, screen, obstacle_lst, book_lst,
                     main_char, invisible_main_char, score, SCORE_FONT,
                     time_end)
    assert mock_execute_left.call_count == 1
    assert mock_execute_right.call_count == 1
    assert mock_execute_stun.call_count == 0
    assert mock_execute_take_progress.call_count == 0

    check_game_event(take_obstacle_event, screen, obstacle_lst, book_lst,
                     main_char, invisible_main_char, score, SCORE_FONT,
                     time_end)
    assert mock_execute_left.call_count == 1
    assert mock_execute_right.call_count == 1
    assert mock_execute_stun.call_count == 1
    assert mock_execute_take_progress.call_count == 0

    score, time_end = check_game_event(take_progress_event, screen,
                                       obstacle_lst, book_lst,
                                       main_char, invisible_main_char,
                                       score, SCORE_FONT, time_end)
    assert mock_execute_left.call_count == 1
    assert mock_execute_right.call_count == 1
    assert mock_execute_stun.call_count == 1
    assert mock_execute_take_progress.call_count == 1
    assert score == 10 and time_end == 10


def test_execute_left(monkeypatch):
    is_execute_left_called = False
    is_execute_right_called = False

    def mock_execute_left(*args, **kwargs):
        nonlocal is_execute_left_called
        is_execute_left_called = True

    def mock_execute_right(*args, **kwargs):
        nonlocal is_execute_right_called
        is_execute_right_called = True

    monkeypatch.setattr("helper.execute_left", mock_execute_left)
    monkeypatch.setattr("helper.execute_right", mock_execute_right)
    left_key_event = pygame.event.Event(pyloc.KEYDOWN, key=pyloc.K_LEFT)
    obstacle_obj = pygame.Rect(0, 0, 10, 10)
    # create other relevant objects to call check_game_event function
    screen = pygame.display.set_mode((100, 100))
    score = 0
    time_end = 0
    obstacle_lst = [obstacle_obj]
    book_lst = []
    main_char = pygame.Rect(0, 0, 10, 10)
    invisible_main_char = pygame.Rect(0, 0, 10, 10)
    SCORE_FONT = pygame.font.Font(None, 10)
    check_game_event(left_key_event, screen,
                     obstacle_lst, book_lst,
                     main_char, invisible_main_char,
                     score, SCORE_FONT, time_end)
    assert is_execute_left_called is True
    assert is_execute_right_called is False


def test_execute_right(monkeypatch):
    is_execute_left_called = False
    is_execute_right_called = False

    def mock_execute_left(*args, **kwargs):
        nonlocal is_execute_left_called
        is_execute_left_called = True

    def mock_execute_right(*args, **kwargs):
        nonlocal is_execute_right_called
        is_execute_right_called = True

    monkeypatch.setattr("helper.execute_left", mock_execute_left)
    monkeypatch.setattr("helper.execute_right", mock_execute_right)
    right_key_event = pygame.event.Event(pyloc.KEYDOWN, key=pyloc.K_RIGHT)
    obstacle_obj = pygame.Rect(0, 0, 10, 10)
    # create other relevant objects to call check_game_event function
    screen = pygame.display.set_mode((100, 100))
    score = 0
    time_end = 0
    obstacle_lst = [obstacle_obj]
    book_lst = []
    main_char = pygame.Rect(0, 0, 10, 10)
    invisible_main_char = pygame.Rect(0, 0, 10, 10)
    SCORE_FONT = pygame.font.Font(None, 10)
    check_game_event(right_key_event, screen,
                     obstacle_lst, book_lst,
                     main_char, invisible_main_char,
                     score, SCORE_FONT, time_end)
    assert is_execute_left_called is False
    assert is_execute_right_called is True


@patch("Help_Me_Study_Game.execute_stun")
@patch("Help_Me_Study_Game.execute_take_progress", return_value=(0, 0))
def test_execute_move(mock_execute_take_progress, mock_execute_stun,
                      monkeypatch):
    is_execute_left_called = False
    is_execute_right_called = False

    def mock_execute_left(*args, **kwargs):
        nonlocal is_execute_left_called
        is_execute_left_called = True

    def mock_execute_right(*args, **kwargs):
        nonlocal is_execute_right_called
        is_execute_right_called = True

    monkeypatch.setattr("helper.execute_left", mock_execute_left)
    monkeypatch.setattr("helper.execute_right", mock_execute_right)
    invalid_key_event1 = pygame.event.Event(pyloc.KEYDOWN, key=pyloc.K_SPACE)
    invalid_key_event2 = pygame.event.Event(pyloc.KEYDOWN, key=pyloc.K_0)
    invalid_key_event3 = pygame.event.Event(pyloc.KEYDOWN, key=pyloc.K_l)
    obstacle_obj = pygame.Rect(0, 0, 10, 10)
    TAKE_OBSTACLE = pygame.USEREVENT + 1
    TAKE_PROGRESS = pygame.USEREVENT + 2
    take_obstacle_event = pygame.event.Event(TAKE_OBSTACLE)
    take_progress_event = pygame.event.Event(TAKE_PROGRESS)
    # create other relevant objects to call check_game_event function
    screen = pygame.display.set_mode((100, 100))
    score = 0
    time_end = 0
    obstacle_lst = [obstacle_obj]
    book_lst = []
    main_char = pygame.Rect(0, 0, 10, 10)
    invisible_main_char = pygame.Rect(0, 0, 10, 10)
    SCORE_FONT = pygame.font.Font(None, 10)
    check_game_event(invalid_key_event1, screen,
                     obstacle_lst, book_lst,
                     main_char, invisible_main_char,
                     score, SCORE_FONT, time_end)
    assert is_execute_left_called is False
    assert is_execute_right_called is False

    check_game_event(invalid_key_event2, screen,
                     obstacle_lst, book_lst,
                     main_char, invisible_main_char,
                     score, SCORE_FONT, time_end)
    assert is_execute_left_called is False
    assert is_execute_right_called is False

    check_game_event(invalid_key_event3, screen,
                     obstacle_lst, book_lst,
                     main_char, invisible_main_char,
                     score, SCORE_FONT, time_end)
    assert is_execute_left_called is False
    assert is_execute_right_called is False

    check_game_event(take_progress_event, screen,
                     obstacle_lst, book_lst,
                     main_char, invisible_main_char,
                     score, SCORE_FONT, time_end)
    assert is_execute_left_called is False
    assert is_execute_right_called is False
    assert mock_execute_stun.call_count == 0
    assert mock_execute_take_progress.call_count == 1

    check_game_event(take_obstacle_event, screen,
                     obstacle_lst, book_lst,
                     main_char, invisible_main_char,
                     score, SCORE_FONT, time_end)
    assert is_execute_left_called is False
    assert is_execute_right_called is False
    assert mock_execute_stun.call_count == 1
    assert mock_execute_take_progress.call_count == 1
