# Kvittoräknaren

## Om projektet
Ett litet program som räknar ut summa och moms för ett kvitto.

## Teknik
- Språk: Python 3.14.3
- Tester: pytest (konfiguration i `pyproject.toml`)

## Struktur
- `code/src/` – programkod
- `code/tests/` – tester (pytest hittar modulerna i `src/`, `libs/` och `settings/` via `pyproject.toml`)
- `code/libs/` – egna hjälpbibliotek som delas mellan moduler
- `code/settings/` – programinställningar (t.ex. momssatser)
- `ai/` – AI-material: `journal/`, `reviews/`, `prompts/`, `diagrams/` (se `ai/README.md`)
- Lägg ny kod och nya tester i rätt katalog ovan, aldrig i projektroten.

## Regler
- Svara mig på svenska. Kod och variabelnamn på engelska.
- Gör små ändringar. Fråga innan du lägger till nya beroenden.
- Skriv eller uppdatera tester för all ny logik.
- Kör testerna innan du säger att du är klar.
- Committa bara när jag ber om det.

## Dokumentation
- Journalen skrivs automatiskt i `ai/journal/` (ny fil efter 20 minuters inaktivitet).
- Innan commit: kör `/journal` för att lägga till en engelsk sammanfattning (AI-verktyg, promptar, ändringar, antaganden, verktygets rad ur tabellen i readme.md).
- Äldre promptloggar finns kvar i `ai/prompts/` som historik.
- Diagram över projektet skapas med `/mermaid` i `ai/diagrams/` (`/mermaid readme` uppdaterar även readme.md).

## Före commit
- Kör `/check-result` och åtgärda ❌-raderna i `ai/reviews/` innan commit. Claudes commit stoppas om granskningen saknas eller är inaktuell.
- `ai/` committas tillsammans med ändringen.
- Vid commit: uppdatera verktygets rad i tabellen i readme.md (lämna bedömningskolumnerna till mig).

## Kommandon
- Kör programmet: python code/src/raknare.py
- Kör tester: pytest
