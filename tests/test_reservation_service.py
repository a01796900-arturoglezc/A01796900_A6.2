import pytest

from src.models.hotel import Hotel
from src.models.customer import Customer
from src.models.reservation import Reservation

from src.services.hotel_service import HotelService
from src.services.customer_service import CustomerService
from src.services.reservation_service import ReservationService
from src.services.file_service import FileService

HOTEL_FILE = "data/hotels.json"
CUSTOMER_FILE = "data/customers.json"
RESERVATION_FILE = "data/reservations.json"


@pytest.fixture(autouse=True)
def clear_all_files():
    """Clear all JSON files before each test."""
    FileService.save_data(HOTEL_FILE, [])
    FileService.save_data(CUSTOMER_FILE, [])
    FileService.save_data(RESERVATION_FILE, [])
    yield
    FileService.save_data(HOTEL_FILE, [])
    FileService.save_data(CUSTOMER_FILE, [])
    FileService.save_data(RESERVATION_FILE, [])


def setup_valid_environment():
    """Helper to create one hotel and one customer."""
    hotel = Hotel("H1", "Test Hotel", "City", 5, 5)
    customer = Customer("C1", "Arturiño of Course", "arturiño@test.com", "1234567890")

    HotelService.create_hotel(hotel)
    CustomerService.create_customer(customer)


def test_create_reservation_success():
    setup_valid_environment()

    reservation = Reservation("R1", "C1", "H1", 101)
    ReservationService.create_reservation(reservation)

    reservations = ReservationService.display_reservations()
    assert len(reservations) == 1
    assert reservations[0].reservation_id == "R1"


def test_create_reservation_duplicate():
    setup_valid_environment()

    reservation = Reservation("R2", "C1", "H1", 101)
    ReservationService.create_reservation(reservation)
    ReservationService.create_reservation(reservation)

    reservations = ReservationService.display_reservations()
    assert len(reservations) == 1


def test_create_reservation_invalid_customer():
    hotel = Hotel("H2", "Hotel", "City", 5, 5)
    HotelService.create_hotel(hotel)

    reservation = Reservation("R3", "C999", "H2", 101)
    ReservationService.create_reservation(reservation)

    reservations = ReservationService.display_reservations()
    assert len(reservations) == 0


def test_create_reservation_invalid_hotel():
    customer = Customer("C2", "Nino", "nino@test.com", "1234567890")
    CustomerService.create_customer(customer)

    reservation = Reservation("R4", "C2", "H999", 101)
    ReservationService.create_reservation(reservation)

    reservations = ReservationService.display_reservations()
    assert len(reservations) == 0


def test_cancel_reservation_success():
    setup_valid_environment()

    reservation = Reservation("R5", "C1", "H1", 101)
    ReservationService.create_reservation(reservation)

    ReservationService.cancel_reservation("R5")

    reservations = ReservationService.display_reservations()
    assert len(reservations) == 0


def test_cancel_reservation_nonexistent():
    ReservationService.cancel_reservation("R999")

    reservations = ReservationService.display_reservations()
    assert len(reservations) == 0
