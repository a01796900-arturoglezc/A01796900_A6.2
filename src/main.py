from src.models.hotel import Hotel
from src.services.hotel_service import HotelService

hotel = Hotel("H1", "Grand Hotel", "Mexico City", 100, 100)
HotelService.create_hotel(hotel)

print(HotelService.display_hotels())
