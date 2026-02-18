"""
Reservation service for managing reservation operations.
"""

import os
from typing import List

from src.models.reservation import Reservation
from src.services.file_service import FileService
from src.services.hotel_service import HotelService
from src.services.customer_service import CustomerService


DATA_FILE = os.path.join("data", "reservations.json")


class ReservationService:
    """Service layer for reservation operations."""

    @staticmethod
    def create_reservation(
        reservation: Reservation,
    ) -> None:
        """Create a reservation if customer and hotel exist."""

        # Validate customer
        customer = CustomerService.get_customer(reservation.customer_id)
        if customer is None:
            print("Error: Customer does not exist.")
            return

        # Validate hotel
        hotel = HotelService.get_hotel(reservation.hotel_id)
        if hotel is None:
            print("Error: Hotel does not exist.")
            return

        if hotel.available_rooms <= 0:
            print("Error: No rooms available.")
            return

        reservations_data = FileService.load_data(DATA_FILE)

        # Prevent duplicate reservation ID
        for existing in reservations_data:
            if existing["reservation_id"] == reservation.reservation_id:
                print("Error: Reservation ID already exists.")
                return

        reservations_data.append(reservation.to_dict())
        FileService.save_data(DATA_FILE, reservations_data)

        # Reduce available rooms
        HotelService.reserve_room(reservation.hotel_id)

        print("Reservation created successfully.")

    @staticmethod
    def display_reservations() -> List[Reservation]:
        """Return all reservations."""
        reservations_data = FileService.load_data(DATA_FILE)
        return [Reservation.from_dict(r) for r in reservations_data]
