# TODO: Image handling

import requests
import yaml
from bs4 import BeautifulSoup
import os

### Constants ###

PROBLEM_URL = "https://www.pbinfo.ro/probleme/"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}


class Problem:

    def __init__(self, soup, problemId) -> None:
        self.__problemObject = {}
        self.__problemId = problemId
        self.__parse_problem(soup)
     
    #Might have to heavily rewrite this once :))
    def __parse_problem(self, soup):

        problemName = soup.find('a', href=lambda href: href and "/probleme/" + str(self.__problemId) in href)
        self.__problemObject['name'] = problemName.text.strip()


        problemTags = soup.find('span', id="container-etichete")
        self.__problemObject['tags'] = []
        for pt in problemTags.children:
            if pt and pt.text.strip() != '':
                self.__problemObject['tags'].append(pt.text.strip())

        problemInfo = soup.find(id="enunt")
        infoChildren = problemInfo.find_all(recursive = False)   
        currentKey = "Pre Text"
        subKey = ""
        

        for child in infoChildren:
            if child.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                currentKey = child.text
                self.__problemObject[currentKey] = ''
            elif child.name != 'ul' and (not "Exemplu" in currentKey):
                try:
                    if not self.__problemObject[currentKey]:
                        self.__problemObject[currentKey] = ''
                    self.__problemObject[currentKey] += child.text
                except:
                    continue
            elif child.name == 'ul':
                i = 0
                self.__problemObject[currentKey] = {}
                for listElement in child.children:
                    if listElement.text and listElement.text != '\n':
                        self.__problemObject[currentKey][i] = listElement.text
            elif "Exemplu" in currentKey:
                if not self.__problemObject[currentKey]:
                    self.__problemObject[currentKey] = {}

                if child.name == 'p':
                    subKey = child.text
                
                elif child.name == 'pre':
                    self.__problemObject[currentKey][subKey] = child.text
            if child.find('img') is not None:
                if 'images' not in self.__problemObject or not self.__problemObject['images']:
                    self.__problemObject['images'] = []
                self.__problemObject['images'].append("https://www.pbinfo.ro" + child.find('img')['src'])
                    
    def indexProblem(self):
        with open(os.path.dirname(os.path.abspath(__file__)) + "/problemIndexing.yaml", "r") as f:
            try:
                pindexing_yaml = yaml.safe_load(f)
                if self.__problemId not in pindexing_yaml:
                    pindexing_yaml[self.__problemObject['name']] = self.__problemId
                    with open(os.path.dirname(os.path.abspath(__file__)) + "/problemIndexing.yaml", 'w') as f:
                        yaml.dump(pindexing_yaml, f)
            except:
                pindexing_yaml = {}
                pindexing_yaml[self.__problemObject['name']] = self.__problemId
                with open(os.path.dirname(os.path.abspath(__file__)) + "/problemIndexing.yaml", 'w') as f:
                    yaml.dump(pindexing_yaml, f)
                

    def get_problem(self):
        return self.__problemObject
    
    def get_problemId(self):
        return self.__problemId


def getProblem(problemId):
    r = requests.get(PROBLEM_URL + str(problemId), headers=HEADERS)
    
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, "html.parser")
        
        if soup:
            p = Problem(soup, problemId)
            p.indexProblem()
        else:
            p = None
    else:
        print("Couldn't get problem")
        return None

    return p.get_problem(), p

getProblem(2828)