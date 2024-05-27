from flask import Blueprint
from controllers.usersController import get_user_json    

users_bp = Blueprint('users', __name__, url_prefix='/users')

@users_bp.route('/<string:userName>', methods=['GET'])
def get_user(userName):
    user = get_user_json(userName)
    if user : return user 
    else : return {"error": "User not found"}
    
