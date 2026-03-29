# Il posto delle fragole — Brand Values as Governance

This document explains how the brand values of *Il posto delle fragole* are translated into governance rules in the constitution and state machine.

## The project

*Il posto delle fragole* is a community space at via Ponchielli 81 in the San Martino neighbourhood of Pesaro, Italy. It was designed by four partner organizations — ARCI, APS LiberaMusica, Cooperativa Labirinto, and Fondazione Wanda di Ferdinando — for young people aged 15–23.

The brand identity was developed through a process that began with participatory co-design (facilitated by Sineglossa, autumn 2025) and was synthesised into an operational identity system by Specula Future Crafting (January–February 2026).

## From co-design to governance

The co-design process produced rich, overlapping value material across nine clusters. The Specula Method's Brand Archeology phase made this governable by:

1. Extracting **radical values** — what is irreducible, what persists even when activities change
2. Translating them from **descriptive** ("uno spazio sicuro") to **operational** ("if it doesn't improve the quality of being together, it's not a valid choice")
3. Building a **Registry of Refusals** — what this brand will never become, logged as governance constraints

## The five governing principles

### Abitabilità (Habitability) — Priority 1

The space exists to improve quality of being together, not to produce outputs. This principle governs any decision that trades relational quality for efficiency, scale, or convenience.

**Operational guard**: Any programming decision that optimizes for attendance numbers at the cost of relational depth requires escalation to the Community Guardian.

### Non Giudizio (Non-Judgment) — Priority 1

People come before labels. The space maintains clear limits without stigma, respect without moralism. This is not passivity — it is precision in how lines are drawn.

**Hard constraint**: No stigmatizing language, no moralizing tone, no labeling of people by their condition or background. Violation blocks output.

### Abilitazione (Enabling) — Priority 1

Care here means infrastructure: access to tools, competencies, and real opportunities. The distinction from "assistance" is structural — assistance creates dependency; enablement creates capacity.

**Critical constraint**: The space will not become one where young people are users of adult-designed services. This is a critical-severity rule with escalation to the Community Guardian.

### Immaginazione in Pratica (Imagination in Practice) — Priority 2

Imagination is not escape; it's a tool. Creativity here is trained and shared, not performed. This governs tone, especially in communication that touches creative activities.

**Operational guard**: Activation content must not imply performance expectations, rankings, or competitive framing.

### Comunità Viva (Living Community) — Priority 2

We don't consume experiences; we cultivate returns. Relationships persist across time. This governs how continuity and memory are treated across all interactions.

## The key tension and its resolution

The co-design material contained a structural tension between *cura* (care, protection, warmth) and *innovazione* (technology, creative risk, experimentation).

The Specula Method's Ethical Gate resolved this not by choosing a side, but by reframing: care was redefined as *infrastructure that enables power*. Psychological safety is the condition that makes creative risk possible — not its opposite.

This resolution is encoded in the constitution's priority order: Abitabilità, Non Giudizio, and Abilitazione all carry Priority 1. Safety and risk coexist as co-dependent, not competing, principles.

## The Registry of Refusals

The brand identity defines not just what the space is, but what it refuses to become:

| Refusal | Logged at |
|---|---|
| Youth as users, not co-creators | Phase 2 — Brand Archeology |
| Promising outcomes rather than presence | Phase 2 — Brand Archeology |
| Measuring success only by attendance | Phase 3 — Ethical Gate |
| Adult reassurance at the cost of Gen Z recognition | Phase 3 — Ethical Gate |

## The living system

Unlike most brand governance, this one encodes *states* rather than just rules. The space can operate in four modes:

- **Essenziale**: when only what matters remains — quiet, grounding
- **Modulare**: when the community builds together — collaborative, structured
- **Denso**: when the space is full of relationships — warm, present
- **Gestuale**: when something spontaneous happens — energetic, open

Each state has a different color weight and interaction tone. The identity moves — but doesn't disperse.

## Validation

```bash
python3 scripts/validate_specula.py \
  --constitution examples/community-space-brand/constitution.json \
  --state-machine examples/community-space-brand/state-machine.json
```

## Sources

- Co-design Report Final (Sineglossa, November 2025)
- Report di sintesi strategica e disambiguazione (Specula Future Crafting, January 2026)
- Brand Manual — Il posto delle fragole (Specula Future Crafting, February 2026)
- Sistema cromatico per interni (Specula Future Crafting, February 2026)

## Full case study

→ [specula-method case study](https://github.com/oddtitoreal/specula-method/tree/main/case-studies/case_study_posto_delle_fragole.md)
