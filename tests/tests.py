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

from doctest import testmod
from os.path import join, dirname
from cStringIO import StringIO
import sys
import unittest

from osm import osm

EXAMPLE_BIG = join(dirname(__file__), './big.scad')


class TestMinimize(unittest.TestCase):
    """Framework for testing file minimization."""
    # pylint: disable-msg=R0904

    def setUp(self):
        """Set streams."""
        # pylint: disable-msg=C0103
        self.input_stream = None


    def test_big(self):
        """Check that there is some output."""
        self.input_stream = open(EXAMPLE_BIG)
        result = osm.osm(self.input_stream)

        self.assertNotEqual(
            result,
            None)
        self.assertNotEqual(
            result,
            '')


    def tearDown(self):
        """Close streams."""
        # pylint: disable-msg=C0103
        self.input_stream.close()


class TestDoc(unittest.TestCase):
    """Test Python documentation strings."""
    def test_doc(self):
        """Documentation tests."""
        self.assertEqual(testmod(osm)[0], 0)


def main():
    """Run tests"""
    unittest.main()


if __name__ == '__main__':
    main()
