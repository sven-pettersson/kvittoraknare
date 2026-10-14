DEFAULT_RATES = {
    "SEK": 1.0,
    "EUR": 11.0,
    "USD": 10.0,
}


def berakna_total(varor, basvaluta="SEK", kurser=None):
    """Returnerar totalsumman inklusive moms i basvalutan, avrundad till två decimaler.

    varor: lista med tupler (namn, pris_exkl_moms, momssats, valuta),
    där momssats anges som decimaltal, t.ex. 0.25 för 25 %.
    valuta är valfri och defaultar till "SEK".

    basvaluta: valutan som summan uttrycks i, default "SEK".
    kurser: dict med antal SEK per 1 enhet av varje valuta.
    Defaultar till DEFAULT_RATES.
    """
    if kurser is None:
        kurser = DEFAULT_RATES

    if basvaluta not in kurser:
        raise ValueError(f"Okänd valuta: {basvaluta}")

    total_sek = 0
    for rad in varor:
        namn, pris, momssats = rad[0], rad[1], rad[2]
        valuta = rad[3] if len(rad) > 3 else "SEK"
        if valuta not in kurser:
            raise ValueError(f"Okänd valuta: {valuta}")
        total_sek += pris * (1 + momssats) * kurser[valuta]

    return round(total_sek / kurser[basvaluta], 2)


if __name__ == "__main__":
    kvitto = [
        ("Mjölk", 15.00, 0.12, "SEK"),
        ("Bok", 200.00, 0.06, "SEK"),
        ("Hörlurar", 400.00, 0.25, "USD"),
    ]
    print(berakna_total(kvitto))  # 16.80 + 212.00 + 5000.00 = 5228.8 SEK
