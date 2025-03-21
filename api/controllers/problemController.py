import os
import yaml
from scraping.problemScraper import getProblem
from scraping.caches import problemCache

def get_from_cache(problemId):
    if problemCache:
        problem = problemCache.get(problemId)
        if problem:
            return problem
        return None
    return None


def get_problem_json(problemId):
    problem = get_from_cache(problemId)

    if problem:
        return problem
    try:
        problem, problemObject = getProblem(problemId)
        problemCache.add(problemObject)

        return problem
    except:
        return None

def get_problem_json_by_name(problemName):
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../scraping/problemIndexing.yaml"), "r") as f:
        pindexing_yaml = yaml.safe_load(f)
        if problemName in pindexing_yaml:
            problemId = pindexing_yaml[problemName]
        else:
            return {
                "error": "Problem not yet discoverable by name. Please use the problemId instead.",
                "info": "The api is user powered, so when when a user searches a problem by it's id, the problem is indexed by it's name. This way, the next user that searches for the problem by it's name will get the problemId."
            }   
        
    problem = get_from_cache(problemId)

    if problem:
        return problem

    problem, problemObject = getProblem(problemId)
    if problemObject:
        problemCache.add(problemObject)

    return problem