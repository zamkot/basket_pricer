import pytest

import pricer


@pytest.fixture
def catalogue():
    return {
        'baked_beans': 0.99,
        'biscuits': 1.2,
        'sardines': 1.89,
        'shampoo (small)': 2.0,
        'shampoo (medium)': 2.5,
        'shampoo (large)': 3.5,
    }


def test_1(catalogue):
    offers = [
        pricer.multibuy('baked_beans', buy=2, get=1),
        pricer.discount('sardines', percent=25),
    ]

    basket = {
        'baked_beans': 4,
        'biscuits': 1,
    }

    subtotal, discount, total = pricer.sum_up(basket, offers, catalogue)

    assert subtotal == 5.16
    assert discount == 0.99
    assert total == 4.17


def test_2(catalogue):
    offers = [
        pricer.multibuy('baked_beans', buy=2, get=1),
        pricer.discount('sardines', percent=25),
    ]

    basket = {
        'baked_beans': 2,
        'biscuits': 1,
        'sardines': 2,
    }

    subtotal, discount, total = pricer.sum_up(basket, offers, catalogue)

    assert subtotal == 6.96
    assert discount == 0.95
    assert total == 6.01
