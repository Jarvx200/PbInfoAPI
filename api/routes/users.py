from flask import Blueprint, jsonify
from scraping.userScraper import getUser    

users_bp = Blueprint('users', __name__, url_prefix='/users')

@users_bp.route('/<string:userName>', methods=['GET'])
def get_user(userName):
    user = getUser(userName)
    if user : return user 
    else : return {"error": "User not found"}
    
