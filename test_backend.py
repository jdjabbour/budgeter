# Python3
# test_backend.py

# pytest -v -m <marker name>

import pytest
import backend as be

@pytest.fixture
def VARS():
    item = "Food"
    amount = 15.0
    debit_credit = 'DEbit'
    date = '10/24/2020'

    sc = be.Scrub_input(item, amount, debit_credit, date)

    return sc

@pytest.mark.run
def test_scrub_item(VARS):
    item = VARS.scrub_item()
    assert item == 'food'
    
@pytest.mark.run
def test_scrub_amount(VARS):
    amount = VARS.scrub_amount()
    assert amount == 15.00

def test_scrub_debit(VARS):
    debit = VARS.scrub_scrub_debit()
    assert debit == 'debit'

def test_debit_amount():
    pass

def test_scrub_credit():
    pass

def test_credit_amount():
    pass

