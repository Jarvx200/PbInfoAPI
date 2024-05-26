from flask import Blueprint
from controllers import usersController, problemController

problems_bp = Blueprint('problems', __name__, url_prefix='/problems')

@problems_bp.route('/<int:problemId>', methods=['GET'])
def get_problem_by_id(problemId):
    return problemController.get_problem_json(problemId)

@problems_bp.route('/<string:problemName>', methods=['GET'])
def get_problem_by_name(problemName):
    return problemController.get_problem_json_by_name(problemName)