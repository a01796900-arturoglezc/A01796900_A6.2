"""
Customer service for managing customer operations.
"""

import os
from typing import List, Optional

from src.models.customer import Customer
from src.services.file_service import FileService


DATA_FILE = os.path.join("data", "customers.json")


class CustomerService:
    """Service layer for customer operations."""

    @staticmethod
    def create_customer(customer: Customer) -> None:
        """Create a new customer."""
        customers_data = FileService.load_data(DATA_FILE)

        for existing in customers_data:
            if existing["customer_id"] == customer.customer_id:
                print("Error: Customer ID already exists.")
                return

        customers_data.append(customer.to_dict())
        FileService.save_data(DATA_FILE, customers_data)
        print("Customer created successfully.")

    @staticmethod
    def get_customer(customer_id: str) -> Optional[Customer]:
        """Retrieve customer by ID."""
        customers_data = FileService.load_data(DATA_FILE)

        for customer_dict in customers_data:
            if customer_dict["customer_id"] == customer_id:
                return Customer.from_dict(customer_dict)

        print("Customer not found.")
        return None

    @staticmethod
    def display_customers() -> List[Customer]:
        """Return all customers."""
        customers_data = FileService.load_data(DATA_FILE)
        return [Customer.from_dict(c) for c in customers_data]

    @staticmethod
    def delete_customer(customer_id: str) -> None:
        """Delete a customer by ID."""
        customers_data = FileService.load_data(DATA_FILE)

        updated_customers = [
            customer for customer in customers_data
            if customer["customer_id"] != customer_id
        ]

        if len(updated_customers) == len(customers_data):
            print("Error: Customer not found.")
            return

        FileService.save_data(DATA_FILE, updated_customers)
        print("Customer deleted successfully.")

    @staticmethod
    def modify_customer(
        customer_id: str,
        name: str = None,
        email: str = None,
        phone: str = None,
    ) -> None:
        """Modify customer information."""
        customers_data = FileService.load_data(DATA_FILE)

        for customer in customers_data:
            if customer["customer_id"] == customer_id:
                if name is not None:
                    customer["name"] = name
                if email is not None:
                    customer["email"] = email
                if phone is not None:
                    customer["phone"] = phone

                FileService.save_data(DATA_FILE, customers_data)
                print("Customer updated successfully.")
                return

        print("Error: Customer not found.")
