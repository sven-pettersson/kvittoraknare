# Prompt 3 — Multi-currency support (SEK, EUR, USD)

## AI tool
OpenCode (model: big-pickle)

## Prompt
> Jag vill att kvittoräknaren ska klara flera valutor (SEK, EUR, USD). Föreslå en plan. Ändra inget än.
>
> (följt av) kör

## Changes
- `raknare.py`
  - Added module-level `DEFAULT_RATES` (`SEK`, `EUR`, `USD`) expressed as SEK per 1 unit.
  - Changed `berakna_total(varor, basvaluta="SEK", kurser=None)` to support mixed currencies.
    - Line items are now `(namn, pris_exkl_moms, momssats, valuta)`; `valuta` is optional and defaults to `"SEK"`.
    - Amounts are converted to SEK via `DEFAULT_RATES` (or an injected `kurser` dict) and then to the chosen `basvaluta`.
    - Unknown currency in an item or in `basvaluta` raises `ValueError`.
  - Updated `__main__` example to mix SEK and USD.
- `test_knappraknare.py`
  - Replaced the single test with a suite: same currency, default currency, mixed currencies, alternate base currency, custom rates, unknown item currency, unknown base currency, and a `DEFAULT_RATES` sanity check.
- `prompts/Prompt-3.md`
  - This file.

## Assumptions
- "Multiple currencies" means individual line items may carry their own currency, summed into one chosen base currency.
- Fixed rates keyed on SEK (placeholder values) are acceptable, injectable via the `kurser` parameter so they can later be swapped for flexible/live rates.
- API could be changed freely (existing callers are updated).
- Rounding is applied once, at the end, to 2 decimals in the base currency.

## Test result
```
8 passed in 0.03s
```

## readme.md (filled section)
The log table in `readme.md` was not part of this prompt; it is filled in at commit time.
