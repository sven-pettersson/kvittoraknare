import pytest
from raknare import berakna_total

class TestExample:
    def test_berakna_total(self):

        kvitto = [
            ("Mjölk", 100.00, 0.25),
            ("Bok", 100.00, 0.25)
        ]
        assert berakna_total(kvitto) == 250
        