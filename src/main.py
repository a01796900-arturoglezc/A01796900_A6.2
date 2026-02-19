"""
Manual test execution for Reservation System.
"""

from src.models.hotel import Hotel
from src.models.customer import Customer
from src.models.reservation import Reservation
from src.services.reservation_service import ReservationService
from src.services.hotel_service import HotelService
from src.services.customer_service import CustomerService


def test_hotel_service():
    """Execute manual tests for hotel service."""
    print("\n===== HOTEL SERVICE TESTS =====")

    # Create hotel
    hotel = Hotel("H1", "Grand Hotel", "Mexico City", 3, 3)
    HotelService.create_hotel(hotel)

    # Duplicate hotel (negative case)
    HotelService.create_hotel(hotel)

    # Display hotels
    print("Hotels:", HotelService.display_hotels())

    # Modify existing hotel
    HotelService.modify_hotel("H1", name="Updated Hotel")

    # Modify non-existing hotel (negative case)
    HotelService.modify_hotel("H999", name="Ghost Hotel")

    # Reserve room
    HotelService.reserve_room("H1")
    HotelService.reserve_room("H1")
    HotelService.reserve_room("H1")

    # Reserve when no rooms available (negative case)
    HotelService.reserve_room("H1")

    # Cancel room
    HotelService.cancel_room("H1")

    # Cancel when all rooms available (negative case)
    HotelService.cancel_room("H999")  # hotel does not exist

    # Delete hotel
    HotelService.delete_hotel("H1")

    # Delete non-existing hotel (negative case)
    HotelService.delete_hotel("H999")

    print("Final hotels:", HotelService.display_hotels())


def test_customer_service():
    """Execute manual tests for customer service."""
    print("\n===== CUSTOMER SERVICE TESTS =====")

    # Create customer
    customer = Customer("C1", "John Doe", "john@email.com", "123456789")
    CustomerService.create_customer(customer)

    # Duplicate customer (negative case)
    CustomerService.create_customer(customer)

    # Display customers
    print("Customers:", CustomerService.display_customers())

    # Modify existing customer
    CustomerService.modify_customer("C1", name="John Updated")

    # Modify non-existing customer (negative case)
    CustomerService.modify_customer("C999", name="Ghost User")

    # Delete existing customer
    CustomerService.delete_customer("C1")

    # Delete non-existing customer (negative case)
    CustomerService.delete_customer("C999")

    print("Final customers:", CustomerService.display_customers())


def test_reservation_service():
    """Execute manual tests for reservation service."""
    print("\n===== RESERVATION SERVICE TESTS =====")

    # Setup required entities
    hotel = Hotel("H2", "Beach Hotel", "Cancun", 2, 2)
    HotelService.create_hotel(hotel)

    customer = Customer("C2", "Alice", "alice@email.com", "5551234")
    CustomerService.create_customer(customer)

    # Create reservation
    reservation = Reservation("R1", "C2", "H2", 101)
    ReservationService.create_reservation(reservation)

    # Duplicate reservation (negative case)
    ReservationService.create_reservation(reservation)

    # Non-existing customer (negative)
    bad_res = Reservation("R2", "C999", "H2", 102)
    ReservationService.create_reservation(bad_res)

    # Non-existing hotel (negative)
    bad_res2 = Reservation("R3", "C2", "H999", 103)
    ReservationService.create_reservation(bad_res2)

    print("Reservations:", ReservationService.display_reservations())

    # Cancel existing reservation
    ReservationService.cancel_reservation("R1")

    # Cancel non-existing reservation (negative case)
    ReservationService.cancel_reservation("R999")

    print("Reservations after cancel:",
          ReservationService.display_reservations())


if __name__ == "__main__":
    test_hotel_service()
    test_customer_service()
    test_reservation_service()
