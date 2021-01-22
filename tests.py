#DO NOT TAMPER WITH THIS FILE
#ANY EDITS YOU MAKE TO THIS FILE WILL BE SAVED TO YOUR PUBLIC GITHUB HISTORY
#TAMPERING WITH THIS FILE WILL BE OBVIOUS AND WILL RESULT IN A ZERO

import main;
import datetime;

year = 2021
month = 1
day = 22

def test_code():
    assert main.factOrSum(3, "sum") == 6, "factOrSum(3, 'sum') == 6 failed"
    assert main.factOrSum(4, "factorial") == 24, "factOrSum(4, 'factorial') == 24 failed"

def test_late():
    assert datetime.datetime.now() < datetime.datetime(year, month, day + 1, 4, 0), "Submitted Late"
