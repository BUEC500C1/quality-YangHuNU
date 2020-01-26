import pytest
from arabic_to_roman import int_to_Roman

def test_c():
  assert int_to_Roman(10) == 'X'
