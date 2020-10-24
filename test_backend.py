# Python3
# test_backend.py

import pytest
import backend as be

@pytest.fixture
def VAR():
    item = "food"
    amount = 15.00
    date = '10/15/2020'
    return item, amount, date

def test_main_item(VAR):
    item  = VAR[0]
    dev_mode = 1
    result = be.main(dev_mode, item, amount, date)
    assert result[0] == item

def test_main_amount():

    dev_mode = 1
    result = be.main(dev_mode, item, amount, date)
    assert result[1] == 15.00

def test_main_date():
    item = "food"
    amount = 15.00
    date = '10/15/2020'
    dev_mode = 1
    result = be.main(dev_mode, item, amount, date)
    assert result[2] == '10/15/2020'