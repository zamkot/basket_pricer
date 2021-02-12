from typing import Tuple

from pricer.pricer import Offer, Basket, Catalogue


def multibuy(item: str, buy: int, get: int) -> Offer:

    def offer(basket: Basket, catalogue: Catalogue) -> Tuple[float, Basket]:

        basket = basket.copy()

        if item not in basket or item not in catalogue:
            return 0, basket

        if basket[item] >= buy + get:
            basket[item] -= (buy + get)
            return buy * catalogue[item], basket
        else:
            return 0, basket

    return offer


def discount(item: str, percent: int) -> Offer:

    def offer(basket: Basket, catalogue: Catalogue) -> Tuple[float, Basket]:

        basket = basket.copy()

        if item not in basket or item not in catalogue:
            return 0, basket

        if basket[item] == 1:
            basket.pop(item)
        else:
            basket[item] -= 1

        return catalogue[item] * (100 - percent) / 100, basket

    return offer
