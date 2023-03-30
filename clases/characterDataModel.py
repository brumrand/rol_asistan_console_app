
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
        name = data
        data = self.skills[data]
        haki = self._hakiUseLevel(data["haki"])
        return self._attackOrThrow({"name":name, "skill": data["level"], "attr":self.attributes[data["base"]], "haki": haki, "cost": (haki*3)}, 0) 
    
    def _hakiUseLevel(self, type):
        if type != "none":
            level = self.hakis[type]
            #print("su nivel de haki de "+type+" es "+level)
            use = input("Cuanto haki desea usar -> ")
            use = int(use)
            if use > level:
                use = level
            elif use <= 0:
                 use = 0
        else :
            use = 0
            return use
        
    def _attackOrThrow (self, data, type):
        if type==0:
            attack = data["skill"]+ data["attr"]+ (data["haki"] *2)
            text = "\n skill  : "+str(data["skill"])+"\n atribute : "+str(data["attr"])+"\n haki lvl : "+str(data["haki"])+"\n cost : "+str(data["cost"])+"\n "+str(data['name'])+" : "+str(attack)
        elif type == 1 :
            attack = data["skill"]+ data["attr"]+ data["haki"]+ data["accurancy"]
            damage =data["damage"]+ attack
            text = "\n skill  : "+str(data["skill"])+"\n atribute : "+str(data["attr"])+"\n haki : "+str(data["haki"])+"\n accurancy : "+str(data["accurancy"])+"\n damage : "+str(data["damage"])+"\n cost : "+str(data["cost"])+"\n attack : " +str(attack)+"--damage : "+str(damage)
        return text

    
        
    
    pass