DISCOUNT_CODE = "RABATT10"
DISCOUNT_RATE = 0.10


def berakna_total(varor, discount_code=None):
    """Return the receipt total including VAT, rounded to two decimals.

    ``varor`` is a list of tuples (name, price_excluding_vat, vat_rate),
    where vat_rate is a decimal, e.g. 0.25 for 25%.
    The RABATT10 discount is applied to prices before VAT is calculated.
    """
    if discount_code is not None and discount_code != DISCOUNT_CODE:
        raise ValueError("Invalid discount code")

    discount_rate = DISCOUNT_RATE if discount_code == DISCOUNT_CODE else 0
    total = 0
    for name, price, vat_rate in varor:
        discounted_price = price * (1 - discount_rate)
        total += discounted_price * (1 + vat_rate)
    return round(total, 2)


if __name__ == "__main__":
    kvitto = [
        ("Mjölk", 15.00, 0.12),
        ("Bok", 200.00, 0.06),
        ("Hörlurar", 400.00, 0.25),
    ]
    print(berakna_total(kvitto))  # 16.80 + 212.00 + 500.00 = 728.8
