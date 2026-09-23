import pathlib
import sys

p = pathlib.Path.cwd()
while not (p / "zoro").is_dir() and p != p.parent:
	p = p.parent
sys.path.insert(0, str(p))

from zoro import data

carriers_df = data.carriers(2, seed=7)
lanes_df    = data.lanes(2, seed=11)
ship_df     = data.shipments(20, seed=42)
support_ticket_df     = data.support_tickets(20, seed=42)

print(f"carriers_df: {len(carriers_df):,} rows")
print(f"lanes_df:    {len(lanes_df):,} rows")
print(f"ship_df:    {len(ship_df):,} rows")
print(f"support_ticket_df: {len(support_ticket_df):,} rows")