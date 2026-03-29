# Avvio rapido

**Il tuo agente AI si comporta in modo incoerente. Non riflette i valori dell'organizzazione quando emergono casi limite.**

Questa guida valida una constitution e una state machine di governance in meno di 15 minuti.

## Passo 1 — Installazione (2 min)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Passo 2 — Validare un esempio reale (3 min)

```bash
python3 scripts/validate_specula.py \
  --constitution examples/community-space-brand/constitution.json \
  --state-machine examples/community-space-brand/state-machine.json
```

Questo valida gli artefatti di governance per *Il posto delle fragole* — uno spazio di comunità a Pesaro costruito con il Metodo Specula. La constitution codifica cinque valori radicali (Abitabilità, Non giudizio, Abilitazione, Immaginazione in pratica, Comunità viva) come regole operative di governance con vincoli espliciti e percorsi di escalation.

→ [Come i valori del brand diventano regole di governance](./examples/community-space-brand/brand-values.md)
→ [Case study completo in specula-method](https://github.com/oddtitoreal/specula-method/tree/main/case-studies/case_study_posto_delle_fragole.it.md)

## Passo 3 — Validare i propri artefatti (10 min)

```bash
cp templates/example-constitution.json my-constitution.json
cp templates/example-state-machine.json my-state-machine.json
# modifica entrambi i file per riflettere i valori e il flusso operativo del tuo agente
python3 scripts/validate_specula.py \
  --constitution my-constitution.json \
  --state-machine my-state-machine.json
```

Il validatore controlla struttura JSON, conformità allo schema, consistenza logica interna a ciascun artefatto, e coerenza di integrazione tra constitution e state machine.

## Prossimi passi

- **Comprendere i tre livelli**: [SKILL.md](./SKILL.md)
- **Confrontare entrambi gli esempi**: [examples/README.md](./examples/README.md)
- **Specifiche runtime canoniche**: [specula-framework](https://github.com/oddtitoreal/specula-framework)
- **Capire il metodo alla base degli artefatti**: [specula-method](https://github.com/oddtitoreal/specula-method)
