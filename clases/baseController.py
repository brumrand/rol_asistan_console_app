
class baseController :
    def __init__(self, manageJsonObjects, characterDataModel) -> None:
        self.manageJsonObjects = manageJsonObjects
        self.characterDataModel =  characterDataModel
        self._setCharacterData()
        pass


    def _setCharacterData(self)-> None:
        charcaterData = self.manageJsonObjects.getJsonData()
        self.characterDataModel.setObjectData(charcaterData["character"])
        pass



    def tirada (self):
        tirada = input("Seleccione su tirada "+str(self.characterDataModel.attrList)+"\n entre las anteriores : ")
        if tirada in self.characterDataModel.attrArray :
            data = self.characterDataModel.returnThrowNecesaryData(tirada)
            print(data)
        else :
            print("habilidad no admitida, se le devolverá al menu de tirada -> ")
            self.tirada()
        pass



    def tecnica (self):
        tirada = input("Seleccione su tirada "+str(self.characterDataModel.customSkillList)+"\n entre las anteriores : ")
        if tirada in self.characterDataModel.customskillsArrays :
            data = self.characterDataModel.techniqueThrow(tirada)
            print(data)
        else :
            print("habilidad no admitida, se le devolverá al menu de técnicas ->")
            self.tecnica()

        pass



    def game (self):
        flag =True
        while flag == True :
            tirada = input("Escriba tecnica para acceder a su interfaz y cualquier otra cosa para acceder a las habilidades -> ")
            if  tirada.lower() == "tecnica":
                self.tecnica()
            else :
                self.tirada()
            tirada = input("Escriba fin para acabar el programa cualquier otra cosa para continuar -> ")
            if tirada == "fin":
                flag = False

    pass