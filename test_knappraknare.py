import pytest
from raknare import berakna_total, convert, format_total

class TestExample:
    def test_berakna_total(self):

        kvitto = [
            ("Mjölk", 100.00, 0.25),
            ("Bok", 100.00, 0.25)
        ]
        assert berakna_total(kvitto) == 250


class TestFormatTotal:
    kvitto = [
        ("Mjölk", 100.00, 0.25),
        ("Bok", 100.00, 0.25)
    ]

    def test_default_currency_is_sek(self):
        assert format_total(self.kvitto) == "250.00 SEK"

    @pytest.mark.parametrize("currency", ["EUR", "USD"])
    def test_other_currencies(self, currency):
        assert format_total(self.kvitto, currency) == f"250.00 {currency}"

    def test_lowercase_currency_is_accepted(self):
        assert format_total(self.kvitto, "usd") == "250.00 USD"

    def test_unknown_currency_raises(self):
        with pytest.raises(ValueError):
            format_total(self.kvitto, "GBP")

    def test_empty_receipt(self):
        assert format_total([]) == "0.00 SEK"

    def test_convert_sek_receipt_to_eur(self):
        assert format_total(self.kvitto, "SEK", "EUR") == "22.73 EUR"

    def test_convert_eur_receipt_to_sek(self):
        assert format_total(self.kvitto, "EUR", "SEK") == "2750.00 SEK"

    def test_unknown_target_currency_raises(self):
        with pytest.raises(ValueError):
            format_total(self.kvitto, "SEK", "GBP")


class TestConvert:
    def test_same_currency_is_unchanged(self):
        assert convert(250, "SEK", "SEK") == 250

    def test_sek_to_usd(self):
        assert convert(250, "SEK", "USD") == 25.00

    def test_eur_to_usd(self):
        assert convert(100, "EUR", "USD") == 110.00

    def test_default_target_is_sek(self):
        assert convert(10, "EUR") == 110.00

    def test_lowercase_codes(self):
        assert convert(250, "sek", "usd") == 25.00

    def test_unknown_currency_raises(self):
        with pytest.raises(ValueError):
            convert(100, "GBP", "SEK")
