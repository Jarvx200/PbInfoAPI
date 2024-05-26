import requests
import urllib.parse
from scraping.problemScraper import getProblem

def get_problem_json(problemId):
    return getProblem(problemId)

