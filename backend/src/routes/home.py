# src/routes/home.py
from flask import Blueprint, jsonify

home_bp = Blueprint('home', __name__)

@home_bp.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to FilmFlow API!"}), 200
