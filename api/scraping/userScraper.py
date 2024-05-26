import requests
from bs4 import BeautifulSoup

### Constants ###

USER_URL = "https://www.pbinfo.ro/profil/"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}


class User:
    def __init__(self, userData, userName) -> None:
        self.__userName = userName
        self.__userData = {}
        self.__parse_user_data(userData)
    
    def __parse_user_data(self, userData):
        self.__userData['username'] = self.__userName

        profilePicture = userData.find('img', title="Imagine Gravatar")
        self.__userData['pfp'] = "https://www.pbinfo.ro/" + profilePicture['src']

        realName = userData.find_all("div", class_="well well-sm center")[0].find("h2").text.strip().replace("\n", " ")
        self.__userData['nume'] = realName

        userStatisticsBlocks = userData.find_all("span", class_="big block")
        self.__userData['trimise']  =   userStatisticsBlocks[0].text.strip()
        self.__userData['corecte']  =   userStatisticsBlocks[1].text.strip()
        self.__userData['succes']   =   userStatisticsBlocks[2].text.strip()

        self.__userData['badge']    =   "https://www.pbinfo.ro/" + userData.find('img', width="107")['src']

    def get_userName(self):
        return self.__userName

    def get_userData(self):
        return self.__userData


def getUser(userName):
    r = requests.get(USER_URL + str(userName), headers=HEADERS)
    
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, "html.parser")

        u = User(soup, userName)

        return u.get_userData()
    else:
        print("Couldn't get user!")
        return None


getUser("silviu")