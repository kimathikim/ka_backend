from flask import Blueprint, request, jsonify
from services.contact_service import ContactService

contact_bp = Blueprint('contact', __name__)
contact_service = ContactService()

@contact_bp.route('/add', methods=['POST'])
def add_contact():
    data = request.get_json()
    result = contact_service.add_contact(data)
    return jsonify(result), 201 if result['success'] else 400

@contact_bp.route('/search', methods=['GET'])
def search_contact():
    registration_number = request.args.get('registration_number')
    result = contact_service.search_contact(registration_number)
    return jsonify(result), 200 if result['success'] else 404
