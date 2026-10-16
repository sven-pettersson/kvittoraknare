def berakna_total(varor):
    """Returnerar totalsumman inklusive moms, avrundad till två decimaler.

    varor: lista med tupler (namn, pris_exkl_moms, momssats),
    där momssats anges som decimaltal, t.ex. 0.25 för 25 %.
    """
    total = 0
    for namn, pris, momssats in varor:
        total += pris * (1 + momssats)
    return round(total, 2)


def format_receipt(items):
    """Return a formatted receipt for items with VAT rates given as percentages."""
    if not items:
        return "Inga varor"

    def format_amount(amount):
        return f"{amount:.2f}".replace(".", ",")

    lines = ["KVITTO"]
    subtotal = 0
    vat_totals = {}

    for name, price, vat_rate in items:
        if len(name) > 20:
            name = name[:17] + "..."
        lines.append(f"{name:<25}{format_amount(price):>6}")
        subtotal += price
        vat_totals[vat_rate] = vat_totals.get(vat_rate, 0) + price * vat_rate / 100

    lines.append("-" * 31)
    lines.append(f"{'Summa exkl. moms':<25}{format_amount(subtotal):>6}")

    total_vat = 0
    for vat_rate in sorted(vat_totals, reverse=True):
        vat_amount = vat_totals[vat_rate]
        total_vat += vat_amount
        lines.append(
            f"{f'Moms {vat_rate:g} %':<25}{format_amount(vat_amount):>6}"
        )

    lines.append("-" * 31)
    lines.append(f"{'ATT BETALA':<25}{format_amount(subtotal + total_vat):>6}")
    return "\n".join(lines)


def print_receipt(items):
    """Print each item including VAT, followed by the receipt total."""
    print("Kvitto")
    for name, price, vat_rate in items:
        item_total = price * (1 + vat_rate)
        print(f"{name}: {item_total:.2f} kr")
    print(f"Totalt: {berakna_total(items):.2f} kr")


VAT_RATES = frozenset({25, 12, 6})


def vat_breakdown(items):
    """Returnerar momsbelopp per momssats, t.ex. {25: 25.0, 12: 6.0}.

    Raises ValueError om en vara har en momssats som inte finns i VAT_RATES.
    """
    breakdown = {}
    for name, price, rate in items:
        if rate not in VAT_RATES:
            raise ValueError(f"Okänd momssats {rate} för {name}")
        vat = price * rate / 100
        breakdown[rate] = breakdown.get(rate, 0) + vat
    return breakdown


if __name__ == "__main__":
    kvitto = [
        ("Mjölk", 15.00, 0.12),
        ("Bok", 200.00, 0.06),
        ("Hörlurar", 400.00, 0.25),
    ]
    print(berakna_total(kvitto)) 
    print("-----------------------") # 16.80 + 212.00 + 500.00 = 728.8
    print_receipt(kvitto)
    print("-----------------------")
    print(format_receipt(kvitto))
