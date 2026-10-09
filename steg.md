# Steg: Rabattkod med 10 % rabatt

Verktyg: Claude Code (Opus 5.5)

## Steg som togs

1. **Läste projektet** – `AGENTS.md`, `readme.md`, `raknare.py` och `test_knappraknare.py` för att förstå koden och reglerna.
2. **Körde befintliga tester** – `pytest` gav 1 grönt test innan någon ändring gjordes.
3. **Lade till rabattkod i `raknare.py`**
   - Nya konstanter `DISCOUNT_CODE = "RABATT10"` och `DISCOUNT_RATE = 0.10`.
   - `berakna_total` fick en valfri parameter `discount_code=None`, så befintliga anrop fungerar som förut.
   - Rabatten dras på varje varas pris **exkl. moms**, och först därefter läggs momsen på.
   - En okänd rabattkod ger `ValueError`, så att ett felstavat värde inte tyst ignoreras.
   - Funktionsnamnet `berakna_total` behölls för att inte bryta befintlig kod. Ny kod och nya variabelnamn skrevs på engelska enligt reglerna.
4. **Skrev tester i `test_knappraknare.py`** (ny klass `TestDiscountCode`):
   - 10 % rabatt på ett enkelt kvitto (200 kr exkl. moms → 225 kr).
   - Rabatt före moms med blandade momssatser (12 %, 6 %, 25 %) → 655,92 kr.
   - Ingen kod ger ingen rabatt.
   - Ogiltig kod ger `ValueError`.
   - Rabatt på tomt kvitto ger 0.
5. **Körde testerna** – `pytest`: 6 av 6 gröna. Körde även `python raknare.py` som skriver ut 728.8 (utan rabatt) och 655.92 (med rabatt).
6. **Skrev denna fil** (`steg.md`) med tabellen från `readme.md`.

## Logg över resultat

| Verktyg      | Antal promptar | Följde din egna regel? | Testerna gröna? | Vad fick du rätta själv? |
|--------------|----------------|-------------------------|-----------------|---------------------------|
| Copilot      |                |                         |                 |                           |
| Claude Code  | 1              | Ja (svarade på svenska, kod på engelska, inga nya beroenden, skrev tester, körde testerna) | Ja, 6/6 | Inget hittills |
| OpenCode     |                |                         |                 |                           |
