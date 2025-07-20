from typing import List, Dict
from mimesis import Person
from mimesis.locales import Locale

def generate_customers(n: int = 100) -> List[Dict[str, str]]:
    person = Person(Locale.EN)
    return [
        {
            "customer_id": f"C{i:04}",
            "customer_name": person.full_name()
        }
        for i in range(n)
    ]
