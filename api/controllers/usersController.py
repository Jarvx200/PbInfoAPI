from flask import jsonify
from scraping.userScraper import getUser

def get_user_json(userName):
    return jsonify(getUser(userName))