"""
Hotel service for managing hotel operations.
"""

import os
from typing import List, Optional

from src.models.hotel import Hotel
from src.services.file_service import FileService


DATA_FILE = os.path.join("data", "hotels.json")


class HotelService:
    """Service layer for hotel operations."""

    @staticmethod
    def create_hotel(hotel: Hotel) -> None:
        """Create a new hotel."""
        hotels_data = FileService.load_data(DATA_FILE)

        # Prevent duplicate IDs
        for existing in hotels_data:
            if existing["hotel_id"] == hotel.hotel_id:
                print("Error: Hotel ID already exists.")
                return

        hotels_data.append(hotel.to_dict())
        FileService.save_data(DATA_FILE, hotels_data)
        print("Hotel created successfully.")

    @staticmethod
    def get_hotel(hotel_id: str) -> Optional[Hotel]:
        """Retrieve hotel by ID."""
        hotels_data = FileService.load_data(DATA_FILE)

        for hotel_dict in hotels_data:
            if hotel_dict["hotel_id"] == hotel_id:
                return Hotel.from_dict(hotel_dict)

        print("Hotel not found.")
        return None

    @staticmethod
    def display_hotels() -> List[Hotel]:
        """Return all hotels."""
        hotels_data = FileService.load_data(DATA_FILE)
        return [Hotel.from_dict(h) for h in hotels_data]