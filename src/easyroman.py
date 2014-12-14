# -*- coding: UTF-8 -*-
__author__ = 'Qunfei Wu'
__version__ = '0.1'
__date__ = '14/12/14'
__copyright__ = """Copyright (c) 2014 Qunfei Wu"""

__doc__ = """
The roman numerals can be express by Context free grammar.
The possible Numerals that can be used in a Roman number and they defined as follows:
T = {'I','V','X','L','C','D','M'}

The start symbol for our Roman Numerals grammar is: ROMAN
    S = ROMAN
    RomanGrammar = (V,T,S,P)

    1.V = {ROMAN,THOUS,le300,HUNDS,le30,TENS,le3,UNITS}
    2.T = {'I','V','X','L','C','D','M'}
    3.S = ROMAN
    4.P =
        ROMAN THOUS HUNDS TENS UNITS THOUS 'M' THOUS | e
        le300 e | C | CC | CCC
        HUNDS le300 |CD | 'D'le300 |CM
        le30 e | X | XX | XXX
        TENS le30 |XL | 'L'le30 |XC
        le3 e | I | II | III
        UNITS le3 |IV | 'V'le30 |IX

Reference:
    http://en.wikipedia.org/wiki/Roman_numerals
    http://en.wikipedia.org/wiki/Context-free_grammar
    http://www.cs.bath.ac.uk/~occ/comp0029/roman_numerals.shtml

Usages:
    import easyroman
    easyroman.to_roman(12)
    return "XII"
"""

# Define exceptions

class RomanError(Exception): pass


class OutOfRangeError(RomanError): pass


class NotIntegerError(RomanError): pass

# Define digit mapping
roman_numeral_map = (('M', 1000),
                     ('CM', 900),
                     ('D', 500),
                     ('CD', 400),
                     ('C', 100),
                     ('XC', 90),
                     ('L', 50),
                     ('XL', 40),
                     ('X', 10),
                     ('IX', 9),
                     ('V', 5),
                     ('IV', 4),
                     ('I', 1))


def to_roman(n):
    """convert integer to Roman numeral"""

    if isinstance(n, int) or isinstance(n, float):
        if int(n) != n:
            raise NotIntegerError, "decimals can not be converted"
        if not (0 < n < 4000):
            raise OutOfRangeError, "number out of range (must be 1..3999), the biggest number in Roman is MMMCMXCIX(3999)"
    else:
        raise NotIntegerError, "%s can not be converted" % str(type(n))

    roman_numeral = ""
    for numeral, integer in roman_numeral_map:
        while n >= integer:
            roman_numeral += numeral
            n -= integer
    return roman_numeral