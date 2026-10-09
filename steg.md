# Prompt

> Lägg till stöd för en rabattkod som ger 10 % rabatt på hela kvittot. Rabatten ska dras innan momsen räknas. Skriv tester för det nya. Beskriv vilka steg du tagit i filen `steg.md`. I den ta också en kopia av tabellen i `readme.md` och fyll i värden för aktuellt verktyg.

# Steg

1. Granskade kvittoräknarens befintliga beräkning, tester och README.
2. Lade till rabattkoden `RABATT10`, som ger 10 % rabatt på varje varas pris före momsberäkningen.
3. Lade till tester för beräkning utan rabatt, rabatt före moms och avvisning av ogiltig rabattkod.
4. Kör testerna med `pytest`.

# Logg över resultat med olika verktyg

| Verktyg      | Antal promptar | Följde din egna regel? | Testerna gröna? | Vad fick du rätta själv? |
|--------------|----------------|-------------------------|-----------------|---------------------------|
| Copilot      | 1              | Ja                      | Ja              | Inget                      |
| Claude Code  |                |                         |                 |                           |
| OpenCode     |                |                         |                 |                           |
