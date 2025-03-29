import unittest
# 🎯 Hotel Management System Classes
class Guest:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def get_details(self):
        return f"Guest: {self.name}, Email: {self.email}, Phone: {self.phone}"

class Room:
    def __init__(self, room_number, room_type, price, is_available=True):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.is_available = is_available

    def book_room(self):
        if self.is_available:
            self.is_available = False
            return f"Room {self.room_number} booked successfully."
        return f"Room {self.room_number} is already booked."

    def cancel_booking(self):
        if not self.is_available:
            self.is_available = True
            return f"Booking for Room {self.room_number} canceled."
        return f"Room {self.room_number} was not booked."

class Booking:
    def __init__(self, guest, room, nights):
        self.guest = guest
        self.room = room
        self.nights = nights
        self.total_price = room.price * nights

    def confirm_booking(self):
        return f"Booking confirmed for {self.guest.name} in Room {self.room.room_number} for {self.nights} nights. Total: ${self.total_price}"

class Payment:
    def __init__(self, guest, amount, method):
        self.guest = guest
        self.amount = amount
        self.method = method

    def process_payment(self):
        return f"Payment of ${self.amount} by {self.guest.name} via {self.method} processed successfully."

# 🎯 Run Hotel Management System
print("Welcome to Royal Stay Hotel Management System\n")

guest1 = Guest("Alice Johnson", "alice@email.com", "123-456-7890")
room1 = Room(101, "Deluxe", 150)
booking1 = Booking(guest1, room1, 3)
payment1 = Payment(guest1, booking1.total_price, "Credit Card")

# Simulating user actions
print(guest1.get_details())
print(room1.book_room())
print(booking1.confirm_booking())
print(payment1.process_payment())
print(room1.cancel_booking())

# 🎯 Unit Testing for Hotel Management System
class TestHotelManagement(unittest.TestCase):

    def test_guest_details(self):
        guest = Guest("John Doe", "john@email.com", "987-654-3210")
        self.assertEqual(guest.get_details(), "Guest: John Doe, Email: john@email.com, Phone: 987-654-3210")

    def test_room_booking(self):
        room = Room(102, "Suite", 200)
        self.assertEqual(room.book_room(), "Room 102 booked successfully.")
        self.assertEqual(room.book_room(), "Room 102 is already booked.")

    def test_booking_confirmation(self):
        guest = Guest("Emily Clark", "emily@email.com", "555-555-5555")
        room = Room(103, "Standard", 100)
        booking = Booking(guest, room, 2)
        self.assertEqual(booking.confirm_booking(), "Booking confirmed for Emily Clark in Room 103 for 2 nights. Total: $200")

    def test_payment_processing(self):
        guest = Guest("Michael Lee", "michael@email.com", "111-222-3333")
        payment = Payment(guest, 300, "PayPal")
        self.assertEqual(payment.process_payment(), "Payment of $300 by Michael Lee via PayPal processed successfully.")
# Run the tests
unittest.main(argv=[''], verbosity=2, exit=False)