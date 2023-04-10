"""
ModsListApi

	method addModification
		:param id: Uniq modification ID - required
		:param name: Modification name - required
		:param description: Modification hint (mouse over) - required
		:param icon: Modification icon (path from res_mods/<game_vaersion>/) - required
		:param enabled: Is modification enabled (can be clicked) - required
		:param login: Show modification on Login Window - required
		:param lobby: Show modification in Lobby - required
		:param callback: Called on modification click - required

	method updateModification
		:param id: Uniq modification ID - required
		:param name: Modification name - not necessary
		:param description: Modification hint (mouse over) - not necessary
		:param icon: Modification icon (path from res_mods/<game_vaersion>/) - not necessary
		:param enabled: Is modification enabled (can be clicked) - not necessary
		:param login: Show modification on Login Window - not necessary
		:param lobby: Show modification in Lobby - not necessary
		:param callback: Called on modification click - not necessary

	method alertModification
		:param id: Uniq modification ID - required

	method clearModificationAlert
		:param id: Uniq modification ID - required
"""

__author__ = "Andrii Andrushchyshyn"
__copyright__ = "Copyright 2023, poliroid"
__credits__ = ["Andrii Andrushchyshyn"]
__license__ = "LGPL-3.0-or-later"
__version__ = "1.4.4"
__maintainer__ = "Andrii Andrushchyshyn"
__email__ = "contact@poliroid.me"
__status__ = "Production"

from .controller import g_controller
from .hooks import *
from .views import *

__all__ = ('g_modsListApi', )

class ModsListApiRepresentation(object):

	@staticmethod
	def addModification(*args, **kwargs):
		g_controller.addModification(*args, **kwargs)

	@staticmethod
	def updateModification(*args, **kwargs):
		g_controller.updateModification(*args, **kwargs)

	@staticmethod
	def alertModification(*args, **kwargs):
		g_controller.alertModification(*args, **kwargs)

	@staticmethod
	def clearModificationAlert(*args, **kwargs):
		g_controller.clearModificationAlert(*args, **kwargs)

g_modsListApi = ModsListApiRepresentation()
