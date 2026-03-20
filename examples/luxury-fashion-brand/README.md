# Luxury Fashion Brand Example

Fictional example showing how brand identity is encoded as governance rules.

## Files

- `constitution.json`: governance principles and constraints
- `state-machine.json`: operational decision flow and guards
- `brand-values.md`: philosophy-to-operations explanation
- `validation-results.txt`: output from validator

## Validate

```bash
python3 scripts/validate_specula.py \
  --constitution examples/luxury-fashion-brand/constitution.json \
  --state-machine examples/luxury-fashion-brand/state-machine.json
```
