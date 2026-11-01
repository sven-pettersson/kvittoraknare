# ai/

AI-material från utvecklingen med Claude Code. Projektets kod ligger i `code/`.

| Katalog | Innehåll | Skapas av |
|---|---|---|
| `journal/` | Arbetsjournal per session (ny fil efter 20 min inaktivitet) | journal-hooken och `/journal` |
| `reviews/` | Granskningar före commit (`check-result-*.md`) | `/check-result` |
| `prompts/` | Äldre promptloggar (historik) | – |
| `diagrams/` | Mermaid-diagram över projektet | `/mermaid` |

PR-texterna från `/pr` och `/promote` byggs av journalens `## Summary` och tabellen i senaste `reviews/check-result-*.md`. CI stoppar PR:er mot `test` som ändrar `code/` utan en granskning.

Hela git-flödet, med manuella motsvarigheter för andra verktyg än Claude Code, beskrivs i [readme.md](../readme.md#arbetsflöde-med-git).
