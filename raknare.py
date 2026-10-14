import json
import math
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from urllib import request
from urllib.parse import urlencode


SUPPORTED_CURRENCIES = {"SEK", "EUR", "USD"}


def _validate_currency(currency):
    if not isinstance(currency, str):
        raise ValueError("Currency must be one of SEK, EUR, or USD.")
    normalized_currency = currency.upper()
    if normalized_currency not in SUPPORTED_CURRENCIES:
        raise ValueError("Currency must be one of SEK, EUR, or USD.")
    return normalized_currency


def _to_decimal(value, label):
    try:
        number = Decimal(str(value))
    except InvalidOperation as error:
        raise ValueError(f"{label} must be a finite number.") from error
    if not number.is_finite():
        raise ValueError(f"{label} must be a finite number.")
    return number


def _get_exchange_rate(source_currency, target_currency):
    if source_currency == target_currency:
        return Decimal("1")

    query = urlencode({"base": source_currency, "symbols": target_currency})
    url = f"https://api.frankfurter.dev/v1/latest?{query}"
    try:
        api_request = request.Request(
            url, headers={"User-Agent": "kvittoraknare/1.0"}
        )
        with request.urlopen(api_request, timeout=10) as response:
            payload = json.loads(response.read())
    except OSError as error:
        raise RuntimeError(
            f"Could not retrieve the {source_currency} to "
            f"{target_currency} exchange rate from Frankfurter."
        ) from error
    except (json.JSONDecodeError, UnicodeDecodeError) as error:
        raise RuntimeError("Frankfurter returned an invalid response.") from error

    if not isinstance(payload, dict) or not isinstance(payload.get("rates"), dict):
        raise RuntimeError("Frankfurter returned an invalid exchange-rate response.")

    rate = payload["rates"].get(target_currency)
    if isinstance(rate, bool) or not isinstance(rate, (int, float)):
        raise RuntimeError(
            f"Frankfurter did not provide a rate for {target_currency}."
        )
    if not math.isfinite(rate) or rate <= 0:
        raise RuntimeError("Frankfurter returned an invalid exchange rate.")
    return Decimal(str(rate))


def berakna_total(varor, target_currency="SEK"):
    """Returnera totalsumman inklusive moms i målvalutan, avrundad till två decimaler.

    Poster anges som (name, price_excluding_vat, vat_rate) eller
    (name, price_excluding_vat, vat_rate, currency). Poster utan valuta
    tolkas som SEK. Momssatsen anges som decimaltal, t.ex. 0.25 för 25 %.
    """
    target_currency = _validate_currency(target_currency)
    exchange_rates = {}
    total = Decimal("0")

    for item in varor:
        if len(item) == 3:
            _, price, vat_rate = item
            source_currency = "SEK"
        elif len(item) == 4:
            _, price, vat_rate, source_currency = item
            source_currency = _validate_currency(source_currency)
        else:
            raise ValueError(
                "Each receipt item must contain three or four values."
            )

        price = _to_decimal(price, "Price")
        vat_rate = _to_decimal(vat_rate, "VAT rate")

        if source_currency not in exchange_rates:
            exchange_rates[source_currency] = _get_exchange_rate(
                source_currency, target_currency
            )

        total += (
            price
            * (Decimal("1") + vat_rate)
            * exchange_rates[source_currency]
        )

    rounded_total = total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return float(rounded_total)


if __name__ == "__main__":
    kvitto = [
        ("Mjölk", 15.00, 0.12),
        ("Bok", 200.00, 0.06),
        ("Hörlurar", 400.00, 0.25),
    ]
    print(berakna_total(kvitto))  # 16.80 + 212.00 + 500.00 = 728.8
