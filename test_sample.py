import numpy as np
import pytest


# content of test_sample.py
def inc2(x):
    return x + 2


def test_answer():
    assert inc2(3) == 5