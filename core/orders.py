import random
from datetime import timedelta, datetime
from typing import Dict, List, Tuple, cast

from config.constants import START_DATE, BASE_EVENTS, EVENT_ROLE_MAP, FLAVORS, SIZES, VARIANT_TYPES, DELIVERY_MODES, PAYMENT_METHODS
from config.types import Customer, ResponsibleEntry, OrderData, EventName, Role

def generate_order_data(
    order_id: int,
    customer: Customer,
    role_to_employees: Dict[Role, List[str]]
) -> Tuple[Dict[str, object], List[ResponsibleEntry], OrderData]:

    current_time = START_DATE + timedelta(minutes=random.randint(0, 60))
    row: Dict[str, object] = {"order_id": order_id}
    responsible: List[ResponsibleEntry] = []

    canceled = random.random() < 0.1
    has_feedback = not canceled and random.random() < 0.6
    has_rework = not canceled and random.random() < 0.05
    has_anomaly = not canceled and random.random() < 0.02

    events = BASE_EVENTS.copy()
    if not has_feedback:
        events.remove("ev_feedback_received")
    if canceled:
        events = ["ev_order_created"]
    if has_anomaly:
        try:
            i1, i2 = events.index("ev_pizza_baked"), events.index("ev_oven_started")
            if i1 < i2:
                events[i1], events[i2] = events[i2], events[i1]
        except ValueError:
            pass

    for event in cast(List[EventName], events):
        current_time += timedelta(minutes=random.randint(3, 8))
        row[event] = current_time
        role = EVENT_ROLE_MAP[event]
        responsible.append(ResponsibleEntry(
            order_id=order_id,
            event_name=event,
            employee_id=random.choice(role_to_employees[role])
        ))

        if event == "ev_preparation_started" and has_rework:
            current_time += timedelta(minutes=random.randint(1, 3))
            row["ev_preparation_restarted"] = current_time
            responsible.append(ResponsibleEntry(
                order_id=order_id,
                event_name="ev_preparation_restarted",
                employee_id=random.choice(role_to_employees["Cook"])
            ))

        if event == "ev_pizza_baked" and has_rework:
            current_time += timedelta(minutes=random.randint(1, 3))
            row["ev_pizza_remade"] = current_time
            responsible.append({
                "order_id": order_id,
                "event_name": "ev_pizza_remade",
                "employee_id": random.choice(role_to_employees["Cook"])
            })

    timestamps: list[datetime] = [
        ts for k, ts in row.items()
        if k.startswith("ev_") and isinstance(ts, datetime)
    ]
    row.update({
        "is_canceled": canceled,
        "has_feedback": has_feedback,
        "total_steps": len(timestamps),
        "duration_minutes": (max(timestamps) - min(timestamps)).total_seconds() / 60
    })

    base_price = round(random.uniform(30, 90), 2)
    discount = random.choice([0, 5, 10])
    order_info = OrderData(
        order_id=order_id,
        customer_id=customer["customer_id"],
        customer_name=customer["customer_name"],
        flavor=random.choice(FLAVORS),
        size=random.choice(SIZES),
        variant_type=random.choice(VARIANT_TYPES),
        delivery_mode=random.choice(DELIVERY_MODES),
        price_total=base_price - discount,
        discount_applied=discount,
        payment_method=random.choice(PAYMENT_METHODS),
    )
    return row, responsible, order_info
