import pytest
from assignment import convert_roman_numeral_to_int

def test_invalid_input():
    # Invalid characters
    assert convert_roman_numeral_to_int("ABCD") == -1
    # Too many repeats
    assert convert_roman_numeral_to_int("IIII") == -1
    # Empty string
    assert convert_roman_numeral_to_int("") == -1

def test_case_insensitivity():
    assert convert_roman_numeral_to_int("i") == 1
    assert convert_roman_numeral_to_int("I") == 1

def test_correct_evaluation():
    assert convert_roman_numeral_to_int("III") == 3
    assert convert_roman_numeral_to_int("IV") == 4
    assert convert_roman_numeral_to_int("IX") == 9
    assert convert_roman_numeral_to_int("LVIII") == 58

def test_complex_cases():
    assert convert_roman_numeral_to_int("MCMXC") == 1990
    assert convert_roman_numeral_to_int("MCMXCIV") == 1994
    assert convert_roman_numeral_to_int("CLX") == 160
    assert convert_roman_numeral_to_int("MMXXIII") == 2023