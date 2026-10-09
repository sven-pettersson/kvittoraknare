import pytest
from raknare import berakna_total

class TestExample:
    def test_berakna_total(self):
        kvitto = [
            ("Mjölk", 100.00, 0.25),
            ("Bok", 100.00, 0.25)
        ]
        assert berakna_total(kvitto) == 250

    def test_berakna_total_med_rabattkod_fore_moms(self):
        kvitto = [
            ("Mjölk", 100.00, 0.25),
            ("Bok", 100.00, 0.06)
        ]
        assert berakna_total(kvitto, rabattkod="RABATT10") == 207.90

    def test_berakna_total_med_ogiltig_rabattkod(self):
        kvitto = [("Mjölk", 100.00, 0.25)]
        with pytest.raises(ValueError, match="Ogiltig rabattkod"):
            berakna_total(kvitto, rabattkod="FELKOD")
        