#!/usr/bin/env python3
"""
Purpose: Unit testing for algorithm_rgb.py
Author : Chris Schnaufer <schnaufer@arizona.edu
Notes:
    This file assumes it's in a subfolder off the main folder
"""

import os
import re
from subprocess import getstatusoutput

import testing

SOURCE_FILE = 'testing.py'
IMAGES = 'images'
PARTIAL_PATH = os.path.abspath(os.path.join('.', SOURCE_FILE))
SOURCE_PATH = os.path.abspath(os.path.join('.', IMAGES))


def test_exists():
    """Asserts that the source file is available"""
    assert os.path.isfile(SOURCE_PATH)


def test_usage():
    """
    Program prints a "usage" statement when requested
    """
    for flag in ['-h', '--help']:
        ret_val, out = getstatusoutput(f'{SOURCE_PATH} {flag}')
        assert ret_val == 1
        assert re.match('usage', out, re.IGNORECASE)


def test_arguments():
    """
    Tests testing.py's check_arguments() function
    """
    return testing.check_arguments()