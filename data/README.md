# Generated data

This folder is where Week 1 writes the synthetic freight dataset. The files
themselves are gitignored. You generate them locally:

```python
from zoro import data
data.save_all()          # writes CSV + Parquet under data/
```

Do not commit the generated tables. Anyone who clones the repo can rebuild the
same rows from `zoro/data.py` with the same seed.

## Generation record

- Seed: 42
- Row counts:
  - carriers: 20
  - lanes: 20
  - shipments: 100,200
  - support_tickets: 2,000
- Schema: See [data-dictionary.md](data-dictionary.md).
