from typing import Dict, Iterable, Protocol, Tuple


Basket = Dict[str, int]
Catalogue = Dict[str, float]


class Offer(Protocol):
    @staticmethod
    def __call__(basket: Basket, catalogue: Catalogue) -> Tuple[float, Basket]:
        ...


def sum_up(
        basket: Basket,
        offers: Iterable[Offer],
        catalogue: Catalogue,
) -> Tuple[float, float, float]:

    subtotal = get_subtotal(basket, catalogue)
    max_discount = 0

    for offer in offers:

        reduced_value, new_basket = offer(basket, catalogue)

        if new_basket != basket:
            s, d, t = sum_up(new_basket, offers, catalogue)
            total = reduced_value + t
            discount = subtotal - total
        else:
            discount = 0

        max_discount = max(max_discount, discount)

    return subtotal, max_discount, subtotal - max_discount


def get_subtotal(basket: Basket, catalogue: Catalogue):
    return sum(count * catalogue[item] for item, count in basket.items())
