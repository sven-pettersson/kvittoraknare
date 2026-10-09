import pytest
from raknare import berakna_total

class TestExample:
    def test_berakna_total(self):
        kvitto = [
            ('Mjolk', 100.00, 0.25),
            ('Bok', 100.00, 0.25)
        ]
        assert berakna_total(kvitto) == 250

class TestDiscount:
    def test_discount_rabatt10_applied_before_vat(self):
        kvitto = [
            ('Vara1', 100.00, 0.25),
            ('Vara2', 100.00, 0.25)
        ]
        assert berakna_total(kvitto, discount_code='RABATT10') == 225.00

    def test_discount_no_discount_for_wrong_code(self):
        kvitto = [
            ('Mjolk', 100.00, 0.25),
        ]
        assert berakna_total(kvitto, discount_code='FELKOD') == 125.00

    def test_discount_with_mixed_vat(self):
        kvitto = [
            ('Mjolk', 15.00, 0.12),
            ('Bok', 200.00, 0.06),
            ('Horular', 400.00, 0.25)
        ]
        assert berakna_total(kvitto, discount_code='RABATT10') == 655.92
