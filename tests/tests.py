#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
OpenSCAD Minimizer test suite

Default syntax:

./tests.py
    Run all unit tests
"""

__author__ = 'Victor Engmark'
__email__ = 'victor.engmark@gmail.com'
__copyright__ = 'Copyright (C) 2010 Victor Engmark'
__license__ = 'GPLv3'

import doctest
import os
from cStringIO import StringIO
import sys
import unittest

from osm import osm

EXAMPLE_BIG = os.path.join(os.path.dirname(__file__), './big.scad')


class TestConvert(unittest.TestCase):
    """Framework for testing file conversion."""
    # pylint: disable-msg=R0904

    def setUp(self):
        """Set streams."""
        # pylint: disable-msg=C0103
        self.input_stream = None
        self.stdin = sys.stdin

        self.output_stream = StringIO()
        self.stdout = sys.stdout


    def tearDown(self):
        """Close streams."""
        # pylint: disable-msg=C0103
        self.input_stream.close()
        sys.stdin = self.stdin

        self.output_stream.close()
        sys.stdout = self.stdout


class TestDoc(unittest.TestCase):
    """Test Python documentation strings."""
    def test_doc(self):
        """Documentation tests."""
        self.assertEqual(doctest.testmod(osm)[0], 0)


def main():
    """Run tests"""
    unittest.main()


if __name__ == '__main__':
    main()
