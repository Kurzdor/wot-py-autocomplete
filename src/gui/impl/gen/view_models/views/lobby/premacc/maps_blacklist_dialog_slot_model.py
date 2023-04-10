# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/premacc/maps_blacklist_dialog_slot_model.py
from gui.impl.gen.view_models.views.lobby.premacc.maps_blacklist_slot_model import MapsBlacklistSlotModel

class MapsBlacklistDialogSlotModel(MapsBlacklistSlotModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(MapsBlacklistDialogSlotModel, self).__init__(properties=properties, commands=commands)

    def getIsResizable(self):
        return self._getBool(5)

    def setIsResizable(self, value):
        self._setBool(5, value)

    def _initialize(self):
        super(MapsBlacklistDialogSlotModel, self)._initialize()
        self._addBoolProperty('isResizable', False)
