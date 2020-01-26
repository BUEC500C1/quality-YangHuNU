import pytest
from arabic_to_roman import arabic_to_Roman

def test_c():
  assert arabic_to_Roman(10) == 'X'
