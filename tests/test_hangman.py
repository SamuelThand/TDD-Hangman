#!/usr/bin/env python

import json
import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestPlaceholder(unittest.TestCase):

    def test_tmp(self):
        self.assertTrue(1, 0)
        pass
