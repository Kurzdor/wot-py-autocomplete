# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/Comp7FullStatsMeta.py
from gui.Scaleform.daapi.view.battle.shared.tabbed_full_stats import TabbedFullStatsComponent

class Comp7FullStatsMeta(TabbedFullStatsComponent):

    def onVoiceChatControlClick(self):
        self._printOverrideError('onVoiceChatControlClick')

    def as_setVoiceChatDataS(self, data):
        return self.flashObject.as_setVoiceChatData(data) if self._isDAAPIInited() else None

    def as_setVoiceChatControlVisibleS(self, value):
        return self.flashObject.as_setVoiceChatControlVisible(value) if self._isDAAPIInited() else None

    def as_setVoiceChatControlSelectedS(self, value):
        return self.flashObject.as_setVoiceChatControlSelected(value) if self._isDAAPIInited() else None
