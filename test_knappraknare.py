import pytest
from raknare import berakna_total, format_total

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
