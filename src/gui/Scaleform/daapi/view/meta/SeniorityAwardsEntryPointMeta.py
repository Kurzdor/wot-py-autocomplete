# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/SeniorityAwardsEntryPointMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class SeniorityAwardsEntryPointMeta(BaseDAAPIComponent):

    def onClick(self):
        self._printOverrideError('onClick')

    def playSound(self, sounr):
        self._printOverrideError('playSound')

    def as_setDataS(self, data):
        return self.flashObject.as_setData(data) if self._isDAAPIInited() else None
