#!/usr/bin/env python
# -*- coding: utf-8 -*-
import secrets


def number_to_have():
    return secrets.randbelow(999 - 101 + 1) + 101


def tiles():
    present_tiles = list(range(1, 11)) * 2 + [25, 50, 75, 100]
    take_tiles = []

    for _ in range(6):
        index = secrets.randbelow(len(present_tiles))
        take_tiles.append(present_tiles[index])
        present_tiles.pop(index)

    return take_tiles


if __name__ == "__main__":
    number_to_have()
