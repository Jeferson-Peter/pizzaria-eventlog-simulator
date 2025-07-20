from datetime import datetime
from typing import Final, List, Dict, Literal

# Tipos literais para restringir valores possíveis
EventName = Literal[
    "ev_order_created", "ev_payment_confirmed", "ev_preparation_started",
    "ev_pizza_baked", "ev_oven_started", "ev_out_for_delivery",
    "ev_order_delivered", "ev_feedback_received",
    "ev_preparation_restarted", "ev_pizza_remade"
]
Role = Literal["Attendant", "Manager", "Cook", "Delivery"]
Flavor = Literal["Pepperoni", "Margherita", "Chicken & Cheese", "Supreme", "Four Cheese"]
Size = Literal["Small", "Medium", "Large", "Family"]
PaymentMethod = Literal["credit", "debit", "cash"]
VariantType = Literal["online", "in_store"]
DeliveryMode = Literal["store", "home"]

# Constantes com tipagem
NUM_CASES: Final[int] = 10_000
START_DATE: Final[datetime] = datetime(2025, 7, 15, 18, 0)

BASE_EVENTS: List[EventName] = [
    "ev_order_created", "ev_payment_confirmed", "ev_preparation_started",
    "ev_pizza_baked", "ev_oven_started", "ev_out_for_delivery",
    "ev_order_delivered", "ev_feedback_received"
]

EVENT_ROLE_MAP: Dict[EventName, Role] = {
    "ev_order_created": "Attendant",
    "ev_payment_confirmed": "Manager",
    "ev_preparation_started": "Cook",
    "ev_pizza_baked": "Cook",
    "ev_oven_started": "Cook",
    "ev_out_for_delivery": "Delivery",
    "ev_order_delivered": "Delivery",
    "ev_feedback_received": "Attendant",
    "ev_preparation_restarted": "Cook",
    "ev_pizza_remade": "Cook"
}

FLAVORS: List[Flavor] = ["Pepperoni", "Margherita", "Chicken & Cheese", "Supreme", "Four Cheese"]
SIZES: List[Size] = ["Small", "Medium", "Large", "Family"]
PAYMENT_METHODS: List[PaymentMethod] = ["credit", "debit", "cash"]
VARIANT_TYPES: List[VariantType] = ["online", "in_store"]
DELIVERY_MODES: List[DeliveryMode] = ["store", "home"]
ROLES: List[Role] = ["Cook", "Delivery", "Attendant", "Manager"]
