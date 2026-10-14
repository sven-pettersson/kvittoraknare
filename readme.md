# Vecka 2 av kursen

## Se kursen för beskrivning

# Logg över resultat med olika verktyg

| Verktyg      | Antal promptar | Följde din egna regel? | Testerna gröna? | Vad fick du rätta själv? |
|--------------|----------------|-------------------------|-----------------|---------------------------|
| Copilot      | 1              | Ja                      | Ja (7 tester)   | Inga manuella rättningar  |
| Claude Code  |                |                         |                 |                           |
| OpenCode     |                |                         |                 |                           |

## Användning

En kvittopost kan anges som `(namn, pris_exklusive_moms, momssats, valuta)`.
Valutan kan vara `SEK`, `EUR` eller `USD`. Poster med det äldre formatet
`(namn, pris_exklusive_moms, momssats)` tolkas som SEK.

```python
from raknare import berakna_total

kvitto = [
    ("Mjölk", 15.00, 0.12, "SEK"),
    ("Bok", 10.00, 0.06, "EUR"),
]
total = berakna_total(kvitto, target_currency="SEK")
```

Vid behov hämtas aktuell kurs från Frankfurter API. Det kräver internetanslutning;
om kursen inte kan hämtas eller svaret är ogiltigt rapporteras ett fel i stället
för att en totalsumma visas. Poster i målvalutan kräver ingen nätverksförfrågan.
Totalsumman avrundas till två decimaler efter att posterna har konverterats och
summerats.

Kör testerna med `pytest`.
