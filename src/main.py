"""
Manual test execution for Reservation System.
"""

from src.models.hotel import Hotel
from src.models.customer import Customer
from src.services.hotel_service import HotelService
from src.services.customer_service import CustomerService


def test_hotel_service():
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


if __name__ == "__main__":
    test_hotel_service()
    test_customer_service()
