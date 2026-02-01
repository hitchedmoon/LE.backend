# app/routes/user_routes.py
from flask import Blueprint, jsonify

# This is the 'user_bp' the error is looking for
user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/test', methods=['GET'])
def test_route():
    return jsonify({"message": "API is working!"}), 200