import pytest

from src.models.customer import Customer
from src.services.customer_service import CustomerService
from src.services.file_service import FileService

DATA_FILE = "data/customers.json"


@pytest.fixture(autouse=True)
def clear_customers_file():
    """Clear customers.json before each test."""
    FileService.save_data(DATA_FILE, [])
    yield
    FileService.save_data(DATA_FILE, [])


def test_create_customer_success():
    customer = Customer("C100", "Arturiño cara de piño pero no Ronaldiño", "arturiño@test.com", "1234567890")
    CustomerService.create_customer(customer)

    customers = CustomerService.display_customers()
    assert len(customers) == 1
    assert customers[0].customer_id == "C100"


def test_create_customer_duplicate():
    customer = Customer("C200", "Pepe pica pocas Papas", "pepe@test.com", "1234567890")
    CustomerService.create_customer(customer)
    CustomerService.create_customer(customer)

    customers = CustomerService.display_customers()
    assert len(customers) == 1


def test_modify_existing_customer():
    customer = Customer("C300", "El viejo", "old@test.com", "1234567890")
    CustomerService.create_customer(customer)

    CustomerService.modify_customer("C300", name="El nuevo")

    customers = CustomerService.display_customers()
    assert customers[0].name == "El nuevo"


def test_modify_nonexistent_customer():
    CustomerService.modify_customer("C999", name="Does Not Exist")

    customers = CustomerService.display_customers()
    assert len(customers) == 0


def test_delete_existing_customer():
    customer = Customer("C400", "Delete User", "delete@test.com", "1234567890")
    CustomerService.create_customer(customer)

    CustomerService.delete_customer("C400")

    customers = CustomerService.display_customers()
    assert len(customers) == 0


def test_delete_nonexistent_customer():
    CustomerService.delete_customer("C999")

    customers = CustomerService.display_customers()
    assert len(customers) == 0
