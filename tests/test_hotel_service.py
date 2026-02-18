import os
import pytest

from src.models.hotel import Hotel
from src.services.hotel_service import HotelService
from src.services.file_service import FileService

DATA_FILE = "data/hotels.json"


@pytest.fixture(autouse=True)
def clear_hotels_file():
    """Clear hotels.json before each test."""
    FileService.save_data(DATA_FILE, [])
    yield
    FileService.save_data(DATA_FILE, [])


def test_create_hotel_success():
    hotel = Hotel("H100", "Test Hotel", "Test City", 10, 10)
    HotelService.create_hotel(hotel)

    hotels = HotelService.display_hotels()
    assert len(hotels) == 1
    assert hotels[0].hotel_id == "H100"


def test_create_hotel_duplicate():
    hotel = Hotel("H200", "Test Hotel", "City", 5, 5)
    HotelService.create_hotel(hotel)
    HotelService.create_hotel(hotel)

    hotels = HotelService.display_hotels()
    assert len(hotels) == 1  # Should not duplicate


def test_modify_existing_hotel():
    hotel = Hotel("H300", "Old Name", "City", 5, 5)
    HotelService.create_hotel(hotel)

    HotelService.modify_hotel("H300", name="New Name")

    hotels = HotelService.display_hotels()
    assert hotels[0].name == "New Name"


def test_modify_nonexistent_hotel():
    HotelService.modify_hotel("H999", name="Does Not Exist")

    hotels = HotelService.display_hotels()
    assert len(hotels) == 0


def test_delete_existing_hotel():
    hotel = Hotel("H400", "Delete Hotel", "City", 5, 5)
    HotelService.create_hotel(hotel)

    HotelService.delete_hotel("H400")

    hotels = HotelService.display_hotels()
    assert len(hotels) == 0


def test_delete_nonexistent_hotel():
    HotelService.delete_hotel("H999")

    hotels = HotelService.display_hotels()
    assert len(hotels) == 0


def test_reserve_room_success():
    hotel = Hotel("H500", "Reserve Hotel", "City", 2, 2)
    HotelService.create_hotel(hotel)

    HotelService.reserve_room("H500")

    hotels = HotelService.display_hotels()
    assert hotels[0].available_rooms == 1


def test_reserve_room_no_availability():
    hotel = Hotel("H600", "Full Hotel", "City", 1, 1)
    HotelService.create_hotel(hotel)

    HotelService.reserve_room("H600")
    HotelService.reserve_room("H600")  # Should fail

    hotels = HotelService.display_hotels()
    assert hotels[0].available_rooms == 0


def test_cancel_room():
    hotel = Hotel("H700", "Cancel Hotel", "City", 2, 2)
    HotelService.create_hotel(hotel)

    HotelService.reserve_room("H700")
    HotelService.cancel_room("H700")

    hotels = HotelService.display_hotels()
    assert hotels[0].available_rooms == 2
