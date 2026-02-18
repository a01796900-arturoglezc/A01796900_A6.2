"""
Customer model definition.
"""

from typing import Dict


class Customer:
    """Represents a customer entity."""

    def __init__(
        self,
        customer_id: str,
        name: str,
        email: str,
        phone: str,
    ) -> None:
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone

    def to_dict(self) -> Dict:
        """Convert Customer object to dictionary."""
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "Customer":
        """Create Customer object from dictionary."""
        return cls(
            customer_id=data["customer_id"],
            name=data["name"],
            email=data["email"],
            phone=data["phone"],
        )
