import pytest
from arabic_to_roman import int_to_Roman

# Ordered Cases
def test_a():
  val = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  syb = ["I", "II", "III", "IV","V", "VI","VII", "VIII","IX","X"]
  for i in range(0, 10):
    assert int_to_Roman(val[i]) == syb[i]
    
# Random Cases
def test_b():
  val = [499, 11, 2453, 89, 2681, 16, 789, 44, 137, 3999]
  syb = ["CDXCIX", "XI", "MMCDLIII", "LXXXIX","MMDCLXXXI", "XVI","DCCLXXXIX", "XLIV","CXXXVII","MMMCMXCIX"]
  for i in range(0, 10):
    assert int_to_Roman(val[i]) == syb[i]
  
# Simple Cases 
def test_c():
  val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
  syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
  for i in range(0, 13):
    assert int_to_Roman(val[i]) == syb[i]
    
# Exceptional Cases
def test_b():
  val = [0, -1, 'abc', '8b9', 4000, 160134, '789', '44', '137', '3999']
  syb = ["Number out of range", "Number out of range", "String is not an int", "String is not an int","Number out of range", "Number out of range","String is not an int", "String is not an int","String is not an int","String is not an int"]
  for i in range(0, 10):
    assert int_to_Roman(val[i]) == syb[i]
