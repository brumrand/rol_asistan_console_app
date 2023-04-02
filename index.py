from clases.baseController import *
from clases.characterDataModel import *
from clases.manageJsonObjects import *

controller = baseController(manageJsonObjects(), characterDataModel())
#controller.tirada()
controller.tecnica()