#!/usr/bin/env python
# -*- coding: utf-8 -*-
import secrets


def number_to_have():
    return secrets.randbelow(999 - 101 + 1) + 101


if __name__ == "__main__":
    number_to_have()