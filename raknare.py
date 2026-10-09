DISCOUNT_CODE = "RABATT10"
DISCOUNT_RATE = 0.10


def berakna_total(varor, discount_code=None):
    """Returnerar totalsumman inklusive moms, avrundad till två decimaler.

    varor: lista med tupler (namn, pris_exkl_moms, momssats),
    där momssats anges som decimaltal, t.ex. 0.25 för 25 %.
    discount_code: valfri rabattkod. Giltig kod ger 10 % rabatt på hela
    kvittot. Rabatten dras på priset exkl. moms, innan momsen räknas.
    Ogiltig kod ger ValueError.
    """
    discount = 0
    if discount_code is not None:
        if discount_code != DISCOUNT_CODE:
            raise ValueError(f"Ogiltig rabattkod: {discount_code}")
        discount = DISCOUNT_RATE

    total = 0
    for namn, pris, momssats in varor:
        discounted_price = pris * (1 - discount)
        total += discounted_price * (1 + momssats)
    return round(total, 2)


if __name__ == "__main__":
    kvitto = [
        ("Mjölk", 15.00, 0.12),
        ("Bok", 200.00, 0.06),
        ("Hörlurar", 400.00, 0.25),
    ]
    print(berakna_total(kvitto))  # 16.80 + 212.00 + 500.00 = 728.8
    print(berakna_total(kvitto, "RABATT10"))  # 728.8 * 0.9 = 655.92
