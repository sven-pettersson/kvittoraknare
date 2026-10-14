# Prompt Log – Run `e23d2870`

**Date:** 2026-10-14
**Branch:** `med-claude-plan`

## AI Tool

| Field  | Value                          |
|--------|--------------------------------|
| Tool   | Claude Code (plan mode)        |
| Model  | Claude Opus 5.5                |

## Prompts

1. > Jag vill att kvittoräknaren ska klara flera valutor (SEK, EUR, USD). Föreslå en plan. Ändra inget än.
2. > Kanske är det snyggast att hela kvittot har en valuta. känns völdigt rörigt annars. vilken valuta ska tex visas på totalsumman
3. *(Plan approved in plan mode)*

## Changes

- **`raknare.py`**
  - Added constant `SUPPORTED_CURRENCIES = ("SEK", "EUR", "USD")`.
  - Added `format_total(items, currency="SEK")`, which returns the total as text with a currency code (e.g. `"728.80 SEK"`). It is case-insensitive and raises `ValueError` for unsupported currencies.
  - `berakna_total` is unchanged and still returns a number.
  - The `__main__` block now prints `format_total(kvitto, "SEK")`.
- **`test_knappraknare.py`**
  - Added a `TestFormatTotal` class with tests for the default currency (SEK), EUR/USD, lowercase input, an unknown currency (`GBP` → `ValueError`) and an empty receipt.
- **`prompts/Prompt-e23d2870.md`**: this file.

## Assumptions

- The whole receipt uses **one currency**. There is no conversion and there are no exchange rates.
- VAT rates are the same regardless of currency, since currency only affects how the total is displayed.
- The output format is `amount + currency code` (`250.00 EUR`), not symbols like `€`/`$`.
- No new dependencies.
- Existing Swedish names (`berakna_total`) were kept to keep the change small. New code uses English names.

## Test Result

```
pytest -q
.......                                                                  [100%]
7 passed in 0.03s

python raknare.py
728.80 SEK
```

## readme.md (filled in)

# Vecka 2 av kursen

## Se kursen för beskrivning

# Logg över resultat med olika verktyg

| Verktyg      | Antal promptar | Följde din egna regel? | Testerna gröna? | Vad fick du rätta själv? |
|--------------|----------------|-------------------------|-----------------|---------------------------|
| Copilot      |                |                         |                 |                           |
| Claude Code  | 2              | Ja                      | Ja (7/7)        | Förtydligade att hela kvittot ska ha en valuta |
| OpenCode     |                |                         |                 |                           |
