import random

regions = [
    ("North America"),
    ("South America"),
    ("Europe"),
    ("Australia"),
    ("South Asia"),
    ("South East Asia"),
    ("Africa"),
    ("East Asia"),
    ("Central Asia"),
]


def random_region():
    region = random.choice(regions)
    return region[1]
