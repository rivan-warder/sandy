from pydantic import BaseModel, EmailStr
from my_math import add


class SimpleClass(BaseModel):
    name: str
    value: int
    email: EmailStr

    def greet(self) -> str:
        return f"Hello, {self.name}!"

    def increment_value(self) -> int:
        self.value += 1
        return self.value

    def add_to_value(self, amount: int) -> int:
        self.value = add(self.value, amount)
        return self.value
