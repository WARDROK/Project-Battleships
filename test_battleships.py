# clean_logic()
import pytest
from settings import read_resolution
from errors import (LowHeightResolution,
                    LowWidthResolution,
                    WrongResolutionData,
                    NotFile,
                    IndexOutOfLogic)
from board import Board
from gamers import player, bot


def test_read_resolution():
    res = read_resolution('screen_width=1920', 'screen_height=1080')
    assert res[0] == 1920
    assert res[1] == 1080


def test_read_resolution_low_height():
    with pytest.raises(LowHeightResolution):
        read_resolution('screen_width=1920', 'screen_height=100')


def test_read_resolution_low_width():
    with pytest.raises(LowWidthResolution):
        read_resolution('screen_width=100', 'screen_height=1080')


def test_read_resolution_wrong_data_typical():
    with pytest.raises(WrongResolutionData):
        read_resolution('screen_width=192U', 'screen_height=1080')


def test_read_resolution_wrong_data():
    with pytest.raises(WrongResolutionData):
        read_resolution('ab6', 'yr*y6')


def test_read_resolution_without_initial_text():
    with pytest.raises(WrongResolutionData):
        read_resolution('1920', '1080')


def test_read_resolution_not_file():
    with pytest.raises(NotFile):
        read_resolution(file="test.txt")


def test_create_game_logic():
    board = Board(10, 10, 50, (0, 0))
    game_logic = board.create_game_logic()
    assert game_logic == [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]


def test_bot_make_attack():
    player.logic = [
        [' ', ' ', ' ', ' ', 'O', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', 'O', ' ', ' ', 'O', 'O', 'O'],
        [' ', ' ', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', 'O', ' ', ' ', ' ', ' ', ' ', 'O', ' '],
        [' ', ' ', 'O', ' ', ' ', ' ', ' ', ' ', 'O', ' '],
        [' ', ' ', 'O', ' ', ' ', ' ', ' ', ' ', 'O', ' '],
        [' ', ' ', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', 'O', 'O', 'O', 'O', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]

    # miss
    bot.make_attack(player.grid, player.logic, 0, 1)

    assert player.logic == [
        [' ', 'X', ' ', ' ', 'O', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', 'O', ' ', ' ', 'O', 'O', 'O'],
        [' ', ' ', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', 'O', ' ', ' ', ' ', ' ', ' ', 'O', ' '],
        [' ', ' ', 'O', ' ', ' ', ' ', ' ', ' ', 'O', ' '],
        [' ', ' ', 'O', ' ', ' ', ' ', ' ', ' ', 'O', ' '],
        [' ', ' ', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', 'O', 'O', 'O', 'O', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]

    # hit
    bot.make_attack(player.grid, player.logic, 2, 2)

    assert player.logic == [
        [' ', 'X', ' ', ' ', 'O', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', 'O', ' ', ' ', 'O', 'O', 'O'],
        [' ', ' ', 'H', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', 'O', ' ', ' ', ' ', ' ', ' ', 'O', ' '],
        [' ', ' ', 'O', ' ', ' ', ' ', ' ', ' ', 'O', ' '],
        [' ', ' ', 'O', ' ', ' ', ' ', ' ', ' ', 'O', ' '],
        [' ', ' ', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', 'O', 'O', 'O', 'O', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]

    # repeat
    bot.make_attack(player.grid, player.logic, 2, 2)

    assert player.logic == [
        [' ', 'X', ' ', ' ', 'O', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', 'O', ' ', ' ', 'O', 'O', 'O'],
        [' ', ' ', 'H', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', 'O', ' ', ' ', ' ', ' ', ' ', 'O', ' '],
        [' ', ' ', 'O', ' ', ' ', ' ', ' ', ' ', 'O', ' '],
        [' ', ' ', 'O', ' ', ' ', ' ', ' ', ' ', 'O', ' '],
        [' ', ' ', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', 'O', 'O', 'O', 'O', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]


def test_bot_make_attack_out_of_array():
    player.logic = [
        [' ', ' ', ' ', ' ', 'O', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', 'O', ' ', ' ', 'O', 'O', 'O'],
        [' ', ' ', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', 'O', ' ', ' ', ' ', ' ', ' ', 'O', ' '],
        [' ', ' ', 'O', ' ', ' ', ' ', ' ', ' ', 'O', ' '],
        [' ', ' ', 'O', ' ', ' ', ' ', ' ', ' ', 'O', ' '],
        [' ', ' ', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', 'O', 'O', 'O', 'O', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]
    with pytest.raises(IndexOutOfLogic):
        bot.make_attack(player.grid, player.logic, 11, 12)
