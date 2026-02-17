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
    
    @staticmethod
    def delete_hotel(hotel_id: str) -> None:
        """Delete a hotel by ID."""
        hotels_data = FileService.load_data(DATA_FILE)

        updated_hotels = [
            hotel for hotel in hotels_data
            if hotel["hotel_id"] != hotel_id
        ]

        if len(updated_hotels) == len(hotels_data):
            print("Error: Hotel not found.")
            return

        FileService.save_data(DATA_FILE, updated_hotels)
        print("Hotel deleted successfully.")

    @staticmethod
    def modify_hotel(
        hotel_id: str,
        name: str = None,
        location: str = None,
        total_rooms: int = None,
        available_rooms: int = None,
    ) -> None:
        """Modify hotel information."""
        hotels_data = FileService.load_data(DATA_FILE)

        for hotel in hotels_data:
            if hotel["hotel_id"] == hotel_id:
                if name is not None:
                    hotel["name"] = name
                if location is not None:
                    hotel["location"] = location
                if total_rooms is not None:
                    hotel["total_rooms"] = total_rooms
                if available_rooms is not None:
                    hotel["available_rooms"] = available_rooms

                FileService.save_data(DATA_FILE, hotels_data)
                print("Hotel updated successfully.")
                return

        print("Error: Hotel not found.")


    @staticmethod
    def reserve_room(hotel_id: str) -> None:
        """Reserve a room in a hotel."""
        hotels_data = FileService.load_data(DATA_FILE)

        for hotel in hotels_data:
            if hotel["hotel_id"] == hotel_id:

                if hotel["available_rooms"] <= 0:
                    print("Error: No rooms available.")
                    return

                hotel["available_rooms"] -= 1
                FileService.save_data(DATA_FILE, hotels_data)
                print("Room reserved successfully.")
                return

        print("Error: Hotel not found.")


