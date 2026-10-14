def berakna_total(varor):
    """Returnerar totalsumman inklusive moms, avrundad till två decimaler.

    varor: lista med tupler (namn, pris_exkl_moms, momssats),
    där momssats anges som decimaltal, t.ex. 0.25 för 25 %.
    """
    total = 0
    for namn, pris, momssats in varor:
        total += pris * (1 + momssats)
    return round(total, 2)


# Statiska växelkurser: antal SEK per 1 enhet av valutan.
# Platshållarvärden, inte riktiga kurser.
EXCHANGE_RATES = {"SEK": 1.0, "EUR": 11.0, "USD": 10.0}


def _rate(currency):
    code = currency.upper()
    if code not in EXCHANGE_RATES:
        raise ValueError(f"Valutan stöds inte: {currency}")
    return code, EXCHANGE_RATES[code]


def convert(amount, from_currency, to_currency="SEK"):
    """Räknar om ett belopp mellan två valutor, avrundat till två decimaler."""
    _, from_rate = _rate(from_currency)
    _, to_rate = _rate(to_currency)
    return round(amount * from_rate / to_rate, 2)


def format_total(items, currency="SEK", to_currency=None):
    """Returnerar totalsumman som text med valutakod, t.ex. "728.80 SEK".

    Hela kvittot har en och samma valuta (currency), som priserna anges i.
    Om to_currency anges räknas summan om till den valutan.
    Okänd valuta ger ValueError.
    """
    code, _ = _rate(currency)
    target, _ = _rate(to_currency or currency)
    amount = convert(berakna_total(items), code, target)
    return f"{amount:.2f} {target}"


if __name__ == "__main__":
    kvitto = [
        ("Mjölk", 15.00, 0.12),
        ("Bok", 200.00, 0.06),
        ("Hörlurar", 400.00, 0.25),
    ]
    print(format_total(kvitto, "SEK"))  # 16.80 + 212.00 + 500.00 = 728.80 SEK
    print(format_total(kvitto, "SEK", "EUR"))  # 728.80 / 11 = 66.25 EUR
