def berakna_total(varor):
    """Returnerar totalsumman inklusive moms, avrundad till två decimaler.

    varor: lista med tupler (namn, pris_exkl_moms, momssats),
    där momssats anges som decimaltal, t.ex. 0.25 för 25 %.
    """
    total = 0
    for namn, pris, momssats in varor:
        total += pris * (1 + momssats)
    return round(total, 2)


SUPPORTED_CURRENCIES = ("SEK", "EUR", "USD")


def format_total(items, currency="SEK"):
    """Returnerar totalsumman som text med valutakod, t.ex. "728.80 SEK".

    Hela kvittot har en och samma valuta. Okänd valuta ger ValueError.
    """
    code = currency.upper()
    if code not in SUPPORTED_CURRENCIES:
        raise ValueError(f"Valutan stöds inte: {currency}")
    return f"{berakna_total(items):.2f} {code}"


if __name__ == "__main__":
    kvitto = [
        ("Mjölk", 15.00, 0.12),
        ("Bok", 200.00, 0.06),
        ("Hörlurar", 400.00, 0.25),
    ]
    print(format_total(kvitto, "SEK"))  # 16.80 + 212.00 + 500.00 = 728.80 SEK
