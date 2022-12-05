from Laborator7.Repository.customer_repository import CustomerRepository
from Laborator7.Repository.book_repository import BookRepository
from Laborator7.Repository.rent_repository import RentRepository
from Laborator7.Service.customer_service import CustomerService
from Laborator7.Service.book_service import BookService
from Laborator7.Service.rent_service import RentService
from Ui.Console.console import Console


def main1():
    book_repository = BookRepository()
    book_service = BookService(book_repository)
    customer_repository = CustomerRepository()
    customer_service = CustomerService(customer_repository)
    rent_repository = RentRepository(book_repository, customer_repository)
    rent_service = RentService(rent_repository, book_repository, customer_repository)
    console = Console(customer_service, book_service, rent_service)

    console.run_menu()


if __name__ == '__main__':
    main1()
