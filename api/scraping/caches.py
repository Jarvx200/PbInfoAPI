
CACHE_SIZE = 100



class Cache:
    def __init__(self) -> None:
        self.cache = []
        self.size = 0
    
    def add(self, obj):
        if self.size == CACHE_SIZE:
            self.cache.pop(0)
            self.size -= 1
        self.cache.append(obj)
        self.size += 1
    
    def printCache(self):
        for obj in self.cache:
            print(obj)

class ProblemCache(Cache):
    def __init__(self) -> None:
        super().__init__()

    def get(self, problemId):
        for problem in self.cache:
            if problem.get_problemId() == problemId:
                return problem.get_problem()
        return None
    
class UserCache(Cache):
    def __init__(self) -> None:
        super().__init__()

    def get(self, userName):
        for user in self.cache:
            if user.get_userName() == userName:
                return user
        return None
    
userCache = UserCache()
problemCache = ProblemCache()
