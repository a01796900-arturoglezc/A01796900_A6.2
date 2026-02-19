"""
Hotel model definition.
"""

from typing import Dict


class Hotel:
    """Represents a hotel entity."""

    # pylint: disable=too-many-arguments, too-many-positional-arguments
    def __init__(
        self,
        hotel_id: str,
        name: str,
        location: str,
        total_rooms: int,
        available_rooms: int,
    ) -> None:
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.total_rooms = total_rooms
        self.available_rooms = available_rooms

    def to_dict(self) -> Dict:
        """Convert Hotel object to dictionary."""
        return {
            "hotel_id": self.hotel_id,
            "name": self.name,
            "location": self.location,
            "total_rooms": self.total_rooms,
            "available_rooms": self.available_rooms,
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "Hotel":
        """Create Hotel object from dictionary."""
        return cls(
            hotel_id=data["hotel_id"],
            name=data["name"],
            location=data["location"],
            total_rooms=data["total_rooms"],
            available_rooms=data["available_rooms"],
        )
