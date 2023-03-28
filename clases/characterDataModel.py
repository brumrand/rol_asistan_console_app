
class characterDataModel :
    def  setObjectData(self, jsonData) -> None:
        self.name = jsonData["name"]
        self.health = jsonData["health"]
        self.stamina = jsonData["stamina"]
        #j["attributes"]:
        self.attributes = jsonData["attributes"]
        #["skills"]:
        self.skills =  jsonData["skills"]
        #["hakis"]:
        self.hakis = jsonData["hakis"]
        
        print("Bienvenido "+self.name)
        print( self.skills)
        pass
    def returnThrowNecesaryData(self, data):
        return self.skills[data]
    pass