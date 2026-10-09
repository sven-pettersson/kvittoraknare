DISCOUNT_CODE = "RABATT10"


def berakna_total(varor, rabattkod=None):
    """Returnerar totalsumman inklusive moms, avrundad till två decimaler.

    varor: lista med tupler (namn, pris_exkl_moms, momssats),
    där momssats anges som decimaltal, t.ex. 0.25 för 25 %.
    rabattkod: valfri rabattkod; RABATT10 ger 10 % rabatt före moms.
    """
    if rabattkod is not None and rabattkod != DISCOUNT_CODE:
        raise ValueError("Ogiltig rabattkod")

    rabatt = 0.9 if rabattkod == DISCOUNT_CODE else 1
    total = 0
    for namn, pris, momssats in varor:
        total += pris * rabatt * (1 + momssats)
    return round(total, 2)


if __name__ == "__main__":
    kvitto = [
        ("Mjölk", 15.00, 0.12),
        ("Bok", 200.00, 0.06),
        ("Hörlurar", 400.00, 0.25),
    ]
    print(berakna_total(kvitto))  # 16.80 + 212.00 + 500.00 = 728.8
