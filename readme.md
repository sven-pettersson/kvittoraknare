# Vecka 2 av kursen

## Se kursen för beskrivning

# Logg över resultat med olika verktyg

| Verktyg      | Antal promptar | Följde din egna regel? | Testerna gröna? | Vad fick du rätta själv? |
|--------------|----------------|-------------------------|-----------------|---------------------------|
| Copilot      |       1         |              Ja, implementerade dock för få tester och förutsatte att en okänd kod blir ett fel. Pluss för att den fatiskt bad om godkännande vid varje steg.           |    Ja, de som skrevs             | Har inte rättat något själv                          |
| Claude Code  |        1        |      Ja, implementerade med ren kod och följde strukturen. dock tar den sig en del friheter                   |   Ja              |          Har inte behövt rätta                 |
| OpenCode     |         1       |          Ja, dock bara det. vilket iofs är bra               |    Ja             |     Nej                      |

## Arbetsflöde med git

`feature/<namn>` → `test` → `staging` → `main` (merge till `main` = release, tagg `vX.Y.Z`)

| Steg | Med Claude Code | Manuellt / andra verktyg (t.ex. Copilot) |
|---|---|---|
| Skapa gren | `/branch <namn>` | `git fetch && git switch -c feature/<namn> --no-track origin/test` |
| Granska före commit | `/check-result` → `ai/reviews/` | Skriv en `ai/reviews/check-result-*.md` för hand |
| Journal | journal-hooken + `/journal` → `ai/journal/` | Skriv sammanfattningen för hand |
| PR mot test | `/pr` | `git push -u origin feature/<namn>` och sedan `gh pr create --base test` |
| Befordra | `/promote staging` / `/promote main` | `gh pr create --base staging --head test` / `gh pr create --base main --head staging` |

### Vad som skyddar flödet

- **Bara Claude Code:** hooks `branch_guard` (ingen commit/push på `main`, `staging` eller `test`) och `commit_gate` (kräver aktuell granskning). Skills och hooks ligger globalt i `~/.claude/` och finns inte i repot.
- **Alla verktyg:** CI (`.github/workflows/ci.yml`) kör pytest på PR:er och kräver en `ai/reviews/check-result-*.md` när `code/` ändras i PR:er mot `test`.


