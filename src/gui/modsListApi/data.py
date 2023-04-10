
import BigWorld
import ResMgr
import logging

from ids_generators import SequenceIDGenerator

from ._constants import DEFAULT_MOD_ICON
from .controller import g_controller
from .lang import l10n
from .events import g_eventsManager
from .utils import prepareDescription

__all__ = ('g_dataProvider', 'ModificationItem', )

logger = logging.getLogger(__name__)

class _DataProvider(object):

	@property
	def modsData(self):
		return self._generateModsData()

	@property
	def staticData(self):
		return self._generateStaticData()

	@staticmethod
	def _generateModsData():
		"""return value Represented by ModsListStaticDataVO (AS)"""
		result = list()
		for item in g_controller.modifications.values():
			if item.available:
				result.append(item.dpData)
		if result:
			result = sorted(result, key=lambda item: item.get('id'))
		if not result:
			result.append({})
		return {'mods' : result}

	@staticmethod
	def _generateStaticData():
		"""return value Represented by ModsListModsVO (AS)"""
		result = {
			'titleLabel': l10n('title'),
			'descriptionLabel': l10n('description'),
			'closeButtonVisible': True
		}
		return result

g_dataProvider = _DataProvider()

IDGenerator = SequenceIDGenerator()

class ModificationItem(object):

	@property
	def uniqueID(self):
		return self.__numID

	@property
	def available(self):
		return self.__availabilityCheck()

	@property
	def dpData(self):
		return self.__genDataForDP()

	def __init__(self):
		self.__numID = IDGenerator.next()
		self.__stringID = ''
		self.__alerting = False
		self.__callback = lambda: logger.warning('handler for "%s" not installed' % self.__stringID)
		self.__enabled = False
		self.__availableInLobby = False
		self.__availableInLogin = False
		self.__name = ''
		self.__description = ''
		self.__icon = ''
		g_eventsManager.invokeModification += self.__invokeModification

	def setData(self, id, name, description, icon, enabled, login, lobby, callback):
		if id is not None:
			self.__stringID = id
		if enabled is not None:
			self.__enabled = enabled
		if lobby is not None:
			self.__availableInLobby = lobby
		if login is not None:
			self.__availableInLogin = login
		if name is not None:
			self.__name = name
		if description is not None:
			self.__description = prepareDescription(description)
		if callback is not None:
			self.__callback = callback
		if icon is not None:
			self.__icon = self.__fixModIcon(icon)
		g_eventsManager.onListUpdated()

	def __fixModIcon(self, path):
		if not path or not ResMgr.isFile(path):
			return DEFAULT_MOD_ICON
		# use '../../' to premature up from "gui/flash" directory
		return '../../%s' % path

	def setAlerting(self, isAlerting):
		self.__alerting = isAlerting
		g_eventsManager.onListUpdated()
		if isAlerting:
			g_eventsManager.onButtonBlinking()

	def __availabilityCheck(self):
		result = False
		if g_controller.isInLobby and self.__availableInLobby:
			result = True
		if not g_controller.isInLobby and self.__availableInLogin:
			result = True
		return result

	def __genDataForDP(self):
		result = {
			'id': self.__numID,
			'isEnabled': self.__enabled,
			'isAlerting': self.__alerting,
			'nameLabel': self.__name,
			'descriptionLabel': self.__description,
			'icon': self.__icon
		}
		return result

	def __invokeModification(self, modificationID):
		if modificationID != self.__numID:
			return
		if callable(self.__callback):
			self.__alerting = False

			# call handler on next frame
			# * fix menu freezes on call handler
			# * fix stuck trace if handler cause error
			BigWorld.callback(0, self.__callback)
