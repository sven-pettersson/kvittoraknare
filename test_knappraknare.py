import pytest
from raknare import berakna_total, format_receipt, print_receipt

class TestExample:
    def test_berakna_total(self):

        kvitto = [
            ("Mjölk", 100.00, 0.25),
            ("Bok", 100.00, 0.25)
        ]
        assert berakna_total(kvitto) == 250

    def test_print_receipt(self, capsys):
        items = [
            ("Mjölk", 100.00, 0.12),
            ("Bok", 200.00, 0.06),
        ]

        print_receipt(items)

        assert capsys.readouterr().out == (
            "Kvitto\n"
            "Mjölk: 112.00 kr\n"
            "Bok: 212.00 kr\n"
            "Totalt: 324.00 kr\n"
        )

    def test_format_receipt_matches_example(self):
        items = [
            ("Kaffe", 100.00, 25),
            ("Bröd", 50.00, 12),
            ("Bok", 200.00, 6),
        ]

        assert format_receipt(items) == (
            "KVITTO\n"
            "Kaffe                    100,00\n"
            "Bröd                      50,00\n"
            "Bok                      200,00\n"
            "-------------------------------\n"
            "Summa exkl. moms         350,00\n"
            "Moms 25 %                 25,00\n"
            "Moms 12 %                  6,00\n"
            "Moms 6 %                  12,00\n"
            "-------------------------------\n"
            "ATT BETALA               393,00"
        )

    def test_format_receipt_returns_message_for_empty_list(self):
        assert format_receipt([]) == "Inga varor"

    def test_format_receipt_truncates_long_item_names(self):
        receipt = format_receipt([("A very long product name", 10.00, 0)])

        assert receipt.splitlines()[1] == "A very long produ...      10,00"

    def test_format_receipt_shows_only_present_vat_rates_in_descending_order(self):
        receipt = format_receipt([
            ("Low rate", 100.00, 6),
            ("High rate", 100.00, 25),
            ("Also high", 50.00, 25),
        ])

        assert "Moms 25 %                 37,50" in receipt
        assert "Moms 6 %                   6,00" in receipt
        assert "Moms 12 %" not in receipt
        assert receipt.index("Moms 25 %") < receipt.index("Moms 6 %")

    def test_format_receipt_uses_decimal_comma_and_two_decimal_places(self):
        receipt = format_receipt([("Tea", 1.20, 25)])
        lines = receipt.splitlines()

        assert lines[1] == "Tea                        1,20"
        assert lines[4] == "Moms 25 %                  0,30"
        assert lines[-1] == "ATT BETALA                 1,50"

    def test_format_receipt_data_rows_are_31_characters_wide(self):
        receipt = format_receipt([("Item", 1.00, 6)])

        assert all(len(line) == 31 for line in receipt.splitlines()[1:])
