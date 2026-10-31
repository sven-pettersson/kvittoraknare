# Diagram – kvittoraknaren

_Genererad 2026-10-30 14:49 med /mermaid._

## Innehåll
- [Katalogstruktur](#katalogstruktur)
- [Modulberoenden](#modulberoenden)
- [Klasser och funktioner](#klasser-och-funktioner)
- [Dataflöde](#dataflöde)
- [Tester](#tester)
- [Arbetsflöde](#arbetsflöde)
- [Brancher](#brancher)

## Katalogstruktur
Projektets mappar och filer: koden ligger i `code/`, AI-materialet i `ai/`.

```mermaid
flowchart TD
    n_root["kvittoraknaren/"]
    n_root --> n__gitignore[".gitignore"]
    n_root --> n_AGENTS_md["AGENTS.md"]
    n_root --> n_ai["ai/"]
    n_ai --> n_ai_README_md["README.md"]
    n_ai --> n_ai_diagrams["diagrams/"]
    n_ai --> n_ai_journal["journal/"]
    n_ai --> n_ai_prompts["prompts/"]
    n_ai --> n_ai_reviews["reviews/"]
    n_root --> n_code["code/"]
    n_code --> n_code_libs["libs/"]
    n_code --> n_code_settings["settings/"]
    n_code --> n_code_src["src/"]
    n_code_src --> n_code_src_raknare_py["raknare.py"]
    n_code --> n_code_tests["tests/"]
    n_code_tests --> n_code_tests_test_knappraknare_py["test_knappraknare.py"]
    n_root --> n_pyproject_toml["pyproject.toml"]
    n_root --> n_readme_md["readme.md"]
    n_ai_journal["journal/ (2 filer)"]
    n_ai_prompts["prompts/ (1 fil)"]
    n_ai_reviews["reviews/ (2 filer)"]
```

## Modulberoenden
Vilka moduler som importerar vad. `raknare.py` har inga importer, så den står ensam.

```mermaid
flowchart LR
    n_code_src_raknare_py["code/src/raknare.py"]
```

## Klasser och funktioner
Publika funktioner och klasser per modul.

```mermaid
classDiagram
    class raknare {
        <<module>>
        +berakna_total(varor)
    }
```

## Dataflöde
Hur `berakna_total` räknar fram kvittots totalsumma inklusive moms.

```mermaid
flowchart TD
    A["varor: lista av (namn, pris, momssats)"] --> B["total = 0"]
    B --> C{"Fler varor?"}
    C -->|"ja"| D["pris * (1 + momssats)"]
    D --> E["total += radbelopp"]
    E --> C
    C -->|"nej"| F["round(total, 2)"]
    F --> G["Totalsumma inkl. moms"]
```

## Tester
Vilka testfiler som testar vilka moduler och funktioner.

```mermaid
flowchart LR
    n_code_tests_test_knappraknare_py["code/tests/test_knappraknare.py"] -->|"berakna_total"| n_code_src_raknare_py["code/src/raknare.py"]
```

## Arbetsflöde
Hur en ändring går från prompt till GitHub med journal, granskning och commit-spärr.

```mermaid
flowchart LR
    P["Prompt"] --> J["Journal (ai/journal)"]
    P --> K["Kodändring (code/)"]
    K --> T["pytest"]
    T --> R["/check-result (ai/reviews)"]
    R --> G{"Commit-spärr: matchar diff-hash?"}
    G -->|"nej"| R
    G -->|"ja"| C["git commit"]
    C --> U["git push"]
```

## Brancher
`main` och övningsbrancherna, där varje AI-verktyg löste samma uppgift (rabattkod resp. valutor) på en egen branch.

```mermaid
gitGraph
    commit id: "1ce9f2f Grundversion"
    commit id: "da0a19d AGENTS.md"
    commit id: "3f61585 readme"
    commit id: "7ac5d31 AGENTS.md" tag: "test-branch"
    branch med-opencode
    commit id: "e3f5563 Rabattkod"
    checkout main
    branch med-claude
    commit id: "4bf9ae4 RABATT10"
    checkout main
    branch med-copilot
    commit id: "c2508b7 Rabattkod"
    checkout main
    branch med-opencode-plan
    commit id: "ef2fe9b Valutor"
    checkout main
    branch med-claude-plan
    commit id: "670a424 Valutastöd"
    commit id: "c3f7a92 Valutakonvertering"
    checkout main
    branch med-copilot-plan
    commit id: "979e306 Multi-currency"
    checkout main
    commit id: "f524b4f Verktygslogg"
    commit id: "9a679e9 gitignore"
    commit id: "c7049fe code och ai"
```
