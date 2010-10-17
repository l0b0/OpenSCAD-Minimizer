#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""OpenSCAD Minimizer - Reduce the size of your .scad file
<http://github.com/l0b0/OpenSCAD-Minimizer>

Default syntax:

osm < input_file

Description:

Removes unnecessary whitespace and comments.

Examples:

osm < old.scad > new.scad
    Minimize old.scad and save the result in new.scad.

<http://www.thingiverse.com/thing:4448>

Bugs:

Please email bug reports including a minimal test file (if applicable) to
victor dot engmark at gmail dot com.
"""

__author__ = 'Victor Engmark'
__email__ = 'victor.engmark@gmail.com'
__copyright__ = 'Copyright (C) 2010 Victor Engmark'
__license__ = 'GPLv3'

import os
import re
import signal
import sys

signal.signal(signal.SIGPIPE, signal.SIG_DFL)
"""Avoid 'Broken pipe' message when canceling piped command."""


def remove_multi_line_comments(text):
    """."""
    text = re.sub(r'/\*.*\*/', r'', text)
    return text


def remove_empty_lines(text):
    """Remove empty lines of text in the input."""
    text = re.sub(r'\A\n+', r'', text) # Start
    text = re.sub(r'\n+', r'\n', text) # Middle
    text = re.sub(r'\n+\Z', r'', text) # End
    return text

def remove_single_line_comments(text):
    """."""
    #TODO
    return text


def remove_newlines(text):
    """."""
    #TODO
    return text


def osm(stream):
    """."""
    text = stream.read()
    text = remove_multi_line_comments(text)
    text = remove_single_line_comments(text)
    text = remove_empty_lines(text)
    print text


def main(argv = None):
    osm(sys.stdin)


if __name__ == '__main__':
    sys.exit(main())
