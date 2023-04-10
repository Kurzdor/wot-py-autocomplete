
from gui.Scaleform.framework import g_entitiesFactories, ViewSettings, GroupedViewSettings, ScopeTemplates
from frameworks.wulf import WindowLayer

from .._constants import MODS_LIST_API_BUTTON_ALIAS, MODS_LIST_API_POPOVER_ALIAS
from ..views.buttonView import ModsListButtonView
from ..views.popoverView import ModsListPopoverView

def getViewSettings():
	buttonSettings = ViewSettings(MODS_LIST_API_BUTTON_ALIAS, ModsListButtonView, 'modsListButton.swf',
								WindowLayer.WINDOW, None, ScopeTemplates.GLOBAL_SCOPE)
	popoverSettings = GroupedViewSettings(MODS_LIST_API_POPOVER_ALIAS, ModsListPopoverView, 'modsListPopover.swf',
										WindowLayer.WINDOW, MODS_LIST_API_POPOVER_ALIAS, MODS_LIST_API_POPOVER_ALIAS,
										ScopeTemplates.DEFAULT_SCOPE)
	return buttonSettings, popoverSettings

for item in getViewSettings():
	g_entitiesFactories.addSettings(item)
