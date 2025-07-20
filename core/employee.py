from typing import List, Dict
from mimesis import Person
from mimesis.locales import Locale

from config.constants import ROLES
from config.types import Employee,Role

def generate_employees() -> List[Employee]:
    person = Person(Locale.EN)
    employees: List[Employee] = []
    emp_id = 1

    for role in ROLES:
        count = 2 if role == "Cook" else 1
        for _ in range(count):
            employees.append({
                "employee_id": f"E{emp_id:03}",
                "employee_name": person.full_name(),
                "role": role
            })
            emp_id += 1

    return employees

def group_employees_by_role(employees: List[Employee]) -> Dict[Role, List[str]]:
    return {
        role: [e["employee_id"] for e in employees if e["role"] == role]
        for role in set(e["role"] for e in employees)
    }
