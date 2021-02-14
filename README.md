# Basker Pricer

Basket Pricer is a Python library for applying special offers to your shopping basket.


## Usage

### Basic functionality

Basket Pricer's core functionality is applying various types of discounts (offers) to a shoppping basket. 

The package comes with two built in offer types:  
* Multibuy ie. "Buy 2 Get 1 Free"
* Discount ie. "25% Off"

The API is pretty straightforward and the usage comes down to passing your `basket`, `offers` and `catalogue` to the `sum_up` function which returns the `subtotal`, `discount` and `total` for the items in the basket.

```python
import pricer
catalogue = {
    'baked_beans': 0.99,
    'biscuits': 1.2,
    'sardines': 1.89,
    'shampoo (small)': 2.0,
    'shampoo (medium)': 2.5,
    'shampoo (large)': 3.5,
}
offers = [
    pricer.multibuy('baked_beans', buy=2, get=1),
    pricer.discount('sardines', percent=25),
]
basket = {
    'baked_beans': 4,
    'biscuits': 1,
}
subtotal, discount, total = pricer.sum_up(basket, offers, catalogue)
print(
    f'Subtotal: {subtotal:.2f}\n'
    f'Discount: {discount:.2f}\n'
    f'Total: {total:.2f}\n'
)
```

### Implementing custom offers

```python
Offer = Callable[[Basket, Catalogue], Tuple[float, Basket]]
```

The protocol for an `Offer` is:  
1. Accept a `Basket` and a `Catalogue` as arguments
2. Apply the offer exactly once - if the basket contains two pieces of a discounted item, the offer should discount only a single piece. This is a requirement for calculating the maximum discount for a basket.
3. Return the total for the discounted items as `float` and a new `Basket` with the discounted items removed

If you need reusable offers, consider implementing them as factory functions (see `pricer/offers.py`) or classes (see `tests/test_user_offer.py`).


## Tests

This repository comes with a collection of unit tests and a tox file adding to the devlopment experience.  
Follow this example to run the tests locally:
```sh
python3 -m venv venv && source ./venv/bin/activate  # creating a virtual environment is optional but recommended
pip install tox
tox -r  # run static type checking and unit tests
```

The package has been tested with Python 3.8 but should work with Python 3.5+
