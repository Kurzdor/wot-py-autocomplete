# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/IngameMenuMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class IngameMenuMeta(AbstractWindowView):

    def quitBattleClick(self):
        self._printOverrideError('quitBattleClick')

    def settingsClick(self):
        self._printOverrideError('settingsClick')

    def helpClick(self):
        self._printOverrideError('helpClick')

    def cancelClick(self):
        self._printOverrideError('cancelClick')

    def onCounterNeedUpdate(self):
        self._printOverrideError('onCounterNeedUpdate')

    def as_setServerSettingS(self, serverName, tooltipFullData, serverState):
        return self.flashObject.as_setServerSetting(serverName, tooltipFullData, serverState) if self._isDAAPIInited() else None

    def as_setServerStatsS(self, stats, tooltipType):
        return self.flashObject.as_setServerStats(stats, tooltipType) if self._isDAAPIInited() else None

    def as_setCounterS(self, counters):
        return self.flashObject.as_setCounter(counters) if self._isDAAPIInited() else None

    def as_removeCounterS(self, counters):
        return self.flashObject.as_removeCounter(counters) if self._isDAAPIInited() else None

    def as_setMenuButtonsLabelsS(self, helpLabel, settingsLabel, cancelLabel, quitLabel):
        return self.flashObject.as_setMenuButtonsLabels(helpLabel, settingsLabel, cancelLabel, quitLabel) if self._isDAAPIInited() else None

    def as_setMenuButtonsS(self, buttons):
        return self.flashObject.as_setMenuButtons(buttons) if self._isDAAPIInited() else None

    def as_setVisibilityS(self, value):
        return self.flashObject.as_setVisibility(value) if self._isDAAPIInited() else None
