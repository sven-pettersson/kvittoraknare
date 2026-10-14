# Prompt 7ac5d31

## AI tool

- OpenCode (model: big-pickle)

## Prompt

> Lägg till stöd för en rabattkod som ger 10 % rabatt på hela kvittot. Rabatten ska dras innan momsen räknas. Skriv tester för det nya.

## Changes

| File | Change |
|------|--------|
| `raknare.py` | Added the `RABATTKODER` dictionary with the code `RABATT10` (10 %). Added the optional parameter `rabattkod` to `berakna_total`. The discount is applied to each item's price excl. VAT before VAT is added. |
| `test_knappraknare.py` | Added the test class `TestRabatt` covering discount with a valid code, that the discount is applied before VAT, an unknown code, no code, and mixed VAT rates. |
| `prompts/Prompt-7ac5d31.md` | Added this prompt documentation. |

## Assumptions

- The discount code is named `RABATT10` since no name was given in the prompt.
- An unknown discount code is ignored and gives no discount (no error is raised).
- Only one discount code is supported and it always gives 10 %.
- The discount is applied to the whole receipt, i.e. to every item's price excl. VAT.

## readme.md

# Vecka 2 av kursen

## Se kursen för beskrivning

# Logg över resultat med olika verktyg

| Verktyg      | Antal promptar | Följde din egna regel? | Testerna gröna? | Vad fick du rätta själv? |
|--------------|----------------|-------------------------|-----------------|---------------------------|
| Copilot      |                |                         |                 |                           |
| Claude Code  |                |                         |                 |                           |
| OpenCode     | 1              | Ja                      | Ja              | Inget                     |
