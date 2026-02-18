"""
Reservation model definition.
"""

from typing import Dict


class Reservation:
    """Represents a reservation entity."""

    def __init__(
        self,
        reservation_id: str,
        customer_id: str,
        hotel_id: str,
        room_number: int,
    ) -> None:
        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.hotel_id = hotel_id
        self.room_number = room_number

    def to_dict(self) -> Dict:
        """Convert Reservation object to dictionary."""
        return {
            "reservation_id": self.reservation_id,
            "customer_id": self.customer_id,
            "hotel_id": self.hotel_id,
            "room_number": self.room_number,
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "Reservation":
        """Create Reservation object from dictionary."""
        return cls(
            reservation_id=data["reservation_id"],
            customer_id=data["customer_id"],
            hotel_id=data["hotel_id"],
            room_number=data["room_number"],
        )
