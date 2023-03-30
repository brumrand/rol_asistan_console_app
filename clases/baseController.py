
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
        data = self.characterDataModel.returnThrowNecesaryData(tirada)
        print(data)
        pass
    pass