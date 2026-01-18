from sqlalchemy.orm import Mapped
from core.models.base import Base


class Product(Base):
    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[int]

    def __repr__(self) -> str:
        return f"Product {self.name}"
