
class characterDataModel :
    def  setObjectData(self, jsonData) -> None:
        self.name = jsonData["name"]
        self.health = jsonData["health"]
        self.stamina = jsonData["stamina"]
        #j["attributes"]:
        self.attributes = jsonData["attributes"]
        #["skills"]:
        self.skills =  jsonData["skills"]
               #attr skills
        attributes = ""
        for key in self.skills:
            attributes = attributes+"\n"+str(key)
        self.attrList = attributes
        #["hakis"]:
        self.hakis = jsonData["hakis"]
         #objetos
        self.objects = jsonData["objects"]
        #tecnicas
        self.techiques = jsonData["techniques"]
        print(self.techiques)
        customSkillList = ""
        for key in self.techiques:
            customSkillList = customSkillList+"\n"+str(key)
        self.customSkillList = customSkillList
         #saludo
        print("Bienvenido "+self.name)

        pass

    def returnThrowNecesaryData(self, data, techData=0):
        name = data
        data = self.skills[data]
        haki = self._hakiUseLevel(data["haki"])
        if name == "lucha1" or  name == "lucha2" or name == "pelea":
            choice = input("Weapon  or armor? ")
            if techData == 0:
                return self._attackOrThrow({
                "name":name, 
                "skill": data["level"],
                "attr":self.attributes[data["base"]], 
                "accurancy":self.objects[choice]["acurrancy"], 
                "damage":self.objects[choice]["damage"] ,
                "haki": haki,     
                "cost": (haki*3)
                }, 1) 
            else:
                return self._attackOrThrow({
                    "name":               techData["name"],
                     "skill":                 data["level"], 
                     "attr":                  self.attributes[data["base"]],
                      "accurancy":      (self.objects[choice]["acurrancy"]+ techData["attack"]), 
                      "damage":         (self.objects[choice]["damage"]+ techData["damage"]) ,
                      "haki":                haki,     
                      "cost":               ((haki*3)+techData["cost"]),
                     "extraInfo":         techData["extraInfo"]
                      }, 3) 

        if name == "bloqueo" or  name == "esquiva" :
            return self._attackOrThrow({
            "name":name, 
            "skill": data["level"], 
            "attr":self.attributes[data["base"]], 
            "armor":self.objects["armor"][name],
            "haki": haki,     
            "cost": (haki*3)}, 2) 
        else :
            return self._attackOrThrow({
            "name":name, 
            "skill": data["level"], 
            "attr":self.attributes[data["base"]], 
            "haki": haki, 
            "cost": (haki*3)}, 0) 

            
    
    def _hakiUseLevel(self, type):
        if type != "none":
            level = self.hakis[type]
            print("su nivel de haki de "+str(type)+" es "+str(level))
            use = input("Cuanto haki desea usar -> ")
            use = int(use)
            if use > level:
                use = level
            elif use <= 0:
                 use = 0
        else :
            use = 0
        return int(use)
        
    def _attackOrThrow (self, data, type):
        if type==0:
            attack = data["skill"]+ data["attr"]+ (data["haki"] *2)
            text = "\n skill  : "+str(data["skill"])+"\n atribute : "+str(data["attr"])+"\n haki lvl : "+str(data["haki"])+"\n cost : "+str(data["cost"])+"\n "+str(data['name'])+" : "+str(attack)
        elif type == 1 :
            attack = data["skill"]+ data["attr"]+ (data["haki"] *2)+ data["accurancy"]
            damage =data["damage"]+ attack
            text = "\n skill  : "+str(data["skill"])+"\n atribute : "+str(data["attr"])+"\n haki : "+str(data["haki"])+"\n accurancy : "+str(data["accurancy"])+"\n damage : "+str(data["damage"])+"\n cost : "+str(data["cost"])+"\n attack : " +str(attack)+"--damage : "+str(damage)
        elif type == 2 :
            attack = data["skill"]+ data["attr"]+ (data["haki"] *2)+ data["armor"]
            text = "\n skill  : "+str(data["skill"])+"\n atribute : "+str(data["attr"])+"\n haki : "+str(data["haki"])+"\n armor : "+str(data["armor"])+"\n cost : "+str(data["cost"])+"\n defensa : " +str(attack)
        elif type == 3 :
            attack = data["skill"]+ data["attr"]+ (data["haki"] *2)+ data["accurancy"]
            damage =data["damage"]+ attack
            text = "\n skill  : "+str(data["skill"])+"\n atribute : "+str(data["attr"])+"\n haki : "+str(data["haki"])+"\n accurancy : "+str(data["accurancy"])+"\n damage : "+str(data["damage"])+"\n cost : "+str(data["cost"])+"\n attack : " +str(attack)+"--damage : "+str(damage)+"\n extra info  : "+str(data["extraInfo"])
        
        return text
    def techniqueThrow(self, data):
        name = data
        data = self.techiques[data]
        extraInfo = ""
        for key in data["efects"]:
            extraInfo = extraInfo+"\n"+str(key)+" : "+str(data["efects"][key])

        tecData = {
         "name": name, 
         "attack": data["attack"], 
         "damage": data["damage"], 
         "cost": data["cost"], 
         "extraInfo": extraInfo }
        return self.returnThrowNecesaryData(str(data["skill"]), tecData)


    
        
    
    pass