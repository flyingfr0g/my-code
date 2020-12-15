#!/usr/bin/env python3

"""Alexnander Scull | building functions to test"""

#The Homer function expecs a word to be passed to it
# if it is not passed a word it will assume the word is "salad"

def homer(sd="salad"):
    return f"You dont win friends with {sd}"

#The Milhouse function expects a word to be passed to it
# if it is not given one it will assume the word is "milhouse"

def milhouse(mh="milhouse"):
    return f"everything is coming up {mh}"

#the troy mcclure function expects a word to be passed to it
# if it is not given one it will assume the word to be 3

def troymmclure(tm=3):
    if tm > 2:
        return f"2 minus {tm} equals negative fun!"
    else:
        return None

# tests must begin with "test"

# tests MUST begin with the word test_ or they will be ignored
def test_homer():
    # assert will return true or raise an AssertionError
    # the primary application is debugging
    assert homer("doughnuts") == "You don't win friends with doughnuts"

# tests MUST begin with the word test_ or they will be ignored
def test_milhouse():
    # assert will return true or raise an AssertionError
    # the primary application is debugging
    assert milhouse("daffodils") == "Everything is coming up daffodils"

# tests MUST begin with the word test_ or they will be ignored
def test_troymcclure():
    assert troymcclure(5) == "2 minus 5 equals negative fun!"
    assert not troymcclure(1)
    
# testing a failure
def test_homer_fail():
    # This should produce a failure.
    assert homer("pretzels") == "You don't win friends with salad"
