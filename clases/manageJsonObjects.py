import json
class manageJsonObjects :
    route = "data/data.json"

    def getJsonData (self):
        file = open(self.route)
        data = json.load(file)
        file.close()
        return data
    pass