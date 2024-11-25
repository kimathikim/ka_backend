from app import db


class ContactService:
    def add_contact(self, contact_data):
        if db.contacts.find_one(
            {"registrationNumber": contact_data["registration_number"]}
        ):
            return {"success": False, "message": "Registration number already exists"}

        db.contacts.insert_one(contact_data)
        return {"success": True, "message": "Contact added successfully"}

    def search_contact(self, registration_number):
        contact = db.contacts.find_one({"registration_number": registration_number})
        if contact:
            contact["_id"] = str(contact["_id"])  # Convert ObjectId to string
            return {"success": True, "contact": contact}
        return {"success": False, "message": "Contact not found"}

