from pathlib import Path
from loguru import logger
import polars as pl
from core.customer import generate_customers
from core.employee import generate_employees, group_employees_by_role
from core.writer import generate_data


def main():
    customers = generate_customers()
    employees = generate_employees()
    role_to_employees = group_employees_by_role(employees)

    df_events, order_rows, responsibles = generate_data(customers, role_to_employees)

    output_dir = Path.home() / "Downloads" / "pizzaria_eventlog" / "parquets"
    output_dir.mkdir(parents=True, exist_ok=True)

    df_events.write_parquet(output_dir / "events.parquet")
    pl.DataFrame(order_rows).write_parquet(output_dir / "orders_master.parquet")
    pl.DataFrame(employees).write_parquet(output_dir / "employees_registry.parquet")
    pl.DataFrame(responsibles).write_parquet(output_dir / "event_responsibles.parquet")

    logger.success(f"✅ Files saved in {output_dir}")

if __name__ == "__main__":
    main()
