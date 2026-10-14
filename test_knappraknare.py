import pytest
from raknare import berakna_total


class TestExample:
    def test_berakna_total(self):
        kvitto = [
            ("Mjölk", 100.00, 0.25),
            ("Bok", 100.00, 0.25)
        ]
        assert berakna_total(kvitto) == 250

    def test_berakna_total_with_discount_code_applies_discount_before_vat(self):
        kvitto = [
            ("Headphones", 100.00, 0.25),
            ("Book", 100.00, 0.06),
        ]

        assert berakna_total(kvitto, discount_code="RABATT10") == 207.9

    def test_berakna_total_with_invalid_discount_code_raises_error(self):
        with pytest.raises(ValueError, match="Invalid discount code"):
            berakna_total([("Book", 100.00, 0.25)], discount_code="UNKNOWN")
