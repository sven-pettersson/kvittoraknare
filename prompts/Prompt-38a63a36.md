# Prompt Log – Run `38a63a36`

**Date:** 2026-10-14
**Branch:** `med-claude-plan`

## AI Tool

| Field  | Value                          |
|--------|--------------------------------|
| Tool   | Claude Code (plan mode)        |
| Model  | Claude Opus 5.5                |

## Prompts

1. > men nu förstår jag inte. Har valutan bara för att sätta in rätt värde på currency? Har vi ingen konvertering överhuvudtaget?
2. *(Answered clarifying question: "Konvertera från SEK")*
3. > No, went to fast I want the receipt to be in one currency but there is the possibility to change the currency according. Have a static values for the currency and set sek as default
4. *(Revised plan approved in plan mode)*
5. > commita och fyll i readme skicka till copilot

## Changes

- **`raknare.py`**
  - Replaced `SUPPORTED_CURRENCIES` with a static rate table `EXCHANGE_RATES = {"SEK": 1.0, "EUR": 11.0, "USD": 10.0}` (SEK per 1 unit).
  - Added helper `_rate(currency)` that validates a currency code (case-insensitive) and returns its rate. Unknown codes raise `ValueError`.
  - Added `convert(amount, from_currency, to_currency="SEK")`, which converts an amount between currencies and rounds it to two decimals.
  - `format_total(items, currency="SEK", to_currency=None)`: `currency` is the receipt's currency. If `to_currency` is given, the total is converted to it.
  - The `__main__` block also prints a converted example (`66.25 EUR`).
- **`test_knappraknare.py`**
  - Added `format_total` tests for SEK → EUR, EUR → SEK and an unknown target currency.
  - Added a `TestConvert` class covering same-currency, SEK → USD, EUR → USD, default target, lowercase codes and unknown currency.
- **`readme.md`**: filled in the Claude Code row of the results table.
- **`prompts/Prompt-38a63a36.md`**: this file.

## Assumptions

- The whole receipt has **one currency** (default SEK), and all prices are given in that currency.
- The exchange rates are **static placeholder values**, not real market rates.
- Rounding to two decimals happens **after** conversion.
- VAT is calculated in the receipt currency before conversion.
- Without `to_currency` no conversion happens, so earlier behaviour and tests are unchanged.
- No new dependencies.

## Test Result

```
pytest -q
................                                                         [100%]
16 passed in 0.02s

python raknare.py
728.80 SEK
66.25 EUR
```

## readme.md (filled in)

# Vecka 2 av kursen

## Se kursen för beskrivning

# Logg över resultat med olika verktyg

| Verktyg      | Antal promptar | Följde din egna regel? | Testerna gröna? | Vad fick du rätta själv? |
|--------------|----------------|-------------------------|-----------------|---------------------------|
| Copilot      |                |                         |                 |                           |
| Claude Code  | 3              | Ja                      | Ja (16/16)      | Valutan var bara en etikett; begärde riktig konvertering med statiska kurser och SEK som standard |
| OpenCode     |                |                         |                 |                           |
