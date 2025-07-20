from typing import TypedDict, Literal
from config.constants import Role, EventName, Flavor, Size, VariantType, DeliveryMode, PaymentMethod


class Employee(TypedDict):
    employee_id: str
    employee_name: str
    role: Role

class Customer(TypedDict):
    customer_id: str
    customer_name: str

class ResponsibleEntry(TypedDict):
    order_id: int
    event_name: EventName
    employee_id: str

class OrderData(TypedDict):
    order_id: int
    customer_id: str
    customer_name: str
    flavor: Flavor
    size: Size
    variant_type: VariantType
    delivery_mode: DeliveryMode
    price_total: float
    discount_applied: int
    payment_method: PaymentMethod
