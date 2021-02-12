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
    pass
