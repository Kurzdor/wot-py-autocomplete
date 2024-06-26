# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale_progression/scripts/client/battle_royale_progression/gui/shared/event_dispatcher.py
from gui.Scaleform.framework import ScopeTemplates
from gui.Scaleform.framework.managers.loaders import GuiImplViewLoadParams
from gui.impl.gen import R
from gui.shared import EVENT_BUS_SCOPE, events, g_eventBus

def showProgressionView(activeTab=None):
    from battle_royale_progression.gui.impl.lobby.views.progression_main_view import ProgressionMainView
    from battle_royale_progression.gui.impl.gen.view_models.views.lobby.views.progression.progression_main_view_model import MainViews
    viewRes = R.views.battle_royale_progression.ProgressionMainView()
    view = ProgressionMainView
    if not activeTab:
        activeTab = MainViews.PROGRESSION
    g_eventBus.handleEvent(events.LoadGuiImplViewEvent(GuiImplViewLoadParams(viewRes, view, scope=ScopeTemplates.LOBBY_SUB_SCOPE), ctx={'menuName': activeTab}), scope=EVENT_BUS_SCOPE.LOBBY)


def showAwardsView(stage):
    from battle_royale_progression.gui.impl.lobby.views.battle_quest_awards_view import BattleQuestAwardsViewWindow
    BattleQuestAwardsViewWindow(stage).load()
