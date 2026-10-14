import io
import json
from urllib.error import URLError
from urllib.parse import parse_qs, urlparse

import pytest

import raknare
from raknare import berakna_total


class TestBeraknaTotal:
    def test_legacy_receipt_items_are_treated_as_sek(self, monkeypatch):
        def fail_if_called(*args, **kwargs):
            pytest.fail("No exchange rate should be needed for SEK to SEK.")

        monkeypatch.setattr(raknare.request, "urlopen", fail_if_called)
        receipt = [
            ("Milk", 100.00, 0.25),
            ("Book", 100.00, 0.25),
        ]

        assert berakna_total(receipt) == 250

    def test_converts_multiple_currencies_to_target_currency(self, monkeypatch):
        calls = []
        rates = {"USD": 10, "EUR": 11}

        def fake_urlopen(url, timeout):
            query = parse_qs(urlparse(url.full_url).query)
            assert url.get_header("User-agent") == "kvittoraknare/1.0"
            calls.append((query["base"][0], query["symbols"][0], timeout))
            response = {"rates": {"SEK": rates[query["base"][0]]}}
            return io.BytesIO(json.dumps(response).encode())

        monkeypatch.setattr(raknare.request, "urlopen", fake_urlopen)
        receipt = [
            ("Headphones", 100, 0.25, "USD"),
            ("Coffee", 10, 0.12, "EUR"),
        ]

        assert berakna_total(receipt, target_currency="SEK") == 1373.2
        assert calls == [("USD", "SEK", 10), ("EUR", "SEK", 10)]

    def test_rounds_once_after_summing_converted_items(self, monkeypatch):
        calls = []

        def fake_urlopen(url, timeout):
            calls.append(url)
            return io.BytesIO(b'{"rates":{"SEK":0.5}}')

        monkeypatch.setattr(raknare.request, "urlopen", fake_urlopen)
        receipt = [
            ("Item one", 0.01, 0, "USD"),
            ("Item two", 0.01, 0, "USD"),
        ]

        assert berakna_total(receipt, target_currency="sek") == 0.01
        assert len(calls) == 1

    def test_rejects_unsupported_currency(self, monkeypatch):
        def fail_if_called(*args, **kwargs):
            pytest.fail("Invalid currencies should be rejected before a request.")

        monkeypatch.setattr(raknare.request, "urlopen", fail_if_called)

        with pytest.raises(ValueError, match="Currency"):
            berakna_total([("Item", 1, 0, "NOK")])

        with pytest.raises(ValueError, match="Currency"):
            berakna_total([], target_currency="GBP")

    def test_rejects_malformed_items_and_non_finite_prices(self, monkeypatch):
        def fail_if_called(*args, **kwargs):
            pytest.fail("Invalid receipt items should be rejected before a request.")

        monkeypatch.setattr(raknare.request, "urlopen", fail_if_called)

        with pytest.raises(ValueError, match="three or four values"):
            berakna_total([("Item", 1)])

        with pytest.raises(ValueError, match="finite number"):
            berakna_total([("Item", float("nan"), 0)])

    def test_reports_network_errors(self, monkeypatch):
        def fail_to_connect(*args, **kwargs):
            raise URLError("offline")

        monkeypatch.setattr(raknare.request, "urlopen", fail_to_connect)

        with pytest.raises(RuntimeError, match="Frankfurter"):
            berakna_total([("Item", 1, 0, "USD")])

    def test_rejects_invalid_exchange_rate(self, monkeypatch):
        def fake_urlopen(url, timeout):
            return io.BytesIO(b'{"rates":{"SEK":0}}')

        monkeypatch.setattr(raknare.request, "urlopen", fake_urlopen)

        with pytest.raises(RuntimeError, match="invalid exchange rate"):
            berakna_total([("Item", 1, 0, "USD")])
