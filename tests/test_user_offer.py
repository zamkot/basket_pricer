import itertools
from functools import partial
from typing import Tuple
from collections import Counter

import pytest

import pricer
from pricer.pricer import Basket, Catalogue


approx = partial(pytest.approx, abs=1e-02)


class CheapestFreeOffer:

    def __init__(self, *items, num_items: int = 3):
        self.items = set(items)
        self.num_items = num_items

    def __call__(
        self, basket: Basket, catalogue: Catalogue
    ) -> Tuple[float, Basket]:

        basket = basket.copy()

        selected_items = [
            (item, count) for item, count
            in basket.items()
            if item in self.items
        ]

        sorted_items = sorted(
            selected_items,
            reverse=True,
            key=lambda item: catalogue[item[0]],
        )

        lineup = list(itertools.chain.from_iterable(
            [item] * count for item, count in sorted_items
        ))  # memory goes brrrrr

        try:
            pay_for = lineup[:self.num_items-1]
            rest = lineup[self.num_items:]
        except IndexError:
            return 0, basket

        return sum(catalogue[item] for item in pay_for), dict(Counter(rest))


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


def test_cheapest_free(catalogue):
    offers = [
        CheapestFreeOffer(
            'shampoo (large)',
            'shampoo (medium)',
            'shampoo (small)',
            num_items=3,
        )
    ]

    basket = {
        'shampoo (large)': 3,
        'shampoo (medium)': 1,
        'shampoo (small)': 2,
    }

    subtotal, discount, total = pricer.sum_up(basket, offers, catalogue)

    assert approx(subtotal) == 17
    assert approx(discount) == 5.5
    assert approx(total) == 11.5
