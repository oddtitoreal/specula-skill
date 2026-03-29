# Community Space Brand Example

Real-world example showing how brand values from a participatory co-design process are encoded as governance rules. Based on *Il posto delle fragole* — a community space for young people in Pesaro, Italy.

Unlike the `luxury-fashion-brand` example (fictional), this example is derived from a real project completed in early 2026 using the Specula Method.

## Files

- `constitution.json`: governance principles, constraints, registry of refusals, and conflict resolution derived from five radical values
- `state-machine.json`: operational decision flow with guards at each transition, plus four space states (essenziale, modulare, denso, gestuale)
- `brand-values.md`: narrative explanation of how brand values became governance rules
- `validation-results.txt`: output from validator

## What makes this example different

The `luxury-fashion-brand` example demonstrates structure — how a constitution and state machine fit together. This example demonstrates *process*: how values emerge from participatory work, get translated through Brand Archeology, and become operational governance.

Key elements:
- **Real refusals**: the Registry of Refusals encodes what the brand chose *not* to become
- **Resolved tension**: the constitution captures the care-vs-innovation polarity and its resolution
- **Living states**: the state machine includes four space configurations, not just a linear flow

## Validate

```bash
python3 scripts/validate_specula.py \
  --constitution examples/community-space-brand/constitution.json \
  --state-machine examples/community-space-brand/state-machine.json
```

## Full context

→ [Brand values explained](./brand-values.md)
→ [Full case study in specula-method](https://github.com/oddtitoreal/specula-method/tree/main/case-studies/case_study_posto_delle_fragole.md)
