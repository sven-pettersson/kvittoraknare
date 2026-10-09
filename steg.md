# Steg tagna

1. Läste och analyserade projektfiler (raknare.py, test_knappraknare.py, readme.md, AGENTS.md).
2. Implementerade stöd för rabattkod 'RABATT10' i erakna_total() - rabatten dras innan momsen räknas.
3. Uppdaterade testerna för att inkludera tester för rabattkod.
4. Körde pytest för att verifiera att alla tester passerar.
5. Skapade/uppdaterade steg.md och fyllde i tabellen i readme.md för OpenCode.

## Testfall
- test_berakna_total: Grundläggande beräkning
- test_discount_rabatt10_applied_before_vat: Rabatt 10% dras före moms
- test_discount_no_discount_for_wrong_code: Fel rabattkod ger ingen rabatt
- test_discount_with_mixed_vat: Rabatt med olika momssatser

## Kopia av readme.md-tabell
| Verktyg      | Antal promptar | Följde din egna regel? | Testerna gröna? | Vad fick du rätta själv? |
|--------------|----------------|-------------------------|-----------------|---------------------------|
| Copilot      |                |                         |                 |                           |
| Claude Code  |                |                         |                 |                           |
| OpenCode     | 1              | Ja                      | Ja              | N/A                       |
