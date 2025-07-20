import random
from pathlib import Path
import polars as pl

from config.constants import NUM_CASES, BASE_EVENTS
from core.orders import generate_order_data


def write_parquet_df(data, filename: str, output_dir: Path):
    pl.DataFrame(data).write_parquet(output_dir / filename)

def generate_data(customers, role_to_employees):
    wide_events, responsibles, order_rows = [], [], []

    for i in range(NUM_CASES):
        order_id = 1000 + i
        customer = random.choice(customers)
        row, resp_rows, order_data = generate_order_data(order_id, customer, role_to_employees)
        wide_events.append(row)
        responsibles.extend(resp_rows)
        order_rows.append(order_data)

    all_events = BASE_EVENTS + ["ev_preparation_restarted", "ev_pizza_remade"]
    df_events = pl.DataFrame(wide_events).with_columns([
        pl.lit(None).cast(pl.Datetime("ns")).alias(ev)
        for ev in all_events if ev not in wide_events[0]
    ]).select(
        ["order_id"] + all_events + ["is_canceled", "has_feedback", "total_steps", "duration_minutes"]
    )

    return df_events, order_rows, responsibles
