import pytest
from raknare import berakna_total, DEFAULT_RATES


class TestBeraknaTotal:
    def test_berakna_total_samma_valuta(self):
        kvitto = [
            ("Mjölk", 100.00, 0.25, "SEK"),
            ("Bok", 100.00, 0.25, "SEK"),
        ]
        assert berakna_total(kvitto) == 250

    def test_valuta_defaultar_till_sek(self):
        kvitto = [
            ("Mjölk", 100.00, 0.25),
            ("Bok", 100.00, 0.25),
        ]
        assert berakna_total(kvitto) == 250

    def test_blandade_valutor(self):
        kvitto = [
            ("Kaffe", 10.00, 0.0, "EUR"),
            ("Bok", 20.00, 0.0, "USD"),
            ("Mjölk", 100.00, 0.0, "SEK"),
        ]
        assert berakna_total(kvitto) == 410

    def test_annan_basvaluta(self):
        kvitto = [
            ("Mjölk", 220.00, 0.0, "SEK"),
        ]
        assert berakna_total(kvitto, basvaluta="EUR") == 20

    def test_egna_kurser(self):
        kvitto = [
            ("Kaffe", 10.00, 0.0, "EUR"),
        ]
        kurser = {"SEK": 1.0, "EUR": 11.0, "USD": 10.0}
        assert berakna_total(kvitto, kurser=kurser) == 110

    def test_obekand_valuta_i_vara(self):
        kvitto = [
            ("Kaffe", 10.00, 0.0, "GBP"),
        ]
        with pytest.raises(ValueError):
            berakna_total(kvitto)

    def test_obekand_basvaluta(self):
        kvitto = [
            ("Kaffe", 10.00, 0.0, "SEK"),
        ]
        with pytest.raises(ValueError):
            berakna_total(kvitto, basvaluta="GBP")

    def test_default_rates_innehaller_valutor(self):
        assert set(DEFAULT_RATES) == {"SEK", "EUR", "USD"}
