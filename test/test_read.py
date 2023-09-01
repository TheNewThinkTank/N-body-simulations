"""
Unit tests for the Read program
"""

import src.attractor.read as read


def test_get_sphere_volume():
    assert 4188790.2047863905 == read.get_sphere_volume(100)
