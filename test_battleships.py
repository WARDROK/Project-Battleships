# testy:
# show_game_logic()
# create_game_logic()
# clean_logic()
# resolution errors 4
# make_attack()
import pytest
from settings import read_resolution
from errors import (LowHeightResolution,
                    LowWidthResolution,
                    WrongResolutionData,
                    NotFile)
from board import Board
from main import show_game_logic
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
    

def test_make_attack():
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
    bot.make_attack(player.grid, player.logic)
    




def test_show_game_logic():
    pass
