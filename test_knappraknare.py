import pytest
from raknare import berakna_total

class TestExample:
    def test_berakna_total(self):

        kvitto = [
            ("Mjölk", 100.00, 0.25),
            ("Bok", 100.00, 0.25)
        ]
        assert berakna_total(kvitto) == 250


class TestRabatt:
    def test_rabattkod_ger_tio_procent_rabatt(self):
        kvitto = [
            ("Mjölk", 100.00, 0.25),
            ("Bok", 100.00, 0.25)
        ]
        assert berakna_total(kvitto, "RABATT10") == 225

    def test_rabatt_dras_innan_moms(self):
        kvitto = [("Vara", 100.00, 0.25)]
        # 100 * 0.9 = 90, sedan moms: 90 * 1.25 = 112.50
        assert berakna_total(kvitto, "RABATT10") == 112.50

    def test_okand_rabattkod_ger_ingen_rabatt(self):
        kvitto = [("Vara", 100.00, 0.25)]
        assert berakna_total(kvitto, "FELKOD") == 125

    def test_ingen_rabattkod_ger_vanlig_summa(self):
        kvitto = [("Vara", 100.00, 0.25)]
        assert berakna_total(kvitto) == 125

    def test_rabatt_med_blandade_momssatser(self):
        kvitto = [
            ("Mjölk", 20.00, 0.12),
            ("Hörlurar", 400.00, 0.25)
        ]
        # 20 * 0.9 * 1.12 = 20.16 ; 400 * 0.9 * 1.25 = 450.00
        assert berakna_total(kvitto, "RABATT10") == 470.16