import pytest
from raknare import berakna_total

class TestExample:
    def test_berakna_total(self):

        kvitto = [
            ("Mjölk", 100.00, 0.25),
            ("Bok", 100.00, 0.25)
        ]
        assert berakna_total(kvitto) == 250


class TestDiscountCode:
    def test_discount_gives_ten_percent_off(self):
        kvitto = [
            ("Mjölk", 100.00, 0.25),
            ("Bok", 100.00, 0.25)
        ]
        # (200 * 0.9) * 1.25 = 225
        assert berakna_total(kvitto, "RABATT10") == 225

    def test_discount_applied_before_vat_with_mixed_rates(self):
        kvitto = [
            ("Mjölk", 15.00, 0.12),
            ("Bok", 200.00, 0.06),
            ("Hörlurar", 400.00, 0.25),
        ]
        # 13.50*1.12 + 180*1.06 + 360*1.25 = 15.12 + 190.80 + 450.00
        assert berakna_total(kvitto, "RABATT10") == 655.92

    def test_no_code_gives_no_discount(self):
        kvitto = [("Bok", 100.00, 0.06)]
        assert berakna_total(kvitto) == 106

    def test_invalid_code_raises(self):
        kvitto = [("Bok", 100.00, 0.06)]
        with pytest.raises(ValueError):
            berakna_total(kvitto, "FEL")

    def test_discount_on_empty_receipt(self):
        assert berakna_total([], "RABATT10") == 0
