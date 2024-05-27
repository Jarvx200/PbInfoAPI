from flask import jsonify
from scraping.userScraper import getUser
from scraping.caches import userCache

def get_from_cache(userName):
    foundUser = userCache.get(userName)
    return foundUser




def get_user_json(userName):
    user = get_from_cache(userName=userName)
    if user:
        return jsonify(user.get_userData())
    try:
        user, userObject = getUser(userName)
        userCache.add(userObject)
        return jsonify(user)
    except:
        return None