
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