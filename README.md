# 🍕 Pizzaria Event Log Simulator

A synthetic **event log generator** for simulating pizza orders, preparation steps, and delivery processes — perfect for:

- Process mining research
- ETL pipeline testing
- Performance analysis
- Academic demonstrations

---

## 🚀 Features

- Chronological event generation per order (e.g., order created, payment, preparation, delivery)
- Simulation of edge cases:
  - **Cancellations**
  - **Rework**
  - **Sequence anomalies**
  - **Customer feedback**
- Employee assignments based on roles (Attendant, Manager, Cook, Delivery)
- Export to **Parquet** files:
  - `events.parquet`
  - `orders_master.parquet`
  - `employees_registry.parquet`
  - `event_responsibles.parquet`

---

## 🧱 Project Structure

```
pizzaria-eventlog-simulator/
├── config/
│   ├── constants.py         # Static lists and config values
│   └── types.py             # TypedDicts and Literals
├── core/
│   ├── customer.py          # Customer generation
│   ├── employee.py          # Employee generation and grouping
│   ├── orders.py            # Main order/event simulation logic
│   └── writer.py            # Parquet export
├── main.py                  # Entry point
├── pyproject.toml           # Project config (managed with uv)
└── README.md                # You're here
```

---

## ⚙️ Requirements

- Python 3.12+
- [Polars](https://pola.rs)
- [Mimesis](https://github.com/lk-geimfari/mimesis)
- [Loguru](https://github.com/Delgan/loguru)

Install dependencies (project was developed using [uv](https://github.com/astral-sh/uv)):

```bash
uv sync
```

Or adapt to your preferred package manager.

---

## ▶️ How to Run

```bash
un run main.py
```

The generated files will be saved in your:

```
~/Downloads/pizzaria_eventlog/parquets/
```

---

## 🧪 Sample Output

| order_id | ev_order_created     | ev_payment_confirmed   | ... | duration_minutes |
|----------|----------------------|-------------------------|-----|------------------|
| 1001     | 2025-07-15 18:15:00  | 2025-07-15 18:18:00     | ... | 47.3             |

---


## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

Developed by Jeferson Peter. Contributions are welcome!
